# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math
def circl_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * radius * math.pi
    return area,circumference

a , c = circl_stats(6)

print('Area:',a,'Circumference:',c)