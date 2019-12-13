import os
from enum import Enum

from args import args

import xml.etree.ElementTree as ET


class Resource(Enum):
    # Enum resources used in this xml-rpc server.

    VM = 1
    VN = 2
    USER = 3
    IMAGE = 4
    HOST = 5
    CLUSTER = 6


# text representation of resources
resources = {Resource.VM: "VM", Resource.VN: "VN", Resource.USER: "USER", Resource.IMAGE: "IMAGE",
             Resource.HOST: "HOST", Resource.CLUSTER: "CLUSTER"}

# ACTIVE state
ACTIVE = 3

# Suffix of directory with resource
RESOURCE_DIR_SUFFIX = "_outputs/"


def read_from_dir(resource, user=-2):
    # Reads all files in the given directory and returns them with POOL tags.
    # If user is not -2, reads files specified for a given user.
    # POOL tags contains then name of given resource.
    # Example: <VM_POOL>...</VM_POOL>

    directory = os.path.join(args.input_dir, dir_name(resource))
    files = os.listdir(directory)

    pool = pool_beginning(resource)

    if user == -2:
        read_all(directory, files)
    else:
        read_active_for_user(directory, files, user)

    pool = pool + pool_end(resource)

    return pool


def read_all(directory, files):
    # Returns content of all files.

    pool = ""

    for file in files:
        f = open(directory + file, "r")
        pool = pool + f.read()
        f.close()

    return pool


def read_active_for_user(directory, files, user):
    # Returns content of all files where UID (user identifier) matches
    # and state of the resource is ACTIVE (3).

    pool = ""

    for file in files:
        root = ET.parse(directory + file).getroot()
        if int(root.find('UID').text) == user:
            if int(root.find('STATE').text) == ACTIVE:
                f = open(directory + file, "r")
                pool = pool + f.read()
                f.close()

    return pool


def dir_name(resource):
    # Creates directory name as MAD generator generates.
    # Directory contains XML formatted files with given resource.

    return resources[resource].lower() + RESOURCE_DIR_SUFFIX


def pool_beginning(resource):
    # Returns pool beginning tag.

    return "<" + resources[resource] + "_POOL>"


def pool_end(resource):
    # Returns pool end tag.

    return "</" + resources[resource] + "_POOL>"
