import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))  # 将父级目录加入执行目录列表

from part1.toolbox.client import Client

class PropertyMatcher:
    def match_properties(self, client, properties):
        matched_properties = []
        for prop in properties:
            if prop['price'] > 0 and prop['price'] <= client['budget']:
                matched_properties.append(prop)
        return matched_properties

