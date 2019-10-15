import sys
import numpy as np
import pandas as pd
import read_mid as rm


def make_transition(file_path):
    df = np.zeros(shape=(128, 128))

    df = pd.DataFrame(df)

    result = rm.parse_mid(file_path)

    for i in range(len(result["pitch"])-1):
        df[result["pitch"][i]][result["pitch"][i+1]] += 1

    # Jupyter Notebook Specifications
    # pd.option_context('display.max_columns', None)
    # # pd.options.display
    # pd.options.display.max_rows = 4000
    # # pd.option_context("display.max_rows", df.shape[0])
    # # pd.option_context('display.max_rows', None)
    # display(df)

    return df


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("No file path specified")
    else:
        for i in range(1, len(sys.argv)):
            print(make_transition(sys.argv[i]))
