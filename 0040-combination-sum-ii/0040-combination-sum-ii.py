class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        n = len(candidates)
        

        def backtrack(ind, target, path):
            if target == 0:
                ans.append(path[:])
                return
            
            for i in range(ind, n):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue 
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i+1, target - candidates[i], path)
                path.pop()

            # backtrack(ind+1, target, path)

        backtrack(0, target, [])
        return ans