#1
# def afficher_nombre_pair(n):
#     for i in range(2, n + 1):
#         if i % 2 == 0:
#             print(f"#{i}")
#
#
#
# afficher_nombre_pair(10)


def afficher_nombre_pair(n):
    i = 2
    while (i <= n):
        if i % 2 == 0:
            print(f"#{i}")
        i += 1

afficher_nombre_pair(10)