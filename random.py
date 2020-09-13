# Python syntax

#!!NOTE!! PY is case sensitive: ie- print and Print are differnt in syntax!

#Strings can be printed as such. Single quotes or double quotes can work
print("Hello World!")

#Python variables don't need a decleration keyword. Just the variable name and value
todays_date = "11/11/11"

#Arithemtic: Python let you do the basics (*,/,+,-) BUT, you also have the modulo opeator 
is_this_number_odd = 15 % 2 
is_this_number_even = 133 % 7 

#Note: still req to put var in () when printing it to the log
print (is_this_number_even)

#A number with a decimal point is called a float in py
regNum = 1003993
floatNum = 1.300

#Errors: Python conveinetly points to where the error occoured with a ^ symbol 
#Two commen errors are 'Syntax Error' and 'Name Error'
# - SyntaxError means there is something wrong with the way your program is written — punctuation that does not belong, a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError.
# - A NameError occurs when the Python interpreter sees a word it does not recognize. Code that contains something that looks like a variable but was never defined will throw a NameError

#Modulo: py offers a companion to the division operator called the Modulo ( % ).
print(29 % 5) -> this would give us 4 because 29/5 is 5 with a REMAINDER OF 4

#Concatenation: This is simply using the ' + ' operator to add strings, integers, etc together. 
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
# Prints "Hey there!How are you doing?"
- OR YOU CAN USE ( += )
full_text += "This will be added to the end of what full_text is already assined to"
print(full_text)

#Multi-line strings
mutli_line = """
This 
Spans
Four 
Lines
"""

#Functions
