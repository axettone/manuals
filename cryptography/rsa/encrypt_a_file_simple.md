# Encrypt a file with a password using openssl

Simple file cryptography using a symmetric key. Very portable because all you need is openssl.

`openssl enc -aes-256-cbc -salt -in PALANTIR-Guide.pdf -out PALANTIR-Guide.pdf.aes`

You may use the `-a` option to enable base64 encoding

>You will be prompted for a password.

## Decrypt

`openssl enc -d -aes-256-cbc -salt -in PALANTIR-Guide.pdf.aes -out PALANTIR-Guide.pdf`

>You will be prompted for a password.

## A note for macOS users

On macOS there's an old version on openssl, using MD5 as the digest algor by default. This may result in lower security and interoperability issues. You should use `-md md5` if you're decoding a file encoded on macOS, unless you specify a better hashing algo.

## Make an alias/function!

Edit your terminal emulator rc file (eg. `~/.bashrc` or `~/.zshrc`) and add those lines:

```
encrypt() {
        openssl enc -e -aes-256-cbc -a -salt -md sha256 -in ${1} -out ${2}
}
decrypt() {
        openssl enc -d -aes-256-cbc -a -salt -md sha256 -in ${1} -out ${2}
}
```
then
`source ~/.bashrc` or `source ~/.zshrc`
and now you can use `encrypt <source> <dest>` and `decrypt <source> <dest>` as you like.