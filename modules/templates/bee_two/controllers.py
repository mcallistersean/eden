# -*- coding: utf-8 -*-

from gluon import *
from s3 import S3CustomController

THEME = "bee_two"

# =============================================================================
# class index(S3CustomController):
#
#     def __call__(self):
#         print 'index!!'
#         self._view(THEME, "index.html")
#         return {}

def rest():
    return s3_rest_controller()

# END =========================================================================
