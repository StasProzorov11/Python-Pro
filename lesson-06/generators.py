from typing import Generator


class Player:

    def __init__(self, first_name: str, last_name: str):

        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


team: list[Player] = [
    Player("John", "Smith"),
    Player("Marry", "Smith"),
    Player("Jack", "Hill"),
    Player("Nick", "Doe"),
    Player("John", "Doe"),
    Player("Marry", "Doe"),
]


# for player in team:
#     print(player)

def dedup(team: list[Player]) -> Generator[str, None, None]:
    players_names: set[str] = set()

    for player in team:
        if player.first_name not in players_names:
            yield player
            players_names.add(player.first_name)

for player in dedup(team):
    print(player)
