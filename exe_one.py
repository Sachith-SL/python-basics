#Even or Odd
num = int(input("Enter a number : "))

if num <= 0:
    print("not a positive value")
elif num %2 == 0:
    print("Even")
else:
    print("Odd")    
