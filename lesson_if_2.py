def stroki (stroka1, stroka2):
    if type(stroka1) is not str or type(stroka2) is not str:
        return 0
    else:
        if stroka1 == stroka2:
            return 1
        elif len(stroka1) > len(stroka2):
            return 2
        elif stroka2 == "learn":
            return 3
        else:
            return 4

a = stroki ("test", "test2")
print(a)

a = stroki ("test", "test")
print(a)

a = stroki ("test1", "test")
print(a)

a = stroki ("test", "learn")
print(a)

a = stroki (21, 22)
print(a)

a = stroki (21, "test")
print(a)