
from colour.plotting import *
import colour
from pprint import pprint
import numpy as np
import scipy.io as sio
# import matplotlib
import pylab
import colour.plotting
from pprint import pprint
import colour.colorimetry as colorimetry
import colour.colorimetry.dataset as dataset

# Main section start from here.

sample = sio.loadmat('vishal.mat')
spd_all_sample = np.transpose(sample.get('vishal'))
siz = spd_all_sample.shape

# Defining a sample spectral power distribution data.

keys = spd_all_sample[0]
x1 = []
y1 = []
all_col = []
for i in range(siz[0]-1):
    values = spd_all_sample[i+1]
    sample_spd_data = dict(zip(keys, values))

    spd = colour.SpectralPowerDistribution('Sample', sample_spd_data)


    # print(spd)
    # single_spd_plot(spd)

    # # May be needed.
    # # Displaying the sample spectral power distribution shape.
    # print(spd.shape)
    # repr(spd.shape)

    spd = colour.SpectralPowerDistribution('Sample', sample_spd_data)
    cmfs = colour.STANDARD_OBSERVERS_CMFS['CIE 1931 2 Degree Standard Observer']
    illuminant = colour.ILLUMINANTS_RELATIVE_SPDS['D65']

    # Calculating the sample spectral power distribution *CIE XYZ* tristimulus values.
    XYZ = colour.spectral_to_XYZ(spd, cmfs, illuminant)
    # print(XYZ)

    # The output domain of *colour.spectral_to_XYZ* is [0, 100] and the input 
    # domain of *colour.XYZ_to_sRGB* is [0, 1]. We need to take it in account and 
    # rescale the input *CIE XYZ* colourspace matrix.
    RGB = colour.XYZ_to_sRGB(XYZ / 100)
    all_col.append(RGB)
    # print(RGB)

    # Plotting the *sRGB* colourspace colour of the *Sample* spectral power distribution.
    # single_colour_plot(ColourParameter('Sample', RGB), text_size=32)

    xy =  colour.XYZ_to_xy(XYZ)
    # print(xy)
    
    # Plotting the *CIE 1931 Chromaticity Diagram*.
    # The argument *standalone=False* is passed so that the plot doesn't get displayed
    # and can be used as a basis for other plots.
    CIE_1931_chromaticity_diagram_plot(standalone=False)

    # Plotting the *xy* chromaticity coordinates.
    x, y = xy
    x1.append(x)
    y1.append(y)

pylab.plot(x1, y1, 'o-', color='white')

display(standalone=True)


