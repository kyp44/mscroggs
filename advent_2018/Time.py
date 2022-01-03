#! /usr/bin/env python3

class Time :
    def __init__(self, h, m=None) :
        if m is None:
            self.mins = h
        else :
            self.mins = 60*h + m

    def __str__(self) :
        h = self.mins // 60
        m = self.mins % 60
        return str(h) + ":{:02d}".format(m)

    def __repr__(self) :
        return str(self)

    def __add__(self, t) :
        ms = self.mins + t.mins
        h = (ms // 60) % 24
        m = ms % 60
        return Time(h, m)

    def __sub__(self, t) :
        ms = self.mins - t.mins
        h = (ms // 60) % 24
        m = ms % 60
        return Time(h, m)

    def __hash__(self) :
        return self.mins % (60*24)

    def __eq__(self, other) :
        return hash(self) == hash(other)

    def __lt__(self, other) :
        return self.mins < other.mins

    def __le__(self, other) :
        return self.mins <= other.mins

    def __gt__(self, other) :
        return self.mins > other.mins

    def __ge__(self, other) :
        return self.mins >= other.mins
