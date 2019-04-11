# 时间复杂度O(nlgn)

def MergeSort(a):
  if len(a) > 1:
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    
    MergeSort(left)
    MergeSort(right)
    
    # 合并
    i, j, k = 0
    
    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        
