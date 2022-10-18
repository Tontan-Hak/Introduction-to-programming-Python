# calculate the average
totalMarks = 0
nrMarks = len(marks)    # number of marks
for mark in marks:
    totalMarks = totalMarks + mark
average = totalMarks / nrMarks

# Display the marks
for mark in marks:
    if mark >= average:
        print(mark, "*")
    else:
        print(mark)