class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        c=0
        left,right=0,len(numbers)-1
        res=[]
        while left<=right:
            sum=numbers[left]+numbers[right]
            if sum == target:
                res=[left+1,right+1]
                return res
                break;
            elif sum < target:
                left+=1
            elif sum > target:
                right-=1

            
          
        