# Ass 3.2
H = input("Enter hours: ")
R = input("Enter rate: ")
try:
    h = float(H)
    r = float(R)
except:
    print("Error, please enter numberic input")
    quit()
print(h,r)
if h > 40: 
    reg = h * r 
    otp = (h - 40.0)*(r*0.5)
    xp = reg * otp
else:
    xp = h*r 
print("Pay",xp)