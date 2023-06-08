championat1 = (2, 3, 1, 4, 0, 2, 3, 1, 2, 1, 3, 0, 2, 1, 3, 0, 4, 2, 1, 2, 0, 3, 1, 2, 2, 1)
championat2 = (1, 2, 4, 3, 1, 2, 0, 3, 2, 1, 1, 2, 2, 3, 0, 4, 2, 1, 3, 1, 2, 0, 4, 3, 1, 2)

all_games = championat1 + championat2
total_goals = sum(all_games)

print("Общее количество мячей: ", total_goals)

