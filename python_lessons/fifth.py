planets = ['Mercury', 'Venus', 'Earth', 'Mars','Jupiter','Saturn','Uranas','Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line


multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult

print(product)

s = 'steganograpHy is the practicE of conceaLing a fiLe, message, image, or video within another file, message, image, Or video.'
msg = ''
for char in s:
    if char.isupper():
        print(char, end='')
print('\n')

for i in range(5):
    print("Doing important work. i =", i)

i = 0
while i < 10:
    print(i, end=' ')
    i +=1


squares = [n**2 for n in range(10)]
print(squares)


squares = []
for n in range(10):
    squares.append(n**2)
print(squares)


short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)


loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)


loud_short_planets = [
    planet.upper() + '!'
    for planet in planets
    if len(planet) < 6
]
print(loud_short_planets)

def count_negatives(nums):
    """Return the number of negative numbers in the given list.

    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative +1
    return n_negative

def count_negatives(nums):
    return len([num for num in nums if num < 0])


def count_negatives(nums):
    return sum([num < 0 for num in nums])

print(count_negatives([-3, -6, 7, 0, -2]))