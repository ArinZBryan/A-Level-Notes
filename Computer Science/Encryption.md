This is the act of scrambling a message using an algorithm, such than any third party to the transaction would be unable to decipher the data without some key, which is required to decode the data.

If we have the key, encryption is a reversible process unlike the process of hashing, which produces a similar output that cannot have the original data retrieved from it.

## Symmetric vs Asymmetric encryption
Symmetric encryption uses one key for both encryption and decryption, whereas asymmetric encryption uses a public key and private key (or pair of keys, one for the sender and one for the recipient) to encrypt and decrypt the data separately.

## Symmetric encryption
There are several methods of symmetric encryption, generally involving a single key.
- **Ceasar Cipher** - Each character is incremented by a fixed value across an entire string.
```c++
char* ceaser_cipher(char* buffer, int length, int shift)
{
    for (int i = 0; i < length; i++)
    {
        buffer[i]+=shift;   
    }
    return buffer;
}
```
- **Substitution Cipher** - Each character is incremented by a varying value, as specified by the key.

```c++
char* substitution_cipher(char* buffer, int buffer_length, int* key, int key_length)
{
    for (int i = 0; i < buffer_length; i++)
    {
        int keypos = i % key_length;
        buffer[i] = (char)((int)buffer[i] + key[keypos]);
    }
    return buffer;
}
```

## Asymmetric encryption
This type of encryption uses two types of key: public and private.

If *Alice* ($A$) wants to send *Bob* ($B$) a message ($M_{unencrypted}$), then it is first encrypted using *Alice's Private Key* ($A_{private}$) and *Bob's public key* ($B_{public}$). Then the encrypted message ($M_{encrypted}$) can be sent.

When *Bob* receives the message ($M_{encrypted}$), he must combine *his private key* ($B_{private}$) and *Alice's public key* ($A_{public}$) to form a decryption key, which is then used to decrypt the message ($M_{encrypted}$) to form the *unencrypted message* ($M_{unencrypted}$)