#!/usr/bin/env python
#
# UserDistinct.py - Simple script to see one's distinct beers
#

import untappd

# Unauthenticated call to the API. Replace with your own API key first
u = untappd.Api('MY API KEY GOES HERE', '', '')

# Get User's distinct beers. By default it will return at max 25 records.
# Let's see what Greg has been drinking lately.
data = u.get_user_distinct(**{'user': 'gregavola'})

for result in data['results']:
    print "%s by %s" % (result['beer_name'], result['brewery_name'])
