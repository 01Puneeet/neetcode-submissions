class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a = []
        b = len(arr)

        for i in range(b):
            if i == b - 1:
                a.append(-1)
            else:
                for j in range(i + 1, b):
                    c = sorted(arr[j:b], reverse=True)
                    d = c[0]
                    a.append(d)
                    break

        return a

















                            # c = arr[i]
            # d = range(arr[i+1],arr[b-1])
            # if c > d:
            #     c.append(a)
            # else:
            #     e = sorted(d)
            #     f = e.append(a)
    #  return a 

                