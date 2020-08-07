#MILES PER HOUR CONVERSION

print("Welcome to miles per hour conversion app!")
mph=input("\n enter the speed in miles per hour please =>")

#for converting the miles into metres ===> miles*1609
mps=float(mph)*1609.34/(60*60)

#using round function for upto 2 decimals precision
mps=round(mps,2)
print("the entered speed in metres per second is=>",mps)

