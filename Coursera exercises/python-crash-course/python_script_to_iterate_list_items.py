def greet_friends(friends):
    for friend in friends:
        print("Hi "+ friend)

greet_friends(["Ryan", "Fred", "Jack", "Shawn", "Maron"])
greet_friends("Barry")
print(greet_friends("Haron")) #Notice a None printed in the output. This is because we don't return anything but we use print here
