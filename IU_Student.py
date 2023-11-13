class ImmaculataStudent:
    def __init__(self, name, major, student_id):
        self.name = name
        self.major = major
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Major: {self.major}")
        print(f"Student ID: {self.student_id}")

# Creating instances of the ImmaculataStudent class
student1 = ImmaculataStudent("John Doe", "Computer Science", "IU12345")
student2 = ImmaculataStudent("Jane Smith", "Business Administration", "IU67890")

# Displaying information about the students
print("Information about Student 1:")
student1.display_info()

print("\nInformation about Student 2:")
student2.display_info()
