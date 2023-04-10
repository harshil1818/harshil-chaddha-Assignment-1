no_of_seconds=int(input("Enter no of Seconds:"))

if(no_of_seconds<60):
    print("no of seconds","seconds")

else:
    e=no_of_seconds//60
    f=no_of_seconds%60
# if statement alone tells us that if a condition is true it will execute a block of statements and if the condition is false it won’t.
    print(e,"minutes", f,"seconds")