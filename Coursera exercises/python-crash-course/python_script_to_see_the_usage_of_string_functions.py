Word = "StuNninG"
print(Word.upper())
print(Word.lower())
print(" ".join(["This", "world", "has", "no", "boundaries."]))
print("....".join(["How", "big", "is", "this", "Universe?"]))
# print(" ".join("Hai", "How", "are", "you?")), this is not possible.
print("This is another example".split())#The inverse of the join method is the split method. By default, it splits by any whitespace characters. 
print("This is another example".split("i"))#You can also split by any other characters by passing a parameter.

String = "YtKTST25555"
#The isnumeric method can check if a string is composed of only numbers.
if String.isnumeric():
    print(int(String))
else:
    String = "111000"
    print(int(String))

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

name = "Manny"
print("Your Lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)


answer = input("Enter a number: ")
x = 10**(len(answer) - 1)

terms = []
for i in answer:
    if i == "0":
        x = x//10
        continue
    else:
        terms.append(f"({i} * {x})")
        x = x//10

print(f"{answer} =", " + ".join(terms))