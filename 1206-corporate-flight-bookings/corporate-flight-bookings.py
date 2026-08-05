class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        # But the problem says there are no bookings initially. f = [1]*(n+1)

        f = [0] * (n+1) # this is for intially no bookings

        # Difference Array
        for i,j,val in bookings:
            f[i-1] += val
            if(j < n):
                f[j] -= val
        # Apply the prefix sum 
        for i in range(1,n):
            f[i] += f[i-1]
        return f[ : n]