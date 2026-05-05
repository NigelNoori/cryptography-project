import rsa_system
import dh_exchange

def print_header(title):
    print(f"==================================")

def main():
    print_header("CUSTOM CRYPTOSYSTEM CLI")
    print("Initializing step-by-step verbose mode for project demonstration.\n")
    
    rsa_instance = None

    while True:
        print("\n    MAIN MENU    ")
        print("1. Diffie-Hellman Key Exchange")
        print("2. RSA Key Generation")
        print("3. RSA Message Encryption & Decryption")
        print("4. RSA Digital Signature")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            print_header("Diffie-Hellman Key Exchange")
            # Using small public parameters so the math is easy to trace
            p = 23
            g = 5
            print(f"[SYS] Using public prime p = {p} and base g = {g}\n")
            
            alice = dh_exchange.DiffieHellman(p, g, name="Alice", verbose=True)
            print("-" * 30)
            bob = dh_exchange.DiffieHellman(p, g, name="Bob", verbose=True)
            
            print("\n[SYS]     Exchange Phase    ")
            alice_shared = alice.compute_shared_secret(bob.public_key)
            bob_shared = bob.compute_shared_secret(alice.public_key)
            
            print("\n[SYS]     Verification    ")
            if alice_shared == bob_shared:
                print(f"[SUCCESS] Both parties share the secret key: {alice_shared}")
            else:
                print("[ERROR] Key exchange failed.")

        elif choice == '2':
            print_header("RSA Key Generation")
            # 8-bit primes keep the terminal output clean and easy to read
            rsa_instance = rsa_system.RSA(bits=8, verbose=True)

        elif choice == '3':
            print_header("RSA Message Encryption & Decryption")
            if not rsa_instance:
                print("[SYS] Generating RSA keys first...")
                rsa_instance = rsa_system.RSA(bits=8, verbose=True)
            
            msg = input("\nEnter a short message to encrypt: ")
            
            print("\n[SYS]     Encryption Phase    ")
            ciphertext = rsa_instance.encrypt(msg)
            print(f"\n[RESULT] Final Ciphertext Array: {ciphertext}")
            
            print("\n[SYS]     Decryption Phase    ")
            plaintext = rsa_instance.decrypt(ciphertext)
            print(f"\n[RESULT] Final Decrypted Message: {plaintext}")

        elif choice == '4':
            print_header("RSA Digital Signature")
            if not rsa_instance:
                print("[SYS] Generating RSA keys first...")
                rsa_instance = rsa_system.RSA(bits=8, verbose=True)
                
            msg = input("\nEnter a message to sign: ")
            
            print("\n[SYS]     Signing Phase    ")
            signature = rsa_instance.sign(msg)
            
            print("\n[SYS]     Verification Phase    ")
            is_valid = rsa_instance.verify(msg, signature)
            
            if is_valid:
                print("\n[RESULT] Signature is VALID. The message is authentic.")
            else:
                print("\n[RESULT] Signature is INVALID.")

        elif choice == '5':
            print("\nExiting program. Good luck with the project submission!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()