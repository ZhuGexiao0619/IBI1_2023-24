class students:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score

    def print_details(self):
        print(f"Name: {self.name}, Major: {self.major}, Code Portfolio Score: {self.code_portfolio_score}, "
              f"Group Project Score: {self.group_project_score}, Exam Score: {self.exam_score}")
student = students("DYT", "BMI", 61, 61, 61)
student.print_details()