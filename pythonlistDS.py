import time
class Student:
    def __init__(self,lname,fname,ssn,email,age):
        self.lname=lname
        self.fname=fname
        self.ssn=ssn
        self.email=email
        self.age=age
    def getssn(self):
        ssn=self.ssn
        return ssn
    def getage(self):
        age=self.age
        return age
def makeList():
    t0=time.time()
    students=[]
    f=open("insertnames.txt","r")
    for line in f:
        a=True
        line=line.split()
        lname=line[0]
        fname=line[1]
        ssn=line[2]
        email=line[3]
        age=line[4]
        for student in students:
            if student.getssn()==ssn:
                print("Error, duplicate student found. Was not added to the list.")
                print("Student was "+str(fname)+" "+str(lname))
                a=False
        if a==True:
            students.append(Student(lname,fname,ssn,email,age))
    f.close()
    t1=time.time()
    dt=t1-t0 
    print(str(dt),"seconds elapsed to make list.")
    return students
def averageAge(students):
    t1=time.time()
    totalage=0.0
    for student in students:
        age=float(student.getage())
        totalage+=age
    avage=totalage/len(students)
    t2=time.time()
    deltat=t2-t1
    print(avage, "is the average age.")
    print(deltat, "seconds elapsed to find average age.")
def deletenames(students):
    t1=time.time()
    f=open("deletenames.txt","r")
    for line in f:
        a=False
        deletessn=line.strip()
        for student in students:
            if deletessn==student.getssn():
                students.remove(student)
                a=True      
        if a==False:
            print(deletessn,"in deletenames.txt was not in the students list.")
    f.close()
    t2=time.time()
    dt=t2-t1
    print(dt, "seconds elapsed to delete the names in deletenames.txt")
    f.close()
def retrievenames(students):
    t1=time.time()
    f=open("retrievenames.txt","r")
    newavgage=[]
    for line in f:
        a=False
        nametoretrieve=line.strip()
        for i in range(len(students)):
            if students[i].getssn()==nametoretrieve:
                newavgage.append(float(students[i].getage()))
                a=True
        if a==False:
            print(nametoretrieve,"in retrievenames.txt was not in the students list.")
    f.close()
    newavg=0.0
    for age in newavgage:
        newavg+=age
    newavg=newavg/len(newavgage)
    t2=time.time()
    dt=t2-t1
    print(dt, "seconds elapsed to retrieve the names in retrievenames.txt")
    print(newavg, "is the average age of all of the students within retrievenames.txt ")
    f.close()
def main():
    students=makeList()
    averageAge(students)
    deletenames(students)
    retrievenames(students)
main()


