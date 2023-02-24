# Assignment 4.3
def computepay(h, r):
    if h <= 40:
        return h*r 
    else:
        return (h*r)+((h-40)*(r/2))

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate: "))
p = computepay(hrs, rate)
print("Pay", p)

# other way
#function
def computepay(hours, per_rate_hours):

    #overtime

    if (hours>40):
        pay = hours * per_rate_hours
        overtime = (hours - 40)   * (0.5 * per_rate_hours)
        payment = pay + overtime

    else:
        payment = hours * per_rate_hours
    return payment


#code begins
hours = input("Enter Hours: ")
per_rate_hours = input("Enter Per Rate Hour: ")


#try and except
try:
	f_hours= float(hours)
	f_per_rate_hours=float(per_rate_hours)
except:
    print("Error")
    quit()

final_pay = computepay(f_hours, f_per_rate_hours)
print("Pay", final_pay)

# other way
def computepay(h,r):
    if h<=40:
        pay=h*r
    elif h>40:
        pay=40*r+(h-40)*r*1.5
        return(pay)

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
p = computepay(h,r)
print(p)