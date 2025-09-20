nums = [12,34,54,21,65,45]
print(nums)
print(nums[2])
print(nums[2:])
print(nums[:2])
print(nums[-1])

names = ["vishal","python","ashish"]
print(names)
value = ["fruits",65,32.5]
print(value)

print(nums,names,value)

nums.append(85)
nums.insert(2,77)
nums.remove(65)
print(nums)
del nums[2:]
print(nums)
nums.extend([22,56,21,20])
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
nums.sort()
print(nums)

name = "Vishal"
print(name[-3])

lst = [i for i in range(1,5)]
print(lst)
lst = [i for i in range(1,25) if i%2 != 0 ]
print(lst)