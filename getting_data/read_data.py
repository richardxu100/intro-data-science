from collections import Counter

def are_there_birds(words):
    return 'birds' in words 

with open('test.txt', 'r') as f:
    birds = are_there_birds(f)

print(birds)

with open('test.txt', 'r') as file:
    [print(line.strip()) for line in file]

def get_domain(email_address):
    return email_address.lower().split('@')[-1]

with open('email_addresses.txt', 'r') as file:
    domains = [get_domain(line.strip()) for line in file if "@" in line]
    domain_counts = Counter(domains)
    print(domain_counts)
