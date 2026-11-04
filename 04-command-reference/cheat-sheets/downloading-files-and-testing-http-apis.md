| Command | What you can do with it |
| --- | --- |
| `curl --version` | Display curl version and supported protocols. |
| `curl -I https://example.com` | Fetch HTTP response headers. |
| `curl -i https://example.com` | Include HTTP headers with the response body. |
| `curl -L https://example.com` | Follow redirects. |
| `curl --fail --show-error --location --output OUTPUT_FILE https://example.com/FILE` | Download to a chosen file while reporting HTTP and transport errors. |
| `curl --connect-timeout 5 --max-time 30 https://example.com` | Bound connection setup and total request time. |
| `curl --retry 3 --retry-delay 2 https://example.com` | Retry eligible failures up to three times with a delay. |
| `curl -H 'Accept: application/json' https://example.com/API` | Request a JSON response through an Accept header. |
| `curl -X POST -H 'Content-Type: application/json' --data @REQUEST.json https://example.com/API` | POST a JSON request body read from a file. |
| `curl --data-urlencode 'KEY=VALUE' https://example.com/API` | Submit a URL-encoded form value. |
| `curl --cacert CA_FILE https://HOST` | Validate a server using a selected CA certificate file. |
| `curl --resolve HOST:443:192.0.2.1 https://HOST` | Connect to a selected address while retaining the requested hostname for HTTPS. |
| `curl -sS -o /dev/null -w '%{http_code}\n' https://example.com` | Print the HTTP status code while discarding the response body. |
| `curl -sS -o /dev/null -w '%{time_namelookup} %{time_connect} %{time_starttransfer} %{time_total}\n' https://example.com` | Measure DNS, connection, first-byte and total request durations. |
| `wget --spider https://example.com` | Check a URL's accessibility without downloading its body. |
| `wget -O OUTPUT_FILE https://example.com/FILE` | Download a URL to a chosen output file. |
| `wget -c https://example.com/FILE` | Attempt to resume an incomplete download. |
| `wget --limit-rate=1m https://example.com/FILE` | Limit a download's transfer rate. |
| `wget --server-response --spider https://example.com` | Inspect HTTP response headers while checking a URL. |
