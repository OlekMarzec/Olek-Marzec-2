class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50


student_pass = Student("Adam", [60, 70, 80])
student_fail = Student("Ewa", [30, 40, 45])

print(f"{student_pass.name}: {student_pass.is_passed()}")
print(f"{student_fail.name}: {student_fail.is_passed()}")
