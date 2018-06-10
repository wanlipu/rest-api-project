lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

print (lottery_player_dict)


class LotteryPlayer:
    def __init__(self):
        self.name = 'Rolf'
        self.numbers = (5, 9, 12, 3, 1, 21)


player = LotteryPlayer()

print (player.name, player.numbers)

