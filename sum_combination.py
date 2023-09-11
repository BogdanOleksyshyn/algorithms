
def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(1, target + 1):
        for n in nums:
            if n <= i:
                dp[i] += dp[i - n]

    return dp[target]

if __name__ == "__main__":
    result = combinationSum4([1,2,3], 4)
    print(result)