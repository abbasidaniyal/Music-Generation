
import pretty_midi
import matplotlib.pyplot as plt
import pandas as pd
import sys


def parse_mid(file_path):

    midi_data = pretty_midi.PrettyMIDI(file_path)

    # midi_data.instruments
    lst_start = []
    lst_end = []
    lst_pitch = []

    for note in midi_data.instruments[0].notes:
        lst_start.append(note.start)
        lst_pitch.append(note.pitch)
        lst_end.append(note.end)

    df = pd.DataFrame()

    df["start_time"] = pd.Series(lst_start)
    df["end_time"] = pd.Series(lst_end)
    df["pitch"] = pd.Series(lst_pitch)

    # df_group=df.groupby('start_time')

    # df=df_group.describe()

    df = df.drop_duplicates(subset="start_time", keep="first")

    df = df.reset_index()

    plt.plot(df["pitch"], df.index.values.tolist(), "bo")
    plt.show()
    return df


if __name__ == "__main__":

    if len(sys.argv)<2:
        print("No file path specified")
    else:
        for i in range(1, len(sys.argv)):
            print(parse_mid(sys.argv[i]))
            
