import math

import pandas as pd
import numpy as np
import datetime
import random

from src.config.constants import PATH_TO_INPUT_DIR


def generate_fake_data():
    random.seed(42)
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=90)

    data = []

    for index in range((end_date - start_date).days):
        date = start_date + datetime.timedelta(days=index)
        day_of_week = date.weekday()  # Monday is 0, Sunday is 6
        is_public_holiday = bool(random.choices([True, False], weights=[5, 95], k=1)[0])
        is_semester = bool(random.choices([True, False], weights=[5, 95], k=1)[0])
        train_traffic = math.ceil(random.uniform(20, 40))

        waiting_time = int(train_traffic / 2) + int(np.random.normal(loc=10, scale=10))
        waiting_time = max(5, waiting_time)
        waiting_time = min(35, waiting_time)

        if day_of_week in [5, 6] or is_public_holiday:
            waiting_time -= int(np.random.uniform(20, 25))
        if is_semester or train_traffic > 0.5:
            waiting_time += int(np.random.uniform(20, 30))

        data.append([date, waiting_time, is_public_holiday, day_of_week, is_semester,
                     train_traffic])

    fake_data = pd.DataFrame(
        data,
        columns=[
            'date', 'waiting_time', 'is_public_holiday',
            'day_of_week', 'is_semester', 'train_traffic'
        ]
    )

    fake_data.to_csv(PATH_TO_INPUT_DIR + 'auto_wait_times.csv', index=False)


if __name__ == '__main__':
    generate_fake_data()
