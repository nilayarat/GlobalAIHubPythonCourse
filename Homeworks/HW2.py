# liste = [1, 2, 3, 4, 5, 6, 7, 8]
# liste[:round(len(liste)/2)], liste[round(len(liste)/2):] = liste[round(len(liste)/2):], liste[:round(len(liste)/2)]
# print(liste)
###########
n = int(input("Please, enter a single digit integer"))
if 0 <= n < 10:
    for i in range(n):
        if i%2==0:
            print(i)
