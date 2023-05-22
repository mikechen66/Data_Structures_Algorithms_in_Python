

# boyer_moore.py

"""

The main idea of the Boyer-Moore algorithm is to improve the running time of
the brute-force algorithm by adding two potentially time-saving heuristics. Roughly
stated, these heuristics are as follows:

Looking-Glass Heuristic: 

When testing a possible placement of P against T, begin the comparisons from the end 
of P and move backward to the front of P.

Character-Jump Heuristic: 

During the testing of a possible placement of P within
T, a mismatch of text character T[i]=c with the corresponding pattern character P[k] 
is handled as follows. If c is not contained anywhere in P, then shift P completely 
past T[i] (for it cannot match any character in P). Otherwise, shift P until an occur-
rence of character c in P gets aligned with T[i]

https://web.cs.ucdavis.edu/~gusfield/cs224f09/bnotes.pdf
https://www.cs.rit.edu/~lr/courses/alg/student/1/KMPBoyerMorris.pdf
https://www.cs.emory.edu/~cheung/Courses/253/Syllabus/Text/Matching-Boyer-Moore2.html
"""


NO_OF_CHARS = 256


def badCharHeuristic(string, size):
    # Initialize all occurrence as -1
    badChar = [-1]*NO_OF_CHARS
    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i;
    # return initialized list
    return badChar


def search(txt, pat):
    m = len(pat)
    n = len(txt)
    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m)
    # s is shift of the pattern with respect to text
    s = 0
    while(s <= n-m):
        j = m-1
        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while j >= 0 and pat[j] == txt[s+j]:
            j -= 1
        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j < 0:
            print("Pattern occur at shift = {}".format(s))
            s += (m-badChar[ord(txt[s+m])] if s+m else 1)
        else:
            s += max(1, j-badChar[ord(txt[s+j])])


def main():
    txt = "ABAAABCD"
    pat = "ABC"
    search(txt, pat)


if __name__ == '__main__':
    main()


# Output:

"""
Pattern occur at shift = 4
"""