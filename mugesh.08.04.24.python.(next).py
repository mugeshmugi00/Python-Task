##def sum3(n):
##      add=0
##      for i in range(len(n)):
##          add+=n[i]
##      print(add)
##n=[1,2,3]
##sum3(n)    

def rotate_left3(nums):
  b=[nums[len(nums)0]] + nums[:len(nums)-1]
  return b
nums=[1,2,3]
print(rotate_left3(nums))
