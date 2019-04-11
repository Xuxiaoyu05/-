# reverse_order_number# 给定一个数组 a 包含 n 个元素，如果其中存在j, k，满足 j < k 且 a[j] > a[k]，则(j, k) 是这个排列的一个逆序
# 一个排列含有逆序的个数称为这个排列的逆序数

# 遍历方法：时间复杂度O(n**2)

# 分治方法：时间复杂度O(nlgn)，事实上是归并排序的变形
# 分治思想分析：（1）将数组分为两部分，分别求出左边的逆序数和右边的逆序数；
#              （2）再计算有多少是由左半边取一个数和右半边取一个数构成(关键：左半边和右半边都是排好序的)

def reverse_order_number(a):
  count = 0
  R_MergeSort(a, count)
  return count
  
def R_MergeSort(a, count):
  if len(a) > 1:  # 不少于两个元素才分为左边数组和右边数组
    length = len(a)
    mid = length // 2
    left = a[:mid]
    right = a[mid:]
    
    R_MergeSort(left)
    R_MergeSort(right)
 
 
  i, j, k = 0, 0, 0
  
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      a[k] = left[i]
      i += 1
    else:
      count += 1
      a[k] = right[j]
      j += 1
    k += 1
  
  while i < len(left):
    a[k] = left[i]
    count += len(right)
    i += 1
    k += 1
  
  while j < len(right)
    a[k] = right[j]
    j += 1
    k += 1
  
  return a
  
alist = [10, 8, 7, 3, 12, 11, 5, 2]
print(reverse_order_number(alist))
