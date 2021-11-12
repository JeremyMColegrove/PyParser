from PyParser import PyParser


index = 0

def print_float (value):
  if type(value) == float:
    print(value)

def print_bool (value):
  print(value)


k = PyParser()

# looping through and compute numbers
print("compute looping 0-9:")
for x in range(0, 10):
  k.setVariables({'a':x})
  k.parse("a*10", print_float)

# clear variables
k.clearVariables()

# # command chaining example
print("command chaining:")
k.parse("a=10, b=5, a*b", print_float)

# complex command comparison
print("command function example:")
k.parse("10.5>floor(10.9)", print_bool)

# complex functions example
print("complex command example:")
k.parse("ln( sqrt(4) + 10) * pi + sin(pi)", print_float)