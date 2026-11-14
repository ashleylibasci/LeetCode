class Solution:
    def compress(self, chars: list[str]) -> int:
        res = []
        count = 1

        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                res.append(chars[i - 1])

                if count > 1:
                    res.extend(str(count))

                count = 1

        chars[:len(res)] = res
        return len(res)
