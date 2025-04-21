import random

def generate_private_key(prime):
    """Generate a private key (a random number less than the prime)."""
    return random.randint(2, prime - 2)

def compute_public_key(prime, base, private_key):
    """Compute the public key using the formula: (base^private_key) % prime."""
    return pow(base, private_key, prime)

def compute_shared_secret(prime, received_public_key, private_key):
    """Compute the shared secret using the formula: (received_public_key^private_key) % prime."""
    return pow(received_public_key, private_key, prime)

if __name__ == "__main__":
    # Example usage
    prime = 23  # A prime number agreed upon by both parties
    base = 5    # A base (primitive root modulo prime) agreed upon by both parties

    # Alice generates her private and public keys
    alice_private_key = generate_private_key(prime)
    alice_public_key = compute_public_key(prime, base, alice_private_key)

    # Bob generates his private and public keys
    bob_private_key = generate_private_key(prime)
    bob_public_key = compute_public_key(prime, base, bob_private_key)

    # Exchange public keys and compute the shared secret
    alice_shared_secret = compute_shared_secret(prime, bob_public_key, alice_private_key)
    bob_shared_secret = compute_shared_secret(prime, alice_public_key, bob_private_key)

    # Verify that both shared secrets are the same
    assert alice_shared_secret == bob_shared_secret, "Shared secrets do not match!"
    print(f"Shared secret: {alice_shared_secret}")