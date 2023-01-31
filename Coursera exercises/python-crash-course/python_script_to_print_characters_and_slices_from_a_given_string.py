print("1) String indexing Example")
saved_string = "cprogramming"
print(saved_string[1])
print(saved_string[10])
print(saved_string[5])
print(saved_string[11])
print(saved_string[-5])
print(saved_string[-1])

print("2) String Slicing Example")
#slicing example
fruit = "pineapple"
print(fruit[1:4]) #here start index is 1 and end is 4 MINUS 1
print(fruit[:4]) #here start index is 0
print(fruit[4:]) #here start index is 4 and end is length of the string MINUS 1

print("3) String Slicing Usage")
message = "A kong string with a silly typo"
#message[2] = "l" this gives error
new_message = message[0:2] + "l" + message[3:]
print(new_message)

print("4) Printing index of characters from the String")
pets = "Cats Dogs"
print(pets.index("Cats"))
print(pets.index("Dog"))
print(pets.index("s"))
#print(pets.index("X")) gives error