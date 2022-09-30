def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians,great_magicians):
	while magicians:
		great_magicians.append(magicians.pop() + ' the Great')

great_magicians = []
magicians = ['liu qian','eric','ani','ma yicheng','anne']
make_great(magicians[:],great_magicians)
show_magicians(great_magicians)
print('\n')
show_magicians(magicians)