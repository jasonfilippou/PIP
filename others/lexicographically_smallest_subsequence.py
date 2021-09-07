# TODO: Try to figure out how to solve this using monotonic stacks.

"""
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Examples:

    - tenerife ===> eifnrt
    - avocado ===> acdov
    - pennandteller (===> {p, e, n, a, d, t, l, r}) ===> adenlprt


- Naive: - Scan string, getting unique characters. There are probably library routines that do this. Linear time assumed. Uses hash table, so linear space.
         - Sort list of unique characters in ascending order. Worst case O(n log_2n) for strings that don't have duplicate characters.
         - Print!

            This has linearithmic time and uses linear space. How can we drop it into linear time? Let's use a visitation set and a monotonic stack.
        We also need to use a temporary stack to hold the elements from the monotonic stack that we pop!

        - Stack: [e, n, r, t, i

        - Visitation set: {t, e, n, r

        Pseudocode:

        visitation_Set = set()
        mon_stack = []


        What happens with input: zyxwvutsr? This algo is O(n^2) :(
"""