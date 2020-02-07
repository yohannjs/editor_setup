import numpy as np
from scipy import signal
from matplotlib import pyplot as plt


def raspi_import(path, channels=5):
    with open(path, 'r') as fid:
        sample_period = np.fromfile(fid, count=1, dtype=float)[0]
        data = np.fromfile(fid, dtype=np.uint16)
        data = data.reshape((-1, channels))
    return sample_period, data


def get_ADC_data(data):
    adc_1 = remove_mean(data[:, 0])
    adc_2 = remove_mean(data[:, 1])
    adc_3 = remove_mean(data[:, 2])
    return adc_1, adc_2, adc_3


def remove_mean(dataSet):
    dataSet = dataSet - np.mean(dataSet)
    return dataSet


def correlate(data):

    adc_1, adc_2, adc_3 = get_ADC_data(data)
    fig, ax = plt.subplots(1,3)
    ax[0].plot(adc_1)
    ax[1].plot(adc_2)
    ax[2].plot(adc_3)
    plt.show()

    corr21 = np.abs(np.correlate(adc_1, adc_2, "full")) # 2-1
    corr31 = np.abs(np.correlate(adc_1, adc_3, "full")) # 3-1
    corr32 = np.abs(np.correlate(adc_2, adc_3, "full")) # 3-2

    l_21 = np.argmax(corr21)
    l_31 = np.argmax(corr31)
    l_32 = np.argmax(corr32)

    fig, ax = plt.subplots(1,3)
    lag = np.array([a for a in range(-int(len(corr21)/2),int(len(corr21)/2)+1)])
    ax[0].plot(lag,corr21)
    ax[1].plot(lag,corr31)
    ax[2].plot(lag,corr32)
    plt.show()

    # variation relative to zero
    l_21 = l_21 - (len(data[:, 1]) - 1)
    l_31 = l_31 - (len(data[:, 1]) - 1)
    l_32 = l_32 - (len(data[:, 1]) - 1)

    print(l_21, l_31, l_32)

    return l_21, l_31, l_32

def get_angle(data):
    s_delay21, s_delay31, s_delay32 = correlate(data)
    theta = np.arctan2(np.sqrt(3)*(s_delay21+s_delay31) , s_delay21-s_delay31-2*s_delay32)
    return theta


period, data = raspi_import("adcData315.bin")
period *= 1e+6
data = signal.detrend(data[100:], axis=1)

angle = (get_angle(data)*180/(np.pi))

print(angle)
