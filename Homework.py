################################################# Code to Review #############################################

############################################## Week 1 – Data Types ###########################################

    #1: Types of values: Integers, floats, string, Booleons
        Int: 123
        Float:12.31 #a float is a decimal
        string: "HI there"
        Booleans: True/False
    
    
    #2: Operators: 2+2, 2*2, 
        7//3 (// gives the quotent) 7 % 3 (The modulus operator (%) gives you only gives the remainder)
    
    
    #3: Floats and Strings
        input()
       'I love cheese \n weeee python is fun'
        #use mnemonic variable naming conventions
        
    #4  Booleans: Bool is its own class. Note to remember.... the = sign always goes on the right
        2==2, 2!=2 
        
        # and, or, and not are the 3 types of logical operators
        
    #5: Variables and Conditions
        
        #Set the prompt
        sleep = float(input("Sleep Score: "))
        strain = float(input("Strain Score: "))
        
        #Set the programs equations
        health = sleep / strain
        
        #Display the result
        print("Heath Score", health)
        
        
        # Example 2 Celcius to Fahrenheit
        C = float(input("Celcius: "))
        
        #Set the programs equations
        F = (9/5)*C + 32
        
        #Display the result
        print("Fahrenheit", F)
        
    #6: Conditionals: Notice how on these they are manual... the ones below are automatic
    x = 32
    if x > 2: # the conditions
        print('I was right')
    #you can add more
    else:
        print('I was wrong')


#################################### Week 2 – For-Loop Iterations ############################################

    #1: For-Loops

    list = ["I", "love", "Python"]
    for any_word in list:
        print(any_word)
        
    #Tip: del(list) delete the list
    
    #2 A loop and a condition
    
    for any in range(10):
    if any % 2 == 1:
        print('{} is odd' .format(any))
    
    
    #tip: type(any) #tell you the variable type
    
    #3:
        if x == 1:
            print("RIGHT")
        elif x > 1: # Else + if = elif
            print("Wrong")
        else:
            print("CLOSEEE")
        
    #4: try and except statements are like an insurance policy on your
    # sequence statement. This is called catching the exceptions.
    raw=input('Enter your height in inches: ')
    try: 
        inches = float(raw)
        Height_in_ft = inches/12
        print(f'{Height_in_ft: .2f} ft')
    except:
        print('Please answer the question')
        
    #5: This a conditional statement that is designed to calculate employee wages
    # if the work over 40 hrs a week they make time and half
    #float() tells the sequence that people might say 40.12 hours
    hours=float(input("Hours worked: "))
    
    try: 
        hours=float(hours)
        if hours <= 40:
            payout = hours * 21
            print("Payout", payout)
        elif hours > 40:
            overtime = (40 * 21) + ((hours - 40) * 21 * 1.5)
            print("Overtime Payout", overtime)
    except: 
        print('Please add the correct pay')
    
    #So the TRY and EXCEPT statements are a place you can store your ifs, elifs, and else statements. The except says dont give this
#################################### Week 3 – For-Loop Iterations ############################################

        #Sequences: 
            
        #1 len(), min(), max() - these are usful on lists
        Justinslist = [1,2,3,TRUE,"Baller"] #this is a list
        
        #concat the list
        
        Justinslist + [23,41,12]
        len("Justinslist") #shows the lenghth
        #you can also nest lists too 
        [Justinslist, Laurenslist]
        
        #2 data Type conversions: int(), float(), str(), 
        
        #3 ranges()
        import random #import serves as library() does
        for i in range(10):
            x = random.random()
            print(x)
    
        #4 List ranges - 
        #range is settup range(start, stop, step)
        list(range(10,100,5)) 
        
 #################################### Week 4 – For-Loop Iterations ############################################
       
 
        #1: Functions: anything that returns a value
        #type(), random.random(), random.int(), 
        #creating your own function: use "def" to define
        
        #here is my own function called addtwonumbers
        def addtwonumbers(a,b):
             return a+b
             reval=addtwonumbers(2,3)
             print(reval)
        
        
        
        #2 
       # - isdigit() checks if everything is a number
       # - isalpha() checks if everything is alphabetical
        def id_validation(employeeID):
     
        if len(employeeID) < 8  or len(employeeID) > 12:
            return False

        letters = employeeID[:-2]
        numbers = employeeID[-2:]

        if letters.isalpha() and numbers.isdigit() and len(letters) >= 6 and len(letters) <= 10 and len(numbers) == 2:
            return True
        else: return False

employeeID = input("Enter employee ID: ")

if id_validation(employeeID):
    print("Valid ID")
else:
    print("Invalid ID")
        
    
def add2numbers():
    a = 1+2
def test (): 
    tmp = add2numbers()
    return tmp
for i in range(5):
    add2numbers()
    test()
    
a = set()
a.add(1)
a.add(1)
a.add(2)
a.add(3)
a.add()

############################# - WEEK 5- More on files and objects - #################
#Takeaway: one major takeaway from this week will be that CSV and json files are the main 
# ones you will need for your career

a=1
dir(a) #this shows you all the ways a can be used'


############################# - WEEK 6 - REGULAR EXPRESSIONS - ##########################################################

import re #Re stands for 'Regular Expressions' and is a package used for extracting and filtering data

handle = open('mbox-short.txt') #opens the file in Read mode and stores it in 'handle'

for line in handle:
        line = line.rstrip()
        if re.search('^From:', line): # notice how its called re.search... search() is from the re package
            print(line)
            
            
# /w is the same thing as [A-Za-z0-9]

# ^a finds words that start with a 
# a$