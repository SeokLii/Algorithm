def solution(players, callings):
    players = dict(zip(players, [i for i in range(len(players))]))
    players_index = dict(zip([i for i in range(len(players))], players))

    for i in callings:
        p1, p1_index = i, players[i]
        p2, p2_index = players_index[p1_index - 1], p1_index - 1

        players[p1], players_index[p1_index] = p2_index, p2
        players[p2], players_index[p2_index] = p1_index, p1

    return list(players_index.values())