import time
import AdminLoginAssist as ala
greeting = ("Hey from Enersom!")

def ptgreeting():
    print(greeting)

class div():

    def intro(projectname):
        print("Starting " + projectname + "...")
        
    def end(projectname):
        print("Ending " + projectname + "...")
        
    def endandquit(projectname):
        print("Ending and quitting" + projectname + "...")
        
    def section(sectionnumber, projectname):
        print("Section " + sectionnumber + "in" + projectname + ".")
        
        
class var():
    
    def attributes(varname):
        vartype = type(varname)
        print(vartype)
        print(varname)
        
    def temporary(name, value):
        
        print(name)
        print(value)

import time

def login(password, username):
    print("1: Username")
    print("2: Password")
    usernameuser = input ("")
    passworduser = input ("")

    if usernameuser == username and passworduser == password:
        pass

    else:
        quit()
login("test", "el")
print("Correct!")
    

    
        
   
    
