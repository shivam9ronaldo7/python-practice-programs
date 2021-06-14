"""
Dunder methods are also known as magic methods

"""


class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __getitem__(self, i):
        return self.players[i]

    def __len__(self):
        return len(self.players)

    def __repr__(self):
        return f'Club {self.name}: {self.players}'

    def __str__(self):
        return f'Club {self.name} with {len(self)} players'


some_club = Club('Arsenal')

some_club.players.append('Ozil')
some_club.players.append('Cech')
some_club.players.append('Aubmayang')
some_club.players.append('Lacazette')
some_club.players.append('Bellarin')

print(len(some_club))

print(some_club[1])

# To use for loop we must implement __getitem__ methods must you define in order to
# be able to use a for loop in your class
for player in some_club:
    print(player)

print(some_club)

print(str(some_club))

print(repr(some_club))
