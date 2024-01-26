''' You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? '''

def climbStairs(n):
       
    if n==1:
        return 1
    if n==2:
        return 2
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]
def main():
    n = 45
    print(climbStairs(n))


if __name__ == "__main__":
    main()
