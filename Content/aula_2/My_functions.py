import numpy as np

def standing_wave(time):
    '''
    This function returns the displacement of the wave in relation to time.
    It describes a cosine harmonic wave.

    input :
    time = propagation time [s]

    return:
    u = displacement of the wave propagation [m]
    '''
    A = 8
    T = 6
    theta0 = 0.
    omega = (2*np.pi)/T

    u = A*np.cos(omega*time + theta0 )
    return u
