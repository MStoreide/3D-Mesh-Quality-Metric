import numpy as np
from scipy.sparse import spdiags
from scipy.optimize import curve_fit

def perceptual_distance(name_firstmesh, name_secondmesh):
    mesh_first = name_firstmesh.strip()
    mesh_second = name_secondmesh.strip()

    # Load the two meshes
    vertices_first, faces_first = read_mesh(mesh_first)
    vertices_second, faces_second = read_mesh(mesh_second)

    # Numbers of vertices of the two meshes
    n_first = vertices_first.shape[1]
    n_second = vertices_second.shape[1]

    # Compute the necessary quantities for the FMPD computation
    cgauss_first, laplacian_first, mass_first = compute_perception_quantities(vertices_first, faces_first)
    cgauss_second, laplacian_second, mass_second = compute_perception_quantities(vertices_second, faces_second)

    # Total area
    surface_first = np.sum(np.diag(mass_first))
    surface_second = np.sum(np.diag(mass_second))

    L_first = laplacian_first
    L_second = laplacian_second

    L_first_diag = spdiags(L_first, 0)
    L_second_diag = spdiags(L_second, 0)

    cgaussabs_first = np.abs(cgauss_first)
    cgaussabs_second = np.abs(cgauss_second)

    # Compute the roughness as the Laplacian of Gaussian curvature
    cgauss_rough_first = np.dot(cgaussabs_first.T, L_first) / L_first_diag.T
    cgauss_rough_second = np.dot(cgaussabs_second.T, L_second) / L_second_diag.T
    cgauss_rough_first = np.abs(cgauss_rough_first)
    cgauss_rough_second = np.abs(cgauss_rough_second)

    # Average roughness
    cgauss_rough_mean_first = np.dot(cgauss_rough_first.T, spdiags(mass_first, 0)) / surface_first
    cgauss_rough_mean_second = np.dot(cgauss_rough_second.T, spdiags(mass_second, 0)) / surface_second

    # Power model for modulating the roughness
    minrough = 0.0005
    maxrough1 = 0.20
    maxrough2 = 5.0 * np.minimum(cgauss_rough_mean_first, cgauss_rough_mean_second)
    maxrough = np.maximum(maxrough1, maxrough2)

    # First, clamp the roughness
    cgauss_rough_first = np.clip(cgauss_rough_first, minrough, maxrough)
    cgauss_rough_second = np.clip(cgauss_rough_second, minrough, maxrough)

    # Modulate the roughness with the power model
    a = 0.15
    epsilon = minrough
    cgauss_rough_first_final = np.power(cgauss_rough_first, a) - np.power(epsilon, a)
    cgauss_rough_second_final = np.power(cgauss_rough_second, a) - np.power(epsilon, a)

    # Second modulation: further decrease the roughness that is larger than the average roughness
    threshold = np.minimum(cgauss_rough_mean_first, cgauss_rough_mean_second)
    threshold = np.maximum(threshold, minrough)
    turnpoint = np.power(threshold, a) - np.power(epsilon, a)
    b = 0.5

    for i in range(n_first):
        if cgauss_rough_first_final[i, 0] > turnpoint:
            cgauss_rough_first_final[i, 0] = (cgauss_rough_first_final[i, 0] - turnpoint) * b + turnpoint

    for i in range(n_second):
        if cgauss_rough_second_final[i, 0] > turnpoint:
            cgauss_rough_second_final[i, 0] = (cgauss_rough_second_final[i, 0] - turnpoint) * b + turnpoint

    # Global roughness
    sum_first = np.dot(cgauss_rough_first_final.T, spdiags(mass_first, 0)) / surface_first
    sum_second = np.dot(cgauss_rough_second_final.T, spdiags(mass_second, 0)) / surface_second

    # Scaling factor to bring the distance into [0, 1] interval
    c = 8.0
    distance = c * np.abs(sum_first - sum_second)

    if distance > 1:
        distance = 1

    return distance
