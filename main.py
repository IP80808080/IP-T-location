import pygeoip
gi = pygeoip.GeoIP('GeoIP.dat', flags=pygeoip.const.MEMORY_CACHE)


location = gi.record_by_addr('1.1.1.1')
print(location)