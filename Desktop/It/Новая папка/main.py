person = {
    "name" : "Ali",
    "age" : [1,23,1,43,],
     "pozition ":True,

}
print(person["age"])

person["name"] = "Kamoliddin"
person["place"] = "Olmaliq"

print(person)



a = (1,)
b = (1)
print(type(a))
print(type(b))


x = person.get("name")# bu keyga murojat qilganda valueni olib keladi va bu alohida joy ochib ishlatiladi hamda data typelar kopligida get bilan ovosak boladi

y =person.values()
print(y) #bu bizga valuelarni olib keladi


person.update(person)
print(person) # bu bizga obyektni update qilib beradi

person.pop("name") # bu bizga key orqali malumotni ochirib beradi

person.copy()
print(person) # bu bizga obyektni copy qilib beradi

person.clear()
print(person) # bu bizga obyektni tozalab beradi

person.fromkeys() #


person.popitem()
print(person)

#del person["name"] #bu bizga key orqali valueni ochirib beradi
#del person #bu holatda person obyektti ochib ketadi
