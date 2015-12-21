__author__ = 'bam4d'

import numpy as np
import numpy.linalg as la

def eucidian_dist(a, b):
    return la.norm(a-b)

# every integer can be represented by a hyper-ring, an n dimensional ring which is synonymous with a base-n number
# representation

# 2D hyper ring space
ring2d = np.array([1,1])
print eucidian_dist(0, ring2d)

# 3D hyper ring space
ring3d = np.array([1,1,1])
print eucidian_dist(0, ring3d)


# Now convert into hyper-ring dimensional spiral representation
def get_spiral_coordinates(ring):

    # The radius of each dimension
    radii = []
    radii.append(ring[0])
    # The angle of each dimension
    angles_rads = []
    for i in range(0, ring.size-1):
        radius = np.sqrt(np.sum(ring[:(i+2)]**2))
        radii.append(radius)

        angle_rads = np.arctan(ring[(i+1)] / radii[i])
        print angle_rads
        angles_rads.append(angle_rads)

get_spiral_coordinates(np.ones(10))


