# Read the marks and store them in a list
marks = []            
keepReading = True
while keepReading:
    mark = int(input("Enter a mark: "))
    if mark == -99:
        keepReading = False
    else:
        marks.append(mark)