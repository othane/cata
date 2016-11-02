"""
Custom middlewares for the cata project
"""
import logging

class FullRequestLoggingMiddleware(object):
    """
    This middleware is a customer logger to give better logging
    of the requests hitting the server
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def process_request(self, request):
        self.logger.info('[{0.method}] {1}, (body:{0.body})'.format(request, request.get_raw_uri()))
        return None

