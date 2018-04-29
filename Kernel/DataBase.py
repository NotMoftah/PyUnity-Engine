import pickle


def __LoadDataBase():
    global _data
    try:
        with open('__data_base__.data', 'rb') as handle:
            _data = pickle.load(handle)
    except (OSError, IOError) as e:
        _data = {}


def __SaveDataBase():
    global _data
    with open('__data_base__.data', 'wb') as handle:
        pickle.dump(_data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def get_variable(variable_name, default=None):
    global _data
    if variable_name in _data:
        return _data[variable_name]
    else:
        return default


def set_variable(variable_name, value):
    global _data
    _data[variable_name] = value
