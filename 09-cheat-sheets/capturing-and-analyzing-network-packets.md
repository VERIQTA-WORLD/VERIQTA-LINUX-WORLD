```bash
sudo tcpdump -D
sudo tcpdump -i INTERFACE -nn -c 100
sudo tcpdump -i INTERFACE -nn -c 100 'host 192.0.2.1'
sudo tcpdump -i INTERFACE -nn -c 100 'tcp port 443'
sudo tcpdump -i INTERFACE -nn -c 100 'udp port 53'
sudo tcpdump -i INTERFACE -nn -c 100 'icmp or icmp6'
sudo tcpdump -i INTERFACE -nn -c 100 'net 192.0.2.0/24'
sudo tcpdump -i INTERFACE -nn -s 0 -c 100 -w CAPTURE.pcap
tcpdump -nn -r CAPTURE.pcap
tcpdump -nn -r CAPTURE.pcap 'tcp port 443'
tshark -D
tshark -r CAPTURE.pcap
tshark -r CAPTURE.pcap -Y dns
tshark -r CAPTURE.pcap -Y 'tcp.analysis.retransmission'
tshark -r CAPTURE.pcap -T fields -e frame.time -e ip.src -e ip.dst
capinfos CAPTURE.pcap
```
