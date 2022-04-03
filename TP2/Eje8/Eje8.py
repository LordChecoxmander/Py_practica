from functools import reduce

# que otra estructura se puede usar que no sean listas sueltas??
list_1=('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T')
list_2=('D', 'G')
list_3=('B', 'C', 'M', 'P')
list_4=('F', 'H', 'V', 'W', 'Y')
list_5=('K')
list_8=('J', 'X')
list_10=('Q', 'Z')


palabra_lis = list(input("ingrese una palabra").upper())

print(palabra_lis)
total =0

for x in palabra_lis:
    match x:
        case x if list_1.count(x) == 1:
            total += 1
        case x if list_2.count(x) == 1:
            total += 2
        case x if list_3.count(x) == 1:
            total += 3
        case x if list_4.count(x) == 1:
            total += 4
        case x if list_5.count(x) == 1:
            total += 5
        case x if list_8.count(x) == 1:
            total += 8
        case x if list_10.count(x) == 1:
            total += 10

print(total)


"""def valor(x):
    print(x)
    match x:
        case x if list_1.count(x) == 1: return 1
        case x if list_2.count(x) == 1: return 2
        case x if list_3.count(x) == 1: return 3
        case x if list_4.count(x) == 1: return 4
        case x if list_5.count(x) == 1: return 5
        case x if list_8.count(x) == 1: return 8
        case x if list_10.count(x) == 1: return 10

sad = list(filter(valor, palabra_lis))
print(sad)"""
