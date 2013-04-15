import os
import time
import sys

import fike

def process(a,b):
    return sum([delay_line(x) for x in range(a,b)])


def delay_line(x):
    time.sleep(1e-3)
    return x


if __name__ == '__main__':

    load = int(sys.argv[1])
    Nprocs = int(sys.argv[2])

    ##################################################################
    ## Call the process function in multiple child processes.
    time_a = time.time()

    ii = [k * load / Nprocs for k in range(0,Nprocs+1)]

    chunks = [fike.Fike(process,a,b)
              for a,b in zip(ii[:-1], ii[1:])
              ]
    ## "Reduce" results from child processes.
    result_a = sum([pp.get_result() for pp in chunks])

    time_a = time.time()-time_a


    ##################################################################
    ## Call the process function only once, in a single process.
    time_b = time.time()    

    result_b = process(0,load)

    time_b = time.time()-time_b


    ##################################################################
    ## Check if results were really the same, and calculate speedup.
    assert result_a == result_b

    print load, Nprocs, time_a, time_b
