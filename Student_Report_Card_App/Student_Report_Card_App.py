import json
import os

class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}
    
    def add_score(self, subject, score):
        self.subjects[subject] = score
        self._update_stats()
    
    def _update_stats(self):
        if self.subjects:
            self.average = sum(self.subjects.values()) / len(self.subjects)
            if self.average >= 90:
                self.grade = 'A'
            elif self.average >= 80:
                self.grade = 'B'
            elif self.average >= 70:
                self.grade = 'C'
            elif self.average >= 60:
                self.grade = 'D'
            else:
                self.grade = 'F'
        else:
            self.average = 0
            self.grade = 'N/A'

def save_data(students, filename='students.json'):
    data = []
    for student in students.values():
        student_data = {
            'name': student.name,
            'subjects': student.subjects,
            'average': student.average,
            'grade': student.grade
        }
        data.append(student_data)
    
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename='students.json'):
    students = {}
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for student_data in data:
                student = Student(student_data['name'])
                student.subjects = student_data['subjects']
                student.average = student_data['average']
                student.grade = student_data['grade']
                students[student.name] = student
    return students

def add_student(students):
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists!")
        return
    
    student = Student(name)
    while True:
        subject = input("Enter subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            score = float(input(f"Enter score for {subject}: "))
            student.add_score(subject, score)
        except ValueError:
            print("Invalid score! Please enter a number.")
    
    students[name] = student
    save_data(students)
    print(f"Student {name} added successfully!")

def view_student(students):
    name = input("Enter student name to view: ")
    student = students.get(name)
    if not student:
        print("Student not found!")
        return
    
    print(f"\nReport Card for {name}:")
    print("-" * 30)
    for subject, score in student.subjects.items():
        print(f"{subject}: {score}")
    print("-" * 30)
    print(f"Average: {student.average:.2f}")
    print(f"Grade: {student.grade}")
    print("-" * 30)

def update_student(students):
    name = input("Enter student name to update: ")
    student = students.get(name)
    if not student:
        print("Student not found!")
        return
    
    print(f"Current subjects: {', '.join(student.subjects.keys())}")
    subject = input("Enter subject to update/add: ")
    try:
        score = float(input(f"Enter new score for {subject}: "))
        student.add_score(subject, score)
        save_data(students)
        print("Score updated successfully!")
    except ValueError:
        print("Invalid score! Please enter a number.")

def main():
    students = load_data()
    
    while True:
        print("\nStudent Report Card App")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_student(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
main()