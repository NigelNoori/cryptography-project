# Cryptography Programming Project: Custom Cryptosystem

This is my implementation for the Cryptosystem Programming Project. The goal of this project was to build a fully functional cryptosystem from scratch without relying on any external cryptographic libraries or built-in crypto functions. 

All algorithms, including modular exponentiation, primality testing, and hashing, were implemented manually.

## Project Requirements Addressed

1. **Key Generation (RSA):** Implemented from scratch. Generates primes using a manual Miller-Rabin test and calculates public/private exponents using the Extended Euclidean Algorithm.
2. **Key Exchange (Diffie-Hellman):** Implemented to securely share a secret key over a simulated public channel.
3. **Message Encryption and Decryption (RSA):** Encrypts and decrypts strings character-by-character using the generated keys.
4. **Digital Signature (RSA):** Implemented using a custom-built polynomial rolling hash function. The digest is encrypted with the sender's private key and verified with their public key.
5. **Step-by-step Outputs & UI:** The system is wrapped in an interactive CLI. I included a `verbose=True` flag in the background architecture so that every mathematical step, ASCII conversion, and key generation detail is printed directly to the terminal for easy grading.

## File Structure
* `main.py`: Exteremly user-friendly CLI menu that ties everything together.
* `crypto_math.py`: Contains all the foundational math algorithms (`gcd`, `extended_gcd`, `mod_pow`, `is_prime`).
* `rsa_system.py`: The RSA class handling keys, encryption, decryption, and the custom hash/signature logic.
* `dh_exchange.py`: The Diffie-Hellman class handling private/public key generation and shared secret computation.

## Notes
* **programmer notes:** I chose Python because it natively handles arbitrarily large integers, which allowed me to focus purely on the cryptographic algorithms rather than building a custom BigInt data structure.
* **Small Prime Numbers:** For the RSA implementation, I set the default prime generation to 8-bit numbers. This was done intentionally so that the step-by-step mathematical outputs in the terminal remain readable and easy to follow. Larger bits work perfectly fine with the algorithm but will flood the console. 
* **Custom Hash:** Since libraries are not allowed, I wrote a basic polynomial rolling hash `_custom_hash()` inside the RSA class purely to meet the digital signature requirement.