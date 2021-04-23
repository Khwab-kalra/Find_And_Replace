def word_list(lines):
    words = set(lines.split(" "))
    counter(words, lines.split(" "))


d = {}


def counter(words, line):
    for i in words:
        c = []
        for j in range(0, len(line)):
            if i == line[j]:
                c.append(j)
            d[i] = c
        print(f'{i} found at index {c}')


def replacement():
    print("REplacement")
    for i in d:
        if i == replace:
            print("Replacing")
            l = lines.split(" ")
            for j in range(0, len(d[i])):
                l[d[i][j]] = new_word
    line = " ".join(l)
    print(line)


lines = input("Enter the string: ")
lines = lines.replace(",", "")
lines = lines.replace(".", "")
lines = lines.lower()
word_list(lines)
replace = input("Enter word to replace: ")
new_word = input("Word to be replaced with: ")
replacement()
