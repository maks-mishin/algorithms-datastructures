def swap_players(players: list, i: int, j: int) -> tuple:
    copy_players = players
    copy_players[i], copy_players[j] = copy_players[j], copy_players[i]
    return tuple(copy_players)


def can_sorting_swap(players: list, count_players: int) -> bool:
    player_permutations = set()
    for i in range(count_players):
        for j in range(count_players):
            player_permutations.add(swap_players(players, i, j))
    return tuple(sorted(players)) in player_permutations


def can_sorting_reverse(players: list, count_players: int) -> bool:
    new_players_positions = set()
    for i in range(count_players - 1):
        for j in range(2, count_players):
            new_players_positions.add(
                tuple(
                    players[:i] +
                    list(reversed(players[i:i + j])) +
                    players[i + j:]
                )
            )
    return tuple(sorted(players)) in new_players_positions


def Football(players: list, count_players: int) -> bool:
    if players == sorted(players):
        return False
    return (can_sorting_reverse(players, count_players)
            or can_sorting_swap(players, count_players))
