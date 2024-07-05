my_dict = {
    "Albert": 21,
    "Franc": 25,
    "Yarik": 22,
    "Anton": 27,
}
print("Созданный 'словарь':", my_dict)
print("Значение по существ.ключу:", my_dict.get("Franc"))
print("Значение по отсутст.ключу:", my_dict.get("Kirill"))
my_dict.update({"Stepan": 24, "Misha": 26})
print("Удалённое значение:", my_dict.pop("Albert"))
print(my_dict)

my_set = {2, 2, 2, 3, 4, 5, "ABBA", "ABBA", "CHEAT", (5, 6, 7), (5, 6, 7), (1, 1)}
print("Множество новое:", my_set)
my_set.update([7, "UPDATE"])
my_set.pop()
print("Множество измененное:", my_set)