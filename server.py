import sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from args import args
from resources.cluster import Cluster
from resources.host import Host
from resources.image import Image
from resources.User import User
from resources.virtualmachine import VirtualMachine


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server.
with SimpleXMLRPCServer(('localhost', args.port), requestHandler=RequestHandler) as server:
    print(f"Server starts listening at {args.host}:{args.port}.")  # TODO add logger

    # Register functions simulated OpenNebula cloud.
    server.register_function(VirtualMachine.list, 'one.vmpool.info')
    server.register_function(VirtualMachine.retrieve_info, 'one.vm.info')

    server.register_function(User.list, 'one.userpool.info')
    server.register_function(Image.list, 'one.imagepool.info')
    server.register_function(Host.list, 'one.hostpool.info')
    server.register_function(Cluster.list, 'one.clusterpool.info')

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)
