number = int(input("Enter the number: "))
power = int(input("Enter power: "))

s = 1
for i in range (0,power):
    s = (s * number)
print (f'The number: {number} to the power of {power} is: ',s)