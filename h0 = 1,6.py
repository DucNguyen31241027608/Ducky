h0 = 1.6

v0 = 14.2

g = 9.8

t = float (input ("Nhập thời gian: "))

h = h0 + v0 * t - 0.5 * g * t**2

v = v0 - g*t

print ("h = ", h)

print ("v = ", v)