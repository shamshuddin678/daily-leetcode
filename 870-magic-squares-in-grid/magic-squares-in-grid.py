class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if(self.check_magic(grid,i,j)):
                    count += 1
        return count
    

    def check_magic(self, grid, r, c):
        # check numbers btw 1-9
        hashset = set()

        for i in range(r,r+3):
            for j in range(c,c+3):
                hashset.add(grid[i][j])
        
        if(hashset != set(range(1,10))):
            return False
                
        # for rows
        for i in range(r,r+3):
            if(grid[i][c] + grid[i][c+1] + grid[i][c+2] != 15):
                return False
        
        # for columns
        for j in range(c,c+3):
            if(grid[r][j] + grid[r+1][j] + grid[r+2][j] != 15):
                return False

        #  diagonal 1
        if(grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15):
            return False
        
        # diagonal 2
        if(grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15):
            return False
        
        return True
