#!/usr/bin/env python
# http://twistedmatrix.com/documents/current/web/howto/using-twistedweb.html
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints


class Simple(Resource):
    isLeaf = True

    def render_GET(self, request):
        return "<h1>Hello world</h1>".encode('utf-8')


# Serve a website
site = Site(Simple())
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
endpoint.listen(site)
reactor.run()
