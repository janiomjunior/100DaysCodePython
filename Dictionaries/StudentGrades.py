student_scores = {"joao": 80, "pedro":65, "paulo":96, "alfredo": 76}
student_grades = {}
for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif 91 > student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif 81 > student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
