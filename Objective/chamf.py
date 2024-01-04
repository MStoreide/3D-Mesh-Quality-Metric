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

# Chamfer Distance

owl_base = o3d.io.read_point_cloud(r'D:\Datasets\Archiving2024\Small\horn\horn_source.ply')
owl_lap = o3d.io.read_point_cloud(r'D:\Datasets\Archiving2024\Small\horn\horn_lap.ply')
owl_qem = o3d.io.read_point_cloud(r'D:\Datasets\Archiving2024\Small\horn\horn_qem.ply')
owl_quad = o3d.io.read_point_cloud(r'D:\Datasets\Archiving2024\Small\horn\horn_quad.ply')

dists_lap = owl_base.compute_point_cloud_distance(owl_lap)
dists_lap = np.asarray(dists_lap)
dists_qem = owl_base.compute_point_cloud_distance(owl_qem)
dists_qem = np.asarray(dists_qem)
dists_quad = owl_base.compute_point_cloud_distance(owl_quad)
dists_quad = np.asarray(dists_quad)


print("Mean of lap: ", (np.mean(dists_lap)))
print("Max of lap: ", (np.max(dists_lap)))
print("Median of lap: ", (np.median(dists_lap)))
print("Std of lap: ", (np.std(dists_lap)))
print(dists_lap.size)

print("Mean of qem: ", (np.mean(dists_qem)))
print("Max of qem: ", (np.max(dists_qem)))
print("Median of qem: ", (np.median(dists_qem)))
print("Std of qem: ", (np.std(dists_qem)))
print(dists_qem.size)

print("Mean of quad: ", (np.mean(dists_quad)))
print("Max of quad: ", (np.max(dists_quad)))
print("Median of quad: ", (np.median(dists_quad)))
print("Std of quad: ", (np.std(dists_quad)))
print(dists_quad.size)
