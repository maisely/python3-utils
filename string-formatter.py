def get_name(n, h):
    return f"Hi my name is {n} and I like {h}"


person = {"id": 1000, "age": 27}
name = "Maise"
hobby = "exercise"

text1 = "Hi my name is {} and I like {}".format(name, hobby)
text2 = "Hi my name is %s and I like %s" % (name, hobby)
text3 = f"Hi my name is {name} and I like {hobby}"
text4 = "Hi my ID is {id} and my age is {age}".format(**person)
text5 = f"Hi my ID is {person['id']} and my age is {person['age']}"

print(text1)
print(text2)
print(text3)
print(get_name("Dao", "food"))
print(text4)
print(text5)
