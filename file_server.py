#!/usr/bin/env python
# http://twistedmatrix.com/documents/current/web/howto/web-in-60/static-content.html
# Similar to command: `twistd -n web --path /home/hakim`
from twisted.web.static import File
from twisted.web.server import Site
from twisted.internet import reactor, endpoints


# Serve static files from given folder
resource = File('/home/hakim')
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
endpoint.listen(factory)
reactor.run()
