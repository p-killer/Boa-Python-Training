class File():
    #sets up the object
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    #opens and returns the file
    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    #just closes the file
    def __exit__(self, *args):
        self.open_file.close()

files = []
for _ in range(10000):
    with File('foo.txt', 'w') as infile:
        infile.write('Hello ... how r u ....')
        files.append(infile)

print("All done safely ")
# phton demo.py