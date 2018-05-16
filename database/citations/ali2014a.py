# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import ali2014a
from ..work.y2015 import katilu2015a

DB(Citation(
    katilu2015a, ali2014a, ref="",
    contexts=[

    ],
))
