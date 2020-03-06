# How to encrypt a file

The principle is simple: use symmetric encryption for the file, but use an asymmetric algorithm to encrypt the symmetric key.

## 1: Generate a public/private keypair (Recipient side)
`openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048`

Extract the public key:

`openssl rsa -pubout -in private_key.pem -out public_key.pem`

Give away your public key!

## 2: Create a disposable encoding symmetric key

The following command will create a 32 byte key

`openssl rand -base64 32 > key.bin`

Encode it with the public key of the recipient

`openssl rsautl -encrypt -inkey public_key.pem -pubin -in key.bin -out key.bin.enc`

## 3: Encrypt your file

Note the we use the cleartext 32 byte key. (Use -a for base64 encoding, perfect for e-mail)

`openssl enc -aes-256-cbc -salt -in PALANTIR-Guide.pdf -out PALANTIR-Guide.pdf.aes -pass file:key.bin`

>Now send your encrypted file and key to the recipient.

## 4: Decrypt (recipient side)

Decrypt the key

`openssl rsautl -decrypt -inkey private_key.pem -in key.bin.enc -out key.bin`

Now you can decrypt the file

`openssl enc -d -aes-256-cbc -in PALANTIR-Guide.pdf.aes -out PALANTIR-Guide.pdf -pass file:key.bin`
