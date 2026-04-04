class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        sorted_players = sorted(players)
        sorted_trainers = sorted(trainers)
        res = 0

        for t in range(len(sorted_trainers)):
            if res < len(sorted_players) and sorted_trainers[t] >= sorted_players[res]:
                res += 1
            
        return res

            
        