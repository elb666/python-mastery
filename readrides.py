# readrides.py

import csv
from collections import namedtuple


def read_rides_as_one_string(filename):
    '''
    Read the bus ride data as one string
    '''
    with open(filename) as f:
        data = f.read()
    return data


def read_rides_as_strings(filename):
    '''
    Read the file as a list of strings
    '''
    with open(filename) as f:
        lines = f.readlines()
    return lines


def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dicts(filename):
    '''
    Read the file as a list of dicts
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip headings
        for row in rows:
            _, _, year = row[1].split('/')
            record = {
                "route": row[0],
                "date": row[1],
                "daytype": row[2],
                "rides": int(row[3]),
                "year": int(year)
            }
            records.append(record)

        return records


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_instances_of_a_class(filename):
    '''
    Read the file as a list of instances of a class
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


class RowWithSlots:
    __slots__ = ("route", "date", "daytype", "rides")

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_instances_of_a_class_with_slots(filename):
    '''
    Read the file as a list of instances of a class
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)
        for row in rows:
            record = RowWithSlots(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


RowNamedTuple = namedtuple('Row', ('route', 'date', 'daytype', 'rides'))


def read_rides_as_instances_of_a_named_tuple(filename):
    '''
    Read the file as a list of instances of a class
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)
        for row in rows:
            record = RowNamedTuple(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    print('Reading as one string')
    rows = read_rides_as_one_string('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    print('Reading as a list of strings')
    rows = read_rides_as_strings('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    print('Reading as a list of tuples')
    rows = read_rides_as_tuples('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    print('Reading as a list of dicts')
    rows = read_rides_as_dicts('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    print('Reading as a list of instances of a class with slots')
    rows = read_rides_as_instances_of_a_class_with_slots('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    print('Reading as a list of instances of a class')
    rows = read_rides_as_instances_of_a_class('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    print('Reading as a list of instances of a named tuple')
    rows = read_rides_as_instances_of_a_named_tuple('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.stop()
