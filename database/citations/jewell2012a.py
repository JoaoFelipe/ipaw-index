# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import jewell2012a
from ..work.y2015 import moreau2015a

DB(Citation(
    moreau2015a, jewell2012a, ref="",
    contexts=[

    ],
))
