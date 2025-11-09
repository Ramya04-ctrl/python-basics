arr = [1, 2, 3, 5, 6]
expected = 0
actual= 0


for i in range(arr[0], arr[-1] + 1):
    expected = expected + i


for i in range(len(arr)):
    actual = actual+ arr[i]

missing = expected - actual
print( missing)
