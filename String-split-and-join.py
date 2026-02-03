def split_and_join(line):
    line1 = (line.split(" "))
    print("-".join(line1))

if __name__ == '__main__':
    line = input()
    result = (line.split(" "))
    print("-".join(result))
