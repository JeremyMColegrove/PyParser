#   This program parses expressions given in string format
#   Recursive decent parser
#   1/16/2019
#   Jeremy Colegrove

import math

class PyParser:
    def __init__(self):
        self.__pos = 0
        self.__ch = ''
        self.__string = ''
        self.__variables = {}
        self.__help = """Complete list of functions includes:
+
-
*
/
^
%
>
<
=
sin
cos
tan
sind
cosd
tand
floor
ceil
fact
round
pi
e
help
"""
    #Sets ch to the current character and moves the 'cursor' down one
    def nextChar(self):
        if self.__pos < len(self.__string):
            self.__ch = self.__string[self.__pos]
            self.__pos+=1

        else:
            self.__ch = ''
    #Checks to see if ch == +, -, *, /, etc.
    #If it is, shifts cursor to right and returns true
    def eat(self, charToEat):
        while self.__ch == ' ':
            self.nextChar()
        if self.__ch == charToEat:
            self.nextChar()
            return True
        return False

    #Parse term keeps shifting cursor to the right until it hits non-float
    #Returns float
    def parseTerm(self):
        #global self.__pos
        self.pos_ = self.__pos
        #First check for unary + or - to handle double -'s'
        if self.eat('-'):
            x = -1*self.parseTerm()
        elif self.eat('+'):
            x = self.parseTerm()
        #Next check if theres a parenthese, restart the parser w/ that process
        elif self.eat('('):
            x = self.parseExpression()
            self.eat(')')
        #If its a digit, run cursor to the right
        elif self.__ch.isdigit() or self.__ch == '.':
            while self.__ch.isdigit() or self.__ch == '.':
                self.nextChar()
            x = self.__string[self.pos_-1:self.__pos-1]
        else:
            #Gather function name here
            while not self.__ch.isdigit() and (self.__ch.isalpha()):
                self.nextChar()
            x = self.__string[self.pos_-1:self.__pos-1]

            #Define functions here
            if x == 'sqrt':
                x = math.sqrt(self.parseTerm())
            elif x == 'log':
                x = math.log10(self.parseTerm())
            elif x == 'ln':
                x = math.log1p(self.parseTerm())
            elif x == 'floor':
                x = math.floor(self.parseTerm())
            elif x == 'ceil':
                x = math.ceil(self.parseTerm())
            elif x == 'round':
                x = round(self.parseTerm())
            elif x == 'sin':
                x = math.sin(self.parseTerm())
            elif x == 'cos':
                x = math.cos(self.parseTerm())
            elif x == 'tan':
                x = math.tan(self.parseTerm())
            elif x == 'sind':
                x = math.sin(math.radians(self.parseTerm()))
            elif x == 'cosd':
                x = math.cos(math.radians(self.parseTerm()))
            elif x == 'tand':
                x = math.tan(math.radians(self.parseTerm()))
            elif x == 'fact':
                x = math.factorial(self.parseTerm())
            elif x == 'clear':
                    self.__variables.clear()
                    return "Done"
            elif x == 'pi':
                x = math.pi
            elif x == 'e':
                x = math.e
            elif x == 'help':
                return self.help
            if x in self.__variables:
                return self.__variables.get(x, 0)
            else:
                #Error breaking, wasn't a function float or parenthese
                return x + "\ntype 'help' for list of functions"
        return float(x)
    #Runs parsing methods in reverse so when they collapse it follows PEMDAS
    def parsePower(self):
        x = self.parseTerm()
        while True:
            if self.eat('^'):
                x = math.pow(x, self.parseTerm())
            elif self.eat('%'):
                x = x // self.parseTerm()
            else:
                return x

    def parseMultiples(self):
        x = self.parsePower()
        while True:
            if self.eat('*'):
                x *= self.parsePower()
            elif self.eat('/'):
                x /= self.parsePower()
            else:
                return x

    def parseExpression(self):
        x = self.parseMultiples()
        while True:
            if self.eat('+'):
                x += self.parseMultiples()
            elif self.eat('-'):
                x -= self.parseMultiples()
            else:
                return x
    def parseEquals(self):
        x = self.parseExpression()
        while True:
            if self.eat('='):
                if not any(char.isdigit() for char in str(x)):
                    self.__variables[x] = self.parseExpression()
                    return "Variable "+x+" set."
                else:
                    if x == self.parseExpression():
                        return "True"
                    else:
                        return "False"
            elif self.eat('<'):
                if x < self.parseExpression():
                    return "True"
                else:
                    return "False"
            elif self.eat('>'):
                if x > self.parseExpression():
                    return "True"
                else:
                    return "False"

            else:
                return x
    def parseProblem(self):
        x = self.parseEquals()
        while True:
            if self.eat(','):
                x = str(x) + ", " + str(self.parseEquals())
            else:
                return x
    def parse(self, str_):
        self.__pos = 0
        self.__string = str_+" "
        self.nextChar()
        try:
            x = self.parseProblem()
        except Exception as e:
            return e
        return x
    def setVariables(self, l):
        self.__variables = dict(self.__variables, **l)
        return True
    def clearVariables(self):
        self.__variables.clear()
