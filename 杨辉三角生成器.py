def yh():
    a = b = [1]
    while True:
        yield a
        for i in range(1,len(a)):
            b[i] = (a[i-1] + a[i])
        b.append(1)
        # print(b)
        a = b.copy()

l = yh()

print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))