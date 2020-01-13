
def f(x):
    return 2*x**2 - 5*x - 2

def df(x):
    return 4*x - 5

#----------------------------------------------

x = 0 # first root guess (usando plot2d no máxima)

for i in range(10):
    x = x - (f(x) / df(x))
    
print("First root:", x)

# Erro absoluto 1
r1 = -0.3507810593582121 # raíz 1 calculada no máxima
absoluteError = abs(r1 - x)
print("Absolute Error 1:", str(absoluteError))

#----------------------------------------------

x = 3 # second root guess (usando plot2d no máxima)

for i in range(10):
    x = x - (f(x) / df(x))
    
print("Second root:", x)

# Erro absoluto 2
r2 = 2.850781059358212 # raíz 2 calculada no máxima
absoluteError = abs(r2 - x)
print("Absolute Error 2:", str(absoluteError))
