'''
This project was written entirely by myself, Adam Comer, and is licensed under the MIT License.
Please see the LICENSE file for more information.

All code is compliant with the GEDCOM 5.5.1 and 5.5.5 specifications.
For more information on GEDCOM, please visit gedcom.org
'''
from GEDPy.tree import Tree

class GEDPy:
    def __init__(self) -> None:
        self.data: str | None = None
        self.SUPPORTED_VERSIONS: list[str] = ['5.5.1', '5.5.5']
        self.trees: dict[str, Tree] = {}

    def __process_header(self) -> dict:
        '''Process the header of the GEDCOM file.'''
        header = {}
        stack = [] # represents a list of keys that the current level is at
        prev: int = 0
        count: int = 0
        for line in self.data:
            if line.startswith("0") and "HEAD" not in line:
                break
            elif line.startswith("0") and "HEAD" in line:
                header["VALUE"] = "HEAD"
                prev = 1
            else:
                parts = line.split()
                level = int(parts[0])
                tag = parts[1]
                value = ' '.join(parts[2:]) if len(parts) >= 3 else ""
                value = value.strip()
                if tag == "CONT":
                    # this is a special case where we need to append the value to the previous item's value
                    # we dont need to consider the level of the CONT tag, just the previous level
                    current_dict = header
                    for key in stack:
                        current_dict = current_dict[key]
                    most_recent_item = list(current_dict.keys())[-1]
                    old_value = current_dict[most_recent_item]
                    current_dict[most_recent_item] = old_value + " " + value
                elif level == prev:
                    # Case 1: level is the same as the previous level, add to the current stack
                    # go to the level denoted in the list of keys in stack and add the new information
                    current_dict = header
                    for key in stack:
                        current_dict = current_dict[key]
                    current_dict[tag] = value
                elif level > prev:
                    # Case 2: level is greater than the previous level, add to the stack
                    # step 1: get the previous item's value and replace it with a new dictionary
                    current_dict = header
                    for key in stack:
                        current_dict = current_dict[key]
                    most_recent_item = list(current_dict.keys())[-1]
                    old_value = current_dict[most_recent_item]
                    current_dict[most_recent_item] = {"VALUE": old_value, tag: value}
                    # step 2: append the new item to the stack
                    stack.append(most_recent_item)
                elif level < prev:
                    # Case 3: level is less than the previous level, pop from the stack
                    if level == 0:
                        break
                    else:
                        while level < prev:
                            stack.pop()
                            prev -= 1
                        # add the new information to the stack
                        current_dict = header
                        for key in stack:
                            current_dict = current_dict[key]
                        current_dict[tag] = value
                if not tag == "CONT":
                    prev = level
                count += 1
        self.data = self.data[count:] # remove the header from the data
        return header


    def load(self, filename: str) -> None:
        try:
            if not filename.endswith('.ged'):
                raise ValueError(f"Provided file: '{filename}' is not a .ged file.")
            else:
                with open(filename, 'r') as f:
                    self.data = f.readlines()
                print(f"Successfully loaded .ged file: '{filename}'")
        except FileNotFoundError:
            print(f"Provided .ged file: '{filename}' not found.")
            raise FileNotFoundError
        except Exception as e:
            print(f"An unknown error occured while loading file: '{filename}'")
            print(e)
            raise Exception
        header = self.__process_header()
        filename = filename.split('\\')[-1].split('/')[-1].split('.')[0]
        self.trees[filename] = Tree(header)
    

    def write(self, tree) -> None:
        '''Write the tree to a .ged file.'''
        print("This feature is not yet implemented.")