class Solution:
    def simplifyPath(self, path: str) -> str:
        splited = path.split("/")

        q = deque()

        for word in splited:
            if not word:
                continue
            elif word == ".":
                continue
            elif word == "..":
                if q:
                    q.pop()
            else:
                q.append(word)

        pathStr = "/".join(list(q))
        return "/" + pathStr
