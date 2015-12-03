#!/usr/bin/env python

import json, sys, collections, argparse

p = argparse.ArgumentParser(description='JSON Formatter')
p.add_argument('-f', '--filename', help='File to format')
p.add_argument('-i', '--inplace', action='store_true', help='Format file in place')
p.add_argument('-u', '--unformat', action='store_true', help='Unformat the JSON')

args = p.parse_args()

file_name = args.filename if args.filename else None
if file_name:
    f = open(file_name)
    data = f.read()
    f.close()
else:
    data = sys.stdin.read()

decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)

format_args = {}
if not args.unformat:
    format_args['indent'] = 2
formatted = json.dumps(decoder.decode(data), **format_args)

if file_name and args.inplace:
    f = open(file_name, 'w')
    f.write(formatted)
    f.close()
else:
    print(formatted)

