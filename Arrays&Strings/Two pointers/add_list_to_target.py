def foo(arr: list[int], target: int) -> bool:
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == target:
            return True
        elif arr[left] + arr[right] > target:
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
    return False
        
        
print(foo([2, 4, 5, 6, 8, 43], 6))