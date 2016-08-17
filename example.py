#!/usr/bin/python

"""@package dried_ice_dev
Documentation about this package
"""

from time import sleep

from lib.forge.lite_logger import LiteLogger
logger = LiteLogger(True)
logger.get_log()
_log = LiteLogger(True).get_log()

from dry_ice import DryIce
DryIce.generate_slices()

from dried_ice.example import HelloWorld
from dried_ice.example import HelloWorldPrx

__copyright__ = "Copyright 2015 The Paladin's Forge"
__email__ = "ThePaladinsForge@gmail.com"
__version__ = "1.0"
__status__ = "Development"  # Prototype, Development, Production


class HelloWorldImpl(HelloWorld):
    def send_async(self, _cb, msg, current=None):
        _log.info("Hello World: {}".format(msg))
        _cb.ice_response(None)

if __name__ == '__main__':
    dry_ice = DryIce()
    server = dry_ice.activate_server("default -p 12345")
    server.add_servant(HelloWorldImpl(), "hello-world")
    prx_l = server.get_local_proxy("hello-world", HelloWorldPrx)
    prx_l.send("Test")
    prx_r = dry_ice.get_client_proxy("hello-world:tcp -h 127.0.0.1 -p 12345", HelloWorldPrx)
    _log.info(prx_r)
    prx_r.send("Test")

    sleep(1)
    dry_ice.shutdown()

LiteLogger().shutdown()
