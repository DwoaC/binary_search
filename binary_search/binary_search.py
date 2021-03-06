import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def binary_search(x_current, x_max, x_min=0):
    '''
    Generator to perform binary search on a range of integers.

    :param x_current: (int) Starting point in the range
    :param x_max: (int) The max possible value that can be found
    :param x_min: (int) The min possible value that can be found
    :send_in: (str) the strings 'high' and 'low' should be sent in to indicate
    if the last value was above or below the target value

    Setting up a binary search in the range 0-100 inclusive and starting at 50.
    >>> bs = binary_search(x_current=5, x_min=0, x_max=10)
    >>> bs
    <generator object binary_search at 0x106ce7468>

    Prime the generator.
    >>> bs.send(None)
    5

    Start searching.
    >>> bs.send('low')
    2
    >>> bs.send('high')
    4
    >>> bs.send('low')
    3

    Once the search is complete sending in more values yeilds the same result.
    >>> bs.send('low')
    3

    Sending anything other than 'high' or 'low' doesn't effect the search and
    yeilds the current search value.
    >>> bs.send(None)
    3

    This can be used to get the current search or to keep loops sensible even
    when valid results can't be calculated.
    '''
    logger.info('Creating new binary searcher. current={}, max={}, min={}'.format(
        x_current,
        x_max,
        x_min
    ))
    history = []
    high_low = None
    while True:
        logger.info('Waiting for high_low')
        logger.info('Got {} passed in'.format(high_low))
        if high_low == 'high':
            x_min = x_current
            x_current = round((x_max + x_current) / 2)
        elif high_low == 'low':
            x_max = x_current
            x_current = round((x_current + x_min) / 2)
        logger.info('Preparing to yielding {}'.format(x_current))
        history.append(x_current)
        high_low = (yield x_current)
        logger.info('Loop complete.  History: {}'.format(history))
