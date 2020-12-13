def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if(ratings[i] > ratings[i - 1]):
                candies[i] = candies[i - 1] + 1
                
        sum = candies[-1]
        for i in reversed(range(len(ratings) - 1)):
            if(ratings[i] > ratings[i + 1]):
                candies[i] = max(candies[i], candies[i + 1] + 1)
            sum += candies[i]
        
        return sum