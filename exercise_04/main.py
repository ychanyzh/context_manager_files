import csv

def read_csv(filename: str) -> list:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        data = [row for row in reader]
    return data

def calculate_high_scores(data: list) -> dict:
    player_scores = {}
    for player, score in data:
        score = int(score)
        if player not in player_scores or score > player_scores[player]:
            player_scores[player] = score
    return player_scores

def save_high_scores(data: list, filename: str) -> None:
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player name', 'Highest score'])
        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        writer.writerows(sorted_data)


input_file = 'user_scores.csv'
output_file = 'high_scores.csv'
data = read_csv(input_file)
player_scores = calculate_high_scores(data)
save_high_scores(player_scores, output_file)
