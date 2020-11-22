from time import sleep
from tqdm import tqdm, trange
import time
class half:
    GRAY = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PINK  = '\033[95m'
    SBLUE = '\033[96m'
    
    GRAY1 = '\033[100m'
    RED1 = '\033[101m'
    GREEN1 = '\033[102m'
    YELLOWq = '\033[103m'
    BLUE1 = '\033[104m'
    PINK1  = '\033[105m'
    SBLUE1 = '\033[106m'

print(half.GREEN+' Please Wait...\n')
sleep(2)
for i in trange(100):
    time.sleep(0.10)
print("Python tutorial #1 by : Mr . Half\n")
sleep(1)
print(half.SBLUE+"---------------------------------------------------------\n")
sleep(1)
print(half.GREEN+"× VARIABLE ×")
print("  Variable are use to store up data for later use.\n")
sleep(1)
print(half.SBLUE+"---------------------------------------------------------\n")
sleep(1)
print(half.GREEN+"× BASIC DATA TYPES ×")
sleep(.10)
print(half.GRAY+"""\n  • ( string ) Sentence , Phrase , Character • identifier = " hello world " """)
sleep(.10)
print("""\n  • ( INT ) Positive & Negative Number •
identifier = .5""")
sleep(.10)
print("""\n  • ( FLOAT ) Decimal numbers •
identifier = 23.4232""")
sleep(.10)
print("""\n  • ( BOOL ) True or False •
identifier = True / False""")
sleep(1)
print(half.SBLUE+"""\n----------------------------------------------------------""")
sleep(1)
print(half.GREEN+"\n × IDENTIFIER ×")
sleep(.75)
print("""\n  The name of the variable which the user decides to choose""")
sleep(1)
print(half.RED+"""\nSYNTAX :""")
sleep(.10)
print("""  ( Identifier = value )""")
sleep(.10)
print("""  First_name = "boboy" """)
sleep(.10)
print("""  Last_name = "Villamer" """)
sleep(.10)
print("""  Age = 17""")
sleep(.10)
print("""  Tall = True\n""")
sleep(1)
print(half.SBLUE+"""----------------------------------------------------------""")
sleep(1)
print(half.GREEN+"""\n× SYNTAX ×\n""")
sleep(.75)
print(half.RED+"""  first_name = "boboy" """)
sleep(.10)
print("""  last_name = "villamer" """)
sleep(.10)
print("""  age = 17""")
sleep(.10)
print("""  tall = True""")
sleep(.10)
print("""  (first_name)\n""")
sleep(1)
print(half.SBLUE+"""---------------------------------------------------------""")
sleep(1)
print(half.GREEN+"""\n× CONCATENATION ×""")
                            
print(half.RED+"""\n  first_name = "boboy" """)
sleep(.10)
print("""  last_name = "villamer" """)
sleep(.10)
print("""  age = 17""")
sleep(.10)
print(""""  tall = True""")
sleep(.10)
print(""""  first_name + " " + last_name)\n""")

sleep(1)
print(half.SBLUE+""""----------------------------------------------------------""")
sleep(1)
print(half.GREEN+"""\n× INPUT ×""")
sleep(.75)
print(""""\n  Used to make the user input something in the console.""")
sleep(.10)
print(half.RED+"""\nSYNTAX :""")
sleep(.10)
print("""  variable = input ()""")
sleep(.10)
print("""  variable = input ("Enter your First name")\n""")
sleep(1)

print(half.SBLUE+"""----------------------------------------------------------""")
sleep(1)
print(half.GREEN+"""\n× SYNTAX ×""")
sleep(.10)
print(half.RED+"""  firstname = input ("Enter your first name : ")""")
sleep(.10)
print("""  print (" hi " + firstname\n)""")
sleep(1)

print(half.SBLUE+"""----------------------------------------------------------""")
sleep(1)

print(half.SBLUE+"""\n× CASTING VARIABLE ×""")
sleep(.10)
print(half.GREEN+"""  A Technique used to convert a datatype to another datatype.""")
sleep(.10)

print(half.RED+"""\nSYNTAX :""")
sleep(.10)
print("""  • Convert Number to String""")
sleep(.10)
print("""               • str(number)""")
sleep(.10)
print("""• Convert String to Number""")
sleep(.10)
print("""               •int(string)""")
sleep(.10)
print("""               •float(string)\n""")
sleep(1)
            
print(half.SBLUE+"""----------------------------------------------------------""")
sleep(1)
print(half.RED+"""\n× SYNTAX ×""")
sleep(.75)
print("""  first_name = "boboy" """)
sleep(.10)
print("""  age = 17""")
sleep(.10)
print("""  print ("hi " + first_name + " " + "your age is " + str(age))\n""")
sleep(1)

print(half.SBLUE+"""----------------------------------------------------------""")
sleep(1)

print(half.GRAY+"""\n×Arithmetic Operators×""")
sleep(.10)
print("""  Operator                Syntax              Results""")
sleep(.10)
print("""  Subtraction             x - y              Difference""")
sleep(.10)
print("""  Addition                   x + y                   Sun""")
sleep(.10)
print("""  Multiplication        x * y                Product""")
sleep(.10)
print("""  Division                    x / y               Quotient""")
sleep(.10)
print("""  Modulus                   x % y            Remainder""")
sleep(.10)
print("""  Floor Division        x // y        Quotient(Roundedoff)""")
sleep(.10)
print("""  Exponent                x ** y                Power\n""")
sleep(1)

print(half.SBLUE+"""----------------------------------------------------------""")
sleep(1)

print(half.PINK+"""\n×One Function Calculator×""")
sleep(.75)
print("""  firstnum = float(input ("Enter first number : "))""")
sleep(.10)
print("""  secondnum = float(input ("Enter second number : "))""")
sleep(.10)
print("""  answer = firstnum * secondnum""")
sleep(.10)
print("""  print (str(firstnum) + " * "  +str(secondnum) + " = " + str(answer))
""")
