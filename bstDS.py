import time
import bst
MEDIUM=True
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
def makeList():
    t0=time.time()
    students=bst.BST()
    if MEDIUM==True:
        f=open("insertnamesmedium.txt","r")
        duplicates=0
    if MEDIUM==False:
        f=open("insertnames.txt","r")
    for line in f:
        line=line.split()
        lname=line[0]
        fname=line[1]
        ssn=line[2]
        email=line[3]
        age=line[4]
        if not students.Insert(Student(lname,fname,ssn,email,age)):
            if MEDIUM==True:
                duplicates+=1
                continue
            print("error, duplicate student found. was not added to the list. student was "+str(fname)+" "+str(lname)+".")
    if MEDIUM==True:
        print(duplicates,"duplicate students were found.")
    f.close()
    t1=time.time()
    dt=t1-t0 
    print(str(dt),"seconds elapsed to make list.")
    return students
totalages=0.0
def addages(current):
    global totalages
    totalages+=current.getage()
    return
totalages1=0.0
def addages1(current):
    global totalages1
    totalages1+=current.getage()
    return
duplicates=0
totalages=0.0
def averageAge(students,addages):
    t1=time.time()
    students.Traverse(addages)
    avage=totalages/students.Size()
    t2=time.time()
    deltat=t2-t1
    print(avage, "is the average age.")
    print(deltat, "seconds elapsed to find the average age.")
def deleteNames(students):
    t1=time.time()
    if MEDIUM==True:
        f=open("deletenamesmedium.txt","r")
        deleteduplicates=0
    if MEDIUM==False:
        f=open("deletenames.txt","r")
    for line in f:
        deletessn=line.strip()
        intdeletessn=deletessn.replace('-','')
        dummystudent=Student('','',intdeletessn,'','')
        if not students.Exists(dummystudent):
            deleteduplicates+=1
            continue
        students.Delete(dummystudent)
    if MEDIUM==True:
        print(deleteduplicates,"ssn's in deletenames.txt were not in the students list.")
    f.close()
    t2=time.time()
    dt=t2-t1
    print(dt,"seconds elapsed to delete the names in deletenames.txt")
    f.close()
totalages1=0.0
def retrieveNames(students,addages):
    t1=time.time()
    if MEDIUM==True:
        f=open("retrievenamesmedium.txt","r")
        retrieveduplicates=0
    if MEDIUM==False:
        f=open("retrievenames.txt","r")
    retrievedstudents=bst.BST()
    for line in f:
        retrievessn=line.strip()
        intretrievessn=retrievessn.replace('-','')
        dummystudent=Student('','',intretrievessn,'','')
        item=students.Retrieve(dummystudent)
        if item is None:
            retrieveduplicates+=1
            continue
        retrievedstudents.Insert(item)
    if MEDIUM==True:
        print(retrieveduplicates,"ssn's in retrievenames.txt were not in the students list.")
    f.close()
    retrievedstudents.Traverse(addages1)
    avage=totalages1/retrievedstudents.Size()
    t2=time.time()
    dt=t2-t1
    print(dt, "seconds elapsed to retrieve the names in retrievenames.txt.")
    print(avage, "is the average age of all of the students within retrievenames.txt.")
    f.close()
def main():
    students=makeList()
    averageAge(students,addages)
    deleteNames(students)
    retrieveNames(students,addages)
main()