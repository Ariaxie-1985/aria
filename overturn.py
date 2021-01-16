class Solution(object):
    def reverse(self, x):
            em = []
            if x == 0:
                return 0
            if -2**31< x < 2**31-1:
                if x > 0:
                    l = list(str(x))
                    if l[-1] == 0:
                        l.pop()
                        for i in range(len(l)-1, -1, -1):
                            em.append(l[i])
                        get_ready = [str(j) for j in em]
                        reverse_num = int(''.join(get_ready))
                        if -2**31< reverse_num < 2**31-1:
                            return reverse_num
                        else:
                            return 0
                    else:
                        for i in range(len(l) - 1, -1, -1):
                            em.append(l[i])
                        get_ready = [str(j) for j in em]
                        reverse_num = int(''.join(get_ready))
                        if -2 ** 31 < reverse_num < 2 ** 31 - 1:
                            return reverse_num
                        else:
                            return 0
                if x < 0:
                    x = -x
                    l = list(str(x))
                    if l[-1] == 0:
                        l.pop()
                        for i in range(len(l) - 1, -1, -1):
                            em.append(l[i])
                        get_ready = [str(j) for j in em]
                        reverse_num = int(''.join(get_ready))
                        if -2 ** 31 < reverse_num < 2 ** 31 - 1:
                            return -reverse_num
                        else:
                            return 0
                    else:
                        for i in range(len(l) - 1, -1, -1):
                            em.append(l[i])
                        get_ready = [str(j) for j in em]
                        reverse_num = int(''.join(get_ready))
                        if -2 ** 31 < reverse_num < 2 ** 31 - 1:
                            return -reverse_num
                        else:
                            return 0
            else:
                return 0