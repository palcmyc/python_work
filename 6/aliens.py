alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]
for alien_number in range(3,31):
	alien_new = {'color': 'green', 'points': 5}
	aliens.append(alien_new)

for alien in aliens[:30]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
	print(alien)
