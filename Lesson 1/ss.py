def ss(nums):
	return sum(x**2 for x in nums)

lst = [2,4,5,6,7]
print ss(lst)

print max([2,5,3,1]), max([2,1,0,-5,4], key=abs)