def _chunk(sequence, n: int):
    for i in range(0, len(sequence), n):
        yield sequence[i : i + n]
