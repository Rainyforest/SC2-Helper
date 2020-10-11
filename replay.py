import spawningtool.parser
import json
import utils
from build import Build
from player import Player

class Replay:
    def __init__(self, replay_path):
        self.path = replay_path
        self.players = [Player(player_info) for player_info in self.get_replay_info()]

    def get_replay_info(self):
        replay = spawningtool.parser.parse_replay(self.path)
        parsed_replay = json.loads(json.dumps(replay))
        json_replay = json.dumps(parsed_replay, indent=4, sort_keys=True)
        game_map = parsed_replay["map"]
        player_one = parsed_replay["players"]["1"]
        player_two = parsed_replay["players"]["2"]
        return [player_one,player_two]

    

