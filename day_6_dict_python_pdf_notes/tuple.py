#Sample code for Tuple, Dictionary, Sets

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]:", tup1[0])
print("tup2[1:5]:", tup2[1:5])

my_anime = ('one piece', 'naruto', 'spy x family', 'btx', 'zenki')
print(len(my_anime))

my_grade = (88, 97, 76, 98, 84, 93, 75, 100)
print(max(my_grade))
print(min(my_grade))

anime_char = ['luffy', 'sanji', 'son goku', 'nami', 'robin']
print(anime_char)
tup_anichar = tuple(anime_char)
print(tup_anichar)
#del tup_anichar
#print(tup_anichar)
teamAnime = (my_anime + tup_anichar)
print(teamAnime)

Team7 = ('naruto', 'sasuke', 'sakura')
if 'sasuke' in Team7:
    print('Sasuke ay nasa Team 7!')

dict = {"Name":"Vinz", "Age":35, "Class":"First"}
#del dict['Age']
#dict.clear()
#del dict

print("dict['Name']:", dict['Name'])
dict['Age'] = 26
print("dict['Age']:", dict['Age'])
print("dict['Class']:", dict['Class'])
dict['School'] = 'Konoha ES'
print("dict['School']:", dict['School'])
numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
print(numbers)
fruits = {"apple", "banana", "cherry", "melon", "guava", "orange"}
print(fruits)
fruits.add("Guyabano")
print(fruits)
fruits.update(["manga", "grapes", "star apple"])
print(fruits)
fruits.remove('manga')
print(fruits)
fruits.discard('manga')
print(fruits)
