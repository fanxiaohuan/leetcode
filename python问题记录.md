python 基础语法：

keyword 不能用作标识符

```python
import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

python 字符强制转换

int(value) 强制整数

str(value) 强制字符串

字符串字符串的截取的语法格式如下：**变量[头下标（0 第一位 -1 最后一位）:尾下标:步长（0正向 -1逆向）]**

 [::-1] 从最后一位开始打印字符串

[0:-1]
enumerate(nums)  字符串下标

数据类型 不常用的：tuple、set、

type() 查询变量数据类型

isinstance() 判断变量类型

- type()不会认为子类是一种父类类型。
- isinstance()会认为子类是一种父类类型。

list*2 重复操作两次

tuple()  元素不能修改 可以切割和拼接

set()

dic{} 不可变、不能重复 内置函数有：clear() keys() values()