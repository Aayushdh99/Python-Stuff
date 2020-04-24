'''
##1 Implement a Library management system which will handle
    the following tasks;
1. Customers should be able to display all the books in the library.
2. Handle the process when a customer requests to borrow a book.
3. Update the library collection when the customer returns a book.
'''

class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    
    def displayavailableBooks(self):
        print()
        print("Available books: ")
        for book in self.availableBooks:
            print(book)
            
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in oour list.")
            
    def addBook(self, returnedBook2):
        self.availableBooks.append(returnedBook)
        print("You have returned the book. Thank You!")

class Customer:
    def requestBook(self):
        print("Enter the name of the book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you are returning: ")
        self.book = input()
        return self.book

library = Library(['Rich Dad, Poor Dad', 'Sapiens', 'Think And Grow Rich'])
customer = Customer()

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice == 1:
        library.displayavailableBooks()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        break

'''
##2 Program to provide layers of abstraction for a car rental system.
    Your program should perform the following:
1. Hatchback, Sedan, SUV should be type of cars that are being provided for rent
2. Cost per day:
Hatchback - $30
Sedan - $50
SUV - $100
3. Give a prompt to the customer asking him the type of car and the number of days 
he would like to borrow and provide the fare details to the user.
'''
class Car:
    def __init__(self):
        # A dictionary to map the type of car and price per day
        self.carFare = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}

    def displayFareDetails(self):
        print("Cost per day: ")
        print("Hatchback: $",self.carFare['Hatchback'])
        print("Sedan: $", self.carFare['Sedan'])
        print("SUV: $", self.carFare['SUV'])

    def calculateFare(self, typeOfCar, numberOfDays):
        # Calculate the fare depending upon the type of car and number of days as requested by the user
        return self.carFare[typeOfCar] * numberOfDays


car = Car()
while True:
    print("Enter 1 to display the fare details")
    print("Enter 2 to rent a car")
    print("Enter 3 to exit")
    userChoice = (int(input()))
    if userChoice is 1:
        car.displayFareDetails()
    elif userChoice is 2:
        print("Enter the type of car you would like to borrow")
        typeOfCar = input()
        print("Enter the number of days you would like to borrow the car")
        numberOfDays = int(input())
        fare = car.calculateFare(typeOfCar, numberOfDays)
        print("Total payable amount: $",fare)
        print("Thank you!")
    elif userChoice is 3:
        break
    