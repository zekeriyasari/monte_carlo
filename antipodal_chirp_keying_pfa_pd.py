# Matched filter performance in WGN
# H0: x[n] = w[n]
# H1: x[n] = s[n] + w[n],  n = 0, 1, ..., N-1
# w[N] is WGN with mean 0 and variance var.
# s[n] is deterministic.

from utils import *
import matplotlib.pyplot as plt

N = 10
M = 10000

pfa = np.logspace(-7, -1, 7)
enr = np.linspace(0, 20, 50)
d2 = 10 ** (enr / 10)

for i in range(pfa.size):
    # generate the deterministic signal.

    Ts = 1 / 1000  # sampling period.
    fs = 1 / Ts  # sampling frequency

    t = np.arange(N)*Ts  # continuous time signal.

    A = 1  # amplitude.
    s0 = linear_chirp(t, 100, 5, 1250, phi=np.pi)  # chirp signal.
    s1 = -s0
    deltas = s1 - s0

    epsilon = s.dot(s)  # signal energy.

    # numerically calculate probability of detection.
    P = np.zeros_like(enr)
    for k in range(d2.size):
        # variance corresponding to d2
        var = epsilon / d2[k]

        # determine the threshold corresponding to gamma
        gamma = np.sqrt(var * epsilon) * Qinv(pfa[i])

        # generate the data.
        data = np.sqrt(var) * np.random.randn(M, N) + s

        # apply the detector.
        T = data.dot(s)  # NP detector.
        P[k] = np.where(T > gamma)[0].size / M

    # analytically calculate probability of detection.
    Pd = Q(Qinv(pfa[i]) - np.sqrt(d2))

    # plot the results.
    plt.plot(enr, P, '*')
    plt.plot(enr, Pd)

plt.xlabel(r'$10\log_{10}\frac{\varepsilon}{\sigma^2}$')
plt.ylabel(r'$P_D$')
plt.title(r'$Damped \; Exponential \; in \; WGN$')
plt.grid()
plt.show()