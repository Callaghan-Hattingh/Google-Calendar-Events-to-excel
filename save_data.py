import pandas as pd

def data_to_df(items):
    x = 0
    for data in items:
        df1 = pd.DataFrame(data)
        break

    for data in items:
        if x < 1:
            x = x + 2
            continue
        df2 = pd.DataFrame(data)

        df1 = pd.concat(
            [df1, df2],
            axis=0,
            join="outer",
            ignore_index=False,
            keys=None,
            levels=None,
            names=None,
            verify_integrity=False,
            copy=True,
        )
    return df1