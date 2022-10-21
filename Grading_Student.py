def gradingStudents(grades):
    # Write your code here
    ans = []
    for i in range(len(grades)):
        if grades[i] >= 38:
            if grades[i] % 5 >= 3:
                grades[i] += (5 - (grades[i] % 5))
    return grades
