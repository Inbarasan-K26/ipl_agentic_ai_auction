def team_bid(team, player, budget):

    score = player["rating"]

    if player["role"] == "All-Rounder":
        score += 5

    if budget >= player["price"] and score > 85:
        return True

    return False