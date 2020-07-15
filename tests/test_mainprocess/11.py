def test():
    try:
        a = int(input("输入被除数："))
        b = int(input("输入除数："))
        c = a / b
        print("您输入的两个数相除的结果是：", c )
        return "正常数据返回"
    except (ValueError, ArithmeticError):
        print("程序发生了数字格式异常、算术异常之一")
        return "异常数据返回"
    except :
        print("未知异常")
    print("程序继续运行")

print(test())







