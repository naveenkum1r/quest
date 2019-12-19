x = 'Pluto is a planet'
y = "Pluto is a planet"
print(x == y)


print("Pluto's a planet!")
print('My dog is named "Pluto"')
hello = "hello\nworld"
print(hello)
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print(triplequoted_hello == hello)
print("hello")
print("world")
print("hello", end='')
print("pluto", end='\n')
planet = 'Pluto'
print(planet[0])
print(planet[-3:])
print(len(planet))
print([char+'! ' for char in planet])
claim = "Pluto is a planet!"
print(claim.upper())
print(claim.lower())
print(claim.index('plan'))
print(claim.startswith(planet))
print(claim.endswith('dwarf planet'))
words = claim.split()
print(words)
datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year,month,day)
print('/'.join([month, day, year]))
print(' 🎃 '.join([day, month, year]))
print(planet + ', we miss you.')
position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me")
print("{}, you'll always be the {}th planet to me. ".format(planet, position))
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(planet, pluto_mass, pluto_mass / earth_mass, population,))
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)
numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])
numbers['eleven'] = 11
print(numbers)
numbers['one'] = 'Pluto'
print(numbers)
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial={planet: planet[0] for planet in planets}
print(planet_to_initial)
print('Saturn' in planet_to_initial)
print('Beteluese' in planet_to_initial)
for k in numbers:
    print("{} = {}".format(k, numbers[k]))


print(' '.join(sorted(planet_to_initial.values())))


for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))