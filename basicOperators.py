from operator import *

def basicOperatorsSimple():
   x = add(5,5)
   y = sum([5,5])
   print("operator " + str(x))
   print("builtin " + str(y))
def basicOperators(userList):
    try:
       x = sum(userList)
       print(x)
    except:
        pass

def basicFormulaMaker(userFormula):
    try:
        x = parseSpecialCharacters(userFormula)
        y = eval(x)
        print(y)
        gatherUserRequest()
    except Exception as e:
        print(e)
        pass
def parseSpecialCharacters(userFormula):
   if userFormula.find("x") != -1:
      userFormula = userFormula.replace("x","*")
   if userFormula.find("^") != -1:
      userFormula = userFormula.replace("^","**")
   return userFormula

def gatherUserRequest():
    li = []
    x = False
    print("Dear user welcome to Mr.Emproeum Wonders")
    print("Please enter a series of numbers since we only provide add right now")
    while x != True:
       try:
          user_input = input()
          if(user_input == "stop"):
              x = True
              break
          if(user_input == "diy"):
              print("Welcome MadLad please enter your own formula")
              y = input()
              basicFormulaMaker(y)
          li.append(int(user_input))
       except:
           pass
    basicOperators(li)
gatherUserRequest()

