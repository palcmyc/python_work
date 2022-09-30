file_path = '/Users/mayicheng/Downloads/文稿/。txt/shakespeare.txt'
try:
  with open(file_path) as file_object:
    contents = file_object.read()
except:
  msg = 'Sorry, the file does not exit.'
else:
  words = contents.split()
  num_words = len(words)
  print(num_words)
