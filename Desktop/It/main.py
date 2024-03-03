a = 12
b = "13"
# print(a + b)# Fatal

name_1 = "Shuhrat"
name_2 = " Jasur"
print(name_1 + name_2)

num_1 = 5
num_2 = "5"
print(num_1 * num_2)

number_1 = 12
number_2 = "12"

print(type(number_1), type(number_2))


lst = [1,2,3,4,5, "6"]

for x in lst:
    if type(x) == str:
        print(x)

string1 = "I am a programmer"
string = "I, am a, programmer"
y = string1.split(" ")
x = string.split(",")
print(y)
print(x)


sentence = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
ch = sentence.split(".")
print(len(ch))


sentence1 = ["banan", "anjir", "olma",]
print(sentence1)
sh = " ".join(sentence1)
print(sh)

name = "Ali"
print(name.upper())
print(name.lower())

if name == name.upper():
    print("Kichkinada yoz")

else:
    print("To'gri")









