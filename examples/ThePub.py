#!/usr/bin/env python
#
# ThePub.py - Simple script to see what's happening in the Pub
#

import untappd

# Unauthenticated call to the API. Replace with your own API key first
u = untappd.Api('MY API KEY GOES HERE', '', '')

# Get The Pub feed. By default it will return at max 25 records.
data = u.get_thepub()

for result in data['results']:
    print "%s %s is drinking a %s by %s" % (result['user']['first_name'],
        result['user']['last_name'], result['beer_name'],
        result['brewery_name'])
