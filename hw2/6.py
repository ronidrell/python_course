def get_two_sum(nums, k):
    ans = False
    for i in range (len(nums) - 1):
        for j in range (i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                ans = True
                return i, j
    if ans == False:
        return None

if __name__ == "__main__":
    print(get_two_sum([2, 7, 11, 15], 18))