primes= [2, 3, 5, 7]
planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],
]


my_favourite_things = [32, 'raindrops on roses', help]

print(planets[0])
print(planets[1])
print(planets[-1])
print(planets[-2])
print(planets[0:3])
print(planets[:3])
print(planets[3:])

print(planets[-3:])
print(planets[-7:0])
planets[3] = 'Malacandra'
print(planets)
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

print(planets[::-2])
print(len(planets))
print(sorted(planets))

print(sum(primes))
print(max(primes))
x = 12
print(x.imag)
c=12 + 3j
print(c.imag)

print(x.bit_length())
planets.append('Pluto')
print(planets)
planets.pop()
print(planets)
planets.index('Earth')
print("Earth" in planets)
print("Calbefraques" in planets)
t = (1, 2, 3)
print(t)
x = 0.125
print(x.as_integer_ratio())
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

a = 1
b = 0
a, b = b, a
print(a, b)