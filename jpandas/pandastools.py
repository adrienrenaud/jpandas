import pandas as pd


def _foo(self):
    print('foo')

pd.DataFrame.foo = _foo
