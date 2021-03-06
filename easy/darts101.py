import sys
# TODO Every player shoot 3 darts a round, unless you reach or exceed 101 points,
#  in which case your round immediately ends. When a dart hits the target you tentatively collect points.
#  There are multiplier rings that increase the points of some darts.
#  For example :
#  When you touch the 19, your total is increased by 19.
#  When you touch the double 19 (2*19) , your total is increased by 2*19=38.
#  When you touch the triple 19 (3*19), your total is increased by 3*19=57.
#  Each time you miss the target, your total is decreased by 20 points. If you miss twice consecutively
#  in the same round, your total is decreased by another 10 points. If you miss three times in the same round,
#  your whole total is reset at 0. To win, you must score exactly 101 points. If you exceed the score of 101
#  after a shoot, you revert to your total before your current round and your round ends here. Your round may
#  therefore end before your third shoot. The player who has reached 101 in the fewest rounds wins the game.
#  You have to print the winner's name.
#  Input:
#  Line1 : A number N of player
#  Next N lines : name of player
#  Next N lines : shoots of a player separated with space (X when a player missed the target).
#  Output:
#  The name of the winner


class GameProcessor:
    def __init__(self):
        self._create_constants()

    def _create_constants(self):
        self.shots = 0
        self.count = 0
        self.misses = 0
        self.round_num = 1
        self.round_count = 0
        self.max_count = 100000000

    def run(self, shots_record):
        self._create_constants()
        records = shots_record.split(' ')
        for shot in records:
            self.process_shot(shot)
            if self.count == 101:
                return self.round_num
            elif self.count > 101:
                self.count = self.round_count
                self.init_round()
                continue
            self.shots += 1
            if self.shots == 3:
                self.round_count = self.count
                self.init_round()
        return self.max_count

    def process_shot(self, shot):
        if shot == 'X':
            self.misses += 1
            if self.misses == 1:
                self.count = max(self.count - 20, 0)
            elif self.misses == 2:
                self.count = max(self.count - 30, 0)
            else:
                self.count = 0
        else:
            if shot.isnumeric():
                self.count += int(shot)
            else:
                temp_record = shot.split('*')
                self.count += int(temp_record[0]) * int(temp_record[1])
            self.misses = 0

    def init_round(self):
        self.round_num += 1
        self.shots = 0
        self.misses = 0


if __name__ == '__main__':
    num_of_players = int(input())
    list_of_players = [input() for i in range(num_of_players)]
    results = dict()
    game_processor = GameProcessor()
    for player in list_of_players:
        player_shots = input()
        print(player_shots, file=sys.stderr)
        results[player] = game_processor.run(player_shots)
    name_of_winner = sorted(results.items(), key=lambda t: t[1])[0][0]
    print(name_of_winner)
