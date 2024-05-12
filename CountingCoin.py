def counting_coin(arr, n):
	res = []
	arr = sorted(arr)
	while n != 0:
		for i in range(len(arr)-1, -1, -1):
			if arr[i] <= n:
				n -= arr[i]
				res.append(arr[i])
				break
	return res
				
arr = [1, 2, 5, 10]
n = 18
print(counting_coin(arr, n))