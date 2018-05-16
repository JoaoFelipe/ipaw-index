# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import dey2014a
from ..work.y2017 import alper2017a

DB(Citation(
    alper2017a, dey2014a, ref="",
    contexts=[

    ],
))
