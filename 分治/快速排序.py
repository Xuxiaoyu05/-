# 选择基准元素，将大于基准的元素放在右边，将小于基准的元素放在左边，再分别对两边进行排序

def quickSort(a, left, right):
  if left < right:
    i = Partition(a, left, right)
    quickSort(a, left, i-1)
    quickSort(a, i+1, right)
  
  return a


def Partition(a, left, right):

  pivot = a[left]
  i = left
  
  for j in range(left+1, right+1):
    if a[j] <= pivot:
      i += 1
      a[i], a[j] = a[j], a[i]
  
  # 将基准元素移到正确位置
  a[left] = a[i]
  a[i] = pivot
  
  return i
  
alist = [3, 5, 6, 3, 9, 8]

print(quickSort(alist, 0, len(alist)-1))
