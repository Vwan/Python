## 注释
```
# 此行命令不会被处理
print "test" # print "not be handled" #后面的命令或字符不会被处理
```

## 数字和计算
 + plus 加
 - minus 减
 / slash 除
 * asterisk 乘
 % percent 取余
 < less-than 小于
 > greater-than 大于
 <= less-than-equal 小于等于
 >= greater-than-equal 大于等于

## 1. 输入数据到程序中

### raw_input
人机交互，计算机问你要输入什么数据，一般是在命令行窗口，提示你通过键盘输入。
比如:
```
print "Please enter your name:"
age = raw_input()
print age
```
### raw_input(prompt)
简化前面的代码，将print行所代表的提示直接作为raw_input方法的提示：

```
age = raw_input("Please enter your name:")
print age
```
那如果想要实现下面这样的问答方式呢？你可能已经想到了，raw_input("> ")就可以实现。
```
I'd like to ask you a few questions. 
Do you like me Zed? 
> yes 
Where do you live Zed? 
> America 
What kind of computer do you have? 
> Tandy
```
### 将变量传给脚本(.py)程序
前面的raw_input命令，是让用户在命令行控制台根据提示输入数据。
我们还可以省却这些交互操作，直接在python运行命令行(python <.py file>)中传入数据，这时需要用到python sys 模块的命令行参数对象 argv。

- 首先导入argv对象

- 将每个参数赋予一个变量名：script, first, second, 以及 third。把 argv 中的东西解包，将所有的参数依次赋予左边的变量名。

  这里的script 代表python 源文件.py

  first,second,third依次代表传给程序的三个变量

```
from sys import argv
script,first,second,third=argv
```
脚本示例：
```
from sys import argv
script,first,second,third=argv
print "first variable is called: ", first
print "second variable is called: ", second
print "third variable is called: ", third
```

运行命令：python ex13.py arg1 arg2 arg3， 结果如下：
```
script is called: ex13.py
argv is called:  ['ex13.py', 'arg1', 'arg2', 'arg3']
first variable is called:  arg1
second variable is called:  arg2
third variable is called:  arg3
```

## 2. 输出数据
### print 输出/打印内容
1. print "content"
2. print "格式化字符串"，这里的格式化字符串有多种：
- %s：字符类型
```
print "my name is %s" % my_name
```
- %d：整型
```
print "he is %d years old" % age
```
- %f：浮点数
```
print "the value of pi is %5.3f" % math.pi
```
- %r：任意格式
```
test='any format'
print "the value of test is %r" % test
```
注意：%r 和 %s的区别：
上一段代码的运行结果如下：
	the value of test is 'any format'
那如果将%r 换成 %s 后，运行结果则为：the value of test is any format
看出区别了吗？

如果没看出来或者觉得不明显的话，换个例子：
```
test = '''line1\nline2\nline3'''
print "the value of test is %r" % test
```
这时候的输出结果是：> the value of test is 'line1\nline2\nline3'
换成%s后：
> the value of test is line1
> line2
> line3

可见，%r 是原封不动的显示变量的定义（也有例外），其背后是调用了repr()方法，%s则是调用了str()方法转换成了字符串显示。

关于str()和repr()的一个例子：
```
>>> import datetime
>>> d = datetime.date.today()
>>> str(d)
'2011-05-14'
>>> repr(d)
'datetime.date(2011, 5, 14)'
```
4. 重复输出
  print '.' * 10
  ..........'
5. print 行后面加, 表示不换行，接着输出下一行内容

### string.format
TBD

## 3. 文件操作
比较常用的一些文件操作方法：
 close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
 read – 读取文件内容。你可以把结果赋给一个变量。
 readline – 读取文本文件中的一行。 
 truncate – 清空文件，请小心使用该命令。
 write(stuff) – 将stuff写入文件。

### 打开
file = open(filename)
file = open(filename, mode), 这里的mode指读写覆盖等

  - 'r' for reading, If mode is omitted, it defaults to 'r'. The default is to use text mode, which may convert '\n' characters to a platform-specific representation on writing and back on reading. 
  - 'w' for writing (truncating the file if it already exists), 
  - 'a' for appending (which on some Unix systems means that all writes append to the end of the file regardless of the current seek position).
  - ‘b' for binary file, which will improve portability. (Appending 'b' is useful even on systems that don’t treat binary and text files differently, where it serves as documentation.) 
  - 'r+', 'w+' and 'a+' open the file for updating (reading and writing); 
  - ’'w+' truncates the file. 

### 读文件
file = open(filename)
content = file.read()
line_content=file.readline()
### 写文件
先打开文件，确保有写权利：file = open(filename,'w')
然后写内容：file.write(content)
最后关闭文件：file.close()

