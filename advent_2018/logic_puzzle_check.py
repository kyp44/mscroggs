from enum import Enum
from collections import namedtuple
from Time import Time

# Possible activities
class Activity(Enum) :
    BILLIARDS = 1
    CURLING = 2
    LUNCH = 3
    MATH = 4
    TENNIS = 5
    SKIING = 6
    CHESS = 7
    CLIMBING = 8
    SKATING = 9
    THIEVERY = 10

# Single time slot
Timeslot = namedtuple("Timeslot", ("activity", "start", "end"))

# Represents schedule for a helper
class Schedule :
    def __init__(self, alist) :
        self.slots = []
        for i,a in enumerate(alist) :
            if i < len(alist)-1 :
                et = alist[i+1][1]
            else :
                et = Time(10,0)
            self.slots.append(Timeslot(a[0], a[1], et))

    def slot(self, act) :
        for s in self.slots :
            if s.activity == act :
                return s
        return None

# Checks that all listed helpers did the activity at the same time
def same_activity(helpers, act) :
    for i in range(len(helpers)-1) :
        s1 = helpers[i].slot(act)
        s2 = helpers[i+1].slot(act)
        if s1 is None or s2 is None :
            raise ValueError("One of the helpers did not even do activity " + str(act))
        if s1 != s2 :
            raise ValueError("Helpers did activity " + str(act) + " at different times!")
    
# Determined schedules for each helper
meg = Schedule([(Activity.SKATING, Time(0,0)),
                (Activity.SKIING, Time(1,10)),
                (Activity.BILLIARDS, Time(2,33)),
                (Activity.LUNCH, Time(4,45)),
                (Activity.MATH, Time(5,42)),
                (Activity.CHESS, Time(7,30)),
                (Activity.TENNIS, Time(9,45))])
kip = Schedule([(Activity.BILLIARDS, Time(0,0)),
                (Activity.THIEVERY, Time(1,21)),
                (Activity.LUNCH, Time(2,52)),
                (Activity.CLIMBING, Time(3,30)),
                (Activity.CURLING, Time(4,45)),
                (Activity.CHESS, Time(5,42)),
                (Activity.MATH, Time(7,30))])
fred = Schedule([(Activity.MATH, Time(0,0)),
                 (Activity.LUNCH, Time(2,52)),
                 (Activity.CLIMBING, Time(3,30)),
                 (Activity.CURLING, Time(4,45)),
                 (Activity.SKATING, Time(5,42)),
                 (Activity.CHESS, Time(7,30)),
                 (Activity.TENNIS, Time(9,45))])
jo = Schedule([(Activity.MATH, Time(0,0)),
               (Activity.BILLIARDS, Time(2,33)),
               (Activity.CURLING, Time(4,45)),
               (Activity.CHESS, Time(5,42)),
               (Activity.SKIING, Time(7,30)),
               (Activity.LUNCH, Time(8,45)),
               (Activity.TENNIS, Time(9,45))])
bob = Schedule([(Activity.BILLIARDS, Time(0,0)),
                (Activity.SKATING, Time(1,21)),
                (Activity.LUNCH, Time(2,52)),
                (Activity.CLIMBING, Time(3,30)),
                (Activity.CURLING, Time(4,45)),
                (Activity.MATH, Time(5,42)),
                (Activity.SKIING, Time(7,30))])

# All helpers
helpers = [meg, kip, fred, jo, bob]

# Check that they all have 7 activites
for h in helpers :
    if len(h.slots) != 7 :
        raise ValueError("Helper does not have 7 activities!")

# Clue 1
ms = meg.slot(Activity.BILLIARDS)
js = jo.slot(Activity.BILLIARDS)
assert(ms == js)
assert(ms.start >= Time(2,33))
assert(ms.end <= jo.slot(Activity.CURLING).start)

# Clue 2
s = Time(0)
for h in helpers :
    mps = h.slot(Activity.MATH)
    if mps is not None :
        s += mps.end - mps.start
assert(s.mins == 691)

# Clue 3
ss = meg.slot(Activity.SKIING)
assert((ss.end - ss.start).mins == 83)
assert(ss.start <= Time(1,32) <= ss.end)

# Clue 4
cs = jo.slot(Activity.CURLING)
assert(969 % (cs.end - cs.start).mins == 0)

# Clue 5
assert(jo.slot(Activity.SKIING).start == Time(7,30))

# Clue 6
ss = meg.slot(Activity.SKATING)
assert(ss.start == Time(0,0))
assert(ss.end == Time(1,10))

# Clue 7
same_activity((meg, bob), Activity.MATH)
mps = meg.slot(Activity.MATH)
assert((mps.end - mps.start).mins == 108)

# Clue 8 (negated because Kip is the thief)
cs = jo.slot(Activity.CURLING)
assert((cs.end - cs.start).mins != 323)

# Clue 9 (negated because Kip is the thief)
assert(jo.slot(Activity.SKIING).start != Time(6,8))

# Clue 10
s = Time(0)
for h in (jo, meg) :
    ls = h.slot(Activity.LUNCH)
    s += ls.end - ls.start
assert(s == Time(1,57))

# Clue 11
same_activity((fred, meg), Activity.CHESS)
cs = fred.slot(Activity.CHESS)
assert((cs.end - cs.start).mins == 135)

# Clue 12
for h in (bob, kip, fred) :
    assert(h.slot(Activity.LUNCH).end == Time(3,30))

# Clue 13
css = [h.slot(Activity.CLIMBING) for h in helpers if h.slot(Activity.CLIMBING) is not None]
assert(len([s for s in css if s.start >= Time(3,30) and s.end <= Time(4,45)]) == 3)

# Clue 14
s = Time(0)
for h in (bob, meg, fred) :
    ss = h.slot(Activity.SKATING)
    s += ss.end - ss.start
assert(s.mins == 269)

# Clue 15
for h in (fred, bob, kip) :
    assert(h.slot(Activity.LUNCH).start == Time(2,52))

# Clue 16
mps = fred.slot(Activity.MATH)
assert((mps.end - mps.start).mins == 172)

# Clue 17
same_activity((jo, fred, meg), Activity.TENNIS)
ts = jo.slot(Activity.TENNIS)
assert((ts.end - ts.start).mins == 15)

# Clue 18
jss = jo.slot(Activity.SKIING)
bss = bob.slot(Activity.SKIING)
assert(jss.start == bss.start)
assert(jss.end == Time(8,45))
assert(jss.end < bss.end)

# Clue 19
hs = (fred, bob, kip, jo)
same_activity(hs, Activity.CURLING)
for h in hs :
    assert(h.slot(Activity.CURLING).start == Time(4,45))

# Clue 20
for h in (fred, jo) :
    s = h.slot(Activity.MATH)
    assert(s.start <= Time(1,12) <= s.end)

# Clue 21
same_activity((jo, kip), Activity.CHESS)
cs = jo.slot(Activity.CHESS)
assert((cs.end - cs.start).mins == 108)
assert(jo.slot(Activity.CURLING).end == cs.start)

# Clue 22
mps = jo.slot(Activity.MATH)
assert((mps.end - mps.start).mins == 153)

# Clue 23
ss = bob.slot(Activity.SKIING)
assert((ss.end - ss.start).mins == 150)

# Clue 24
same_activity((bob, kip), Activity.BILLIARDS)
bs = bob.slot(Activity.BILLIARDS)
assert(bs.start == Time(0,0))
assert(bs.end == Time(1,21))

# Final message
print("Solution satisfies all clues!")
