# import random

# class Student:

#     __id = int(random.random() * 10**8)

#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_student_details(self):
#         student_detail = {}
#         student_detail["student_id"] = self.__id
#         student_detail["student_name"] = self.name
#         student_detail["student_age"] = self.age
#         student_detail["grade"] = self.grade
#         return student_detail

#     def return_values(self):
#         return f"Hi I am {self.name} and I am {self.age} with grade of {self.grade}"


# aravindan = Student("Aravindan", 10, 80)
# student_detail = aravindan.get_student_details()


class Admission:
    def __init__(self, course_name, student_details, strength):
        self.admission_object = {course_name: []}
        self.course_strength = strength
        self.course_name = course_name
        self.details = student_details

    def admission_decission(self):
        give_admission = False
        if self.details['grade'] >= 50:
            give_admission = True
        return give_admission
    
    def admission_status(self):
        admssion_allowed = self.admission_decission()
        if admssion_allowed:
            self.admission_object[self.course_name].append(self.details)
            self.course_strength -= 1
        return self.admission_object



  adm = Admission('Science', student_detail, 100)
  print('Admission strength currently is', adm.course_strength)
  print('Admission decission for Aravindan is', adm.admission_decission())
  print('Admission Staus for Aravindan is', adm.admission_status())
  print('Admission strength currently is', adm.course_strength)
  print('\n\n')

# adm2 = Admission('Maths', Student('rajeshk', 15, 70).get_student_details(), 50)
# print('Admission strength currently is', adm2.course_strength)
# print(adm2.admission_decission())
# print(adm2.admission_status())
# print('Admission strength currently is', adm2.course_strength)

a = 'abc'
def abc():
    global a
    a = 123
    print(a)
    return a


# Inheritence and Polymorphism

class Bird:

	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):

	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):

	def flight(self):
		print("Ostriches cannot fly.")

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()
