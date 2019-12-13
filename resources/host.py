# # Simulate calls for host service
import os

from resources.resource import Resource, read_from_dir


class Host:
    @staticmethod
    def list(session):
        # Lists all hosts.

        return [bool(1), read_from_dir(Resource.HOST), int(0)]