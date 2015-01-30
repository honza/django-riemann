django-riemann
==============

Send logging information to a [Riemann][1] instance via Django's `LOGGING`
directive.

[1]: http://riemann.io/

Installl
--------

```
pip install django-riemann
```

Fields
------

```
host: the host name of the app that is sending the logs
service: 'django-logger'
state: log level
time: time of the log event
tags: logger name
description: traceback if available
```

Configuration
-------------



``` python
RIEMANN_LOGGER_HOST = '127.0.0.1'
RIEMANN_LOGGER_PORT = '5555'
RIEMANN_LOGGER_TRANSPORT = 'udp'  # or 'tcp'


LOGGING = {
    ...
    'handlers': {
        'riemann': {
            'level': 'INFO',
            'class': riemann.handler.RiemannHandler'
        }
    }
}
LOGGING['root']['handlers'].append('riemann')
```

License
-------

BSD, short and sweet
