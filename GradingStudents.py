def gradingStudents(grades):
    final_grade = []
    grade_multiple = []
    for grade in grades:
        prev_grade = grade
        while grade % 5 != 0:
            grade += 1
        if grade < 40 or (grade - prev_grade) >= 3:
            final_grade.append(prev_grade)
        elif (grade - prev_grade) < 3:
            final_grade.append(grade)
    return final_grade
     
    
#grades = [73, 67, 38, 33]
print(gradingStudents(grades))