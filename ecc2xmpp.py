import settings
import argparse
import logging
import socket
import signal
import sys

from datetime import datetime

################################################################################

class xmppServer:

	def __init__(self, addr, port):

		self.addr = addr
		self.port = port

	def run(self):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		s.bind((self.addr, self.port))

		logging.info('Server bound to address %s port %d', self.addr, self.port)

		s.listen(0) # don't allow unaccepted connections to be queued by the OS

################################################################################

def terminate(signalNumber, frame):

	logging.info('%s received - terminating' % signal.Signals(signalNumber).name)

	sys.exit()

################################################################################
### Main program ###############################################################
################################################################################

def main():

	logging.basicConfig(filename = 'log/{:%Y-%m-%d}.log'.format(datetime.now()),
						filemode = 'a',
						level    = logging.INFO,
						format   = '%(asctime)s - %(levelname)s : %(message)s',
						datefmt  = '%d/%m/%Y %H:%M:%S')

	logging.info('STARTUP')

	signal.signal(signal.SIGINT,  terminate)  # keyboard interrupt ^C
	signal.signal(signal.SIGTERM, terminate)  # kill [default -15]

	argparser = argparse.ArgumentParser(description='XMPP Client Bridge for ECC Messaging')

	argparser.add_argument('-a', '--addr', action='store', help='address to accept connections', type=str, default = '127.0.0.1')
	argparser.add_argument('-p', '--port', action='store', help='port for client connections'  , type=int, default = 5222)

	command_line_args = argparser.parse_args()

	logging.info('Arguments %s', vars(command_line_args))

	server = xmppServer(command_line_args.addr, command_line_args.port)

	server.run()

	logging.info('SHUTDOWN')

################################################################################

if __name__ == "__main__":

	main()

################################################################################
