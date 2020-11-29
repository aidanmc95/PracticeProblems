array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = 3

def removeDuplicates(self, nums: List[int]) -> int:
        spot = 1
        check = nums[0]
        length = len(nums)
        while(spot < length):
            if(check == nums[spot]):
                del nums[spot - 1]
                length = len(nums)
            else:
                check = nums[spot - 1]
                spot += 1
            print(nums)
            print(spot, check, length)
        print(nums)
        return len(nums)

print array