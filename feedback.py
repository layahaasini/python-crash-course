name = input("Please enter your name: ")
print("Hi, " + name.title())
rating = int(input("Please rate our presentation out of 10, 10 being the highest: "))
if rating<=5:
    feedback = input("Please give us your feedback on how to improve!: ")
else:
    print("We're glad you enjoyed it!")
print("Thanks for the feedback!")  