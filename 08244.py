class Solution:
    def remove_element(self, nums, val):
        if not nums:
            return 0, nums
        else:
            index = 0
            for i in range(len(nums)):

                if nums[i] != val:
                    nums[index] = nums[i]
                    index += 1
        return index, nums[:index]


if __name__ == '__main__':
    obj = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(obj.remove_element(nums, val))
