| Command | What you can do with it |
| --- | --- |
| `openssl version -a` | Inspect the installed OpenSSL version and build details. |
| `openssl list -digest-algorithms` | List supported digest algorithms. |
| `openssl dgst -sha256 FILE` | Calculate a SHA-256 file digest with OpenSSL. |
| `openssl x509 -in CERTIFICATE.pem -noout -text` | Decode and inspect a PEM X.509 certificate. |
| `openssl x509 -in CERTIFICATE.pem -noout -dates` | Print certificate validity dates. |
| `openssl x509 -in CERTIFICATE.pem -noout -subject -issuer` | Print certificate subject and issuer. |
| `openssl x509 -in CERTIFICATE.pem -noout -fingerprint -sha256` | Print a SHA-256 certificate fingerprint. |
| `openssl x509 -in CERTIFICATE.pem -noout -checkend 86400` | Check whether a certificate remains valid for at least one day. |
| `openssl verify -CAfile CA.pem CERTIFICATE.pem` | Verify a certificate against a selected CA file. |
| `openssl s_client -connect HOST:443 -servername HOST -verify_return_error < /dev/null` | Inspect a TLS handshake using SNI and stop on certificate-verification errors. |
| `openssl rand -hex 32` | Generate 32 random bytes displayed as hexadecimal. |
| `openssl rand -base64 32` | Generate 32 random bytes displayed as Base64. |
| `sha256sum -- FILE` | Calculate a SHA-256 file digest. |
| `sha512sum -- FILE` | Calculate a SHA-512 file digest. |
| `base64 -- FILE` | Encode a file as Base64, which is not encryption. |
| `base64 --decode -- ENCODED_FILE` | Decode Base64 data. |
| `gpg --list-keys` | List public keys in the GPG keyring. |
| `gpg --list-secret-keys --keyid-format LONG` | List secret-key references and long key IDs. |
| `gpg --fingerprint KEY_ID` | Display a GPG key's fingerprint. |
| `gpg --verify SIGNATURE_FILE DATA_FILE` | Verify a detached signature against its data file. |
| `gpg --armor --detach-sign FILE` | Create an ASCII-armored detached signature. |
| `gpg --encrypt --recipient KEY_ID FILE` | Encrypt a file to a selected recipient key. |
| `gpg --decrypt FILE.gpg` | Decrypt a GPG file to standard output. |
