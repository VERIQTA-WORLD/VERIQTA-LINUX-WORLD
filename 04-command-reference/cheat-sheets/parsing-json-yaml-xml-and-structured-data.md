| Command | What you can do with it |
| --- | --- |
| `jq . FILE.json` | Pretty-print and validate JSON with jq. |
| `jq '.KEY' FILE.json` | Read a JSON property. |
| `jq -r '.KEY' FILE.json` | Print a JSON property without string quotes. |
| `jq '.items[]' FILE.json` | Emit each item in a JSON array. |
| `jq '.items[] \| select(.enabled == true)' FILE.json` | Select JSON items whose enabled property is true. |
| `jq 'keys' FILE.json` | List JSON object keys or array indexes. |
| `jq 'length' FILE.json` | Count JSON elements or string characters, depending on value type. |
| `jq -c '.items[]' FILE.json` | Emit array items as compact JSON records. |
| `jq -s . FILE_ONE.json FILE_TWO.json` | Read two JSON inputs into one array. |
| `jq --arg value "$VALUE" '.KEY = $value' FILE.json` | Set a JSON property using a shell value passed safely as data. |
| `jq -e '.KEY != null' FILE.json` | Use jq's exit status to test for a non-null property. |
| `python3 -m json.tool FILE.json` | Pretty-print and validate JSON with Python. |
| `yq --version` | Identify the installed yq implementation and version. |
| `yq --help` | Read this yq implementation's supported syntax. |
| `xmllint --noout FILE.xml` | Check whether XML is well formed without printing it. |
| `xmllint --format FILE.xml` | Format XML for readability. |
| `xmllint --xpath 'count(//ITEM)' FILE.xml` | Evaluate an XPath count expression. |
| `xmlstarlet sel -t -v '/ROOT/KEY' FILE.xml` | Extract an XML element's value with XMLStarlet. |
| `csvlook FILE.csv` | Render CSV as a readable table. |
| `csvcut -n FILE.csv` | List CSV column names. |
| `csvstat FILE.csv` | Summarize CSV column statistics. |
