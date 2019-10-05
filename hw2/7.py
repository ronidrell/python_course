def get_three_sum(nums, k):
    ans = False
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums)-1):
            for l in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[l] == k:
                    ans = True
                    return i, j, l
    if ans == False:
        return None


if __name__ == "__main__":
    print(get_three_sum([2, 7, 11, 15], 24))