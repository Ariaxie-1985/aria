class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        else:
            if flowerbed[0] != 0:
                for i in range(0, len(flowerbed)-2):
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] != 1:
                        n = n-1
                        flowerbed[i+1] = 1
                        if n == 0:
                            return True
                    if flowerbed[i] == 1 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0 and flowerbed[i+3] != 1:
                        n = n - 1
                        flowerbed[i+2] = 1
                        if n == 0:
                            return True
                else:
                    return False
            else:
                for i in range(0, len(flowerbed)-1):
                    if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                        n = n-1
                        flowerbed[i] = 1
                        if n == 0:
                            return True
                else:
                    return False


if __name__ == '__main__':
    r = Solution.canPlaceFlowers(self=int, flowerbed=[1, 0, 0, 0, 0, 0, 1], n=2)
    print(r)