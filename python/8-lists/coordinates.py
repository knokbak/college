############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Using tuples for coordinates
# OK - 1 Nov 2023

dundee = (56.46202, -2.970700)
aberdeen = (57.149651, -2.0997755)

x, y = dundee
print(f'Dundee is at {x} latitude and {y} longitude')

x2, y2 = aberdeen
print(f'Aherdeen is {x2-x:6f} degrees east and {y2-y:6f} degrees north of Dundee')
