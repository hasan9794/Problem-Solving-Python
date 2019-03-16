# Program number 3 Count Pattern


def count_Pattern(text1, text2):
    tuple1 = text1
    tuple2 = text2

    str = ''.join(tuple1)
    tuple1String = str

    str = ''.join(tuple2)
    newString = str
    print(newString.count(tuple1String))

count_Pattern(('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f'))
