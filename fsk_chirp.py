
# Time-frequency analysis of chirp signals.

from utils import *
from scipy import fftpack, signal
import matplotlib.pyplot as plt

N = 1024  # number of points.
Ts = 1 / 1000  # sampling period.
fs = 1 / Ts  # sampling frequency

t = np.arange(N) * Ts  # continuous time.
sn0 = linear_chirp(t[:int(N/2)], 250, 0.5, 100)  # chirp signal with positive chirp rate.
sp0 = linear_chirp(t[int(N/2):], 100, 1, 250)  # chirp signal with negative chirp rate.
s0 = np.hstack((sn0, sp0))  # bi-orthogonal chirp signals. Signifies symbol `0`

sp1 = linear_chirp(t[:int(N/2)], 100, 0.5, 250)  # chirp signal with positive chirp rate.
sn1 = linear_chirp(t[int(N/2):], 250, 1, 100)  # chirp signal with negative chirp rate.
s1 = np.hstack((sp1, sn1))  # bi-orthogonal chirp signals. Signifies symbol `1`

xf0 = fftpack.fft(s0)  # fft of the signal
f = fftpack.fftfreq(N, Ts)  # get the sampled frequencies.

fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(t, s0)  # plot signal in time.
ax[0, 0].set_xlabel('$t \; [sec]$')
ax[0, 0].set_ylabel('$x(t)$')

ax[1, 0].plot(fftpack.fftshift(f), 1 / N * np.abs(fftpack.fftshift(xf0)))  # amplitude spectrum.
ax[1, 0].set_xlabel('$f \; [Hz]$')
ax[1, 0].set_ylabel('$|X(f)|$')
ax[1, 0].grid()

f, Pxx = signal.periodogram(s0, fs)
ax[0, 1].semilogy(f, Pxx)
ax[0, 1].set_xlabel('$f \; [Hz]$')
ax[0, 1].set_ylabel('$PSD$')

ax[1, 1].specgram(s0, NFFT=128, Fs=fs, noverlap=64)  # spectrogram of the signal.
ax[1, 1].set_xlabel('$t \; [sec]$')
ax[1, 1].set_ylabel('$f \; [Hz]$')
plt.tight_layout()

xf1 = fftpack.fft(s1)  # fft of the signal
f = fftpack.fftfreq(N, Ts)  # get the sampled frequencies.

fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(t, s1)  # plot signal in time.
ax[0, 0].set_xlabel('$t \; [sec]$')
ax[0, 0].set_ylabel('$x(t)$')

ax[1, 0].plot(fftpack.fftshift(f), 1 / N * np.abs(fftpack.fftshift(xf0)))  # amplitude spectrum.
ax[1, 0].set_xlabel('$f \; [Hz]$')
ax[1, 0].set_ylabel('$|X(f)|$')
ax[1, 0].grid()

f, Pxx = signal.periodogram(s1, fs)
ax[0, 1].semilogy(f, Pxx)
ax[0, 1].set_xlabel('$f \; [Hz]$')
ax[0, 1].set_ylabel('$PSD$')

ax[1, 1].specgram(s1, NFFT=128, Fs=fs, noverlap=64)  # spectrogram of the signal.
ax[1, 1].set_xlabel('$t \; [sec]$')
ax[1, 1].set_ylabel('$f \; [Hz]$')
plt.tight_layout()

plt.show()

