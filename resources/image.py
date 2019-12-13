# # Simulate calls for image service
import os

from resources.resource import Resource, read_from_dir


class Image:
    @staticmethod
    def list(session, filter_tag, page_offset, page_size):
        # Lists all images.

        return [bool(1), read_from_dir(Resource.IMAGE), int(0)]
