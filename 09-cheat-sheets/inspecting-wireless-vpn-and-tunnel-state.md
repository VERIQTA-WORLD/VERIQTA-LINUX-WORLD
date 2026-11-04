| Command | What you can do with it |
| --- | --- |
| `iw dev` | List wireless interfaces. |
| `iw dev INTERFACE link` | Inspect a wireless interface's current association. |
| `iw dev INTERFACE station dump` | Read associated station statistics. |
| `iw reg get` | Inspect wireless regulatory settings. |
| `rfkill list` | Read radio block states. |
| `nmcli radio` | Inspect NetworkManager radio state. |
| `nmcli device wifi list` | List available Wi-Fi networks. |
| `nmcli connection show --active` | List active NetworkManager connections. |
| `ip -d link show` | Inspect detailed link and tunnel properties. |
| `ip tunnel show` | List IP tunnels. |
| `sudo wg show` | Inspect WireGuard interfaces and peers without showing private keys. |
| `sudo wg show interfaces` | List WireGuard interface names. |
| `sudo ip xfrm state` | Inspect IPsec state, which can expose keying material. |
| `sudo ip xfrm policy` | Inspect IPsec traffic-selection policies. |
| `openvpn --version` | Print OpenVPN version and build information. |
| `openvpn --show-ciphers` | List OpenVPN-supported ciphers. |
| `tailscale status` | Inspect Tailscale peer and connection state. |
| `tailscale netcheck` | Inspect Tailscale network connectivity diagnostics. |
