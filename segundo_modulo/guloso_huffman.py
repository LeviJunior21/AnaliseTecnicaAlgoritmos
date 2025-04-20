def huffman(decoder, to):
    res = ""
    for i in to:
        for dec in decoder:
            if i == dec[0]:
                res += dec[1]
    return res
    

decoder = [
    ("A", "0"),
    ("B", "101"),
    ("C", "100"),
    ("D", "111"),
    ("E", "1101"),
    ("F", "1100")
]

to = "ABACAFE"
to = list(to)

encoder = huffman(decoder, to)
print(encoder)