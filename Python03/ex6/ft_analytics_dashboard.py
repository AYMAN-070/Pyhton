# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_analytics_dashboard.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/03 14:12:48 by ayhammou          #+#    #+#              #
#    Updated: 2026/01/05 10:48:49 by ayhammou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
	print("=== Game Analytics Dashboard ===")
	print()
	list_scores = [2300, 1800, 2150, 2050, 1500, 500]
	dict_player = {
		"Alice":{"score": 2300, "achievements": 5},
		"Bob":{"score": 1800, "achievements": 3},
		"Charlie":{"score": 2150,"achievements": 7},
		"Diana":{"score": 0, "achievements": 0},
	}
	players = ["Alice", "Bob", "Charlie", "Bob", "Alice", "Diana", "Charlie"]
	achievements = ["first_kill", "level_10", "boss_slayer", "level_10"]
	regions = ["north", "east", "central"]
	
	print("=== List Comprehension Examples ===")
	high_scorers = [x for x, y in dict_player.items() if y["score"] > 2000]
	doubled = [x * 2 for x in list_scores]
	active = [x for x, y in dict_player.items() if y["score"] > 0 ]
	print("High scorers (>2000): ", high_scorers)
	print("Scores doubled : ", doubled)
	print("Active players : ", active)
	print()
	
	print("=== Dict Comprehension Examples ===")
	scores = {name: data["score"] for name, data in dict_player.items()}
	high = 0
	medium = 0
	low = 0
	for x in list_scores:
		if x >= 2000:
			high += 1
		if x >= 1000 and x < 2000: 
			medium += 1
		if x >= 0 and x < 1000:
			low += 1
	categories = {"high": high, "medium": medium, "low": low}
	count = {x: y["achievements"] for x, y in dict_player.items()}
	print("Player scores :", scores)
	print("Score categories:", categories)
	print("Achievement counts: ", count)
	print()

	print("=== Set Comprehension Examples ===")
	unique_players = {p for p in players}
	unique_achievements = {a for a in achievements}
	region = {r for r in regions}
	print("Unique players :", unique_players)
	print("Unique achievements:", unique_achievements)
	print("Achievements counts: ", region)
	print()

	print("=== Combined Analysis ===")
	print("TOtal unique player: ", len(unique_players))
	print("TOtal unique achievements: ", len(unique_achievements))
	average = sum(list_scores) / len(list_scores)
	print("Average score: ", average)
	top_score = max(list_scores)
	top_player = [name for name, data in dict_player.items() if data["score"] == top_score]
	top_performer_achievement = [data["achievements"] for name, data in dict_player.items() if name == top_player[0]]
	print(f"Top performer: {top_player[0]} ({top_score} points, {top_performer_achievement[0]} achievements)")