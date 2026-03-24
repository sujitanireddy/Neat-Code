#Question -> https://neetcode.io/problems/longest-repeating-substring-with-replacement/question?list=neetcode150

""""
The core idea behind this problem can be tricky to understand at first, but once it makes sense, the solution feels quite simple.

I went through both Neets explanation and Gregs walkthrough; they follow the same strategy, though Gregs implementation is slightly clearer when stepping through a dry run.

By walking through each line of the code on a whiteboard and tracing what changes at every step, I finally understood how and why the algorithm works and what the underlying intuition really is.

ord returns the ASCII value of a character - FYI.

Greg's Video -> https://www.youtube.com/watch?v=tkNWKvxI3mU
"""
#time Complexity: O(n)
#Space Complexity: O(1)
def characterReplacement(self, s: str, k: int) -> int:

        L = 0
        freq = [0] * 26
        longest = 0

        for R in range(len(s)):

            freq[ord(s[R]) - 65] += 1

            #window size - max(freq) < k
            while ((R-L) + 1) - max(freq) > k:

                freq[ord(s[L]) - 65] -= 1
                L += 1
            
            longest = max(longest, (R - L) + 1)

        return longest