class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       d = {}
       
       for w in strs:
           s = ''.join(sorted(w))
           
           if s not in d:
               d[s] = []
           
           d[s].append(w)
       
       return list(d.values())