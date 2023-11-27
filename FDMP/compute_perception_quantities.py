import numpy as np
from scipy.sparse import coo_matrix, diags

def compute_perception_quantities(vertices, faces):
    n = vertices.shape[1]
    m = faces.shape[1]
    
    sum_angles = np.zeros(n)
    area = np.zeros(m)
    epsilon = 1e-10
    
    for i in range(3):
        i1 = (i - 1) % 3
        i2 = i
        i3 = (i + 1) % 3
        
        pp = vertices[:, faces[i2, :]] - vertices[:, faces[i1, :]]
        qq = vertices[:, faces[i3, :]] - vertices[:, faces[i1, :]]
        
        # normalize the vectors
        pp_length = np.sqrt(np.sum(pp ** 2, axis=0))
        qq_length = np.sqrt(np.sum(qq ** 2, axis=0))
        
        Ipp_zero = np.where(pp_length < epsilon)
        pp_length[Ipp_zero] = 1
        
        Iqq_zero = np.where(qq_length < epsilon)
        qq_length[Iqq_zero] = 1
        
        pp_nor = pp / np.tile(pp_length, (3, 1))
        qq_nor = qq / np.tile(qq_length, (3, 1))
        
        # compute angles and clamped cotans
        cos_ang = np.sum(pp_nor * qq_nor, axis=0)
        cos_ang = np.clip(cos_ang, -1, 1)
        ang = np.arccos(cos_ang)
        
        ctan_i = 1 / (2 * np.tan(ang / 2))
        ctan_i = np.clip(ctan_i, 0.001, 1000)
        
        ii_lap_i = faces[i2, :]
        jj_lap_i = faces[i3, :]
        
        for j in range(m):
            indextemp = faces[i1, j]
            sum_angles[indextemp] += ang[j]
        
        if i == 0:
            rr = np.cross(pp.T, -qq.T)
            rr = rr.T
            area = np.sqrt(np.sum(rr ** 2, axis=1)) / 2.0
    
    ii_lap = np.concatenate((ii_lap_1, jj_lap_1, ii_lap_2, jj_lap_2, ii_lap_3, jj_lap_3))
    jj_lap = np.concatenate((jj_lap_1, ii_lap_1, jj_lap_2, ii_lap_2, jj_lap_3, ii_lap_3))
    ss_lap = np.concatenate((ctan_1, ctan_1, ctan_2, ctan_2, ctan_3, ctan_3))
    
    laplacian = coo_matrix((ss_lap, (ii_lap, jj_lap)), shape=(n, n)).tocsc()
    
    diag_laplacian = np.sum(laplacian, axis=1).flatten()
    Diag_laplacian = diags(diag_laplacian, 0, format='csc')
    laplacian = Diag_laplacian - laplacian
    
    ii_mass = np.concatenate((faces[0, :], faces[1, :], faces[2, :]))
    jj_mass = np.concatenate((faces[0, :], faces[1, :], faces[2, :]))
    area = area / 3.0
    ss_mass = np.concatenate((area, area, area))
    
    mass = coo_matrix((ss_mass, (ii_mass, jj_mass)), shape=(n, n)).tocsc()
    
    ii_adja = np.concatenate((faces[0, :], faces[1, :], faces[2, :]))
    jj_adja = np.concatenate((faces[1, :], faces[2, :], faces[0, :]))
    ss_adja = np.concatenate((np.arange(1, m + 1), np.arange(1, m + 1), np.arange(1, m + 1)))
    
    adja = coo_matrix((ss_adja, (ii_adja, jj_adja)), shape=(n, n)).tocsc()
    
    I_adja = np.where(adja.T != 0)
    I_adja = I_adja[0][adja[I_adja] == 0]
    adja[I_adja] = -1
    
    I, J, V = adja.row, adja.col, adja.data
    I = I[V == -1]
    J = J[V == -1]
    flag_boundary = np.zeros(n, dtype=bool)
    flag_boundary[I] = True
    flag_boundary[J] = True
    
    constants = np.tile(2 * np.pi, n)
    I_boundary = np.where(flag_boundary)
    constants[I_boundary] = np.tile(np.pi, len(I_boundary))
    
    # Gaussian curvature
    cgauss = constants - sum_angles
    
    return cgauss, laplacian, mass


def cross_inline(x, y):
    z = x.copy()
    z[:, 0] = x[:, 1] * y[:, 2] - x[:, 2] * y[:, 1]
    z[:, 1] = x[:, 2] * y[:, 0] - x[:, 0] * y[:, 2]
    z[:, 2] = x[:, 0] * y[:, 1] - x[:, 1] * y[:, 0]
    return z
