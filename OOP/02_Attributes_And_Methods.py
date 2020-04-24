
## 1. Employee example

class Employee:
    numberOFWorkingHours = 40
    
employeeOne = Employee()
employeeTwo = Employee()

print(employeeOne.numberOFWorkingHours)
print(employeeTwo.numberOFWorkingHours)
    
Employee.numberOFWorkingHours = 45
print(employeeOne.numberOFWorkingHours)
print(employeeTwo.numberOFWorkingHours)

employeeOne.name = 'John'
print(employeeOne.name)
#print(employeeTwo.name)
employeeTwo.name = 'Mary'
print(employeeTwo.name)

employeeOne.numberOFWorkingHours = 40
print(employeeOne.numberOFWorkingHours)
print(employeeTwo.numberOFWorkingHours)

## 2. Understanding the parameter - self
class Employee:
    def employeeDetails(self):
        self.name = 'john'
        print('name = ', self.name)
        age = 30
        print('age = ', age)
    
    def printEmployeeDetails(self):
        print('Printing in another method ')
        print('name = ', self.name)
        # age is a part of employeeDetails
        # so it displays an error
        print('age = ', age)
            
employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()

## 3. Static Method and Instance methods
class Employee:
    def employeeDetails(self):
        self.name = 'john'
        
    def welcomeMessage(self):
        print('Welcome to our organization!')
        
employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()

## 4. Static Method and Instance methods
class Employee:
    def __init__(self, name):
        self.name = name
        
    def displayEmployeeDetails(self):
        print(self.name)
   
employeeOne = Employee('Mark')
employeeTwo = Employee('John')
employeeOne.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()

## 2.
'''
Write an object oriented program to create a precious stone. 
Not more than 5 precious stones can be held in possession at 
a given point of time. If there are more than 5 precious stones, 
delete the first stone and store the new one.
'''

class PreciousStone:
    numberOfPreciousStones = 0
    preciousStoneCollection = []
    
    def __init__(self, name):
        self.name = name
        # Increment the number of preciouos stones
        PreciousStone.numberOfPreciousStones += 1
        #Append the precious stone to the list of total no of stones are <=5
        if PreciousStone.numberOfPreciousStones <= 5:
            PreciousStone.preciousStoneCollection.append(self)
        else:
            # If more than 5 stones are present, delete the first one and store the new one
            del PreciousStone.preciousStoneCollection[0]
            PreciousStone.preciousStoneCollection.append(self)
    
    @staticmethod
    def displayPreciousStones():
        for preciousStone in PreciousStone.preciousStoneCollection:
            print(preciousStone.name, end = ' ')
        print()

preciousStoneOne  = PreciousStone("Ruby")
preciousStoneTwo  = PreciousStone("Emerald")
preciousStoneThree  = PreciousStone("Sapphire")
preciousStoneFour  = PreciousStone("Diamond")
preciousStoneFive  = PreciousStone("Amber")
preciousStoneFive.displayPreciousStones()
preciousStoneSix = PreciousStone("Onyx")
print('After updating :')
preciousStoneSix.displayPreciousStones()        
















