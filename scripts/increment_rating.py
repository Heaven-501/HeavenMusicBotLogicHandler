import yaml
import re

# Load YAML
with open("something.yml") as f:
    data = yaml.safe_load(f)

user = "Mino"
info = data[user]

# Increment Heaven Rating
info['current_points'] += info.get('daily_increase', 0.05)
current_points = round(info['current_points'], 2)

# Update YAML
with open("something.yml", "w") as f:
    yaml.dump(data, f)

# Update Mino.html
with open("Mino.html", "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(
    r'(id="heavenRating">)(.*?)<\/div>',
    rf'\1🌀 {current_points} Heaven Points</div>',
    html
)

with open("Mino.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Updated Heaven Rating for {user}: 🌀 {current_points}")
