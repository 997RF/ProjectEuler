import numpy as np
import pandas as pf


def fibonacci(first, second):
    next = first + second
    return next


a = np.empty(900)
a[0] = 1
a[1] = 2
for x in range(850):
    a[x+2] = fibonacci(a[x], a[x+1])

df = pf.DataFrame(a, columns=['main'])
df = df.loc[df['main'] < 4000000]
df = df.loc[df['main'] % 2 == 0]
df = df.reset_index()
print(np.sum(df['main']))
