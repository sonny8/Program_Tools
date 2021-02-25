import time
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
        print("Section " + sectionnumber + "in" + projectname ".")
        
        
class var():
    
    def attributes(varname):
        vartype = type(varname)
        print(vartype)
        print(varname)
    
