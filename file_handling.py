import os

#f=open('hello.txt','x')
f = open("hdemo.txt", "w")
f.write("Now the file has more content!")
f.close()
if os.path.exists("hdemo.txt"):
  os.remove("hdemo.txt")
else:
  print("The file does not exist")