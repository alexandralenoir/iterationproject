def total_students():
    print("This tracker is set for a maximum of 20 students.")
    return 20

def present_student_count():
    print("How many students are present today?")
    present_string = input("Enter number of students present:")
    
    if present_string.isdigit():
        return int(present_string)
    else:
        print("Error! Please enter a valid number.")
        return -1
   





        

#OOP Enhancements/ encapsulation
class StudentAttendance:
    def __init__(self, total_students):
        self.total_students = total_students
        self.present_students = 0
        self.attendance = ['A']  * total_students # Initialize all as absent
        
    def mark_present(self, count):
        if 0 <= count <= self.total_students:
            self.present_students = count
            for i in range(count):
                self.attendance[i] = 'P' # Mark present
        else:
            raise ValueError("Invalid number of present students.")
                    
    def display_attendance(self):
        print(f"Total Students: {self.total_students}")
        print(f"Present Students: {self.present_students}")
        print(f"Absent Students: {self.total_students - self.present_students}")
        print("Attendance Record:", ' '.join(self.attendance))
                        
#Inheritance

class OnlineAttendance(StudentAttendance):
    def display_attendance(self): # overriding method
        super().display_attendance()
        print("Note: This is online attendance tracking.")



total = total_students()
present = present_student_count()

if present < 0:
    print("Error! Number of students cannot be negative.")
elif present > total:
    print("Error! Number of students cannot exceed total number of students.")
else:
    print("\n--- Classroom Attendance ---")
    attendance_tracker = StudentAttendance(total)
    attendance_tracker.mark_present(present)
    attendance_tracker.display_attendance()

    print("\n--- Online Attendance ---")
    online_tracker = OnlineAttendance(total)
    online_tracker.mark_present(present)
    online_tracker.display_attendance()
                        