import numpy as np
import pandas as pd
import pymeshlab as pym
from scipy import *
from scipy.stats import *

# Hausdorff Distance
ms = pym.MeshSet()
ms.load_new_mesh(r'D:\Datasets\Archiving2024\Medium\stat\stat_lap.obj')
ms.load_new_mesh(r'D:\Datasets\Archiving2024\Medium\stat\stat_qem.obj')
ms.load_new_mesh(r'D:\Datasets\Archiving2024\Medium\stat\stat_quad.obj')
ms.load_new_mesh(r'D:\Datasets\Archiving2024\Medium\stat\stat_source.obj')

baseline = ms.current_mesh()
samples = baseline.face_number()
print(f"Baseline mesh has", samples, "faces")

lap_haus = ms.get_hausdorff_distance(sampledmesh = 3, targetmesh = 0, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
qem_haus = ms.get_hausdorff_distance(sampledmesh = 3, targetmesh = 1, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
quad_haus = ms.get_hausdorff_distance(sampledmesh = 3, targetmesh = 2, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))

lap_hausDF = pd.DataFrame.from_dict(lap_haus, orient='index', columns=['Laplacian'])
qem_hausDF = pd.DataFrame.from_dict(qem_haus, orient='index', columns=['Quadric Error Metrics'])
quad_hausDF = pd.DataFrame.from_dict(quad_haus, orient='index', columns=['Quads'])

lap_hausDF['Quadric Error Metrics'] = qem_hausDF['Quadric Error Metrics'].values
lap_hausDF['Quads'] = quad_hausDF['Quads'].values

hausDF = lap_hausDF.T

latex = pd.DataFrame.to_latex(hausDF['mean'])
print(latex)