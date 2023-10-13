# Compute Gravitational Lens Effect #
# C is circumference, units of black hole circum #
# R is radius of disk containing light from the universe #
# A is "Angular Diameter" of disk #
import math

pi = 3.14159
C = 1.0

print("Circumference, Angle, Radius")
for i in range(0, 2):
    if i == 2: C = 1.10
    if i == 1: C = 1.05
    if i == 0: C = 1.01
    A = 300 * math.sqrt(1.0 - 1.0 / C)
    A = A / 2
    # Assume holding diagram 12 inches from eye
    R = 12 * math.tan(A * pi / 180)
    print(C, " ", A * 2, " ", R)
