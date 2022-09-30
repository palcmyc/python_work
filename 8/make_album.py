def make_album(singer, albums, number = ''):
	alb = {}
	if number:
		alb['singer'] = singer
		alb['album'] = albums
		alb['number'] = number
	else:
		alb['singer'] = singer
		alb['album'] = albums
	return alb
albums = make_album('zhoujielun','qilixiang','10')
print(albums)