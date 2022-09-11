import random
print1(random.randint(20, 50))

#multiple randint
for i in range(3):
    print(random.randint(1, 100))

anime = ['luffy', 'nami', 'robin', 'sanji', 'madara', 'kakashi']
print(random.choice(anime))

random.shuffle(anime)
print(anime)
