import pandas as pd

from src.config.constants import PATH_TO_INPUT_DIR


def examine_fake_data():
    fake_data = pd.read_csv(PATH_TO_INPUT_DIR + 'auto_wait_times.csv')

    print(fake_data)
    print(fake_data.describe())
    print(fake_data.describe(include='all'))


if __name__ == '__main__':
    examine_fake_data()
