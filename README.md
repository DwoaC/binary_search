# binary_search
Generator that searches ranges of integers.

I'm a big fan of [CodeInGame.com](https://www.codingame.com) for practicing interesting
development problems.  One particular problem, [Shadows Of The Knight](https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1),
is a binary search problem.  The key in the problem is that there are 2 binary searches
happening at the same time, one in the x direction and one in the y direction.

I thought this was a great opportunity to play with a generator that makes use of both
sides of the yield statement.

Random points:
* I hate sending in strings as parameters to change behaviour.  Given how the game
is implemented I think this is sensible in this context.  The sent values could have
been changed to 1, -1 and 0.  If we uses constants to represent these as high, low and
null it would be just as readable as the strings.
* There is a lot to be said for the search raising a StopIteration exception
when we reach a final value.  Again it fit easier with the game to just
let the searcher keep repeating the last value.  This way the x and y searches
could continue on operating in parallel.
* Dito for raising an exception for sending in values other than 'high', 'low' and
None


Setting up a binary search in the range 0-100 inclusive and starting at 50.
    >>> from binary_search import binary_search
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
