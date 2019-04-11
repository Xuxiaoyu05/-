# 在排序数组 a 里查找元素p，如果找到，则返回元素下标，如果找不到，则返回-1
# 时间复杂度O(lgn)

def BinarySearch(a, p):
  left = 0
  right = len(a) - 1  # 右端点
  
  while left <= right:  # 当查找区间不为空
    mid = left + (right - left) // 2
    if p == a[mid]:
      return mid
    elif p > a[mid]:
      left = mid + 1
    else:
      right = mid - 1
  return -1
