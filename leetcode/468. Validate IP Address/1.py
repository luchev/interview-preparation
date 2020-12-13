# Complexity (n = input string length)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if parseIPv4(IP):
            return 'IPv4'
        if parseIPv6(IP):
            return 'IPv6'
        return 'Neither'


def parseIPv4(ip: str) -> bool:
    sections = ip.split('.')
    if len(sections) != 4:
        return False
    for section in sections:
        try:
            section_int = int(section)
            if str(section_int) != section:
                return False
            if not 0 <= section_int <= 255:
                return False
        except:
            return False
    return True


def parseIPv6(ip: str) -> bool:
    sections = ip.split(':')
    if len(sections) != 8:
        return False

    allowed_chars = set([str(x) for x in range(0, 10)] +
                        ['a', 'b', 'c', 'd', 'e', 'f'])
    for section in sections:
        if len(section) > 4:
            return False

        try:
            section_int = int(section, 16)
        except:
            return False

    return True
