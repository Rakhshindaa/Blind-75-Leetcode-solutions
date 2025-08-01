def knapsack(W, val, wt):
    n = len(wt)
    #initialize 2D array to store the max weights along with their profits. 
    #rows will be the number of weights(bags) and columns will be the max capacity of the bag
    #dp[i][j] will represent the current max profit 
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    #traverse through each weight along with their corresponding profit
    for i in range(n + 1): # i=items 
        for j in range(W + 1): #j=profits
            # if there is no item or the knapsack's capacity is 0
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                pick = 0
                # Pick ith item if it does not exceed the capacity of knapsack
                if wt[i - 1] <= j:
                    #adding the current profit+profit of the diagonal value
                    pick = val[i - 1] + dp[i - 1][j - wt[i - 1]]
                # Don't pick the ith item if it exceeds max capacity
                notPick = dp[i - 1][j]
                #comparing the profit values if we pick the item and if we dont pick the item
                dp[i][j] = max(pick, notPick)
    #returning answer/solution
    return dp[n][W] 
#inputs
val = [1, 2, 3] #profits
wt = [4, 5, 1] #weights
W = 4 #maximum weight of the bag
print(knapsack(W, val, wt))