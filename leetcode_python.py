#%%
'''
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
'''
from typing import List
def twosum(nums:List[int],target:int)->List[int]:
    hashtable=dict()
    for id,num in enumerate(nums):
        if target-num in hashtable:
            return [hashtable[target-num],id]
        else:
            hashtable[num]=id
    return []
twosum([2,3,4,5],8)
#%%
'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
'''
from typing import List

def removeDuplicates(nums:List[int])->int:
    if not nums:
        return 0
    else:
        n=len(nums)
        slow=fast=1
        while fast<n:
            if nums[fast]!=nums[fast-1]:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow
removeDuplicates([1,2,3,3,3,4])

#%%
'''
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
'''
from typing import List
def maxProfit(prices:List[int])->int:
    profit=0
    for i in range(1,len(prices)):
        tem=prices[i]-prices[i-1]
        if tem>0:profit+=tem
    return profit
maxProfit([3,4,2,4,5])

#%%
