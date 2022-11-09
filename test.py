import pyshark

capture = pyshark.LiveCapture(interface='en0')
capture.sniff(timeout=50)
for packet in capture.sniff_continuously(packet_count=5):
    print('Just arrived:', packet)


# capture.sniff(packet_count=10)

# def print_dns_info(pkt):
#     if pkt.dns.qry_name:
#         print('DNS Request from %s: %s' % (pkt.ip.src, pkt.dns.qry_name))
#     elif pkt.dns.resp_name:
#         print('DNS Response from %s: %s' % (pkt.ip.src, pkt.dns.resp_name))

# capture.apply_on_packets(print_dns_info, timeout=100)