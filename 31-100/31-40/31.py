class CoinSums(object):
    def __init__(self):
        self.cnt = 0
        
    def __call__(self, target, coins):
        for coin_idx, which_coin in enumerate(coins):
            ceiling = target // which_coin
            for number_of_coin in range(ceiling, 0, -1):
                agg = which_coin * number_of_coin
                remaining = target - agg
                if not remaining:
                    self.cnt += 1
                if coin_idx < len(coins)-1:
                    self.__call__(remaining, coins[coin_idx+1:])
        return self.cnt

def main():
    coinsums = CoinSums()
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    result = coinsums(200, coins)
    print(result)

if __name__ == "__main__":
    main()
