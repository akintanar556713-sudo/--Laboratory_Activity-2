class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def update_score(self, new_score):
        """Updates the student's score."""
        if new_score < 0 or new_score > 100:
            raise ValueError("Score must be between 0 and 100.")
        self.score = new_score
        print(f"Score updated to {self.score}")

    def check_status(self):
        """Checks if the student passed."""
        if self.score >= 50:
            return "Pass"
        return "Fail"


try:
 
    name = input("Enter student name: ")
    score_input = float(input("Enter current score: "))
    

    student = Student(name, score_input)
    
   
    print(f"Status for {student.name}: {student.check_status()}")
    
    change = input("Do you want to update the score? (yes/no): ")
    if change.lower() == "yes":
        new_score = float(input("Enter new score: "))
        student.update_score(new_score)
        print(f"New Status: {student.check_status()}")

except ValueError as e:
 
    print(f"Error: {e}")
except Exception:
    print("Something went wrong.")