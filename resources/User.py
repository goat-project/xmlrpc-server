# # Simulate calls for user service
import os

from resources.resource import Resource, read_from_dir


class User:
    @staticmethod
    def list(session):
        # Lists all users.

        return [bool(1), read_from_dir(Resource.USER), int(0)]
