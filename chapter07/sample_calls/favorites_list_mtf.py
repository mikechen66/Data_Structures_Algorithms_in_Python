

# favorites_list_mtf.py


from favorites_list import FavoritesList
from positional_list import PositionalList


def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)       #reinsert value before walk


class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic."""
    # we override _move_up to provide move-to-front semantics
    def _move_up(self, p):               
        # Move accessed item at Position p to front of list.
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))     # delete/reinsert
    # Override top because list is no longer sorted
    def top(self, k):
        # Generate sequence of top k elements in terms of access count.
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        # Begin by making a copy of the original list
        temp = PositionalList()
        for item in self._data:                            # positional lists support iteration
            temp.add_last(item)
        # Repeatedly find, report, and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
                # We have found the element with highest count
            yield highPos.element()._value                 # report element to user
            temp.delete(highPos)                           # remove from temp list


if __name__ == '__main__':
    fav = FavoritesListMTF()
    for c in 'hello. this is a test of mtf':               # well, not the mtf part...
        fav.access(c)
        k = min(5, len(fav))
        # Incur TypeError without str(list comprehension)
        # print('Top {0}) {1:25} {2}'.format(k, [x for x in fav.top(k)], fav))
        print('Top {0}) {1:25} {2}'.format(k, str([x for x in fav.top(k)]), fav))


# Output:

"""
Top 1) ['h']                     (h:1)
Top 2) ['h', 'e']                (h:1), (e:1)
Top 3) ['h', 'e', 'l']           (h:1), (e:1), (l:1)
Top 3) ['l', 'h', 'e']           (l:2), (h:1), (e:1)
Top 4) ['l', 'h', 'e', 'o']      (l:2), (h:1), (e:1), (o:1)
Top 5) ['l', 'h', 'e', 'o', '.'] (l:2), (h:1), (e:1), (o:1), (.:1)
Top 5) ['l', 'h', 'e', 'o', '.'] (l:2), (h:1), (e:1), (o:1), (.:1), ( :1)
Top 5) ['l', 'h', 'e', 'o', '.'] (l:2), (h:1), (e:1), (o:1), (.:1), ( :1), (t:1)
Top 5) ['l', 'h', 'e', 'o', '.'] (l:2), (h:2), (e:1), (o:1), (.:1), ( :1), (t:1)
Top 5) ['l', 'h', 'e', 'o', '.'] (l:2), (h:2), (e:1), (o:1), (.:1), ( :1), (t:1), (i:1)
Top 5) ['l', 'h', 'e', 'o', '.'] (l:2), (h:2), (e:1), (o:1), (.:1), ( :1), (t:1), (i:1), (s:1)
Top 5) ['l', 'h', ' ', 'e', 'o'] (l:2), (h:2), ( :2), (e:1), (o:1), (.:1), (t:1), (i:1), (s:1)
Top 5) ['l', 'h', ' ', 'i', 'e'] (l:2), (h:2), ( :2), (i:2), (e:1), (o:1), (.:1), (t:1), (s:1)
Top 5) ['l', 'h', ' ', 'i', 's'] (l:2), (h:2), ( :2), (i:2), (s:2), (e:1), (o:1), (.:1), (t:1)
Top 5) [' ', 'l', 'h', 'i', 's'] ( :3), (l:2), (h:2), (i:2), (s:2), (e:1), (o:1), (.:1), (t:1)
Top 5) [' ', 'l', 'h', 'i', 's'] ( :3), (l:2), (h:2), (i:2), (s:2), (e:1), (o:1), (.:1), (t:1), (a:1)
Top 5) [' ', 'l', 'h', 'i', 's'] ( :4), (l:2), (h:2), (i:2), (s:2), (e:1), (o:1), (.:1), (t:1), (a:1)
Top 5) [' ', 'l', 'h', 'i', 's'] ( :4), (l:2), (h:2), (i:2), (s:2), (t:2), (e:1), (o:1), (.:1), (a:1)
Top 5) [' ', 'l', 'h', 'i', 's'] ( :4), (l:2), (h:2), (i:2), (s:2), (t:2), (e:2), (o:1), (.:1), (a:1)
Top 5) [' ', 's', 'l', 'h', 'i'] ( :4), (s:3), (l:2), (h:2), (i:2), (t:2), (e:2), (o:1), (.:1), (a:1)
Top 5) [' ', 's', 't', 'l', 'h'] ( :4), (s:3), (t:3), (l:2), (h:2), (i:2), (e:2), (o:1), (.:1), (a:1)
Top 5) [' ', 's', 't', 'l', 'h'] ( :5), (s:3), (t:3), (l:2), (h:2), (i:2), (e:2), (o:1), (.:1), (a:1)
Top 5) [' ', 's', 't', 'l', 'h'] ( :5), (s:3), (t:3), (l:2), (h:2), (i:2), (e:2), (o:2), (.:1), (a:1)
Top 5) [' ', 's', 't', 'l', 'h'] ( :5), (s:3), (t:3), (l:2), (h:2), (i:2), (e:2), (o:2), (.:1), (a:1), (f:1)
Top 5) [' ', 's', 't', 'l', 'h'] ( :6), (s:3), (t:3), (l:2), (h:2), (i:2), (e:2), (o:2), (.:1), (a:1), (f:1)
Top 5) [' ', 's', 't', 'l', 'h'] ( :6), (s:3), (t:3), (l:2), (h:2), (i:2), (e:2), (o:2), (.:1), (a:1), (f:1), (m:1)
Top 5) [' ', 't', 's', 'l', 'h'] ( :6), (t:4), (s:3), (l:2), (h:2), (i:2), (e:2), (o:2), (.:1), (a:1), (f:1), (m:1)
Top 5) [' ', 't', 's', 'l', 'h'] ( :6), (t:4), (s:3), (l:2), (h:2), (i:2), (e:2), (o:2), (f:2), (.:1), (a:1), (m:1)
"""