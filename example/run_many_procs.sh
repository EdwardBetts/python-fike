#!/usr/bin/bash
for k in {1,2,4,8,16,32,64,128,256}; do
    python fike_example_args.py 1000 $k;
done
