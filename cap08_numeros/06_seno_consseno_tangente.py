import math

print(f"PI", math.pi)

"""math.sin(x)
Return the sine of x radians."""
print('Sin')
print('sin (3):', math.sin(3))
print('sin (-3):', math.sin(-3))
print('sin (0):', math.sin(0))
print()


"""math.cos(x)
Return the cosine of x radians."""

print('Cos')
print('cos(3): ', math.cos(3))
print('cos(-3): ', math.cos(-3))
print('cos(0): ', math.cos(0))
print('cos(math.pi): ', math.cos(math.pi))
print('cos(2 * math.pi): ', math.cos(2*math.pi))
print()

"""math.tan(x)
Return the tangent of x radians."""
print('Tan')
print("(tan(3): ", math.tan(3))
print("tan(-3): ", math.tan(-3))
print("tan(0): ", math.tan(0))
print("tan(math.pi): ", math.tan(math.pi))
print("tan(math.pi/2): ", math.tan(math.pi/2))
print("tan(math.pi/4): ", math.tan(math.pi/4))
print()

"""math.hypot(x, y)
Return the Euclidean norm, sqrt(x*x + y*y). 
This is the length of the vector from the origin to point (x, y)."""
print('Hypot')
print('hypot(3,2):', math.hypot(3,2))
print('hypot(-3,3):', math.hypot(-3,3))
print('hypot(0,2):', math.hypot(0,2))
print()


print('Radians')
print('radians(3):', math.radians(3))
print('radians(-3):', math.radians(-3))
print('radians(0):', math.radians(0))
print()


"""math.degrees(x)
Convert angle x from radians to degrees."""
print("Degrees")
print("Degrees 0.05235987755982989 {:.1f}".format(math.degrees(0.05235987755982989)))
print("Degrees -0.05235987755982989 {:.1f}".format(math.degrees(-0.05235987755982989)))
