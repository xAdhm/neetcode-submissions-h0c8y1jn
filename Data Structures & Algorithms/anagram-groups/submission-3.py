class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        shared = {}

        for s in strs:
            letters = "".join(sorted(s))

            if letters in shared:
                shared[letters].append(s)
            else:
                shared[letters] = [s]

        return list(shared.values())