List = ["a", "b", "a", "c", "c", "e", "a"]

def test(List):
    return list(dict.fromkeys(List))

print(test(List))