
from operator import itemgetter
studentlist = []
marks = []
agez = []
studentclass=[]
teachers = []
q = True

maxstudents = int(input("Enter Number of Students: "))
i = 0
for i in range(0, maxstudents):

        name = str(input("Enter Student Name: "))
        studentlist.append(name)
        print("Enter Age: ")
        age = input()
        agez.append(age)
        teachername = str(input("Enter Teacher Name: "))
        teachers.append(teachername)

        slass = input("ENTER THE CLASS ")
        studentclass.append(slass)
        subject = int(input("Enter Mark for Subject1: "))
        marks.append(subject)
        marks2 = int(input("Enter Mark for Subject 2: "))
        marks.append(marks2)
        marks3 = int(input("Enter Mark for Subject 3: "))
        marks.append(marks3)
        marks4 = int(input("Enter Mark for Subject 4: "))
        marks.append(marks4)
        marks5 = int(input("Enter Mark for Subject 5: "))
        marks.append(marks5)


while q == True:

    print("\n++++++ Welcome to Student management Board ++++++\n")
    print("[Choice 1: Showing the List of student IN List  ]")
    print("[Choice 2: Add New Student]")
    print("[Choice 3: Searching student]")
    print("[Choice 4: Dropping a student]\n")

    x = int(input("Enter a choice: "))

    if x == 1:
        valt = str(input("DO YOU WANT TO print in alphabet order LIST OR NOT: YES OR NO "))
        valt = valt.upper()
        if valt =="YES":
            print("LIST OF STUDENTS \n")
            for m in range(0,maxstudents):
                 print('Name of the student is ' + str(studentlist[m]))
                 print('AGE OF THE STUDENT ' + str(agez[m]) + " AND SECTION OF THE STUDENT   " + str(studentclass[m]))
                 for k in range(5):
                  print(' The mark in the subject' + str(k+1) + "=" + str(marks[k]))
            print("LIST OF STUDENTS  in order \n")

             # print(sorted(studentlist[g], key=itemgetter(0)))
            #print(agez)
        else:
            print(studentlist)
            print(marks)
    elif x == 2:
        addnewmember = str(input("Enter New Student: "))
        studentlist.append(addnewmember)
        age = str(input("Enter New  Student Age: "))
        agez.append(age)
        teachername = str(input("Enter Teacher Name: "))
        teachers.append(teachername)
        print("The STUDENT LIST \n")
        for i in range(0,maxstudents):
            print(' New student Record Added in the list is --' + str(studentlist[i+1].upper()) + ' with the age ' + str(agez[i+1]) + " and the teacher for the student is " + str(teachers[i+1].upper()))

    elif x == 3:
         playersearching = input("Choose the Name of the Student To Search: ")

         if (playersearching in studentlist):
             playerindex = studentlist.index(playersearching)
             mentor = str(input("Enter the new teacher name"))
             teachers[playerindex] = mentor
             print(' There is a Record Found in the list for the student--' + str(
                 playersearching) + ' the new teacher for the student is--' + str(teachers[playerindex]))


         else:
            print("\n++ There is No Student Found in the  LIST ")

    elif x == 4:
        playerdelete = input("Choose a Student Name To Delete: ")
        if (playerdelete in studentlist):
              studentlist.remove(playerdelete)
              for student in studentlist:
                 print(student)
        else:
            print("\n++ There is No Student  Found in the  List ++")

    choice = str(input("DO YOU WANT TO CONTINUE OR NOT: YES OR NO "))
    choice = choice.upper()
    if (choice == "YES"):
       q = True
    else:
      q = False
