class Solution:
    def isValid(self, s: str) -> bool:
        close_dict = { "(":")", "{":"}", "[":"]" }
        open_list = []
        for symbol in s:
            if symbol in close_dict.keys():
                open_list.append(symbol)
            elif open_list == [] or symbol != close_dict[open_list.pop()]:
                return False
        return open_list == []
