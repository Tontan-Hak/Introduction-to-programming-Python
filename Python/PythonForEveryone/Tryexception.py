# Try / except
astr = 'Bob'
try:
    print('Hello') 
    istr = int(astr)
    print('There') 
except:
    istr = -1

print('Done', istr)

# Sample try
rawstr = input('Enter a number:')
try: 
    ival = int(rawstr)
except: 
    ival = -1

if ival > 0 :  
    print('Nice work')
else:  
    print('Not a number')