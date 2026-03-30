ROCK_GROUP_MAP = {
    -3: "clastic",
    -2: "carbonate",
    -1: "evaporite",
}

ROCK_GROUP_REVERSE = {v: k for k, v in ROCK_GROUP_MAP.items()}


def normalize_rock_group(value):
    if isinstance(value, int):
        return ROCK_GROUP_MAP[value]

    if isinstance(value, str):
        value = value.lower()
        if value in ROCK_GROUP_REVERSE:
            return value

    raise ValueError(f"Invalid rock group: {value}")