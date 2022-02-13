def Card(a):
    a = str(a)
    b = '*'
    b *= len(a)-4
    print(b, a[len(a)-4:])

Card(input())