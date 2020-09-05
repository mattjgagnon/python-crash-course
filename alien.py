alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print(alien_0)

# delete a key-value pair
del alien_0['points']
print(alien_0)

# get a key-value pair that may not exist (avoids an error)
point_value = alien_0.get('points', 'No point value assigned.')

print(point_value)
