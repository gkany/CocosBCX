sysbench --num-threads=2 --test=fileio --file-total-size=2G --file-test-mode=rndrw prepare
sysbench --num-threads=2 --test=fileio --file-total-size=2G --file-test-mode=rndrw run
sysbench --num-threads=2 --test=fileio --file-total-size=2G --file-test-mode=rndrw cleanup

