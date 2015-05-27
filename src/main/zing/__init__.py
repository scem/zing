from zing.zinger import Zinger as Z
class Zinger(Z): pass

from zing.newsroom import NewsRoom as NR
from zing.newsroom import OPEN, CLOSED
class NewsRoom(NR):
    OPEN = OPEN
    CLOSED = CLOSED

from zing.follower import Follower as F
from zing.follower import ONLINE, OFFLINE
class Follower(F):
    OFFLINE = OFFLINE
    ONLINE = ONLINE