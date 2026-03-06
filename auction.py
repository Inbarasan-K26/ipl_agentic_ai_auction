from teams import teams
from players import players
import random


def run_auction():

    for player in players:

        print("\nAuctioning:", player["name"], "|", player["role"], "| Rating:", player["rating"], "| Price:", player["price"])

        bidding_teams = []

        # Check which teams want to bid
        for team in teams:

            if team["budget"] >= player["price"]:

                # Simple AI decision
                if player["rating"] > random.randint(70, 95):
                    bidding_teams.append(team)

        if bidding_teams:

            winner = random.choice(bidding_teams)

            winner["players"].append(player["name"])
            winner["budget"] -= player["price"]

            print(winner["name"], "bought", player["name"])

        else:
            print("No team bought", player["name"])


    # FINAL OUTPUT
    print("\n================ FINAL TEAMS ================\n")

    team_no = 1

    for team in teams:

        print(f"{team_no}. {team['name']} Squad:")

        player_no = 1

        for player in team["players"]:
            print(f"   {player_no}. {player}")
            player_no += 1

        print("----------------------------------\n")

        team_no += 1