class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charsToIndexes = {}
        for idx, s in enumerate(strs):
            key = "".join(sorted(s))
            if key not in charsToIndexes:
                charsToIndexes[key] = [idx]
                continue
            charsToIndexes[key].append(idx)

        groupedAnagrams = []
        for indexes in charsToIndexes.values():
            groupedAnagrams.append([strs[index] for index in indexes])

        return groupedAnagrams

            
        