from collections import defaultdict
def totalFruit(fruits):
    """
    :type fruits: List[int]
    :rtype: int
    """

    left = right = 0
    ans = 0

    trees = defaultdict(int)

    for right in range(len(fruits)):
        trees[fruits[right]] += 1
        while(len(trees) > 2):
            trees[fruits[left]] -= 1
            if trees[fruits[left]] == 0:
                del trees[fruits[left]]
            left += 1
        ans = max(ans, right-left+1)
    return ans
        

fruits = [1,2,3,2,2]
# 4
print(totalFruit(fruits))

