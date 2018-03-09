from .interface import UserParser, DefaultUserParser
from typing import Type
import incantation as inc


def make_table(user: dict, parser: Type[UserParser] = DefaultUserParser):
    return inc.Table(data_source=[[''] + list(user.values()),
                                  [''] + list(user.values())],
                     columns=[''] + list(user.keys()))
