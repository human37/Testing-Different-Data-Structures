import time
import hash
class Student:
    def __init__(self,lname,fname,ssn,email,age):
        self.lname=lname
        self.fname=fname
        self.ssn=ssn
        self.email=email
        self.age=age
    def getintssn(self):
        intssn=self.ssn.replace('-','')
        return int(intssn)
    def getage(self):
        age=self.age
        return float(age)
    def __eq__(self,other):
        if self.getintssn()==other.getintssn():
            return True
        return False
    def __lt__(self,other):
        if self.getintssn()<other.getintssn():
            return True
        return False
    def __gt__(self,other):
        if self.getintssn()>other.getintssn():
            return True
        return False 
    def __le__(self,other):
        if self.getintssn()<=other.getintssn():
            return True
        return False
    def __ge__(self,other):
        if self.getintssn()>=other.getintssn():
            return True
        return False
    def __ne__(self,other):
        if self.getintssn()!=other.getintssn():
            return True
        return False
    def __int__(self):
        return self.getintssn()
def makeList():
    t0=time.time()
    students=hash.Hash(300000)
    f=open("insertnamesmedium.txt","r")
    duplicates=0
    for line in f:
        line=line.split()
        lname=line[0]
        fname=line[1]
        ssn=line[2]
        email=line[3]
        age=line[4]
        if not students.Insert(Student(lname,fname,ssn,email,age)):
            duplicates+=1
    print(duplicates,"duplicate students were found.")
    f.close()
    t1=time.time()
    dt=t1-t0 
    dt=dt.__round__(2)
    print(str(dt),"seconds elapsed to make list.")
    return students
totalages=0.0
def addages(current):
    global totalages
    totalages+=current.getage()
totalages2=0.0
def addages2(current):
    global totalages2
    totalages2+=current.getage()
def averageAge(students,addages):
    t1=time.time()
    students.Traverse(addages)
    avage=totalages/students.Size()
    t2=time.time()
    dt=t2-t1
    dt=dt.__round__(2)
    print(avage, "is the average age.")
    print(dt, "seconds elapsed to find the average age.")
def deleteNames(students):
    t1=time.time()
    f=open("deletenamesmedium.txt","r")
    deleteduplicates=0
    for line in f:
        deletessn=line.strip()
        intdeletessn=deletessn.replace('-','')
        dummystudent=Student('','',intdeletessn,'','')
        if not students.Exists(dummystudent):
            deleteduplicates+=1
            continue
        students.Delete(dummystudent)
    print(deleteduplicates,"ssn's in deletenames.txt were not in the students list.")
    f.close()
    t2=time.time()
    dt=t2-t1
    dt=dt.__round__(2)
    print(dt,"seconds elapsed to delete the names in deletenames.txt")
    f.close()
def retrieveNames(students,addages2):
    t1=time.time()
    f=open("retrievenamesmedium.txt","r")
    retrieveduplicates=0
    retrievedstudents=hash.Hash(300000)
    for line in f:
        retrievessn=line.strip()
        intretrievessn=retrievessn.replace('-','')
        dummystudent=Student('','',intretrievessn,'','')
        item=students.Retrieve(dummystudent)
        if item is None:
            retrieveduplicates+=1
            continue
        retrievedstudents.Insert(item)
    print(retrieveduplicates,"ssn's in retrievenames.txt were not in the students list.")
    f.close()
    retrievedstudents.Traverse(addages2)
    avage=totalages2/retrievedstudents.Size()
    t2=time.time()
    dt=t2-t1
    dt=dt.__round__(2)
    print(dt, "seconds elapsed to retrieve the names in retrievenames.txt.")
    print(avage, "is the average age of all of the students within retrievenames.txt.")
    f.close()
def main():
    students=makeList()
    averageAge(students,addages)
    deleteNames(students)
    retrieveNames(students,addages2)
main()