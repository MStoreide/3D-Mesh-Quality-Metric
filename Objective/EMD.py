import numpy as np
import pandas as pd
import open3d as o3d
import pymeshlab as pym
from scipy import *
from scipy.stats import *


# Remember the keywords of the conference. Sustainability is a big one. 

#Notes for the paper
#The metrics consider surfaces where changes are  to humans. Large flat areas of objects is the most common. 
#But what if the scale difference between flat and decor is very low across the surface of the object.
#The surface of the example shield object is a good example. 
# I REALLY want a way to calculate this! To provide a number! Detect flat and unflat areas, and calculate difference?!


# Earth-Movers Distance

#Use Numpy arrays here. Convert to 2D?

mesh1 = [1,2,4]
mesh2 = [4,5,2]
EMD = wasserstein_distance(mesh1, mesh2)
print(EMD)