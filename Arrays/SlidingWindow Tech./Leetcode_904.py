# Ques No 904 - Fruit Into Baskets:

# Problem Statement:
# You are visiting a farm that has a single row of fruit trees arranged from left to right. 
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
#  You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. 
# The picked fruits must fit in one of your baskets.
#Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.



# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].



class SOlution:
    def totalFruit(self,fruits):
        low , high , res = 0,0,0
        seen = {}
        for high in range(len(fruits)):
            if fruits[high] in seen:
                seen[fruits[high]]+=1
            else:
                seen[fruits[high]]=1
            while len(seen)>2:
                seen[fruits[low]]-=1
                if seen[fruits[low]]==0:
                    del seen[fruits[low]]
                low+=1
            if len(seen) <= 2:
                res = max(res , high-low+1)
        return res
obj = SOlution()
print(obj.totalFruit([0,1,2,2]))
            