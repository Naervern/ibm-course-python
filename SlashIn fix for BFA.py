def updateslashin(text):
    newtext = ''
    for line in text:
        if '/in' in line and '/e' not in line:
            editing = line.split()
            for word in editing:
                if word == '/in':
                    editing.insert(editing.index(word)+2,'/e')
            line = ' '.join([word for word in editing])
        print(line)
        newtext += line + '\n'
    return newtext

def openfile():
    filename = input("Specify the name of the macro cache file (without .txt extension) or default to \"macros-cache.txt\". Make sure it's in the root directory.\n")
    if filename == '':
        filename = 'macros-cache'
    try:
        f = open(filename+".txt", "r")
    except IOError:
        print('File not located')
        filename, f = openfile()
    return filename, f

def main():
    title = "Adding /e after /in macros"
    filename, f = openfile()
    f2 = open(filename.lower()+"-fixed.txt", "w")
    f2.write(updateslashin(f.read().splitlines()))
    f.close()
    f2.close()
    print("Macros cache generated as", filename.lower()+"-fixed.txt")
    input()

if __name__ == '__main__':
    main()