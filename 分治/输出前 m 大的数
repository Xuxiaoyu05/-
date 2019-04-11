# 给定一个数组包含 n 个元素，统计前 m 大的数并把这 m 个数从大到小输出

# 想法1：快排后输出，复杂度O(nlgn)
# 想法2：分治法，把前m大的元素都弄到数组最右边(O(n))，然后对最右边m个元素排序输出，总的复杂度O(n+mlgm)

# 输出前 m 大的数字
def Max_Mth(a, left, right, i):
  if left == right:
    return quickSort(a[left:], 0, len(a[left:])-1)[::-1]
  
  q = Partition(a, left, right)
  k = q - left + 1
  
  if i == k:
    return quickSort(a[q:], 0, len(a[q:])-1)[::-1]  # 若找到第m大的元素，元素右边的值都为大于该元素的值
  elif i < k:
    return Max_Mth(a, left, q-1, i)
  else:
    return Max_Mth(a, q+1, right, i-k)
  
# 快排
def quickSort(arr, left, right):
  if left >= right:
    return
  
  i = Partition(arr, left, right)
  quickSort(arr, left, i-1)
  quickSort(arr, i+1, right)
  
  return arr
  
# 划分
def Partition(arr, left, right):
  pivot = arr[left]
  i = left
  
  for j in range(left+1, right+1):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[left] = arr[i]
  arr[i] = pivot
  
  return i

alist = [1, 7, 11, 3, 5, 6, 4, 9, 8]
n = len(alist)
m = 2
i = n - m + 1  # 此处应为
print(Max_Mth(alist, 0, n - 1, i))
