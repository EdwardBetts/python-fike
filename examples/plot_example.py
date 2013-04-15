from pylab import *


if __name__ == '__main__':
    #aa = loadtxt('test_result.txt')
    aa = loadtxt('res10000.txt')

    cpu = aa[:,1]
    tp = aa[:,2]
    t0 = mean(aa[:,3])

    ion()

    figure(figsize=(6,8))
    suptitle('Multiprocessing performance')

    subplot(2,1,1)
    semilogy(cpu, 'k--')
    semilogy(t0/tp, 'b-o', lw=2)

    ylabel('Speedup')
    xlabel('Processes')
    ylim(1,100)
    grid()

    subplot(2,1,2, sharex=gca())
    plot(t0/tp/cpu, 'r-o', lw=2)

    ylabel('Efficiency')
    xlabel('Processes')
    xticks(mgrid[0:9], [1,2,4,8,16,32,64,128,256])
    ylim(0.0,1.1)
    grid()
