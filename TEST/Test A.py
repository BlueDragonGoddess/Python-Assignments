#Test Part A
#Submitted by Colton Dean c0741555
def main():
    choice = 'Y'
    outfile = open('grades.txt' , 'w')
    while(choice != 'N'):
    
        ID = str(input('Please input Student ID '))
        quizTotal = float(input('Please input quiz totals '))
        assignmentTotal = float(input('Please input assignment totals '))
        testTotal = float(input('Please input test totals '))
        choice = str(input('Do you have another student to enter? Y/N'))
        GPA = calculateGPA(quizTotal, assignmentTotal, testTotal)
        GPAFour = convertToFourPoint(GPA)
    

        outfile.write(str(ID)+ " "+ "GPA: "+ str(GPA) + " " + "GPA: "+ str(GPAFour))

        
    print("Thank you have a nice day!")
    outfile.close()

    
    
def calculateGPA(quizTotal, assignmentTotal, testTotal):
    GPA = (quizTotal * 0.2) + (testTotal * 0.6) + (assignmentTotal *0.2)
    print(GPA)
    return GPA

def convertToFourPoint(GPA):
    if(GPA>94):
        GPAFour = 4
    if(GPA>87 and GPA<93):
        GPAFour = 3.7
    if(GPA>80 and GPA<86):
        GPAFour = 3.5
    if(GPA>77 and GPA<79):
        GPAFour = 3.2
    if(GPA>73 and GPA<76):
        GPAFour = 3.0
    if(GPA>70 and GPA<72):
        GPAFour = 2.7
    if(GPA>57 and GPA<69):
        GPAFour = 2.3
    if(GPA>63 and GPA<66):
        GPAFour = 2.0
    if(GPA>60 and GPA<62):
        GPAFour = 1.7
    if(GPA>50 and GPA<59):
        GPAFour = 1

        
    print(GPAFour)
    return GPAFour
