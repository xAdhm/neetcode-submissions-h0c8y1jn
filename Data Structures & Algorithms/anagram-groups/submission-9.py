class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            sSorted = ''.join(sorted(s))
            groups[sSorted].append(s)

        return list(groups.values())