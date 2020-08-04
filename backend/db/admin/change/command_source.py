from enum import Enum
from typing import Callable

from db.admin.change.api.fossabot_api import query_fossabot
from db.admin.change.api.nightbot_api import query_nightbot
from db.admin.change.api.streamelements_api import query_streamelements
from db.admin.change.api.streamlabs_api import query_streamlabs


class CommandSource(Enum):
    FOSSABOT = "fossabot", query_fossabot
    NIGHTBOT = "nightbot", query_nightbot
    STREAMELEMENTS = "streamelements", query_streamelements
    STREAMLABS = "streamlabs", query_streamlabs

    def __init__(self, name: str, query: Callable):
        self._name = name
        self._query = query

    def __new__(cls, *args, **kwargs):  # Allow reverse lookup
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    @property
    def name(self):
        return self._name

    @property
    def query(self):
        return self._query
