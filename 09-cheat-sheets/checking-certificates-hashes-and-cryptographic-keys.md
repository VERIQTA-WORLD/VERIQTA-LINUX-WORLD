```bash
openssl version -a
openssl list -digest-algorithms
openssl dgst -sha256 FILE
openssl x509 -in CERTIFICATE.pem -noout -text
openssl x509 -in CERTIFICATE.pem -noout -dates
openssl x509 -in CERTIFICATE.pem -noout -subject -issuer
openssl x509 -in CERTIFICATE.pem -noout -fingerprint -sha256
openssl x509 -in CERTIFICATE.pem -noout -checkend 86400
openssl verify -CAfile CA.pem CERTIFICATE.pem
openssl s_client -connect HOST:443 -servername HOST -verify_return_error < /dev/null
openssl rand -hex 32
openssl rand -base64 32
sha256sum -- FILE
sha512sum -- FILE
base64 -- FILE
base64 --decode -- ENCODED_FILE
gpg --list-keys
gpg --list-secret-keys --keyid-format LONG
gpg --fingerprint KEY_ID
gpg --verify SIGNATURE_FILE DATA_FILE
gpg --armor --detach-sign FILE
gpg --encrypt --recipient KEY_ID FILE
gpg --decrypt FILE.gpg
```
