class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """

        MAX = 100000
        '''
        frequency array:
        index = player id
        value = no of losses of the player
        '''
        losses = [0] * (MAX + 1)

        # Store every player who participated in at least one match
        players = set()

        # Go to every match checks winners,loosers
        for winner,looser in matches:
            # Both players participated in a match, so remember both of them.
            players.add(winner)
            players.add(looser)
            
            # so increase that player's loss count.
            losses[looser] += 1
        
        zero_lost = []  # Players who lost 0 times
        one_lost = []    # Players who lost exactly 1 time

        # check only players who actually participated
        for player in players:
            # player exists but never loose
            if(losses[player] == 0):
                zero_lost.append(player)
            # player lsot at one time
            elif(losses[player] == 1):
                one_lost.append(player)
        zero_lost.sort()
        one_lost.sort()
        return [zero_lost,one_lost]