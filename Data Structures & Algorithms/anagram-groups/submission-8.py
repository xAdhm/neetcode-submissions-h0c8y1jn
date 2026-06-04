class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            sortedS = "".join(sorted(s))

            if sortedS in groups:
                groups[sortedS].append(s)
            else:
                groups[sortedS] = [s]

        return list(groups.values())