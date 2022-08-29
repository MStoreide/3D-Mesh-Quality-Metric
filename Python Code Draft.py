#Rambling pseudocode for the metric

# import best 3D toolbox as ?? (PyMesh?)
# import numpy as np 
# import pyplot as plt

# mesh = pymesh.load_mesh(3Dfile) -- Must be a mesh --Prints general info about the mesh
# print("Filename", \n"ObjectName", \n"Dimensions") --Dimensions must be taken from some metadata. 

# function vertex.variance(3Dfile) --Will calculate the variance in vertices
#   for vertex in 3Dfile
#       calculate min, max, and mean xyz difference
# print("X variance: ", x.var, \n"Y variance: ", y.var, \n"Z variance: ", z.var)
# print("Min variance: " vertex.var.min, \n"Max variance: ", vertex.var.max, \n"Mean variance: ", vertex.var.mean)
# plt.plot(x.vertex.values)
# plt.plot(y.vertex.values)
# plt.plot(z.vertex.values)

# function polygon.variance(3Dfile) --Will calculate the variance in polygons
#   for ????
#       ?? 
# print("Min poly size: ", min.poly.size, \n"Max poly size: ", max.poly.size, \n"Mean poly size: ", mean.poly.size)
# plt.plot(poly.sizes)