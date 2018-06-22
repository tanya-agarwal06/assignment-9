'''class Circle():
    def __init__(self,radius):
        self.rad=radius
    def getarea(self):
        print("area of circle is:" +str(3.14*self.rad*self.rad))
    def getcircumference(self):
        print("circumference is :" +str(2*3.14*self.rad))
a=Circle(3)
a.getarea()
a.getcircumference()'''

#2
'''class Student():
    def __init__(self,name,rollno):
        self.n=name
        self.r=rollno
    def display(self):
        print("the information of students is :Name is "+str(self.n) + "roll no is "+str(self.r))
a=Student(" Tanya ",97)
a.display()'''

#3
'''class Temperature():
    def __init__(self,celsius,farhenite):
        self.c=celsius
        self.f=farhenite
    def celsius(self):
        print("the temperature in celsius to farhenite is:" +str((self.c*1.8)+32))
    def farhenite(self):
        print("the temperature from farhenite into celsius:" +str((self.f-32)*0.5556))
a=Temperature(12,78)
a.celsius()
a.farhenite()'''

#4
'''class MovieDetails():
    def __init__(self,moviename,artistname,yearofrelease,ratings):
        self.m=moviename
        self.a=artistname
        self.y=yearofrelease
        self.r=ratings
    def display(self):
        print("the details of movie, name is:" +str(self.m) + ", artist name is" +str(self.a) + " ,year of release is" +str(self.y) + " ratings are " +str(self.r))
    def update(self,m,a,y,r):
        self.moviename2=m
        self.artistname2=a
        self.yearofrelaese=y
        self.ratings=r
        print("the details of movie, name is:" +str(self.m) + ", artist name is" +str(self.a) + " ,year of release is" +str(self.y) + " ratings are " +str(self.r))

c=MovieDetails(" Race "," saif ", 2016 ," three stars ")
c.display()
name1=input("enter updated movie")
artistname1=input("enter updated artist name")
yearofrelease1=input("enter updated year of release")
ratings1=input("enter updated ratings of movie")
c.update(name1,artistname1,yearofrelease1,ratings1)'''

#4
'''class MovieDetails():
    def __init__(self):
        moviename=input("enter movie name")
        an=input("enter artist name")
        year=int(input("enter year of release"))
        r=int(input("enter ratings of the movie"))
        self.name=moviename
        self.an=an
        self.year=year
        self.r=r
    def display(self):
        print("the details of movie, name is:" +str(self.name) + ", artist name is" +str(self.an) + " ,year of release is" +str(self.year) + " ratings are " +str(self.r))
    def update(self,m,a,y,r):
        self.moviename2=m
        self.an2=a
        self.year2=y
        self.r2=r
        print("the details of movie, name is:" +str(self.moviename2) + ", artist name is" +str(self.an2) + " ,year of release is" +str(self.year2) + " ratings are " +str(self.r2))

c=MovieDetails()
c.display()
moviename1=input("enter updated movie")
an1=input("enter updated artist name")
year1=input("enter updated year of release")
r1=int(input("enter updated ratings of movie"))
c.update(moviename1,an1,year1,r1)'''

#5
class Expenditure():
    def __init__(self):
        b=int(input("enter savings"))
        a=int(input("enter amount that has been spent"))
        self.a=a
        self.b=b
    def display(self):
        print("savings are rs%d and spent rs%d"%(self.a,self.b))
    def salary(self):
        self.c=self.a+self.b
    def displaysalary(self):
        print("total salary is ", self.c)
e=Expenditure()
e.display()
e.salary()
e.displaysalary()
    
