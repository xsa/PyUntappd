"""
untappd.py - v0.1

Python wrapper for the Untappd API - http://untappd.com/api/docs


Copyright (c) 2011 Xavier Santolaria <xavier@santolaria.net>

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""

import hashlib
import json
import pycurl
import urllib

from StringIO import StringIO

class Api:
    """
        Untappd API class

        Arguments:
            ``apikey``
                Your API Key provided when you are approved

        Arguments (optional):
            ``user``
                Required for authenticated requests
            ``password``
                Required for authenticated requests
    """
    def __init__(self, arg1, arg2, arg3):
        self.url = 'http://api.untappd.com/v3/'
        self.apikey = arg1
        self.user = arg2
        self.password = arg3

    def _return_result(self, method, params=None):
        """
            Internal method to return the results.

            Arguments:
                ``method``
                    The Untappd API method for this request
                    Required for authenticated requests
                ``params``
                    GET parameters to send to the Untappd API
        """

        c = pycurl.Curl()

        query_url = self.url + method + '?key=' + self.apikey

        if params:
            data = urllib.urlencode(params)
            c.setopt(pycurl.URL, '%s&%s' % (query_url, data) )
        else:
            print query_url
            c.setopt(pycurl.URL, query_url)

        if self.user and self.password:
            # MD5'ing password for Untappd auth. mechanism
            md5p = hashlib.md5(self.password).hexdigest()
            c.setopt(pycurl.USERPWD, '%s:%s' % (self.user, md5p))
        try:
            b = StringIO()
            c.setopt(pycurl.WRITEFUNCTION, b.write)
            c.perform()
            result = json.loads(b.getvalue())
        except IOError, e:
            result = json.load(e)
        return result


    def get_beer_info(self, id):
        """
            Returns extended information about a  beer.

            Arguments (required):
                ``bid``
                    The numeric beer ID of the beer you wish to look up
        """
        return self._return_result('beer_info', params={'bid': id})

    def get_brewery_info(self, id):
        """
            Returns extended information about a brewery.

            Arguments (required):
                ``brewery_id``
                    The numeric brewery ID of the beer you wish to look up
        """
        return self._return_result('brewery_info', params={'brewery_id': id})

    def get_feed(self, **kwargs):
        """
            Returns all the friend check-in feed of the authenticated user.
            This includes only beer checkin-ins from Friends.
            By default it will return at max 25 records.

            Arguments (optional):
                ``offset``
                    The offset that you like the dataset to begin with
        """
        return self._return_result('feed', params=kwargs)

    def get_thepub(self):
        """
            Returns all public feed for Untappd. Includes only beer
            checkin-ins non private users by an authenticated user.
            By default it will return at max 25 records.

            Arguments: None
        """
        return self._return_result('thepub')

    def get_user_badges(self, **kwargs):
        """
            Returns all the user's badges.
            If you want to obtain the authenticated user's information,
            you don't need to pass the "user" query string.

            Arguments (optional):
                ``user``
                    The user that you wish to call the request upon.
                    If you do not provide a username - the feed will
                    return results from the authenticated user.
        """
        params = {'user': self.user}

        if 'user' in kwargs:
            params['user'] = kwargs['user']

        return self._return_result('user_badge', params=params)

    def get_user_distinct(self, **kwargs):
        """
            Returns all the user's distinct beers.
            By default it will return at max 25 records.

            Arguments (optional):
                ``user``
                    The user that you wish to call the request upon.
                    If you do not provide a username - the feed will
                    return results from the authenticated user.
                ``offset``
                    The offset that you like the dataset to begin with
        """
        params = {'user': self.user, 'offset': 0}

        if 'user' in kwargs:
            params['user'] = kwargs['user']
        if 'offset' in kwargs:
            params['offset'] = kwargs['offset']

        return self._return_result('user_distinct', params=params)

    def get_user_feed(self, **kwargs):
        """
            Returns all the friend check-in feed of the selected user.
            This includes only beer checkin-ins the selected user.
            By default it will return at max 25 records.

            Arguments (optional):
                ``user``
                    The user that you wish to call the request upon.
                    If you do not provide a username - the feed will
                    return results from the authenticated user.
                ``offset``
                    The offset that you like the dataset to begin with
        """
        params = {'user': self.user, 'offset': 0}

        if 'user' in kwargs:
            params['user'] = kwargs['user']
        if 'offset' in kwargs:
            params['offset'] = kwargs['offset']

        return self._return_result('user_feed', params=params)

    def get_user_info(self, **kwargs):
        """
            Returns the user information for a selected user.
            If you want to obtain the authenticated user's information,
            you don't need to pass the "user" query string.

            Arguments (optional):
                ``user``
                    The user that you wish to call the request upon.
                    If you do not provide a username - the feed will
                    return results from the authenticated user.
        """
        params = {'user': self.user}

        if 'user' in kwargs:
            params['user'] = kwargs['user']

        return self._return_result('user', params=params)

    def get_venue_feed(self, id):
        """
            Returns a feed for a single venue for Untappd.
            By default it will return at max 25 records.

            Arguments (required):
                ``venue_id``
                    The Venue ID that you want to display checkins
        """
        return self._return_result('venue_checkins', params={'venue_id': id})

    def get_venue_info(self, id):
        """
            Returns extended information about a venue.

            Arguments (required):
                ``venue_id``
                    The numeric venue ID of the venue you wish to look up
        """
        return self._return_result('venue_info', params={'venue_id': id})

    def get_wish_list(self, **kwargs):
        """
            Returns all the user's wish listed beers.

            Arguments (optional):
                ``user``
                    The user that you wish to call the request upon.
                    If you do not provide a username - the feed will
                    return results from the authenticated user.
                ``offset``
                    The offset that you like the dataset to begin with
        """
        params = {'user': self.user, 'offset': 0}

        if 'user' in kwargs:
            params['user'] = kwargs['user']
        if 'offset' in kwargs:
            params['offset'] = kwargs['offset']

        return self._return_result('wish_list', params=params)
