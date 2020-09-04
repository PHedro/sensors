from tempertature_flow.database_setup import DataPoint


def store_data_point(data_point):
    print(data_point)


def store_data_point_psql(data_point, session=None):
    session.add(
        DataPoint(
            id=data_point.get("id"),
            type=data_point.get("type"),
            temperature_f=data_point.get("content", {}).get("temperature_f"),
            temperature_c=data_point.get("content", {}).get("temperature_c"),
            time_of_measurement=data_point.get("content", {}).get(
                "time_of_measurement"
            ),
        )
    )
    session.commit()
