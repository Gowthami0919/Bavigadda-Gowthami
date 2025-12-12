n = int(input())

if n <= 0:
    print("Series can't be started")
else:
    start = 2
    for i in range(1, n):
        print(start, end=", ")
        start += 2
    print(start)