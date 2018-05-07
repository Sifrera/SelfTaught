print("String one.")
print("String two.")
print("String three.")

x = 9
if x < 10:
    print("%d is less than 10" % x)
else:
    print("%d is over or equal 10" % x)

y = 24
if y < 10:
    print("%d is less than 10" % y)
elif y >= 10 and y < 25:
    print("%d is between 10 and 25" % y)
else:
    print("%d is equal or over 25" % y)

print(y%x)
print(y//x)

age = 21
if age == 20:
    print("Damn you young")
elif age == 21:
    print("Legal at last")
else:
    print("You old as dirt")

