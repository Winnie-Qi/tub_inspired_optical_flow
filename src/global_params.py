import numpy as np
from matplotlib import pyplot as plt
import math

plt.close('all')

class params:
    global scale_factor # scale factor to compress in time (detect faster motions)
    
    scale_factor = 0.1 
    
    #routes

    kernel_route = 'kernel'

    event_route = '../slider_far/events.txt'

    # n_events = 1e4

    mono_wm1 = 1.95
    
    mono_wm2 = 0.23

    bi_wm1 = 0.83
    
    bi_wm2 = -0.34

    x0 = 0

    y0 = 0
    
    sigma = 3

    xi0= math.pi * 2

    f0x = 0.057 # units: cycles/pix ?
    
    f0y = f0x

    half_kernel_size = 11 # kernelsize -11 to 11 # pls change kernel size here

    # Get a subset of events
    i_offset = 2000000
    
    num_events = 80000

    #####

    f0x_new = -0.1012  # related to -90 pix/sec of ground truth optical flow

    # Voting spread of each event
    sigma_xy = 1.  # [pixels]

    sigma_t =  1.0 # [time bins]

    # DAVIS camera pixel resolution
    sensor_width = 240

    sensor_height = 180

    # Select sub-region of the image
    band_height = 40

    band_width = 80

    offset_height = 20

    offset_width = 70

    def get_scale_factor():
        return scale_factor

    def mono_mium1():
        return 0.55*scale_factor
    
    def mono_mium2():
        return 0.55*scale_factor

    def mono_sigmam1():
        return 0.10*scale_factor

    def mono_sigmam2():
        return 0.16*scale_factor

    def bi_mium1():
        return 0.44*scale_factor

    def bi_mium2():
        return 0.63*scale_factor

    def bi_sigmam1():
        return 0.12*scale_factor

    def bi_sigmam2():
        return 0.21*scale_factor
    
    def gaussian(t, mu, sigma):
        return np.exp( -0.5 * ((t-mu)/sigma)**2 )