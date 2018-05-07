shows = ["The Walking Dead",
         "Entourage",
         "The Sopranos",
         "The Vampire Diaries" ]
for show in shows:
    print(show)

for i in range(25, 51):
    print(i)

for x, show in enumerate(shows):
    print(i)
    print(show)

while True:
    ans = input("Guess a number or type 'q' to quit.\t\t")
    nums = ["1","15","5","9"]
    if ans in nums:
        print("Correct!")
    elif ans == "q":
        break
    else:
        print("Wrong!")
    
numsA = [8, 19, 148, 4]
numsB = [9, 1, 33, 83]
final = []
for x in numsA:
    for y in numsB:
        result = x * y
        final.append(result)

print(final)
