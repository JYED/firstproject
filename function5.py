x = 1
y = 2
z = -8

def root(a,b,c):
    r1 = (-b + (b**2 - 4*a*c) ** 0.5) / (2 * a)
    r2 = (-b - (b**2 - 4*a*c) ** 0.5) / (2 * a)

    return r1, r2
   

r1, r2 = root(x,y,z)

print('근은 {}또는 {}'.format(r1,r2))
