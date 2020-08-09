import settings
import argparse
import logging
import signal
import sys

from datetime import datetime

################################################################################

class xmppServer:

    def __init__(self, port):

        self.port = port

    def run(self):

    	pass

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

	argparser.add_argument('-p', '--port', action='store', help='port for client connections', type=int, default = 5222)

	command_line_args = argparser.parse_args()

	logging.info('Arguments %s', vars(command_line_args))

	server = xmppServer(command_line_args.port)

	server.run()

	logging.info('SHUTDOWN')

################################################################################

if __name__ == "__main__":

	main()

################################################################################
