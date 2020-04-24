## 1. Example : Check if an employee have achieved his weekly target or not

# Employee class
class Employee:
    # Define an attributes(name, designation....)
    name = 'Ben'
    designation = 'Sales Executive'
    salesMadeThisWeek = 6
    
    # Method for checking the target    
    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print('Target has been achieved')
        else:
            print('Target has not been achieved')
    
    # Method for changing the name            
    def changeName (self):
        # Change the value of the attribute within a method
        Employee.name = "Mark"       
        
#  object instantiation
employeeOne = Employee()
print(employeeOne.name)
employeeOne.hasAchievedTarget()

employeeTwo = Employee()
employeeTwo.changeName()
print(employeeTwo.name)
       