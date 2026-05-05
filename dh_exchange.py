import crypto_math
import random

class DiffieHellman:
    def __init__(self, p, g, name="User", verbose=False):
        """Initializes with public prime (p) and base (g)."""
        self.p = p
        self.g = g
        self.name = name
        self.verbose = verbose
        
        # 1. Generate Private Key
        self.private_key = random.randint(2, self.p - 2)
        
        # 2. Generate Public Key to share
        # A = g^a (mod p)
        self.public_key = crypto_math.mod_pow(self.g, self.private_key, self.p)
        
        if self.verbose:
            print(f"[{self.name}] Generated Private Key: {self.private_key}")
            print(f"[{self.name}] Computed Public Key: {self.public_key}")

    def compute_shared_secret(self, other_public_key):
        """Computes the final shared secret using the other party's public key."""
        # S = B^a (mod p)
        shared_secret = crypto_math.mod_pow(other_public_key, self.private_key, self.p)
        
        if self.verbose:
            print(f"[{self.name}] Computing shared secret using received public key {other_public_key}...")
            print(f"[{self.name}] Final Shared Secret: {shared_secret}")
            
        return shared_secret