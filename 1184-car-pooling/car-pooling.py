class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        road = [0]*1001
        
        for passengers,start,end in trips:
            for i in range(start,end):
                road[i] += passengers
            
        for passengers in road:
            if(passengers > capacity):
                return False
        return True
