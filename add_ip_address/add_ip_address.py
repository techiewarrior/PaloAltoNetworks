from urllib import request
import ssl
from api_key import pa220key

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# ip_address_net = '192.168.1.'
# host_ips = range(1, 11)


def add_ip_address():
    xpath = "&type=config&action=set&xpath=/config/devices/entry"\
        "[@name='localhost.localdomain']/vsys/entry[@name='vsys1']"\
        "/address/entry[@name='test4']&"\
        "element=<ip-netmask>1.1.1.4/32</ip-netmask>"
    host = '192.168.1.128'
    api_key = str(pa220key)
    key = '?key=' + api_key
    add_ip_address = 'https://' + host + '/api/' + key + xpath
    fh = request.urlopen(add_ip_address, context=ctx)
    fh_read = fh.read().decode()
    # return fh_read
    print(fh_read)


add_ip_address()
