# for i in range(2,10,2):
#     print(i)
#
#
#
# x = 2
# while x < 10:
#     print(x)
#     x = x+2
def nombre_pairs_while(n):
    i = 2
    while (i <= n):
        if i % 2 == 0:
            print(f"#{i}")
        i += 1

nombre_pairs_while(10)
print()
nombre_pairs_while(20)