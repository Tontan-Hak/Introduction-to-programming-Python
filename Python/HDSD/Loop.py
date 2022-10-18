# code
marks = [60, 50, 40, 20, 90]
count = 0
for m in marks:
    if m >= 50:
        print(m)
        count = count + 1
passRate = count / len(marks)
print("The pass rate is", round(passRate * 100), "%")

# 
start = 1
end = 16
for n in range(start, end+1):
	print(n, 2**n)

# 
def convert(f):
    c = (f - 32) * 5 / 9
    c = round(c, 2)
    return c

def estimate(f):
    c = (f - 30 ) / 2
    c = round(c, 2)
    return c

for f in range(20, 120 + 1, 4):
    print(f, convert(f), estimate(f))

# 
def convert(f):
    c = (f - 32) * 5 / 9
    c = round(c, 2)
    return c

def estimate(f):
    c = (f - 30 ) / 2
    c = round(c, 2)
    return c

def main():
    for f in range(60, 101, 5):
        print(f, convert(f), estimate(f))

if __name__ == "__main__":
	main()