def test_practice(arr):
    i = 0
    x = len(arr) - 1
    while i < x:
        if arr[i] == arr[x]:
            i += 1
            x -= 1
        else:
            return False
    return True

print(test_practice("racecar"))