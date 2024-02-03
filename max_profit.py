def solve(prices):
        max_profit = 0
        i=0
        j=1
        while i < len(prices):
            while j < len(prices):
                profit = prices[j] - prices[i]
                if profit <= 0:
                    i = j-1
                    # print(prices[j],prices[i])
                    break
                if profit > max_profit:
                    max_profit = profit 
                j += 1
            i+=1
            j = i+1
        return max_profit

print(solve([7,6,4,3,1]))
print(solve([7,1,5,3,6,4]))