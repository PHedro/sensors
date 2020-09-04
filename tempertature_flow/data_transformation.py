def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def enhance_data(data_point):
    for _enhancement in METADATA_ENHANCEMENTS:
        data_point = _enhancement(data_point)

    return data_point


def enhance_temperature(data_point):
    _content = data_point.get("content")
    _fahrenheit = _content.get("temperature_f")
    if not _fahrenheit:
        raise ValueError
    _celsius = fahrenheit_to_celsius(_fahrenheit)
    _content.update({"temperature_c": _celsius})
    data_point.update({"content": _content})
    return data_point


METADATA_ENHANCEMENTS = (enhance_temperature,)
