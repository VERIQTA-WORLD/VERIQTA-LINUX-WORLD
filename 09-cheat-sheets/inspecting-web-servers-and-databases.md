```bash
nginx -v
sudo nginx -t
sudo nginx -T
apachectl -v
sudo apachectl configtest
sudo apachectl -S
httpd -v
sudo httpd -t
curl -I http://127.0.0.1
pg_isready -h HOST -p 5432
psql --version
psql -h HOST -U ACCOUNT -d DATABASE -c 'SELECT version();'
psql -h HOST -U ACCOUNT -d DATABASE -c 'SELECT now();'
pg_dump -h HOST -U ACCOUNT -d DATABASE -f BACKUP.sql
mysql --version
mysql -h HOST -u ACCOUNT -p -e 'SELECT VERSION();'
mysqladmin -h HOST -u ACCOUNT -p ping
mysqldump -h HOST -u ACCOUNT -p DATABASE > BACKUP.sql
sqlite3 --version
sqlite3 -readonly DATABASE.sqlite 'PRAGMA integrity_check;'
redis-cli -h HOST PING
redis-cli -h HOST INFO server
```
