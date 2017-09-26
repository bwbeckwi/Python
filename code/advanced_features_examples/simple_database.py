from sqlite3 import connect


class ContextManager:

    def __init__(self, gen):

        self.gen = gen

    def __call__(self, *args, **kwargs):

        self.args, self.kwargs = args, kwargs

        return self

    def __enter__(self):

        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)

    def __exit__(self, *args):

        next(self.gen_inst, None)


def point_table(cur):

    cur.execute('create table points(x int, y int)')
    yield
    cur.execute('drop table points')


point_table = ContextManager(point_table)


with connect('points.db') as conn:

    cur = conn.cursor()

    with point_table(cur):

        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(2, 1)')
        cur.execute('insert into points (x, y) values(2, 2)')

        for row in cur.execute('select x, y from points'):

            print(row)

        for row in cur.execute('select sum(x + y) from points'):

            print(row)
