from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains):                              #exONnb
        count_map = defaultdict(int)

        for entry in cpdomains:
            count_str, domain = entry.split()
            count = int(count_str)

            parts = domain.split(".")

            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                count_map[subdomain] += count

        return [f"{count} {domain}" for domain, count in count_map.items()]
