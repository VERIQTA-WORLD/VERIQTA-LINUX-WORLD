```bash
curl --version
curl -I https://example.com
curl -i https://example.com
curl -L https://example.com
curl --fail --show-error --location --output OUTPUT_FILE https://example.com/FILE
curl --connect-timeout 5 --max-time 30 https://example.com
curl --retry 3 --retry-delay 2 https://example.com
curl -H 'Accept: application/json' https://example.com/API
curl -X POST -H 'Content-Type: application/json' --data @REQUEST.json https://example.com/API
curl --data-urlencode 'KEY=VALUE' https://example.com/API
curl --cacert CA_FILE https://HOST
curl --resolve HOST:443:192.0.2.1 https://HOST
curl -sS -o /dev/null -w '%{http_code}\n' https://example.com
curl -sS -o /dev/null -w '%{time_namelookup} %{time_connect} %{time_starttransfer} %{time_total}\n' https://example.com
wget --spider https://example.com
wget -O OUTPUT_FILE https://example.com/FILE
wget -c https://example.com/FILE
wget --limit-rate=1m https://example.com/FILE
wget --server-response --spider https://example.com
```
