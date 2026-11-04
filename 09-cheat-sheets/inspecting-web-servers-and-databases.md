| Command | What you can do with it |
| --- | --- |
| `nginx -v` | Print the Nginx version. |
| `sudo nginx -t` | Check Nginx configuration syntax and referenced files. |
| `sudo nginx -T` | Check and print the Nginx configuration, which may expose secrets. |
| `apachectl -v` | Print Apache version information through apachectl. |
| `sudo apachectl configtest` | Check Apache configuration syntax. |
| `sudo apachectl -S` | Inspect Apache virtual-host configuration. |
| `httpd -v` | Print the httpd version. |
| `sudo httpd -t` | Check httpd configuration syntax. |
| `curl -I http://127.0.0.1` | Fetch HTTP headers from the local web server. |
| `pg_isready -h HOST -p 5432` | Check whether PostgreSQL is accepting connections. |
| `psql --version` | Print the psql client version. |
| `psql -h HOST -U ACCOUNT -d DATABASE -c 'SELECT version();'` | Query PostgreSQL server version using an authorized account. |
| `psql -h HOST -U ACCOUNT -d DATABASE -c 'SELECT now();'` | Query the database server's current timestamp. |
| `pg_dump -h HOST -U ACCOUNT -d DATABASE -f BACKUP.sql` | Write a PostgreSQL logical backup to a file. |
| `mysql --version` | Print the MySQL client version. |
| `mysql -h HOST -u ACCOUNT -p -e 'SELECT VERSION();'` | Query MySQL server version with interactive password prompting. |
| `mysqladmin -h HOST -u ACCOUNT -p ping` | Check MySQL server responsiveness with password prompting. |
| `mysqldump -h HOST -u ACCOUNT -p DATABASE > BACKUP.sql` | Write a MySQL logical backup, using workload-appropriate consistency options separately. |
| `sqlite3 --version` | Print the SQLite version. |
| `sqlite3 -readonly DATABASE.sqlite 'PRAGMA integrity_check;'` | Check SQLite database integrity through a read-only connection. |
| `redis-cli -h HOST PING` | Send a Redis PING command. |
| `redis-cli -h HOST INFO server` | Read Redis server information. |
