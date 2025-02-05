import requests

username = "Achu101"  # Replace with your LeetCode username
url = f"https://leetcode-stats-api.herokuapp.com/{username}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    total_solved = data["totalSolved"]
    current_streak = data["currentStreak"]
    best_streak = data["bestStreak"]

    # Update README.md
    with open("README.md", "r") as file:
        content = file.readlines()

    for i, line in enumerate(content):
        if "<!-- LEETCODE-STATS -->" in line:
            content[i] = f"🔥 Total Problems Solved: {total_solved}\n⚡ Current Streak: {current_streak}\n🏆 Best Streak: {best_streak}\n"

    with open("README.md", "w") as file:
        file.writelines(content)

else:
    print("Failed to fetch LeetCode stats!")
