TABLE_HEADER = "Team                           | MP |  W |  D |  L |  P"
OPPOSITE_RESULTS = { "win": "loss", "draw": "draw", "loss": "win" }

def tally(rows):
    matches = {}
    for row in rows:
        [player_1, player_2, match_result] = row.split(';')

        matches = update(player_1, match_result, matches)
        matches = update(player_2, OPPOSITE_RESULTS[match_result], matches)

    sorted_matches = sort_matches(matches)

    return printed(sorted_matches)

def sort_matches(matches):
    matches = [{
        'NAME': player,
        'MP': matches[player]['MP'],
        'W': matches[player]['W'],
        'D': matches[player]['D'],
        'L': matches[player]['L'],
        'P': matches[player]['P']} for player in matches]

    return sorted(matches, key=lambda match: (-match['P'], match['NAME'].lower()))

def update(player, match_result, matches):
    if (player not in matches):
        matches[player] = { 'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0 }

    matches[player]['MP'] += 1

    if (match_result == 'win'):
        matches[player]['W'] += 1
        matches[player]['P'] += 3
    elif (match_result == 'draw'):
        matches[player]['D'] += 1
        matches[player]['P'] += 1
    else:
        matches[player]['L'] += 1
        matches[player]['P'] += 0

    return matches

def printed(sorted_matches):
    return [TABLE_HEADER] + [formated(player) for player in sorted_matches]


def formated(player):
    return f"{player['NAME'].ljust(30)} |  {player['MP']} |  {player['W']} |  {player['D']} |  {player['L']} |  {player['P']}"
