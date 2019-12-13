# # Simulate calls for cluster service
import os

from resources.resource import Resource, read_from_dir


class Cluster:
    @staticmethod
    def list(session):
        # Lists all clusters.

        return [bool(1), read_from_dir(Resource.CLUSTER), int(0)]
