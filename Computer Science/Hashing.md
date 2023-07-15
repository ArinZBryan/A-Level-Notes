Hashing the process of forming a unique value or 'hash' from an input string. It is commonly used to verify the integrity of some data before and after transmission.

Though it *can* be used as a method of [encryption](./Encryption.md), hashing algorithms *should not* be used for such a purpose, as they are usually trivially easy to reverse engineer or brute force. This is however, not true of SHA256 or SHA512, are still yet to be cracked.

Hashing, unlike [encryption](./Encryption.md) does not generate a hash of equal length to that of the document, instead it will be a fixed length for each of the various hashing algorithms. For example, a single byte when passed through CRC32 will produce an output of the same length as an entire executable passed through the same algorithm (in this case, 32 bits).

There are several common hashing algorithms:
- MD5
- CRC32
- SHA256

## Hashing for verification
Hashing is most commonly used on the document-level to verify the 'accuracy' of documents. More specifically, it is used to verify that the document has not changed since a hash was taken. If even a single bit of a document has changed, so will the hash. Thus, if a hash of the original can be obtained, any other copy of the document can be hashed, and the hashes compared. Any changes will be evident in this case.

## Hashing in security-conscious situations
Hashing is commonly used for storing passwords. As it is not reversible, if the hash of the password is stored, only the hash of the input password must be checked, thus not exposing any sensitive issues.

### Rainbow Tables
A rainbow table is a precomputed table of hashes that are used to crack passwords. It holds hashes for every permutation of letters and numbers in a given string. This allows for a known hash to have the possible strings that produce it to be given quickly.
Generally, to defeat this method of attack, 'salting' is used.

> **Salting**  
> This is the process of adding a little extra data to a given piece of data before it is hashed. This means that if the 'salt' is kept secret, even if the hashing algorithm is 'cracked' so to say, the data would still be safe for a time.

### Some common salts:
- random chars from seeded pseudo-random number generator
- IP address
- MAC address
- Sector the file is located on on disk

## Collisions
With hashing algorithms that produce strings that are short (i.e.. 32bit), collisions can become common. It is for this reason, that largely , people have moved away from algorithms such as CRC32, and to a lesser extent, MD5. 