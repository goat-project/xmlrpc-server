import argparse

parser = argparse.ArgumentParser(description='XMLRPC server, simulator of OpenNebula cloud responses.')

parser.add_argument(
    '--host',
    required=False,
    default='localhost',
    help='Host to bind to'
)

parser.add_argument(
    '--port',
    required=False,
    type=int,
    default=2633,
    help='port to bind to'
)

parser.add_argument(
    '--input-dir',
    required=True,
    help='Path to input files in XML format simulated OpenNebula responses'
)

parser.add_argument(
    '-d',
    '--debug',
    default=False,
    help='Enable debug mode'
)

parser.add_argument(
    '--log-path',
    help='Path to log'
)

args = parser.parse_args()
