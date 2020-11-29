import numpy as np

import matplotlib.pyplot as plt

from neuron import h

import genrn

h.celsius = 21

soma = h.Section()

def getval( section, mech, var ):
    return section.__getattribute__(mech).__getattribute__(var)

chans = {'nav1.7': ['a1p7', 'b1p7', 'c1p7'], 'nav1.8': ['a1p8', 'b1p8', 'c1p8']}
traces = ['minf', 'mtau', 'hinf', 'htau']
data = {}

for nav in chans:
    for chan in chans[nav]:
        data[chan] = {}
        for trace in traces:
            data[chan][trace] = []
        soma.insert(chan)


vs = np.linspace(-70,30,100)
for v in vs:
    h.finitialize(v)
    data['a1p7']['minf'].append(getval( soma(0.5), 'a1p7', 'minf')
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
#
#for trace in traces:
#    for nav in chans:
#        plt.title(nav + " " + trace)
#        for chan in chans[nav]:
#            plt.plot(vs, data[chan][trace], label=chan)
#        plt.legend()
#        plt.show()