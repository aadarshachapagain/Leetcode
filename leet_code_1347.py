
# 1347. Minimum Number of Steps to Make Two Strings Anagram
# Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

# Return the minimum number of steps to make t an anagram of s.

# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        first = list(s)
        second = list(t)

        # count the frequency of each letter in  first input word
        dict_input = {alpha: first.count(alpha) for alpha in first}
        # find the frequency of the letters in second input word
        dict_output = {beta: second.count(beta) for beta in first}

        # find the difference between the frequency of each letter and add those values
        def diff(dict_a, dict_b):
            result_dict = {}
            for a in dict_a:
                diff_a = (dict_a[a] - dict_b[a]
                          # if any letter occurs more in second input word assign 0
                          ) if dict_a[a] > dict_b[a] else 0
                result_dict[a] = diff_a
            return sum(result_dict.values())

        print("dict_input:", dict_input)
        print("dict_output:", dict_output)
        print("result=", diff(dict_input, dict_output))
        print("Output: ", diff(dict_input, dict_output))
        return diff(dict_input, dict_output)


obj = Solution()
obj.minSteps("leetcode", "practise")
