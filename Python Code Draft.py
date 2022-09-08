#Rambling pseudocode for the metric
# This script will function as a metric for the quality of 3D objects, with the application being cultural heritage.
# It will provide various information about the 3D model, incuding general, vertex info, and polygon info. 
# It calculates the geometric complexity of the object, and gives feedback on how many polygons are required and used.

# import pymesh as pym
# import numpy as np 
# import pyplot as plt

# mesh = pym.load_mesh(3Dfile) -- Must be a mesh. Prints general info about the mesh
# print("Filename", \n"ObjectName", \n"Dimensions") --Dimensions must be taken from some metadata.
# 
# print("Fileinfo: ", \n"Vertices: ", vertex.amount, \n"Polygons: ", poly.amount)
# 
# def object.complexity(3Dfile) --Will give a general impression of the complexity of the geometry
#   bregman divergence for the distance?
#   must account for curvature
#   boolean approach?
#   xyz distances over different segments will also be important
#   should report:
#                   Mean variance in geometry across the model
#                   Complexity in a value between 0 and 100
#                   How many vertexes add geometry less than n
#                   Heatmap of where the "important" geometry is placed
#                   What accuracy the model is on based on the dimensions and polygon size

# def vertex.variance(3Dfile) --Will calculate the variance in vertices
#   for n.vertex in 3Dfile
#       calculate min, max, and mean xyz difference --Both individual and together
# print("X variance: ", x.var, \n"Y variance: ", y.var, \n"Z variance: ", z.var)
# print("Min variance: " vertex.var.min, \n"Max variance: ", vertex.var.max, \n"Mean variance: ", vertex.var.mean)
# plt.plot(x.vertex.values)
# plt.plot(y.vertex.values)
# plt.plot(z.vertex.values)

# def polygon.variance(3Dfile) --Will calculate the size variance in polygons
#   for polygon in 3Dfile --May need to 'calculate this
#       poly.array[i] = poly.size(i+1) --Get the polysize for each poly in array
#       if [i] > max.poly.size
#           set max.poly.size to i --Do the same with min
#       mean.poly.size = sum(poly.array) / i in poly.array -- Sum all values divided by the index sum gets mean
# print("Min poly size: ", min.poly.size, \n"Max poly size: ", max.poly.size, \n"Mean poly size: ", mean.poly.size)
# plt.plot(poly.sizes)

# def size.resolution(3Dfile)
#   something to tell about the relationship between polysize and object dimensions
#   connect to polygon.variance function
#   report something about polysize and where the complex geometry. Is the polygons enought to create the geo?


# Tell something more as well?
# Implement in 3D viewers? 3DHOP, Open3D, FRAMES, Yale, PoTree?
# Evaluate meshes through different simplification algorithms. Edge collapse, quadric error metric. My own?
# Check Blender Sourcecode and see what can be "extracted"

# Should include color texture check.
# Either UV or vertex based.
# For UV, check island size, edges, seam-lengths, and amount of seams.
# Also check for spatial differences in the texture projection, this wwould be very useful!

# Remember all algorithms used must be "citable"

# Add maximum x y and z variance across the model. This will tell how flat or not it is

# What is the metric supposed to give value to? Mesh quality?
#                                               Vertex distribution based on geometry?