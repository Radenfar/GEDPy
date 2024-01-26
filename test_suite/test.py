import os
import random
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 
from GEDPy import GEDPy

def get_random_tree() -> str:
    trees_folder: str = r'C:\Users\adamc\Documents\GitHub\GEDPy\test_suite\trees'
    trees = os.listdir(trees_folder)
    return os.path.join(trees_folder, random.choice(trees))

ged: GEDPy = GEDPy()
ged.load(get_random_tree())
tree = ged.trees[list(ged.trees.keys())[0]]
print(tree.header)

