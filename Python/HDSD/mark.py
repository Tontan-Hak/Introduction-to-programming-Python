# We have a class of 5 students. Each has a mark for assignment 1, assignment 2 and exam
mark = [
    [60, 55, 80],
    [40, 30, 40],
    [80, 7, 85],
    [20, 10, 30],
    [88, 70, 95]
    ]
total = 0 
nbStudents = len(mark)
for student in mark: 
    assignment2 = student[1]
    print(assignment2)
    total = total + assignment2
arverage = total / nbStudents
print("average:", arverage)