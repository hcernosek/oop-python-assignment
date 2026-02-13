import re

# STUDENT CLASS
class Student:
    def __init__(self, name, email, grades=[]):
        self.name = name
        self.email = email
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def add_grades_from_list(self, grade_list):
        for grade in grade_list:
            print(f"Adding {grade} to {self.name} grades attribute...")
            self.add_grade(grade)

        print(f"{self.name} Updated Grades: {self.grades}")
        print("-")


    def average_grade(self):
        if not self.grades:
            return "No Grades Entered for Student"
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        if not len(self.grades) == 0:
            print(f"Average: {int(self.average_grade())}%")
        else:
            print("No Grades to Average")

        print("-")

    def grades_tuple(self):
        return tuple(self.grades)


# HELPER FUNCTIONS

def get_student_by_email(student_dict, email):
    print(f"looking up {email}...")
    return student_dict.get(email)

# valid email check with regex for bonus
def is_valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None

# divider to format script output
def divider(message=""):
    print("\n------------------------------")
    print(f"{message}")
    print("------------------------------\n")
# MAIN 'SCRIPT'

# create three student objects and...
student1 = Student("Ava Collins", "ava@email.com", [80, 82, 79])
student2 = Student("Noah Reed", "noah@email.com", [95, 86, 90])
student3 = Student("Mia Patel", "mia@email.com", [96, 93, 91])
student4 = Student("\'No Show\' Nancy", "nancy@email.com")

divider("DISPLAY OF STUDENT OBJECT:")

# Display student info and averages.
student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()


divider("ADDING TWO GRADES TO EACH STUDENT:")

#... add two grades to each.
student1.add_grades_from_list([70,73])
student2.add_grades_from_list([82,89])
student3.add_grades_from_list([88,94])

# dict to look up student object from email
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3,
}

divider("STUDENT LOOKUP EXAMPLE:")
lookup_email = "noah@email.com"
lookup_student = get_student_by_email(student_dict, lookup_email)
print(f"Search result for {lookup_email}: {lookup_student.name if lookup_student else 'Not found'}")


divider("ALL UNIQUE GRADES (w/ SETS):")
all_unique_grades = set(student1.grades + student2.grades + student3.grades) # elements in sets can be contained only once
print(f"All unique grades: {sorted(all_unique_grades)}")


divider("TUPLE IMMUTABILITY DEMONSTRATION:")
grade_tuple = student1.grades_tuple()
print(f"Grades tuple for {student1.name}: {grade_tuple}")
print("Lets try to change my grade...\n")
try:
    grade_tuple[0] = 100
except TypeError as error: # trying to mutate a tuple returns a TypeError
    print(f"Cheater, cheater pumpkin eater...tuples are immutable: {error}")


divider("LIST OPERATIONS EXAMPLES:")
for student in [student1, student2, student3, student4]:
    print(f"{student.name} Grades Before Modifying: {student.grades}")
    print(f"Grade count: {len(student.grades)}")
    try:
        removed = student.grades.pop()
        print(f"Removed last grade {removed} from {student.name}")
    except IndexError: # No Show Nancy's fault...
        print("No Grades to Remove")

    if student.grades:
        print(f"First grade: {student.grades[0]}")
        print(f"Last Grade After .pop(): {student.grades[-1]}")
        print(f"Grade Count After .pop(): {len(student.grades)}")
    print("-")
    

divider("BONUS:")
# Bonus: Validate emails and count grades above 90.
for student in [student1, student2, student3]:
    print(f"Email valid for {student.name}: {is_valid_email(student.email)}")
print("-")

greater_than_90 = sum(1 for grade in student1.grades + student2.grades + student3.grades if grade > 90)
print(f"Grades above 90: {greater_than_90}")
