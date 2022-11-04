'''
Filename: c:\Users\istel\GitCode\EX_PythonCode\Fourier.py
Path: c:\Users\istel\GitCode\EX_PythonCode
Created Date: Monday, October 31st 2022, 2:27:57 pm
Author: Istel90

Copyright (c) 2022 Your Company
'''
#%% Necessary packages
import os
import numpy as np

from scipy.io.wavfile import write
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft
from matplotlib import pyplot as plt

#%%
SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds

# def Wave 정리 
def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

# Generate a 2 hertz sine wave that lasts for 5 seconds
x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)
plt.plot(x, y)
plt.show()

# 노이즈 만들기
_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3

mixed_tone = nice_tone + noise_tone
normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

plt.plot(normalized_tone[:1000])
plt.show()


#%% apply FFT Fast Fourier Transform

# Remember SAMPLE_RATE = 44100 Hz is our playback rate
write("mysinewave.wav", SAMPLE_RATE, normalized_tone)

# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION

yf = fft(normalized_tone)
xf = fftfreq(N, 1 / SAMPLE_RATE)
plt.plot(xf, np.abs(yf))
plt.show()

yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)
plt.plot(xf, np.abs(yf))
plt.show()

# The maximum frequency is half the sample rate
points_per_freq = len(xf) / (SAMPLE_RATE / 2)
# Our target frequency is 4000 Hz
target_idx = int(points_per_freq * 4000)
yf[target_idx - 1 : target_idx + 2] = 0

plt.plot(xf, np.abs(yf))
plt.show()



#%%
# sampling rate
sr = 2000
# sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)

freq = 1.
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7   
x += 0.5* np.sin(2*np.pi*freq*t)

plt.figure(figsize = (8, 6))
plt.plot(t, x, 'r')
plt.ylabel('x: Amplitude')

plt.show()


# 정리
X = fft(x)
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T 

# 확인
test = np.abs(X)
uniqueFreq = np.unique(test )

plt.figure(figsize = (12, 6))
plt.subplot(121)
plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, 10)

plt.subplot(122)
plt.plot(t, ifft(X), 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()


plt.figure(figsize = (8, 6))
plt.plot(t, x, 'r')
plt.ylabel('Amplitude')
plt.title('Original signal')
plt.show()


# FFT the signal
sig_fft = fft(x)
# copy the FFT results
sig_fft_filtered = sig_fft.copy()
sig_fft_filtered2 = sig_fft.copy()
sig_fft_filtered3 = sig_fft.copy()

# obtain the frequencies using scipy function
freq = fftfreq(len(x), d=1./2000)
# define the cut-off frequency
cut_off = 6

# high-pass filter by assign zeros to the 
# FFT amplitudes where the absolute 
# frequencies smaller than the cut-off 
sig_fft_filtered[ np.abs(freq) < cut_off] = 0

# get the filtered signal in time domain
filtered = ifft(sig_fft_filtered)


sig_fft_filtered2[ np.abs(freq) > 6 ] = 0
sig_fft_filtered2[ np.abs(freq) < 3] = 0
filtered2 = ifft(sig_fft_filtered2)

sig_fft_filtered3[ np.abs(freq) > 2 ] = 0
filtered3 = ifft(sig_fft_filtered3)


# plot the filtered signal
plt.figure(figsize = (12, 6))
plt.plot(t, filtered)
plt.plot(t, filtered2)
plt.plot(t, filtered3)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()



#%% 랜덤하게 주파스 그려줌

t = np.arange(100)
n2 = np.zeros((100,), dtype=complex)
n2[50:55] = np.exp(2j*np.random.uniform(0, 4*np.pi, (5,)))
s2 = np.fft.ifft(n2)
plt.plot(t, s2, label='real')

X2 = fft(s2)
N2 = len(X2)
n = np.arange(N2)
T2 = N2/100
freq2 = n/T2 

Test = np.abs(X2)
# plot
# plt.figure(figsize = (12, 6))
plt.subplot(121)
plt.stem(freq2, X2, 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(40, 100)

plt.subplot(122)
plt.plot(t, ifft(X2), 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()


# copy the FFT results
sig_fft_filtered_test = X2.copy()

# obtain the frequencies using scipy function
freq = fftfreq(len(s2), d=1./100)

# define the cut-off frequency
cut_off = 50

# high-pass filter by assign zeros to the 
# FFT amplitudes where the absolute 
# frequencies smaller than the cut-off 
sig_fft_filtered_test[ np.abs(freq) < cut_off] = 0

# get the filtered signal in time domain
filtered_test = ifft(sig_fft_filtered_test)

# plot the filtered signal
plt.figure(figsize = (12, 6))
plt.plot(t, filtered_test)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()



# # copy the FFT results
# sig_fft_filtered_test2 = X2.copy()
# sig_fft_filtered_test2[ np.abs(freq) < 49] = 0
# sig_fft_filtered_test2[ np.abs(freq) > 50] = 0

# # get the filtered signal in time domain
# filtered_test2 = ifft(sig_fft_filtered_test2)

# # plot the filtered signal
# plt.figure(figsize = (12, 6))
# plt.plot(t, filtered_test2)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.show()




#%%
