def minTaps(self, n: int, ranges: List[int]) -> int:
        print(n)
        new_list = a = [0] * (n + 1)
        
        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            
            new_list[left] = max(new_list[left], right - left)
            
        print(new_list)
        start = end = count = 0
        
        while(end < n):
            count += 1
            start, end = end, max(i + new_list[i] for i in range(start, end + 1))
            
            if(start == end):
                return -1
        
        return count