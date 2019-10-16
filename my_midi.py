import enum

class NoteType(enum.Enum):
    off = 0
    on = 1

class NoteMessgae:
    __init__(self, **kwargs):
        self.type = kwargs.get("type",NoteType.off)
        self.time = kwargs.get("time",0) 
        self.channel = kwargs.get("channel",0)
        self.note = kwargs.get("note",60)
        self.velocity = kwargs.get("velocity",64)


class TrackMessage:
    __init__(self, *args, **kwargs):
        pass

class MetaMessagess:
    '''Pass the following Key-Word Arguements (=default value)
        \nnumerator=4
        \ndenominator=4
        \nkey=C
        \ntempo=90
        \nname=Demo
        \nclocks_per_click"=24
    '''
    __init__(self, **kwargs):
        self.time_sign_numerator = kwargs.get("numerator", 4)
        self.time_sign_denominator = kwargs.get("denominator", 4)
        self.key_signature = kwargs.get("key", "C")
        self.tempo = kwargs.get("tempo", 90)
        self.track_name = kwargs.get("name", "Demo")
        self.clocks_per_click = kwargs.get("clocks_per_click", 24)
        self.track_list = []

    def add_track(*args):
        self.track_list.append(Track(args))
