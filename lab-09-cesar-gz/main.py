# -*- coding: utf-8 -*-
"""
Cesar Gutierrez
CPSC 223P-01
Wed Apr 13, 2021
cesarg7@csu.fullerton.edu
"""

def getStudents():
	"""get all the students from the grades file"""
	temp = []
	studentList = []

	with open("Class Lab Assignments\lab-09-cesar-gz\grades.txt", 'r') as assignmentFile:
		#parse thru and add to temp list
		for line in assignmentFile:
			line = line.strip('\n')

			#split by comma
			student = line.split(',')

			temp.append(student)

	#remove top line
	temp.pop(0)

	#save only the first column of each row
	for i in range(len(temp)):
		studentList.append(temp[i][0])

	return studentList

def getGrades():
    """gets all the grades from the grades file"""
    grades = []

    with open("Class Lab Assignments\lab-09-cesar-gz\grades.txt", "r") as assignmentFile:
        #parse through and add to the temp list
        for line in assignmentFile:
            line = line.strip('\n')
            grade = line.split(',')
            grades.append(grade)
    
    # remove the header line
    grades.pop(0)
    return grades

def getAttendance():
    attendance = []
    with open("Class Lab Assignments\lab-09-cesar-gz/attendance.txt", "r") as attendanceFile:
        for line in attendanceFile:
            line = line.strip("\n")
            attend = line.split(",")
            attendance.append(attend)
    attendance.pop(0)
    return attendance

def getDates():
    with open("Class Lab Assignments\lab-09-cesar-gz/attendance.txt", "r") as attendanceFile:
        # only read in the first line to get the titles
        line = attendanceFile.readline()
        line = line.strip("\n")
        dates = line.split(", ")
    dates.pop(0)
    return dates

def getAssignmentNames():
    """lists all the assignment names"""
    with open("Class Lab Assignments\lab-09-cesar-gz\grades.txt", "r") as assignmentFile:
        # only read in the first line to get the titles
        line = assignmentFile.readline()
        line = line.strip('\n')
        assigns = line.split(', ')

    assigns.pop(0)

    return assigns


class FileEdit:

    # our lists to start off with
    students = getStudents()
    assigns = getAssignmentNames()
    dates = getDates()

    # full files for parsing
    fullGrades = getGrades()
    fullAttends = getAttendance()

    grades = []
    attendance = []

    def __init__(self):
        pass

    def listStudents(self):
        """ list the students """
        for i in range(len(self.students)):
            print(self.students[i])

    def listGrades(self):
        """ list the grades """
        # access each row
        for i in range(len(self.students)):
            print(f"\n{self.students[i]}", end="\n")
            # access each cell
            for j in range(len(self.assigns)):
                print(f"{self.assigns[j]}: {''.join(self.fullGrades[i][j+1])}")

    def listAttendance(self, person):
        """ list the attendance of each student """
        print(self.students[person-1])
		#access each row and column
		
        for i in range(len(self.dates)):			
            status = ''.join(self.fullAttends[person-1][i+1])

            if status == 'p':
                status = "Present"
			
            elif status == 'a':
                status = "Absent"
			
            else:
                status = ''
                
            print(f"{self.dates[i]}: {status}")

    def submitGrade(self, assignmentName):
        """ submit student's grades"""
        # recieve user input for the student's grades and store in a list
        for i in range(len(self.students)):
            grade = input(f"\nGrade for {self.students[i]} for {self.assigns[assignmentName - 1]} > ")
            self.fullGrades[i].insert(assignmentName, grade)
        
        with open("Class Lab Assignments\lab-09-cesar-gz\grades.txt", "r+") as assignmentFile:
            lines = assignmentFile.readline()
            
            #get back to the start
            assignmentFile.seek(0)

            #rewrite the first line
            assignmentFile.write(lines[0])

            #writing the student grade to each line
            for i in range(min(len(lines), len(self.fullGrades))):
                assignmentFile.write(lines[i+1].rstrip(',\n'))
                assignmentFile.write(',')
                assignmentFile.write(''.join(self.fullGrades[i][assignmentName])+(','*(len(self.assigns)-assignmentName)))
                assignmentFile.write('\n')
            assignmentFile.truncate()

    def takeAttendance(self, date):
        """ take attendance of each student """
        #receive user input for the students grades and store in a list		
        for i in range(len(self.students)):
            attend = input(f"\nStudent {self.students[i]} (p/a) > ")
            self.fullAttends[i].insert(date, attend)

        with open("Class Lab Assignments\lab-09-cesar-gz/attendance.txt", 'r+') as attendanceFile:
            lines = attendanceFile.readlines()

			#get back to the start
            attendanceFile.seek(0)

			#rewrite the first line
            attendanceFile.write(lines[0])

			#writing the student grade to each line
            for i in range(min(len(lines), len(self.fullAttends))):
                attendanceFile.write(lines[i+1].rstrip(',\n'))
                attendanceFile.write(',')
                attendanceFile.write(''.join(self.fullAttends[i][date])+(','*(len(self.dates)-date)))
                attendanceFile.write('\n')
                attendanceFile.truncate()


"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                            main starts here
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

myEdit = FileEdit()

while(True):

    print("")
    print("What do you want to do?")
    print("1 - List all students")
    print("2 - List all grades")
    print("3 - List attendance")
    print("4 - Submit a grade")
    print("5 - Take attendance")
    print("Q - Quit")
    print("")
    userInput = input("> ")

    if userInput == "1":
        myEdit.listStudents()
        print("\n")

    elif userInput == "2":
        myEdit.listGrades()
        print("\n")

    elif userInput == "3":
        # grab student names
        listOfStudents = getStudents()

        #recieve input from user to grab the student we want to display attendance for
        print("Which Student?")

        #display all students w a corresponding number
        for i in range(len(listOfStudents)):
            print(f"{i+1} - {listOfStudents[i]}")
    
        person = int(input("\n> "))
        myEdit.listAttendance(person)

        print("\n")

    elif userInput == "4":
        # grab the assignment names list from the file
        assigns = getAssignmentNames()

        print("Which assignment?")

        for i in range(len(assigns)):
            print(f"{i+1} - {assigns[i]}")

        submission = int(input("\n> "))
        myEdit.submitGrade(submission)
        print("\n")

    elif userInput == "5":
        dates = getDates()
        print("Which date?")
        for i in range(len(dates)):
            print(f"{i+1} - {dates[i]}")
        
        day = int(input("\n> "))
        myEdit.takeAttendance(day)
    
    elif userInput == "Q" or "q":
        break
