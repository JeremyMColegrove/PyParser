from PyParser import PyParser

def etc (value):
  print(value)

  
k = PyParser()
k.setVariables({'a':5, 'b':'5*a+17'})
func = 'a*b+b, a+b'
print("Composition of function is " + k.getComposition(func))
k.parse(func, etc)
