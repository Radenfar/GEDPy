from GEDPy.person import Person

class Tree:
    def __init__(self, header: dict[str, str]) -> None:
        '''
        This class represents a GEDCOM tree object.
        '''
        self.header: dict[str, str] = header
        self.root: int = 0
        self.people: list[Person] = [] # will use an ind
        self.records = []
    
    def print_records(self) -> None:
        for record in self.records:
            print(record)