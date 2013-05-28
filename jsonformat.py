#!/usr/bin/env python

import json, sys, collections

d = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
print json.dumps(d.decode(sys.argv[1]), indent=2)

