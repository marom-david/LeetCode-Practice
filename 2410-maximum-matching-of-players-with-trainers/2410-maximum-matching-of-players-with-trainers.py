class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players = sorted(players)
        trainers = sorted(trainers)
        res = 0

        for t in range(len(trainers)):
            if res < len(players) and trainers[t] >= players[res]:
                res += 1
            
        return res

            
        