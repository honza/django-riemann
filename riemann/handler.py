import socket
import logging
import traceback
from django.conf import settings
from bernhard import Client, UDPTransport, TCPTransport

RIEMANN_HOST = getattr(settings, 'RIEMANN_LOGGER_HOST', '127.0.0.1')
RIEMANN_PORT = getattr(settings, 'RIEMANN_LOGGER_PORT', '5555')
RIEMANN_TRANSPORT = getattr(settings, 'RIEMANN_LOGGER_TRANSPORT', 'udp')
HOST = socket.gethostname()

if RIEMANN_TRANSPORT == 'udp':
    transport = UDPTransport
elif RIEMANN_TRANSPORT == 'tcp':
    transport = TCPTransport
else:
    raise Exception("'%s' transport unknown" % RIEMANN_TRANSPORT)

c = Client(host=RIEMANN_HOST, port=RIEMANN_PORT, transport=transport)


class RiemannHandler(logging.Handler, object):

    def emit(self, record):
        event = {
            'host': HOST,
            'service': 'django-logger',
            'state': record.levelname,
            'time': int(record.created),
            'tags': [record.name]
        }

        if record.exc_info:
            tb = traceback.format_exception(*record.exc_info)
            event['description'] = ''.join(tb)

        c.send(event)
