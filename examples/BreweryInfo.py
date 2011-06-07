#!/usr/bin/env python
#
# BreweryInfo.py - Simple script to get information about a brewery
#

import untappd

# Unauthenticated call to the API. Replace with your own API key first
u = untappd.Api('MY API KEY GOES HERE', '', '')

# Get information about Brouwerij Abdij Saint Sixtus
data = u.get_brewery_info('263')

print "%s from %s" % (data['results']['name'], data['results']['country'])
