# -*- coding: utf-8 -*-
# from encodings import aliases
import encodings.aliases  # noinspection PyUnresolvedReferences
arr = encodings.aliases.aliases
keys = list( arr.keys() )
keys.sort()
for key in keys:
    print("%s => %s" % (key, arr[key]))