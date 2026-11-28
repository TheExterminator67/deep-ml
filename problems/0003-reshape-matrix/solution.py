import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

    rows = len(a)
    cols = len(a[0])
    new_cols, new_rows = new_shape

    if new_rows <=0 or new_cols <=0 or rows * cols != new_rows*new_cols:
        return []

    return np.array(a).reshape(new_shape).tolist()


    return reshaped_matrix