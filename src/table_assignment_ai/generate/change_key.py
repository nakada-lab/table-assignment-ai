from datetime import datetime
import json
from operator import itemgetter

data = json.load(open("../../../data/dataset.json", "r"))

sorted_data = sorted(data, key=itemgetter("visit_time"))

modded_data = {
    sorted_data[i]["visit_time"]: {
        "uuid": sorted_data[i]["uuid"],
        "departure_time": sorted_data[i]["departure_time"],
        "duration": int(
            (
                datetime.strptime(sorted_data[i]["departure_time"], "%H:%M:%S")
                - datetime.strptime(sorted_data[i]["visit_time"], "%H:%M:%S")
            ).total_seconds()
        ),
        "group_composition": sorted_data[i]["group_composition"],
        "ordered_items": sorted_data[i]["ordered_items"],
    }
    for i in range(len(sorted_data))
}

with open("../../../data/update_dataset.json", "w") as f:
    json.dump(modded_data, f, indent=2, ensure_ascii=False)
