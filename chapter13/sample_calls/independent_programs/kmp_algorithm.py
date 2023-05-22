

kmp_algorithm.py


# KMP Algorithm: Knuth Morris Pratt Algorithm

"""
The KMP algorithm is a solution to the string search problem wherein we are required to 
find if a given pattern string occurs in another main string. It is one of the advanced 
string matching algorithm that was conceived by Donald Knuth, James Morris and Vaughan 
Pratt, hence the name "KMP algorithm".

The algorithm keeps a track of the comparison of characters between main text and pattern, 
thereby ensuring that comparisons that have already been done are not repeated, i.e. 
backtracking of the main string never occurs. All this results in a linear matching time 
and a more optimized solution.
"""


# Function to compute LPS array
def compute_lps_array(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
    lps[0] = 0 # lps[0] is always 0
    i = 1
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


def kmp_search(pat, txt):
    M = len(pat)
    N = len(txt)
    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
    # Preprocess the pattern (calculate lps[] array)
    compute_lps_array(pat, M, lps)
    i = 0 # index for txt[]
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


if __name__ == '__main__':
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    kmp_search(pat, txt)


# Output:

"""
Found pattern at index 10
"""
