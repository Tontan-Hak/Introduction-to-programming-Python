# ind the min, max and average of mark that are >= 10
from traceback import print_tb


mark = [80, 5, 20 , 30 , 90, 70]

smallest = 100
biggest = 0 
total = 0 
nrMarks = 0     # nuimber of marks >=0

for mark in mark: 
    if mark > 10: 
        total = total + mark 
        nrMarks = nrMarks + 1 
        if mark < smallest: 
            smallest = mark
        if mark > biggest:
            biggest = mark
average = total / nrMarks
print("mininmum mark: ", smallest)
print("maximum mark:", biggest)
print("average mark: ", round(average))
