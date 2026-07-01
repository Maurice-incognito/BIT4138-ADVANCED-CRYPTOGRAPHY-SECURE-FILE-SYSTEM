# Student: [Your Name] - BIT4138

print("=== PKI Component Identification — Class Activity 1 ===")
print()

components = [
    {
        "component": "Certificate Authority (CA)",
        "role": "Trusted organization that issues and signs digital certificates",
        "responsibilities": [
            "Verifies identities of certificate applicants",
            "Issues signed digital certificates",
            "Revokes compromised certificates",
            "Publishes Certificate Revocation Lists (CRL)"
        ],
        "examples": "DigiCert, Sectigo, GlobalSign, Let's Encrypt"
    },
    {
        "component": "Registration Authority (RA)",
        "role": "Acts as intermediary between users and the Certificate Authority",
        "responsibilities": [
            "Verifies user identity before certificate issuance",
            "Approves or rejects certificate requests",
            "Forwards verified requests to the CA"
        ],
        "examples": "University registration offices, corporate IT departments"
    },
    {
        "component": "Digital Certificate",
        "role": "Electronic document binding a public key to an identity",
        "responsibilities": [
            "Proves ownership of a public key",
            "Contains issuer, subject, validity period, public key",
            "Signed by CA to guarantee authenticity"
        ],
        "examples": "SSL/TLS certificates, email certificates, code signing certs"
    },
    {
        "component": "Certificate Repository",
        "role": "Database storing issued and revoked certificates",
        "responsibilities": [
            "Stores all issued certificates",
            "Makes certificates publicly accessible",
            "Hosts Certificate Revocation Lists"
        ],
        "examples": "LDAP directories, online certificate databases"
    },
    {
        "component": "End User",
        "role": "Individual or system that uses certificates for secure communication",
        "responsibilities": [
            "Generates key pairs",
            "Requests certificates from CA via RA",
            "Uses certificate for HTTPS, email, or signing"
        ],
        "examples": "Website owners, email users, banks, government agencies"
    }
]

for item in components:
    print(f"{'='*60}")
    print(f"Component      : {item['component']}")
    print(f"Role           : {item['role']}")
    print(f"Responsibilities:")
    for r in item['responsibilities']:
        print(f"  - {r}")
    print(f"Examples       : {item['examples']}")
    print()

print("="*60)
print("PKI Component Identification Complete!")
print("All five components identified and explained.")