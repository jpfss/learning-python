# -*- coding: utf-8 -*-

# 引用模块
import phone
import math
from fib import fib
import supports

# Now you can call defined function that module as follows
supports.print_func("Zara")

# =============================================================================
# The from...import Statement
# =============================================================================

print(fib(100))

# =============================================================================
# The from...import * Statement
# =============================================================================
# 在模块中，模块的名称（作为字符串）可用作全局变量 __name__ 的值。
# 模块中的代码将被执行，就像您导入它一样，但 __name__ 设置为"__main__"
if __name__ == "__main__":
    f = fib(100)
    print(f)
# =============================================================================
# Locating Modules 本地模块路径优先级
# =============================================================================

# 当前目录
# 如果没有找到模块，Python 会在 shell 变量 PYTHONPATH 中搜索每个目录
# 如果一切都失败了，Python 会检查默认路径。
# 在 UNIX 上，此默认路径通常为 /usr/local/lib/python3

# money
Money = 2000


def AddMoney():
    # Uncomment the following line to fix the code:
    # 必须有global关键字否则局部变量-我们在设置之前访问了局部变量 Money 的值
    global Money
    Money = Money + 1


print(Money)
AddMoney()
print(Money)
# =============================================================================
# The dir( ) Function
# =============================================================================
# Import built-in module math
content = dir(math)
print(content)
# =============================================================================
# Packages in Python
# =============================================================================
phone.pots()
phone.isdn()
phone.g3()
