'''
A directory can be specified via a pathname. THere are 2 types of those:

    - Absolute pathnames, which start from the root (/).
    - Relative pathnames, which start from the current working directory.

There are also two specially named directories: '.' for the current directory and '..' for the parent directory.  In addition, repeated slashes in a pathname are to be ignored
(so that // is the same as /).

As a result, the same file or directory can be specified by multiple pathnames, For instance,

/usr/lib/../bin/pyscrapy   is the same as /usr/bin/pyscrapy

scripts//./scripts/pathrise/././ is the same as scripts/pathrise

Given a pathname, return the SHORTEST EQUIVALENT pathname. If a path tries to go up beyond the root (like /usr/../../), throw an error.

This is a Google question.
'''

# Non-trivial examples:
#       Absolute:   /bin////./proc/sys//../../mnt/././. <===> /bin/mnt
#       Relative: files////latex/img///../temp/../img/./termite.png <===> files/latex/img/termite.png

'''
Naive:

    - Tokenize string at '/' (that's one pass).
        - Result should be an array of strings, every one of which will represent a directory or file (for the last one).    
        - Check list(filter(None, my_string.split("/")))
    - Go through array, Erase all instances of '.'.
    - Go through array again, every time you see '..', erase one position before. If you see '..' again, go even further back.
        - This last piece can be quadratic :( 
'''

'''
Optimize:
    - We will instead discuss an algorithm that goes through the string once for tokenization and once more, for simplification. That's it.
    - The algorithm will use a stack, to help us "erase" directories that are rendered null by the presence of '..'.
    - In the tokenized result, '.' can be removed.
    - My final result will be my stack, with slashes in between its elements, and perhaps a leading slash if the original path was absolute (easy to determine).
'''


class Solution:
    def simplifyPath(self, s: str) -> str:
        assert s is not None, "Give me something to work with"
        s = s.strip()
        stack = []
        if s[0] == '/':
            stack.append(s[0])  # Our stack will contain at most one slash, and it's this one.
        tokens = list(filter(None, s.split("/")))
        for token in tokens:
            if token == "..":
                if len(stack) > 0 and stack[-1] == '/':             # Should also work with len(stack) == 1
                    raise RuntimeError("Root has no parent.")
                elif len(stack) > 0 and stack[-1] != '/':
                    stack.pop()
                else:   # stack empty, just put a parent reference.
                    stack.append(token)
            elif token != '.':
                stack.append(token)
        return '/'.join(stack) if s[0] != '/' else '/'.join(stack)[1:]



if __name__ == '__main__':
    soln = Solution()
    for path in ["/bin/proc", "/bin/./proc", "/bin/../../", "/proc/mnt/hd/../sd/./",  # Third one should raise
                 "../", "../foo/bar", "../.", "/."                                    # Note that parent directories for relative paths should be accepted
                 "/bin////./proc/sys//../../mnt/././.", "files////latex/img///../temp/../img/./termite.png",
                 "files////latex/img///../temp/../img/./.hiddenFolder"]:  # Note the hidden directory at the end!
        try:
            print(f"Path {path} simplifies to {soln.simplifyPath(path)}")
        except RuntimeError:
            print(f"Path {path} threw an exception.")
