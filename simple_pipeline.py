from tempertature_flow.data_generator import generate_data_points
from tempertature_flow.data_transformation import enhance_data
from tempertature_flow.persistence import store_data_point


def execute():
    data_points = generate_data_points(
        ids=["GLOBALLY_UNIQUE_IDENTIFIER"], types=["Sensor"]
    )
    while True:
        data_point = enhance_data(next(data_points))
        store_data_point(data_point)


if __name__ == "__main__":
    execute()
