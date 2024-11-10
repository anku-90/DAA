def knapsack_dp(values,weights,capacity):
    n=len(values)
    dp =[[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1]<=w:
                include_item = values[i-1]+dp[i-1][w-weights[i-1]]
                exclude_item = dp[i-1][w]

                dp[i][w] = max(include_item,exclude_item)
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][capacity]

def main():
    num_items=int(input("enter the number of items:"))
    weights=[]
    values=[]

    for i in range(num_items):
        weight=int(input(f"enter the weight of {i+1} item:"))
        value=int(input(f"enter the value of {i+1} item:"))
        weights.append(weight)
        values.append(value)

    capacity=int(input("enter the capacity of knapsack(Dp):"))

    max_value  = knapsack_dp(values,weights,capacity)
    print(f"the maximum value of dp knapsack is :{max_value}")

main()
        