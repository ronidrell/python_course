def get_sorted_squares(nums):
    nums = [(x ** 2) for x in nums]
    nums.sort()
    return nums

if __name__ == "__main__":
    print(get_sorted_squares([-4, -1, 0, 3, 10]))
    print(get_sorted_squares([-7, -3, 2, 3, 11]))
