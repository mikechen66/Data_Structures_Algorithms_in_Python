

# multimap.py

"""

Internally the mapping is represented as a list of (key, value) pairs (which
is what maintains the order) AND a mapping of keys to a list of positions in
the pair list (for making everything faster). Need to keep in mind that any
given list in _key_ids may be empty.

# Source code: 
https://github.com/pombredanne/MultiMap/blob/master/multimap.py

"""


import collections.abc
from bisect import bisect


class MultiMap(collections.Mapping):
    """An ordered mapping which supports multiple values for the same key."""
    def __init__(self, *args, **kwargs):
        self._pairs = []
        for arg in args:
            if isinstance(arg, collections.Mapping):
                for x in arg.items():
                    self._pairs.append(self._conform_pair(x))
            else:
                for x in arg:
                    self._pairs.append(self._conform_pair(x))
        for x in kwargs.items():
            self._pairs.append(self._conform_pair(x))
        self._rebuild_key_ids()
    def _rebuild_key_ids(self):
        """Rebuild the internal key to index mapping."""
        self._key_ids = collections.defaultdict(list)
        for i, x in enumerate(self._pairs):
            self._key_ids[x[0]].append(i)
    def _conform_key(self, key):
        """Force a given key into certain form. For overriding."""
        return key
    def _conform_value(self, value):
        """Force a given value into certain form. For overriding."""
        return value
    def _conform_pair(self, pair):
        """
        Force a given key/value pair into a certain form.
        Override the _conform_key and _conform_value if you want to change
        the mapping behaviour.
        """
        pair = tuple(pair)
        if len(pair) != 2:
            raise ValueError('MultiMap element must have length 2')
        return (self._conform_key(pair[0]), self._conform_value(pair[1]))
    @classmethod
    def fromkeys(cls, keys, value=None):
        return cls([(k, value) for k in keys])
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._pairs)
    def __nonzero__(self):
        return bool(self._pairs)
    def __getitem__(self, key):
        """Get the FIRST value for the given key."""
        key = self._conform_key(key)
        try:
            return self._pairs[self._key_ids[key][0]][1]
        except IndexError:
            raise KeyError(key)
    def __contains__(self, key):
        """Is the given key in this mapping"""
        # Need to explicitly check the value of the id list, as it may be in
        # there already but be empty.
        return bool(self._key_ids[self._conform_key(key)])
    def has_key(self, key):
        return key in self
    def __len__(self):
        return len(self._key_ids)
    def alllen(self):
        return len(self._pairs)
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    def getall(self, key):
        key = self._conform_key(key)
        return [self._pairs[i][1] for i in self._key_ids[key]]
    # These are for compatibility with other multi-value mapping libraries.
    getlist = list = getall
    def iteritems(self):
        """
        Iterator across all the non-duplicate keys and their values.
        Only yields the first key of duplicates.
        """
        keys_yielded = set()
        for k, v in self._pairs:
            if k not in keys_yielded:
                keys_yielded.add(k)
                yield k, v  
    def __iter__(self):
        """Iterate across the unique keys in the mapping."""
        return (x[0] for x in self.iteritems())
    def keys(self):
        """A list of the first keys in the mapping, in order."""
        return list(self)
    def iterkeys(self):
        """Iterate across the first keys in the mapping."""
        return iter(self)
    def iterallkeys(self):
        """Iterate across ALL of the keys in the mapping, in order."""
        for x in self._pairs:
            yield x[0]
    def allkeys(self):
        """A list of ALL of the keys in the mapping, in order."""
        return [x[0] for x in self._pairs]
    def items(self):
        """A list of items with the first keys in the mapping."""
        return list(self.iteritems())
    def itervalues(self):
        """Iterate across the value for the first keys in the mapping."""
        return (x[1] for x in self.iteritems())
    def values(self):
        """A list of values for the first keys in the mapping."""
        return list(self.itervalues())
    def iterallvalues(self):
        """Iterate across ALL of the values in the mapping."""
        for x in self._pairs:
            yield x[1]
    def allvalues(self):
        """A list of ALL values in the mapping."""
        return [x[1] for x in self._pairs]
    def iterallitems(self):
        """Iterate across ALL of the pairs in the mapping."""
        return iter(self._pairs)
    def allitems(self):
        """A list of ALL of the pairs in the mapping."""
        return self._pairs[:]


if __name__ == '__main__':
    # Initialize a MultiMap
    m1 = MultiMap(a=1, b=2)
    print(m1)
    m2 = MultiMap(a=1, b=2, c=3, d=4)
    print(m2)


# Output:

"""
MultiMap([('a', 1), ('b', 2)])
MultiMap([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
"""