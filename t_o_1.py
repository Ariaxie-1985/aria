class Solution(object):
    def reverse(self, x):
        res = 0
        last = 0
        while x!=0:
            #每次取末尾数字
            tmp = x%10
            last = res
            res = res*10 + tmp
            #判断整数溢出
            if last != int(res/10):
                return 0
            x //= 10
        return res

#
#
# class Solution(object):
#     def reverse(self, x):
#         res = 0
#         while(x!=0):
#             #每次取末尾数字
#             tmp = x%10
#             #判断是否 大于 最大32位整数
#             if (res>214748364 or (res==214748364 and tmp>7)):
#                 return 0
#             #判断是否 小于 最小32位整数
#             if (res<-214748364 or (res==-214748364 and tmp<-8)):
#                 return 0
#             res = res*10 + tmp
#             x //= 10
#         return res
# class Solution:
#     def reverse(self, x: int) -> int:
#         res = 0
#         x1 = abs(x)
#         while(x1!=0):
#             temp = x1%10
#             if res > 214748364 or (res==214748364 and temp>7):
#                 return 0
#             if res<-214748364 or (res==-214748364 and temp<-8):
#                 return 0
#             res = res*10 +temp
#             x1 //=10
#         return res if x >0 else -res

if __name__ == '__main__':
    r = Solution.reverse(self=int, x=99999999999999999)
    print(r)