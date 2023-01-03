import paramiko

# Set the path and filename for the private and public keys
private_key_path = "id_rsa"
public_key_path = "id_rsa.pub"

# Generate a new RSA key
key = paramiko.RSAKey.generate(2048)

# Save the private key to a file
key.write_private_key_file(private_key_path)

# Save the public key to a file
with open(public_key_path, "w") as f:
  f.write("{} {}".format(key.get_name(), key.get_base64()))

print("Private key saved to:", private_key_path)
print("Public key saved to:", public_key_path)
