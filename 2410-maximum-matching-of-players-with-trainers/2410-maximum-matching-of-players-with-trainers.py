class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        res = 0

        for t in range(len(trainers)):
            if res < len(players) and trainers[t] >= players[res]:
                res += 1
            
        return res

            
        