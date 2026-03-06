from teams import teams

print("\n===== IPL DASHBOARD =====\n")

for team in teams:

    print("Team:", team)
    print("Players:", teams[team]["players"])
    print("Budget Left:", teams[team]["budget"])
    print()
    