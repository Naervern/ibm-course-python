def main():
    f = open("macros-cache.txt", "r")
    newtext = ''
    for line in f.read().splitlines():
        if '/in' in line and '/e' not in line:
            editing = line.split()
            for word in editing:
                if word == '/in':
                    editing.insert(editing.index(word)+2,'/e')
            line = ' '.join([word for word in editing])
        print(line)
        newtext += line + '\n'
    f = open("macros-cache.txt", "w")
    f.write(newtext)
    f.close()

if __name__ == '__main__':
    main()