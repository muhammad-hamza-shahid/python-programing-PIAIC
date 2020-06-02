for a in range(5):
    print("hello")

for numbers in range(10):
    print(numbers)

for step in range(1,20): #start from the 1 index to 19 index
    print(step)

for jump in range(1,20,2):
    print(jump)

for reverse in range(10,1,-2):
    print(reverse)

cities = ["karachi","rawalpindi","multan"]
print(cities)

for city in cities:
    print(f'city in observation is {city}')

for a in 'Pakistan':
    print(a)

for a in range(10):
    if a==5:
        break
    print(a)

for a in range(10):
    if a==5:
        continue
    print(a)

for a in range(10):
    if a==5 or a==3:
        continue
    print(a)