astr="Hello Bob!"

try:
    istr=int(astr)
except:
    istr=-1   
print("First:",istr)


astr=2
try:
    istr=int(astr)
except:
    istr=-1
print("Second:",astr)