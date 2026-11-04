```bash
jq . FILE.json
jq '.KEY' FILE.json
jq -r '.KEY' FILE.json
jq '.items[]' FILE.json
jq '.items[] | select(.enabled == true)' FILE.json
jq 'keys' FILE.json
jq 'length' FILE.json
jq -c '.items[]' FILE.json
jq -s . FILE_ONE.json FILE_TWO.json
jq --arg value "$VALUE" '.KEY = $value' FILE.json
jq -e '.KEY != null' FILE.json
python3 -m json.tool FILE.json
yq --version
yq --help
xmllint --noout FILE.xml
xmllint --format FILE.xml
xmllint --xpath 'count(//ITEM)' FILE.xml
xmlstarlet sel -t -v '/ROOT/KEY' FILE.xml
csvlook FILE.csv
csvcut -n FILE.csv
csvstat FILE.csv
```
