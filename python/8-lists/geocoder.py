############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Using reverse_geocoder to get location from coordinates
# OK - 1 Nov 2023

import reverse_geocoder

coord_lat = float(input('Enter latitude: '))
coord_lon = float(input('Enter longitude: '))
coords = (coord_lat, coord_lon)

print(type(coords))
print(reverse_geocoder.search(coords))
