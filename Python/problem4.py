array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = 3

def removeDuplicates(self, nums: List[int]) -> int:
    if (len(nums) == 0) return 0;
    spot = 1
        check = nums[0]
        length = len(nums)
        while(spot < length):
            if(check == nums[spot]):
                del nums[spot - 1]
                length = len(nums)
            else:
                check = nums[spot]
    return len(nums)

print array