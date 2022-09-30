def count_words(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "can't find"
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
	return num_words

numb = count_words('/Users/mayicheng/Downloads/文稿/。txt/shakespeare.txt')
print(numb)