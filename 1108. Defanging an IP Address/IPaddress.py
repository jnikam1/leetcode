class Solution:
    def defangIPaddr(self, address: str) -> str:
        string1= address.replace('.','[.]')
        return string1