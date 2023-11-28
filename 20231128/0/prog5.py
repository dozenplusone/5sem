class C:
    word1, word2, word3 = input().split()


while s := input():
    match s.split():
        case [C.word1, *rd] if "yes" in rd:
            print("Case 1")
        case [C.word2]:
            print("Case 2")
        case [C.word3, *_, C.word2]:
            print("Case 3")
