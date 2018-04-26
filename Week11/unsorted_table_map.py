from map_base import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []                              # list of _Item's

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:                          # Found a match:
                item._value = v                           # reassign value
                return                                    # and quit
        # did not find match for key
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:                # Found a match:
                self._table.pop(j)                        # remove item
                return                                    # and quit
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key                             # yield the KEY

    def pop(self, key, d=None):
        ''' Remove specified key and return the corresponding value.
            If key is not found, d is given, then return D.
            If key is not found, d is not given, raise KeyError.

            @key: the key to delete from Map
            @d: returned value if key is not found

            return: value associated with key if found.
                    d if d is given, and key not found.
        '''
        try:
            toReturn = self[key]
            del self[key]
            return toReturn
        except KeyError:
            if d is not None:
                return d
            else:
                raise KeyError()

    def items(self):
        ''' yield an iterator of (key, value) pairs stored within Map ADT.

            yield: each item stored within self._table

            self._table stores Item, Item contains _key, _value.
        '''
        for each in self._table:
            yield(each._key, each._value)


def main():
    table = UnsortedTableMap()
    values = ["Ezreal", "Blizcrank", "Annie", "Teemo", "Zed"]
    for i in range(len(values)):
        table[i] = values[i]  # Calls __setitem__ from UnsortedTableMap

    print("Popping key 3... An existing key")
    print("Your returned value is: ", table.pop(3))
    print("Popping key \"What\"... A not existing key, with parameter d \
          = \"hey\"")
    print("Your returned value is: ", table.pop("What", "hey"))

    try:
        print("Popping key 90... A not existing key")
        table.pop(90)
    except KeyError:
        print("You got KeyError exception.")

    print("------------------------------------------------------")
    print("Testing items()..........")
    for each in table.items():
        print(each)


main()
