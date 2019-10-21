import enum

class NoteType(enum.Enum):
    off = 0
    on = 1

class NoteMessgae:
    def __init__(self, *args,**kwargs):
        self.type = kwargs.get("type",NoteType.off)
        self.time = kwargs.get("time",0)
        self.channel = kwargs.get("channel",0)
        self.note = kwargs.get("note",60)
        self.velocity = kwargs.get("velocity",64)


class MetaMessagess:
    """Pass the following Key-Word Arguements (=default value)
        \nkey=C
        \ntempo=90
        \nname=Demo
    """
    def __init__(self, **kwargs):

        self.key_signature = kwargs.get("key", "C")
        self.tempo = kwargs.get("tempo", 90)
        self.track_name = kwargs.get("name", "Demo")

        self.track_list = []

    # def add_track(self,*args):
    #     self.track_list.append(Track(args))


class TimeSignMessage:
    """
    Class used to store time signature message signals
    Pass the following Key-Word Arguements (=default value)
        \nnumerator=4
        \ndenominator=4
        \nclocks_per_click=24
        \ntime_stamp
        \ntime_pause=0
        \n """

    def __init__(self, *args, **kwargs):
        self.time_sign_numerator = kwargs.get("numerator", 4)
        self.time_sign_denominator = kwargs.get("denominator", 4)
        self.clocks_per_click = kwargs.get("clocks_per_click", 24)
        self.time_stamp = kwargs["time_stamp"]
        self.time_of_pause_before = kwargs.get("time_of_pause_before", 0)

    def __str__(self):
        return f"Time Signature Changed to : {self.time_sign_numerator} / {self.time_sign_denominator} @ {self.time_stamp} seconds"
    def __repr__(self):
        return f"Time Signature Changed to : {self.time_sign_numerator} / {self.time_sign_denominator} @ {self.time_stamp} seconds"

class TempoMessage:
    """
    Class used to store tempo message signals
    Pass the following kwargs (=default value)
    \ntempo=90
    \ntime_stamp,
    \ntime_of_pause_before=0
    """

    def __init__(self, *args, **kwargs):
        self.tempo = kwargs.get("tempo", 90)
        self.time_stamp = kwargs["time_stamp"]
        self.time_of_pause_before = kwargs.get("time_of_pause_before", 0)

    def __str__(self):
        return f"Tempo Change : {self.tempo} @ {self.time_stamp} seconds"
    def __repr__(self):
        return f"Tempo Change : {self.tempo} @ {self.time_stamp} seconds"

