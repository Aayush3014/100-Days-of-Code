# math.ceil() rounds up to the next nearest integer.

import math
def paint_wall(height,width):
    coverage = 5
    cans_req = (height*width)/coverage
    print(math.ceil(cans_req))
paint_wall(7,13)