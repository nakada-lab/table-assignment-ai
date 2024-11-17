import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import uuid
import random

np.random.seed(42)

n = 1000

uuids = [str(uuid.uuid4()) for _ in range(n)]

datetimes = [datetime(2024, 12, 31, 23, 59, 59) - timedelta(
    days=random.randint(0, 365),
    hours=random.randint(0, 23),
    minutes=random.randint(0, 59)
) for _ in range(n)]

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def group_size():
    if random.random() < 0.95:
        return random.randint(1,4)
    else:
        return random.randint(5, 10)

group_sizes = [group_size() for _ in range(n)]

df = pd.DataFrame({
    'UID': uuids,
    'DateTime': datetimes,
    'DayOfWeek': [d.strftime('%A') for d in datetimes],
    'NumberOfPeople': group_sizes
})

df['DateTime'] = df['DateTime'].dt.strftime('%Y-%m-%dT%H:%M:%S')

df.to_csv('./data/main_table_data.csv', index=False)