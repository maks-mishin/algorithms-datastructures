import unittest
import random

from tasks.mass_vote import MassVote


class TestMassVote(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(MassVote(5, [1, 1, 5, 6, 7, 8]), 'minority winner 6')
        self.assertEqual(MassVote(1, [80]), 'majority winner 1')
        self.assertEqual(MassVote(5, [60, 10, 10, 15, 5]), 'majority winner 1')
        self.assertEqual(MassVote(3, [10, 15, 10]), 'minority winner 2')
        self.assertEqual(MassVote(5, [111, 111, 110, 110]), 'no winner')
        self.assertEqual(MassVote(5, [5, 5, 5, 5]), 'no winner')

    def test_majority(self):
        majority_votes = 51
        total_votes = 100

        for _ in range(100):
            votes = [majority_votes]
            while sum(votes) < total_votes:
                new_vote = random.randint(0, total_votes - majority_votes)
                if sum(votes) + new_vote <= total_votes:
                    votes.append(new_vote)

            random.shuffle(votes)
            majority_index = votes.index(majority_votes) + 1
            self.assertEqual(
                MassVote(len(votes), votes),
                f'majority winner {majority_index}'
            )

    def test_minority(self):
        minority_votes = 50
        total_votes = 100

        for _ in range(100):
            votes = [minority_votes]
            while sum(votes) < total_votes:
                new_vote = random.randint(0, 49)
                if sum(votes) + new_vote <= total_votes:
                    votes.append(new_vote)

            random.shuffle(votes)
            minority_index = votes.index(minority_votes) + 1
            self.assertEqual(
                MassVote(len(votes), votes),
                f'minority winner {minority_index}'
            )

    def test_no_winner(self):
        no_winner_votes = 22
        total_votes = 100

        for _ in range(100):
            votes = [no_winner_votes, no_winner_votes]
            while sum(votes) < total_votes:
                new_vote = random.randint(0, 15)
                if sum(votes) + new_vote <= total_votes:
                    votes.append(new_vote)

            random.shuffle(votes)
            self.assertEqual(MassVote(len(votes), votes), 'no winner')


if __name__ == '__main__':
    unittest.main()
