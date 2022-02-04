
class Member:
    def __init__(self,full_name):
        self.full_name = full_name
    def intro(self):
        print(f"Hello my name is {self.full_name} !")
jason = Member("jason")
jason.intro()

class Student(Member):
    def __init__(self, full_name, reason ):
        super().__init__(full_name)#pulls from member
        self.reason= reason
    def about_me(self):
        print(f"{self.full_name} codes because {self.reason}")

stephen = Student("Stephen", "he like to learn")
stephen.about_me()
class Instructor(Member):
    def __init__(self, full_name, bio, skills=[]):
        super().__init__(full_name)
        self.bio = bio
        self.skills = ["Python", "Javascript", "C++"]
    def add_skill(self, new_skills):
        self.skills.append(new_skills)#how do I take them out of the array
    def test(self):
        print(f"My name is {self.full_name} I like {self.bio} my skills are {self.skills}") 

eric = Instructor("Eric", "Duke and puppies", "")
eric.add_skill("stretching")
eric.test()

class Workshops():
    def __init__(self, date, subject, instuctors =[], students=[]):
        self.date = date
        self.subject = subject
        self.instructor = instructor
        self.students = students
    def add_participant(self, new_member):#can i do a conditonal in here?
        self.Member.append(new_member)





# ______________________________________________________
# enumerate() allows us to iterate through a sequence but it keeps 
# track of both the index and the element. The enumerate() function 
# takes in an iterable as an argument, such as a list, string, tuple, or
#  dictionary.