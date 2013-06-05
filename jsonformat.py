#!/usr/bin/env python

import json, sys, collections

data = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
d = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
print json.dumps(d.decode(data), indent=2)

