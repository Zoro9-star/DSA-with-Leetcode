#Container with Most Water

height = [2,3,4,5,18,17,6] #The given heights which is basically an array

def maxArea(height):  #defining a function with height parameter
    left = 0          #assigning left variable with value 0 which is the starting point of the array(index 0)
    right = len(height)-1     # assigning right variable with value 6 (length of array is 7)
    max_area = 0             #assigning area as 0

    while left<right:      #first condition (0<6(True))
        width = right - left  #defining a varible width = 6-0 = 6
        h = min(height[left],height[right])    #defining a variable h which is min(2,6)= 2
        area = h*width   #another varible area which will be 6*2 = 12
        max_area = max(max_area,area)  # updating max_area with max(0,12)= 12 , from now max_area = 12

        if height[left] < height[right]:  # here 2<6 (True)
            left +=1  # adding 1 with left means left = 1
        else:
            right -= 1
    print(max_area)
maxArea([2,3,4,5,18,17,6])
