players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print the first 3
print(players[0:3])

# print 4 from the beginnine
print(players[:4])

# print the 4th to the end
print(players[3:])

# print the ast 3
print(players[-3:])

# print every 2nd one up to 5
print(players[0:5:2])

for player in players[:3]:
    print(player.title())
