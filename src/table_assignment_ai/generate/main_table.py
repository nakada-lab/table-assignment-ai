from datetime import datetime, timedelta
import uuid
import random
import json
from faker import Faker

fake = Faker("jp-JP")
Faker.seed(9320)

n = 1000

today = datetime(2018, 7, 29, 23, 59, 59)


def random_age(gender):
    age_groups = {
        (0, 4): (2740000, 2608000),
        (5, 9): (2942000, 2794000),
        (10, 14): (3040000, 2895000),
        (15, 19): (3114000, 2959000),
        (20, 24): (3536000, 3334000),
        (25, 29): (3767000, 3612000),
        (30, 34): (4467000, 4321000),
        (35, 39): (4775000, 4644000),
        (40, 44): (4167000, 4080000),
        (45, 49): (3853000, 3807000),
        (50, 54): (3862000, 3869000),
        (55, 59): (4828000, 4936000),
        (60, 64): (4345000, 4557000),
        (65, 69): (3825000, 4174000),
        (70, 74): (3199000, 3728000),
        (75, 79): (2464000, 3221000),
        (80, 84): (1562000, 2298000),
    }
    weighted_ages = []
    for age_range, (male_count, female_count) in age_groups.items():
        count = male_count if gender == "M" else female_count
        weighted_ages.extend([age_range] * count)
    chosen_range = random.choice(weighted_ages)
    return random.randint(chosen_range[0], chosen_range[1])


def fake_composition():
    composition = []
    if random.random() < 0.95:
        num = random.randint(1, 4)
    else:
        num = random.randint(5, 10)
    for i in range(num):
        fake_user = fake.profile()
        composition.append(
            {"age": random_age(fake_user["sex"]), "gender": fake_user["sex"]}
        )
    return composition


cafe_menu = [
    {"emoji": "☕", "name": "コーヒー"},
    {"emoji": "🍵", "name": "お茶"},
    {"emoji": "🥛", "name": "牛乳"},
    {"emoji": "🧃", "name": "ジュース"},
    {"emoji": "🧋", "name": "バブルティー"},
    {"emoji": "🍰", "name": "ショートケーキ"},
    {"emoji": "🎂", "name": "バースデーケーキ"},
    {"emoji": "🧁", "name": "カップケーキ"},
    {"emoji": "🍪", "name": "クッキー"},
    {"emoji": "🍫", "name": "チョコレート"},
    {"emoji": "🍩", "name": "ドーナツ"},
    {"emoji": "🍦", "name": "ソフトクリーム"},
    {"emoji": "🍨", "name": "アイスクリーム"},
    {"emoji": "🥪", "name": "サンドイッチ"},
    {"emoji": "🥗", "name": "サラダ"},
    {"emoji": "🥐", "name": "クロワッサン"},
    {"emoji": "🥯", "name": "ベーグル"},
]

data = [
    {
        "uuid": f"{uuid.uuid4()}",
        "visit_time": (
            datetime(
                2018,
                7,
                29,
                random.randint(9, 22),
                random.randint(0, 59),
                random.randint(0, 59),
            )
        )
        .time()
        .isoformat(),
        "departure_time": None,
        "duration": None,
        "group_composition": (group_composition := fake_composition()),
        "ordered_items": [
            dict(
                cafe_menu[random.randint(0, len(cafe_menu) - 1)],
                quantity=random.randint(1, len(group_composition)),
            )
            for _ in range(len(group_composition))
        ],
    }
    for i in range(n)
]

with open("../../../data/main_dataset.json", "w") as f:
    json.dump(
        data,
        f,
        indent=2,
        ensure_ascii=False,
    )
