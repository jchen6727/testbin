import numpy as np

import matplotlib.pyplot as plt

from neuron import h

soma = h.Section()

chans = ['a1p7', 'a1p8', 'b1p7', 'b1p8', 'c1p7', 'c1p8']
plots = ['minf', 'mtau', 'hinf', 'htau']
data = {}

for chan in chans:
    data[chan] = {}
    for plot in plots:
        data[chan][plot] = []
    soma.insert(chan)


vs = np.linspace(-70,30,100)
for v in vs:
    h.finitialize(v)
    data['a1p7']['minf'].append(soma(0.5).a1p7.minf)
    data['a1p7']['mtau'].append(soma(0.5).a1p7.mtau)
    data['a1p7']['hinf'].append(soma(0.5).a1p7.hinf)
    data['a1p7']['htau'].append(soma(0.5).a1p7.htau)

    data['a1p8']['minf'].append(soma(0.5).a1p8.minf)
    data['a1p8']['mtau'].append(soma(0.5).a1p8.mtau)
    data['a1p8']['hinf'].append(soma(0.5).a1p8.hinf)
    data['a1p8']['htau'].append(soma(0.5).a1p8.htau)

    data['b1p7']['minf'].append(soma(0.5).b1p7.minf)
    data['b1p7']['mtau'].append(soma(0.5).b1p7.mtau)
    data['b1p7']['hinf'].append(soma(0.5).b1p7.hinf)
    data['b1p7']['htau'].append(soma(0.5).b1p7.htau)

    data['b1p8']['minf'].append(soma(0.5).b1p8.minf)
    data['b1p8']['mtau'].append(soma(0.5).b1p8.mtau)
    data['b1p8']['hinf'].append(soma(0.5).b1p8.hinf)
    data['b1p8']['htau'].append(soma(0.5).b1p8.htau)

    data['c1p7']['minf'].append(soma(0.5).c1p7.minf)
    data['c1p7']['mtau'].append(soma(0.5).c1p7.tau_m)
    data['c1p7']['hinf'].append(soma(0.5).c1p7.hinf)
    data['c1p7']['htau'].append(soma(0.5).c1p7.tau_h)

    data['c1p8']['minf'].append(soma(0.5).c1p8.minf)
    data['c1p8']['mtau'].append(soma(0.5).c1p8.tau_m)
    data['c1p8']['hinf'].append(soma(0.5).c1p8.hinf)
    data['c1p8']['htau'].append(soma(0.5).c1p8.tau_h)

for plot in plots:
    plt.title(plot)
    for chan in chans:
        plt.plot(vs, data[chan][plot], label=chan)
    plt.legend()
    plt.show()