
import math
import matplotlib.pyplot as plt

import numpy as np

p0 = [0.23,2.94]

p1 = [-0.27,3.52]
q1 = [1,1]
p2 = [4.4,-0.96]
q2 = [2,2]

x = abs(p1[1]-p0[1])
y = abs(p1[0]-p0[0])
print ("{}, {}".format(x,y))
total_degree = math.atan( x / y )

in_degree = math.atan(q1[1]/q1[0])
print (in_degree*360/(2*math.pi))

diff_degree = total_degree - in_degree

print (diff_degree*360/(2*math.pi))


ratio =  math.sqrt( q1[0]**2 + q1[1]**2 )  / math.sqrt( x**2 + y **2 )

print (ratio)

R = [ 3, 3]
A = math.sqrt( R[0]**2 + R[1]**2 ) / ratio
alpha = math.atan( R[1]/ R[0] )

add_x = math.cos( diff_degree + alpha ) * A
add_y = math.sin( diff_degree + alpha ) * A

print ( p0[0] - add_x )
print ( p0[1] + add_y )