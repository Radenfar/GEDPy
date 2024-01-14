import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 
from GEDPy import GEDPy


ged: GEDPy = GEDPy()
ged.load(r'C:\Users\adamc\Documents\GitHub\GEDPy\test_suite\test.ged')