#list

#有序，可以包含任何类型的对象
list1 = [1,2,[3,4,5],'w1',True]
print(list1) #打印所有元素
print(list1[0]) #打印单个元素
print(list1[-1]) #打印倒数第一个元素
print(len(list1)) #长度
print(list1[0:3]) #包前不包后
print(list1[:3])
print(list1[3:])
print(list1[:])
print(list1[0:5:2]) #from 0 to 5 with a step of 2
# step can be negative but cannot be 0
print(list1[::-1]) # reverse


nums1 = [1,2,3]
nums2 = [4,5,6]
nums = nums1 + nums2;
nums = nums * 2
print(nums)
print(1 in nums)
print(2 not in nums)
print(max(nums))
print(min(nums))

print(nums.index(2)) #索引
print(nums.count(2)) #计数

str = "hello"
list2 = list(str) #string转list
print(list2)
list2[0] = 'H'   #改变元素
print(list2)

#添加元素
list2.append('.') #到最后
list2.insert(0,'*') #到指定位置
print(list2)
list2.extend(['World','*']) #追加新的序列到原来的队列尾部
print(list2)


#删除元素
list2.pop(0) #参数是索引，不写默认删除最后一个
print(list2)

list2.remove('.') #根据元素，如果有多个默认删第一个
print(list2)

list2.clear()
print(list2)

#翻转与排序
list3 = [1,2,3,4,5]
list3.reverse()
print(list3)

list3.sort()
print(list3)

list3.sort(reverse = True)
print(list3)

for i in list3:
    print(i)

r = range(5)
print(list(r))

for i in range(5):
    print(i)
