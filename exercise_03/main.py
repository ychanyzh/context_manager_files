import os
import random
import csv

players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
rounds = 100

def simulate_score(players: list, rounds: int) -> list:
    scores = []
    for _ in range(rounds):
        for player in players:
            score = random.randint(0, 1000)
            scores.append((player, score))
    return scores

def save_to_csv(data: list, filename: str) -> None:
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player name', 'Score'])
        writer.writerows(data)

scores_data = simulate_score(players, rounds)
save_to_csv(scores_data, 'user_scores.csv')
