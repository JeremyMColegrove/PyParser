# PyParser
**Python parser with support for variables
This program parses expressions given in string format and returns with a float
Complete list of supported expressions:**

- \+    (Addition)
- \-    (Subtraction)
- \*    (Multiplication)
- \/    (Division)
- \^    (Power)
- \%    (Modulus)
- \>    (Greater Than)
- \<    (Less Than)
- \=    (Equal Too)
- sin   (SIN Function in Radians)
- cos   (COS Function in Radians)
- tan   (TAN Function in Radians)
- sind  (SIN Function in Degrees)
- cosd  (COS Function in Degrees)
- tand  (TAN Function in Degrees)
- floor (Floor)
- ceil  (Ceil)
- fact  (Factorial)
- round (Rounding)
- pi    (Constant for PI)
- e     (Constant for e)
# VARIABLES


## DYNAMIC
You can set variables before you parse the string, and these variables can be changed.
```
from PyParser import PyParser

def etc (value):
  print(value)
  
k = PyParser()
k.setVariables({'a':5, 'b':10})
k.parse("a*b", etc)
```
This sets the variables **a** to **5** and **b** to **10** before the string is parsed.
## Compositon of functions
Support for composition of functions has been added in V2.0
```
from PyParser import PyParser
def etc (value):
  print("Value is " + value)
  
k = PyParser()
k.setVariables({'a':5, 'b':'5*a+17'})
func = 'a*b+b'
print("Composition of function is " + k.getComposition(func))
k.parse(func, etc)
```

## Simultaneous Computations
You can compute multiple functions at once by seperating with commas. The 2nd parameter in the parse function takes a function that gets called with each computed value.

```
from PyParser import PyParser
def etc (value):
  print("Value is "+value)
  
k = PyParser()
k.setVariables({'a':5, 'b':'5*a+17'})
func = 'a*b+b, a+b'
print("Composition of function is " + k.getComposition(func))
k.parse(func, etc)
```
This will print
```
Composition is (5)*(5*(5)+17)+(5*(5)+17), (5)+(5*(5)+17)
Value is 252.0
Value is 47.0
```

## NOTE
You can dynamically clear variables by calling **object.clearVariables()**
Multiplication must be explicitly stated using `*`. If you parse 5x the whole term will be ignored and strange results may occur



