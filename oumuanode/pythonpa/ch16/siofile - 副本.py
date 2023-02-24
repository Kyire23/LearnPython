from io import StringIO
f = StringIO('Hello\nPython\n')
for s in f:
    print(s.strip())
