# Letter Counter


print("Hello welcome to letter counter app!")
x=input("Whats ur name?")
print("Hello",x)

print("I can count the no. of occurence of a letter in a message")

#taking input of message
msg=input("so,whats your message? => ")

#taking input of letter
let=input("which letter occurence would you like to count? = >")

count=0

#comparing the target letter with each letter in message
#since i want case irrespective, compare by converting them both into 
# any one case,here with uppercase
for letter in msg:
    if letter.upper()==let.upper():
        count+=1
print("Count=",count)
