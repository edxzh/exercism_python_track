def slices(series, length):
    if length > len(series) or length < 1:
        raise ValueError("Error")

    result = list(series[idx : idx + length] for idx, val in enumerate(series) if idx + length <= len(series))

    return result
