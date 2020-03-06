# Encrypt a file with a password using openssl

Simple file cryptography using a symmetric key. Very portable because all you need is openssl.

`openssl enc -aes-256-cbc -salt -in PALANTIR-Guide.pdf -out PALANTIR-Guide.pdf.aes`

You may use the `-a` option to enable base64 encoding

>You will be prompted for a password.

## 4: Decrypt

`openssl enc -d -aes-256-cbc -in PALANTIR-Guide.pdf.aes -out PALANTIR-Guide.pdf`

>You will be prompted for a password.