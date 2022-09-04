def MassVote(n: int, votes: list) -> str:
    total_votes = sum(votes)

    filtered_votes_max = list(filter(lambda x: x == max(votes), votes))
    if len(filtered_votes_max) > 1:
        return 'no winner'

    winner_votes = filtered_votes_max[0]
    winner_part = round(winner_votes / total_votes * 100, 3)
    winner_index = votes.index(winner_votes) + 1

    if winner_part > 50.0:
        return f'majority winner {winner_index}'
    return f'minority winner {winner_index}'
