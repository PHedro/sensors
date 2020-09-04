import random
from datetime import datetime
from uuid import uuid4


def generate_data_dict(_id=None, _type="Sensor"):
    return {
        "id": _id if _id else str(uuid4()),
        "type": _type,
        "content": {
            "temperature_f": round(random.random() * 100, 4),
            "time_of_measurement": datetime.isoformat(datetime.now()),
        },
    }


def _random_params(_array=None, extra_enabled=True):
    _array = _array if _array else []
    threshold = len(_array)
    if threshold == 1 and not extra_enabled:
        result = _array[0]
    elif threshold == 0:
        result = str(uuid4())
    else:
        _max = threshold + random.randint(0, 10) if extra_enabled else threshold - 1
        _index = random.randint(0, _max)
        if _index < threshold:
            result = _array[_index]
        else:
            result = str(uuid4())
    return result


def generate_data_points(ids=None, types=None, extra_ids=True, extra_types=True):
    while True:
        _id = _random_params(_array=ids, extra_enabled=extra_ids)
        _type = _random_params(_array=types, extra_enabled=extra_types)
        _data_point = generate_data_dict(_id=_id, _type=_type)
        print(_data_point)
        yield _data_point
