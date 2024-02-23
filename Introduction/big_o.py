arr = [1, 2, 3, 4]  # Example array, you can replace it with your own values

for i in range(len(arr)):
    for j in range(i, len(arr)):
        print(arr[i] + arr[j])
