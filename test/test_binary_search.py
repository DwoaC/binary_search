import unittest
from binary_search import binary_search

import logging
logger = logging.getLogger(__name__)

class TestBinarySearch(unittest.TestCase):

    def test_sending_values_into_binary_search(self):
        bs = binary_search(x_current=50, x_min=0, x_max=100)
        self.send_in_to_generator(
            searcher=bs,
            values_to_send=('low', 'high', 'low', 'high', 'low'),
            final_value=34)

        bs = binary_search(x_current=50, x_min=0, x_max=100)
        self.send_in_to_generator(
            searcher=bs,
            values_to_send=('low', 'high', 'low', 'high', 'low', None),
            final_value=34)

        bs = binary_search(x_current=95, x_min=0, x_max=100)
        self.send_in_to_generator(
            searcher=bs,
            values_to_send=('high', 'low', 'high', 'low'),
            final_value=96)

        bs = binary_search(x_current=50, x_min=0, x_max=100)
        self.send_in_to_generator(
            searcher=bs,
            values_to_send=('low', 'low', 'low', 'low', 'low', 'low', 'low'),
            final_value=0)

        bs = binary_search(x_current=50, x_min=0, x_max=100)
        self.send_in_to_generator(
            searcher=bs,
            values_to_send=('high', 'high', 'high', 'high', 'high', 'high', 'high'),
            final_value=100)

    def send_in_to_generator(self, searcher, values_to_send, final_value):
        logger.info('Creating generator')
        searcher.send(None)
        logger.info('Calling next to start generator')
        for low_high in values_to_send:
            logger.info('Sending: {}'.format(low_high))
            result = searcher.send(low_high)
            logger.info('Getting result')
            logger.info('Got result: {}'.format(result))
        self.assertEqual(result, final_value)