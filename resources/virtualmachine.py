# Simulate calls for virtual machine service
import os

from args import args
from resources.resource import Resource, pool_beginning, pool_end, dir_name, read_from_dir

import xml.etree.ElementTree as ET


class VirtualMachine:
    @staticmethod
    def list(session, filter_tag, page_offset, page_size, vm_state):
        # Lists all virtual machines.
        # If filter_tag is not -2, lists all active virtual machines specified
        # for a user given by UID (user identifier) in filter_tag.

        # avoid pagination
        if page_offset > 0:
            return [bool(1), pool_beginning(Resource.VM) + pool_end(Resource.VM), int(0)]

        return [bool(1), read_from_dir(Resource.VM, filter_tag), int(0)]

    @staticmethod
    def retrieve_info(session, identifier):
        # Retrieves info for a virtual machine given by identifier.

        directory = os.path.join(args.input_dir, dir_name(Resource.VM))
        files = os.listdir(directory)

        # find first occurrence of identifier and return whole file
        for file in files:
            root = ET.parse(directory + file).getroot()
            if identifier == int(root.find('ID').text):
                f = open(directory + file, "r")
                vm = f.read()
                f.close()

                return [bool(1), vm, int(0)]

        # should never happen
        print("unable find given ID")  # TODO add logging
        return [bool(1), "<VM></VM>", int(0)]
