
class Member:
    def __init__(self,full_name):
        self.full_name = full_name
    def intro(self):
        print(f"Hello my name is {self.full_name} !")
# jason = Member("jason")
# jason.intro()

class Student(Member):
    def __init__(self, full_name, reason ):
        super().__init__(full_name)#pulls from member
        self.reason= reason
    def about_me(self):
        print(f"{self.full_name} codes because {self.reason}")

# stephen = Student("Stephen", "he like to learn")
# stephen.about_me()
class Instructor(Member):
    def __init__(self, full_name, bio, skills=[]):
        super().__init__(full_name)
        self.bio = bio
        self.skills = ["Python", "Javascript", "C++"]
    def add_skill(self, new_skills):
        self.skills.append(new_skills)#how do I take them out of the array
    # def test(self):
    #     print(f"My name is {self.full_name} I like {self.bio} my skills are {self.skills}") 

# eric = Instructor("Eric", "Duke and puppies", "")
# eric.add_skill("stretching")
# eric.test()

class Workshop(Member):
    def __init__(self, date, subject, instructors = [], students = []):
        self.date = date
        self.subject = subject
        self.instructors = instructors #do i make these caps like the class
        self.students = students

    def add_participant(self, member): #can i do a conditonal in here?
        if type (member) is Student:
            self.students.append(member)
        else:
            self.instructors.append(member)
    def print_details(self, ):
        print(f"Workshop - {self.date} - {self.subject}")
        print(f"Students") #couldnt find away to refrence a classes name in an fstring
        for idx, student in enumerate(self.students):#self means its accessing this dictionary
            print(f"{idx +1 }. {student.full_name} - {student.reason}")#the object name and key will access a previous 
            #idx prints the num, 
        print(f"Instructors") 
        for idx, instructor in enumerate(self.instructors):
            print(f"{idx +1}. {instructor.full_name} - {instructor.skills}")
            print(f"{instructor.bio}")
        # print(f"")
        
        # print(f"Workshop - {self.subject} - {self.date}")
        



workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()




# ______________________________________________________
# enumerate() allows us to iterate through a sequence but it keeps 
# track of both the index and the element. The enumerate() function 
# takes in an iterable as an argument, such as a list, string, tuple, or
#  dictionary.