student_scores = {
    "harry": 81,
    "Ron": 78,
    "Hermon": 99,
    "draco": 74,
    "Nev": 62
}

student_grades = {}

for i in student_scores:
    if student_scores[i] > 90:
        student_grades[i] = "Outstanding"
    elif student_scores[i] > 80:
        student_grades[i] = "Exceeds Expectations"
    if student_scores[i] > 70:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"
print(student_grades)
