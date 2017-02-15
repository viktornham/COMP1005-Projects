#I decided to store weights of class grades so that they can be modified if needed

aweight = 0.4

mweight = 0.2

tweight = 0.1

fweight = 0.3


amark = float(input("Enter your assignment mark: "))

mmark = float(input("Enter your midterm mark: "))

tmark = float(input("Enter your tutorial mark: "))

fmark = float(input("Enter your final exam mark: "))


fgrade = amark*aweight + mmark*mweight + tmark*tweight + fmark*fweight

if fmark >= 50 and fgrade >= 60:
    print("Final mark is " + str(fgrade) + ".")
    print("The student passes.")

#Your program must print out two statements indicating the final grade the student received and whether the student passed the course or not. 
#I initially used /n to designate new line within print statement but was unsure if that was appropriate. 

else:
    print("Final mark is " + str(fgrade) + " & the student recieved " + str(fmark) + " on the exam.")
    print("The student does not pass.")
