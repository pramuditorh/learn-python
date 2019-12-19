class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        tempScores = 0
        grade = ""
        for i in scores:
            tempScores += i
        
        tempScores = tempScores/len(scores)

        if tempScores >= 90 and tempScores <= 100:
            grade = "O"
        elif tempScores >= 80 and tempScores < 90:
            grade = "E"
        elif tempScores >= 70 and tempScores < 80 :
            grade = "A"
        elif tempScores >= 55 and tempScores < 70:
            grade = "P"
        elif tempScores >= 40 and tempScores < 55:
            grade = "D"
        else:
            grade = "T"

        return grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())