class GEDPy:
    def __init__(self) -> None:
        pass
    
    def load(self, filename: str) -> None:
        try:
            if not filename.endswith('.ged'):
                raise ValueError(f"Provided file: '{filename}' is not a .ged file.")
            else:
                with open(filename, 'r') as f:
                    self.data = f.read()
                print(f"Successfully loaded .ged file: '{filename}'")
        except FileNotFoundError:
            print(f"Provided .ged file: '{filename}' not found.")
            raise FileNotFoundError
        