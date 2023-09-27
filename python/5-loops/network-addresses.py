############################################################
# Licensed under the BSD 3-Clause License                  #
# See https://github.com/knokbak/college/blob/main/LICENSE #
############################################################

# Print list of IP addresses in a /24 network
# OK - 27 Sep 2023

network_prefix = '172.16'
subnet_id = 37

for host_id in range(0, 256):
    print(f'{network_prefix}.{subnet_id}.{host_id}')

print('Network complete!')
