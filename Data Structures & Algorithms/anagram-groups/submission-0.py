class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for s in strs:
            sSorted = "".join(sorted(s))

            if sSorted in groups:
                groups[sSorted].append(s)
            else:
                groups[sSorted] = [s]
        
        return list(groups.values())