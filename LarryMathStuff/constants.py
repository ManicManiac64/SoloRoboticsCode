import math

"""
Very self-explanatory. Constants go here.
"""

deadband = 0.05

# robot dimensions (length, width, plus the diagonal (or radius of the robot times 2, hence the R))

L = 30
W = 30
R = math.sqrt(L ** 2 + W ** 2)

# motor IDs

FRDRIVE = 2
FRANGLE = 6
FLDRIVE = 0
FLANGLE = 4
BLDRIVE = 1
BLANGLE = 5
BRDRIVE = 3
BRANGLE = 7