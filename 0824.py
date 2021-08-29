class Solution:
    def remove_duplicates(self,nums) -> int:
        if not nums:
            return 0
        else:
            fast = 1
            slow = 1
            n = len(nums)
            while fast < n:
                if nums[fast] != nums[(fast - 1)]:
                    nums[slow] = nums[fast]
                    slow += 1
                fast += 1
            return slow


if __name__ == '__main__':
    obj = Solution()
    nums = [0, 0, 1, 1, 2, 3]
    print(obj.remove_duplicates(nums))
