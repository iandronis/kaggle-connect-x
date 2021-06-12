import numpy as np
from kaggle_environments import evaluate, make

from src import agents
from src.utils import render_game


def play_game(agent1, agent2, environment, configuration):
    env = make(environment=environment, configuration=configuration, debug=True)
    env.run([agent1, agent2])
    render_game(env)


def get_win_rate(
    agent1, agent2, environment: str, configuration={}, episodes=100
):
    rewards = evaluate(
        environment=environment,
        agents=[agent1, agent2],
        configuration=configuration,
        num_episodes=episodes // 2,
    )
    rewards += [
        [b, a]
        for [a, b] in evaluate(
            environment=environment,
            agents=[agent2, agent1],
            configuration=configuration,
            num_episodes=episodes - episodes // 2,
        )
    ]

    agent_1_win_rate = np.round(
        rewards.count([1, -1]) / len(rewards), decimals=2
    )
    print(f"Agent 1 Win Rate: {agent_1_win_rate}")
    agent_2_win_rate = np.round(
        rewards.count([-1, 1]) / len(rewards), decimals=2
    )
    print(f"Agent 2 Win Rate: {agent_2_win_rate}")

    agent_1_invalid_games = rewards.count([None, 0])
    print(f"Agent 1 Invalid games: {agent_1_invalid_games}")
    agent_2_invalid_games = rewards.count([0, None])
    print(f"Agent 2 Invalid games: {agent_2_invalid_games}")


def main():
    get_win_rate(
        agent1=agents.agent_random_check_winning_move,
        agent2=agents.agent_leftmost,
        environment="connectx",
    )


main()
