from datetime import datetime, timedelta
import uuid
import random
import json
from faker import Faker

fake = Faker('jp-JP')
Faker.seed(13413245)

n = 3

today = datetime(2018, 7, 29, 23, 59, 59)

def fake_composition():
    composition = []
    if random.random() < 0.95:
        num = random.randint(1,4)
    else:
        num = random.randint(5, 10)
    for i in range(num):
        fake_user = fake.profile()
        birthdate = fake_user['birthdate']
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        composition.append({
            'age': age,
            'gender': fake_user['sex']
        })
    return composition

cafe_menu = [
    {'emoji': '☕', 'name': 'コーヒー'},
    {'emoji': '🍵', 'name': 'お茶'},
    {'emoji': '🥛', 'name': '牛乳'},
    {'emoji': '🧃', 'name': 'ジュース'},
    {'emoji': '🧋', 'name': 'バブルティー'},
    {'emoji': '🍰', 'name': 'ショートケーキ'},
    {'emoji': '🎂', 'name': 'バースデーケーキ'},
    {'emoji': '🧁', 'name': 'カップケーキ'},
    {'emoji': '🍪', 'name': 'クッキー'},
    {'emoji': '🍫', 'name': 'チョコレート'},
    {'emoji': '🍩', 'name': 'ドーナツ'},
    {'emoji': '🍦', 'name': 'ソフトクリーム'},
    {'emoji': '🍨', 'name': 'アイスクリーム'},
    {'emoji': '🥪', 'name': 'サンドイッチ'},
    {'emoji': '🥗', 'name': 'サラダ'},
    {'emoji': '🥐', 'name': 'クロワッサン'},
    {'emoji': '🥯', 'name': 'ベーグル'},
]

data = {i: {
    "uuid": f'{uuid.uuid4()}',
    "visit_time": (datetime(2018, 7, 29, 23, 59, 59) - timedelta(
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )).time().isoformat(),
    "departure_time": "2023-11-20T16:15:00",
    'group_composition': (group_composition := fake_composition()),
    "ordered_items": [
    dict(cafe_menu[random.randint(0, len(cafe_menu) - 1)],
         quantity=random.randint(1, len(group_composition)))
    for _ in range(len(group_composition))
]
    } for i in range(n)}

with open('../../../data/main_dataset.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False,)