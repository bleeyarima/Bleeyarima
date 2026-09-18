#!/usr/bin/env python3
import dns.resolver
import sys

def dns_lookup(domain, record_type):
    """Perform a DNS lookup for the given record type."""
    try:
        answers = dns.resolver.resolve(domain, record_type)
        print(f"\n{record_type} records for {domain}:")
        for rdata in answers:
            print(f"  {rdata}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
    except dns.resolver.NoAnswer:
        print(f"No {record_type} records found for {domain}.")
    except dns.resolver.Timeout:
        print("DNS query timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python lookup.py <domain> [record_type]")
        print("Record types: A, AAAA, MX, NS, TXT, CNAME, SOA, etc. (default: A)")
        sys.exit(1)

    domain = sys.argv[1]
    record_type = sys.argv[2].upper() if len(sys.argv) > 2 else "A"

    # Validate record type
    valid_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA", "PTR", "SRV"]
    if record_type not in valid_types:
        print(f"Invalid record type. Choose from: {', '.join(valid_types)}")
        sys.exit(1)

    dns_lookup(domain, record_type)

if __name__ == "__main__":
    main()
