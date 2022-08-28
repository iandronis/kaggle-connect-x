from kaggle_environments import make

from src.agents import agent_random

# Create the game environment
# Set debug=True to see the errors if your agent refuses to run
env = make("connectx", debug=True)

# Two random agents play one game round
env.run([agent_random, agent_random])

# Show the game
data = env.render(mode="html")
with open("data.html", "w") as file:
    file.write(data)
