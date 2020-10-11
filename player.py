from build import Build
import utils
import re
class Player:
    def __init__(self, player_info):
        self.race = player_info["race"]
        self.build_order = [Build(build_info) for build_info in player_info["buildOrder"]]
        self.localize()

    def localize(self):
        table = utils.load_translation_dict()
        for build in self.build_order:
            splitted_build_name = " ".join(re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', build.name)).split())
            build.name = table[splitted_build_name] if (splitted_build_name in table.keys()) else splitted_build_name