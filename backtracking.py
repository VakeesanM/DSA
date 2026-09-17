"""
Backtracking is just dfs. The only difference is that in normal dfs, the tree given. But in backtracking you have to create it yourself.


The puesdo for bassically backtracking problems is this:

def backtracking(param):
    if base_case:
        results.append(path)
        return results
    
        for choice in chocies:
            if violates_constraints:
                continue
            
                
            make_choice
            backtrack(updated_params)
            undo_choice # often with just .pop()

Thats it. 
"""


# Here is code for a simple Backtracking; permuations


from typing import List

def permuations(word) -> List[str]:

    results = []
    used = [False] * len(word)
    def backtrack(path, used):
        if len(path) == len(word):
            results.append(''.join(path))
            return

        for i,char in enumerate(word):
            if used[i]:
                continue
            used[i] = True
            path.append(char)
            backtrack(path,used)
            path.pop()
            used[i] = False

    backtrack([], used)
    return results


print(permuations("abc"))