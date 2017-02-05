#!/usr/bin/env python
# http://adcaes.org/2015/09/14/getting-started-with-twisted/
from twisted.internet.task import react, defer
import treq


def get_url(url):
    def handle_response(resp):
        print('Response code %d from %s' % (resp.code, url))

    def handle_failure(failure):
        print('Something failed: %s' % failure.getErrorMessage())

    print('Getting url: %s' % url)
    d = treq.get(url)
    d.addCallback(handle_response)
    d.addErrback(handle_failure)

    return d


def main(reactor, *args):
    urls = ['http://github.com', 'http://google.com', 'http://facebook.com']
    ds = map(get_url, urls)
    d = defer.gatherResults(ds)

    return d


react(main)
