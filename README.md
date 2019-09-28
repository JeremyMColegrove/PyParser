# PythonParser
Python parser with variable support
This program parses expressions given in string format

Complete list of supported expressions:

+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
^ (Power)
% (Modulus)
> (Greater Than)
< (Less Than)
= (Equal Too)
sin (SIN Function in Radians)
cos (COS Function in Radians)
tan (TAN Function in Radians)
sind (SIN Function in Degrees)
cosd (COS Function in Degrees)
tand (TAN Function in Degrees)
floor (Floor)
ceil (Ceil)
fact (Factorial)
round (Rounding)
pi (Constant for PI)
e (Constant for e)
clear (Clears all Variables)
help (Displays All Available Expressions)

VARIABLES:

STATIC
You can set variables directly in the string you want parsed. i.e
***
from eval import eval
eval().parse("a=5")
***
This sets the letter a to 5, and can not be changed.

DYNAMICLLY
You can set variables before you parse the string, and these variables can be changed. You pass a dictionary to the function setVariables i.e
***
from eval import eval
k = eval()
k.setVariables({'a':5, 'b':10})
***
This sets the variables a to 5 and b to 10 before the string is parsed.

NOTE:
You can dynamically clear variables too by calling object.clearVariables()



