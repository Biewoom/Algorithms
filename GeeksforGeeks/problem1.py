def findMaxSubarraySum(arr ,n, k):
    print("arr: ", arr)
    Sum = 0

    for i in range(0, k):
        Sum += arr[i]**2

    for i in range(k, n):
        Sum += arr[i]
        
    Max = Sum

    print("initial Max: ", Max)
    for i in range(0, n - k + 1):
        Sum -= arr[i]**2; Sum += arr[i]
        Sum -= arr[i + k - 1]; Sum += arr[i+k-1]**2
        Max = max(Max, Sum)

    return Max


if __name__ == '__main__':
    t = int(input())
    for iter_t in range(t):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        result  = findMaxSubarraySum(arr, N, K)
        print(result)
