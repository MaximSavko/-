def Palindrop(st):
    if st == st[::-1]:
        print(st, ' - Слово палиндром')
    else: print(st, 'Слово не палиндром')

Palindrop(input())