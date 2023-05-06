from fake_data_gen import generate_fake_data
from examine_fake_data import examine_fake_data


def data_gen_flow():
    generate_fake_data()
    examine_fake_data()


if __name__ == '__main__':
    data_gen_flow()
