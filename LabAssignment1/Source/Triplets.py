def three_sum(nums): #define the function
  result = [] #define the list
  nums.sort()  #sort the numbers
  for i in range(len(nums)-2): #loop from 0 to length of list - 2
    if i> 0 and nums[i] == nums[i-1]: #check if conecutive nos are equal except for 1st element
      continue
    l, r = i+1, len(nums)-1 #define l with index as 1 and r with last index value
    while l < r:
      s = nums[i] + nums[l] + nums[r] #calculate sum of first two elements and last element
      if s > 0:  #check if sum is greater than zero
        r -= 1  #reduce the index value of r by 1 and continue the loop
      elif s < 0: #check if the sum is less than zero
          l += 1 #increase the index value by 1 and continue loop
      else:
        # if sum is zero then append to result list
        result.append((nums[i], nums[l], nums[r]))
        # remove duplicates
        while l < r and nums[l] == nums[l+1]:
          l+=1
          while l < r and nums[r] == nums[r-1]:
            r -= 1
            l += 1
            r -= 1
          return result

x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ] #define the list
print(three_sum(x))   #calls the function and prints the return value