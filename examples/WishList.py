#!/usr/bin/env python
#
# WishList.py - Simple script to see one's wished beers
#

import untappd

# Unauthenticated call to the API. Replace with your own API key first
u = untappd.Api('MY API KEY GOES HERE', '', '')

# Let's see what Tim has on his wish list.
data = u.get_wish_list(**{'user': 'timm3h'})

for result in data['results']:
    print "%s by %s (http://untappd.com/beer/%s)" % (result['beer_name'],
        result['brewery_name'], result['beer_id'])
