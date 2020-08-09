# ecc2xmpp

XMPP Client Bridge for ECC Messaging

    $ python3 ecc2xmpp.py -h

    Usage: ecc2xmpp.py [-h] [-a ADDR] [-p PORT]

    XMPP Client Bridge for ECC Messaging

    optional arguments:
      -h, --help            show this help message and exit
      -a ADDR, --addr ADDR  address to accept connections
      -p PORT, --port PORT  port for client connections

**ADDR**

The default ADDR is 127.0.0.1 which will only accept connections from XMPP clients running on the same host. If you wish to allow network connections, either specify the IP address of the relevant interface, or specify 0.0.0.0 to accept connections on all interfaces

Note the signifcant security dangers in permitting network connections.

**PORT**

The default port for XMPP clients is 5222. You may need to specify a different port if you are running multiple XMPP servers or wish to navigate firewall traversal.

