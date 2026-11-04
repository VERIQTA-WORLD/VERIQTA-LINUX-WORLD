| Command | What you can do with it |
| --- | --- |
| `sudo tcpdump -D` | List packet-capture interfaces. |
| `sudo tcpdump -i INTERFACE -nn -c 100` | Capture 100 packets without resolving names. |
| `sudo tcpdump -i INTERFACE -nn -c 100 'host 192.0.2.1'` | Capture up to 100 packets involving a selected address. |
| `sudo tcpdump -i INTERFACE -nn -c 100 'tcp port 443'` | Capture up to 100 packets involving TCP port 443. |
| `sudo tcpdump -i INTERFACE -nn -c 100 'udp port 53'` | Capture up to 100 packets involving UDP port 53. |
| `sudo tcpdump -i INTERFACE -nn -c 100 'icmp or icmp6'` | Capture up to 100 ICMP or ICMPv6 packets. |
| `sudo tcpdump -i INTERFACE -nn -c 100 'net 192.0.2.0/24'` | Capture up to 100 packets involving a selected network. |
| `sudo tcpdump -i INTERFACE -nn -s 0 -c 100 -w CAPTURE.pcap` | Write up to 100 full-length packets to a capture file, which may contain sensitive data. |
| `tcpdump -nn -r CAPTURE.pcap` | Read a capture file without name resolution. |
| `tcpdump -nn -r CAPTURE.pcap 'tcp port 443'` | Read only packets matching a TCP-port filter. |
| `tshark -D` | List interfaces available to TShark. |
| `tshark -r CAPTURE.pcap` | Decode a saved packet capture. |
| `tshark -r CAPTURE.pcap -Y dns` | Show packets matching the DNS display filter. |
| `tshark -r CAPTURE.pcap -Y 'tcp.analysis.retransmission'` | Show packets classified as TCP retransmissions. |
| `tshark -r CAPTURE.pcap -T fields -e frame.time -e ip.src -e ip.dst` | Extract timestamps and IPv4 source/destination fields. |
| `capinfos CAPTURE.pcap` | Inspect capture-file metadata and statistics. |
