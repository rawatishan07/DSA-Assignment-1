def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
   
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

def main():
    arr = [10, 20, 30, 40, 50] # List to test the algorithm
    target = 30
    result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    print(f"Index of {target}: {result}")
    
if __name__ == "__main__":
    main()