另可使用with 关键词，将文件操作group起来，并且不需要手动加上file.close()操作：
```
with open(filename,'w') as file:
	file.write(content)
```
### 其他
exists(filename)：判断文件是否存在，需要用到from os.path import exists 
[file.seek(offset)](https://docs.python.org/2/library/stdtypes.html#file.seek): 设置文件要读取的当前位置。比如Offset为0，则从文件最开始读取。有点类似指针或光标指向offset的。

## 4 逻辑关系

- and 与 
- or 
- not 非
- != (not equal) 不等于 
- == (equal) 等于 
- = (greater-than-equal) 大于等于 
- <= (less-than-equal) 小于等于 
- True 真
- False 假

**逻辑计算流程：**

1. 找到相等判断的部分 (== or !=)，将其改写为其最终值 (True 或 False)。
2. 找到括号里的 and/or，先算出它们的值。 
3. 找到每一个 not，算出他们反过来的值。
4. 找到剩下的 and/or，解出它们的值。
5. 等你都做完后，剩下的结果应该就是 True 或者 False 了。

## 5 流程控制

### 条件语句
```
if a > b:
	print a - b
elif a < b:
	print b - a
else:
	print a + b
```
### 循环语句
#### for-loop
```
list = [1,2,3]
for i in list:
	print i
```

``` 
for i in range(0,6)
```
#### while-loop
```

```
注意：
1. 尽量少用 while-loop，大部分时候 for-loop 是更好的选择。 
2. 重复检查你的 while 语句，确定你测试的布尔表达式最终会变成 False 。 
3. 如果不确定，就在 while-loop 的结尾打印出你要测试的值。看看它的变化。

## Collections

记住: ordinal == 有序，以 1 开始；cardinal == 随机选取, 以 0 开始。

### List

```
a = [1,2,3,4]
a.append(5)
a.append([6,7])
print a[0]
```

### Dictionary

类似于其他语言的Map

```
a = {'name':'openmind',"age":100}
print a['name']
```

```
>>> stuff[1] = "Wow" 
>>> stuff[2] = "Neato" 
>>> print stuff[1] 
Wow 
>>> print stuff[2] 
Neato
```

删除

```
del stuff[1]
```



### Tuple



## Help

### help(module_name)
从命令行输入python, 进入python控制台后，导入模块后，可通过help(module name)来查看帮助。
```
>>> import ex25
>>> help(ex25)
Help on module ex25:

NAME
    ex25

FILE
    c:\projects\python\learnpythonthehardway\ex25.py

FUNCTIONS
    break_words(stuff)
        This function will break up words for us.

    print_first_and_last(sentence)
        Prints the first and last words of the sentence.
```

### pydoc

同help(module_name), 生成Python module的帮助描述，可以直接从命令行查看python api，不需要进入python控制台：

pydoc的参数可以是：
- 方法名
- 模块名
- 包名
- 模块或包中模块的类、方法的引用
- python 源文件路径
> The argument to pydoc can be the name of a function, module, or package, or a dotted reference to a class, method, or function within a module or module in a package. If the argument to pydoc looks like a path (that is, it contains the path separator for your operating system, such as a slash in Unix), and refers to an existing Python source file, then documentation is produced for that file.

- pydoc raw_input:
```
PS C:\Users\> python -m pydoc raw_input
Help on built-in function raw_input in module __builtin__:

raw_input(...)
    raw_input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.
```

- pydoc <python source file location>
```
PS C:\Users\vivia> pydoc C:\Users\vivia\OneDrive\Projects\Python\learnPythonTheHardWay\ex47\skeleton\ex47\game.py
Help on module game:

NAME
    game

FILE
    c:\users\vivia\onedrive\projects\python\learnpythonthehardway\ex47\skeleton\ex47\game.py

CLASSES
    __builtin__.object
        Room

    class Room(__builtin__.object)
     |  Methods defined here:
     |
     |  __init__(self, name, description)
     |
     |  add_paths(self, paths)
     |
     |  go(self, direction)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
```

### Function vs Method

method是一种特殊的function，与class或类实例相关联。Function则不然
所有的method都是function, 但不是所有的function都是method
在python中，可以使用 def 新建函数。函数可以做三样事情： 
1. 它们给代码片段命名，就跟“变量”给字符串和数字命名一样。 
2. 它们可以接受参数，就跟你的脚本接受 argv 一样。 
3. 通过使用 #1 和 #2，它们可以让你创建“微型脚本”或者“小命令”。

python function可以接受 0-多个参数。关于多个参数，可以用* args来表示，比如
```
def func(*args):
	arg1,arg2 = args
```

或者在function中不明确表示各变量名,而是直接当作tuple：
```
def print_2(*args):
    print "type of args is %r:" % type(args)
    print "this *args is called"
    for arg in args:
    	print "arg: %r" % (arg)

print_2(1,3,4)
```
运行结果为：
```
type of args is <type 'tuple'>:
this *args is called
arg: 1
arg: 3
arg: 4
```
## 其他

### check if it is a number

```
next = raw_input("> ")
if isinstance(next,int):
```

```
next = raw_input("> ")
if type(next) == type(1):
```

## 附录

### Python关键词及其他

Keywords（关键字）
 and 
 del 
 from 
 not 
 while 
 as 
 elif 
 global 
 or 
 with 
 assert 
 else 
 if 
 pass 
 yield 
 break 
 except 
 import
 print 
 class 
 exec 
 in 
 raise 
 continue 
 finally 
 is 
 return 
 def 
 for 
 lambda 
 try 

数据类型 
 True 
 False 
 None 
 strings 
 numbers 
 floats 
 lists 

字符串转义序列(Escape Sequences) 
 \\ 
 \' 
 \" 
 \a 
 \b 
 \f
 \n 
 \r 
 \t 
 \v 

字符串格式化(String Formats) 
 %d 
 %i 
 %o 
 %u 
 %x 
 %X 
 %e 
 %E 
 %f 
 %F 
 %g 
 %G 
 %c 
 %r 
 %s 
 %% 

操作符号
 + 
 - 
 * 
 ** 
 / 
 // 
 %
 < 
 > 
 <= 
 >= 
 == 
 != 
 <> 
 ( ) 
 [ ] 
 { } 
 @ 
 , 
 : 
 . 
 = 
 ; 
 += 
 -= 
 *= 
 /= 
 //= 
 %= 
 **=