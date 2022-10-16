#模板 for two sum problems 
def two sum(self, nums:List[int])->List[int]:
  nums.sort() #對數組排序
  #左右指針
  lo, hi = 0, len(nums)-1
  #根据 sum 和 target 的比较，移动左右指针
  while(lo < hi):
    sum = nums[lo] + nums[hi]
    if sum < target: 
      lo++
    elif sum > target: 
      hi--
    elif sum == target:
      return [nums[lo], nums[hi]]
  return []
