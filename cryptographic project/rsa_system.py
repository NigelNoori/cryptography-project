import crypto_math

class RSA:
    def __init__(self, bits=8, verbose=False):
        """Initializes and generates keys. Defaults to small bits for easy tracing."""
        self.verbose = verbose
        if self.verbose:
            print("\n--> [RSA] Starting Key Generation")
            
        # 1. Generate two prime numbers
        self.p = crypto_math.generate_prime(bits, verbose=self.verbose)
        self.q = crypto_math.generate_prime(bits, verbose=self.verbose)
        
        # 2. Compute n and phi
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        
        # 3. Choose e (Public Exponent)
        # Typically 65537, but we find a small valid one for cleaner step-by-step output
        self.e = 3
        while crypto_math.gcd(self.e, self.phi) != 1:
            self.e += 2
            
        # 4. Compute d (Private Exponent)
        self.d = crypto_math.mod_inverse(self.e, self.phi)
        
        if self.verbose:
            print(f"[RSA] p = {self.p}, q = {self.q}")
            print(f"[RSA] Modulus (n) = {self.n}, Totient (phi) = {self.phi}")
            print(f"[RSA] Public Key: (e={self.e}, n={self.n})")
            print(f"[RSA] Private Key: (d={self.d}, n={self.n})")
            print("........................................\n")

    def encrypt(self, message):
        """Encrypts a string message character by character."""
        if self.verbose:
            print(f"[RSA] Encrypting message: '{message}'")
        
        ciphertext = []
        for char in message:
            m = ord(char)
            # C = M^e (mod n)
            c = crypto_math.mod_pow(m, self.e, self.n)
            ciphertext.append(c)
            if self.verbose:
                print(f"      Char '{char}' (ASCII {m}) -> Encrypted: {c}")
                
        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypts an array of integers back to a string."""
        if self.verbose:
            print(f"[RSA] Decrypting ciphertext: {ciphertext}")
            
        plaintext = ""
        for c in ciphertext:
            # M = C^d (mod n)
            m = crypto_math.mod_pow(c, self.d, self.n)
            plaintext += chr(m)
            if self.verbose:
                print(f"      Cipher {c} -> Decrypted ASCII {m} -> Char '{chr(m)}'")
                
        return plaintext

    def _custom_hash(self, message):
        """A simple custom hash function to create a message digest for signing."""
        digest = 0
        for i, char in enumerate(message):
            # A basic polynomial rolling hash concept
            digest = (digest + ord(char) * (i + 1)) % self.n
        return digest

    def sign(self, message):
        """Creates a digital signature by encrypting the message hash with the private key."""
        digest = self._custom_hash(message)
        # S = Hash^d (mod n)
        signature = crypto_math.mod_pow(digest, self.d, self.n)
        
        if self.verbose:
            print(f"[RSA] Signing message...")
            print(f"      Message Digest: {digest}")
            print(f"      Signature generated: {signature}")
            
        return signature

    def verify(self, message, signature):
        """Verifies a digital signature using the public key."""
        digest = self._custom_hash(message)
        # Hash = S^e (mod n)
        decrypted_signature = crypto_math.mod_pow(signature, self.e, self.n)
        
        is_valid = digest == decrypted_signature
        if self.verbose:
            print(f"[RSA] Verifying signature...")
            print(f"      Calculated Digest: {digest}")
            print(f"      Decrypted Signature: {decrypted_signature}")
            print(f"      Signature Valid: {is_valid}")
            
        return is_valid