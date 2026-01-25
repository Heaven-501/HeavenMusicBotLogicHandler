fetch("leaderboard.json")
  .then(r => r.json())
  .then(data => {
    const list = document.getElementById("board");

    Object.values(data)
      .filter(u => !u.hidden)
      .sort((a, b) => b.points - a.points)
      .forEach((u, i) => {
        const li = document.createElement("li");
        li.textContent = `#${i + 1} @${u.username} — ${u.points} pts`;
        list.appendChild(li);
      });
  });
