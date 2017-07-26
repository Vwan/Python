有其他脚本语言的经验，整体做下来还比较顺畅，过程中有一些看着简单的时候想着要一个一个字敲会有些烦躁，导致心流受影响，后来想到一个办法，即后面所述的方法，好了很多。

遇到问题的时候，都是先搜索。以前是会直接找别人发的类似问题的帖子，比如stackoverflow, cnblog等，后来受开智的教育，会先强迫自己点开官方文档找答案，实在解决不了再看别人的帖子。希望以后可以和其他同学一起交流问题互相学习。

对于基础更好些的同学，做前面的练习可能更觉得没多大挑战性，为避免“不屑”情绪，突然想到一个方法，既可以从头到尾做下来，还可以多带动点脑子，我自己试验了ex33，觉得还挺有趣的。

方法就是：看着书中每章的“你应该看到的结果”部分，倒推出代码（需要用到该章的知识点），而不是看着代码一个一个的敲出来。然后再跟作者的源代码作比较。

比如ex33, 我看着运行结果倒推出来的代码是：

```
i = 0
numbers = []
while i < 6:    
    print "At the top i is %d" % i
    numbers.append(i)
    print "Numbers now: %d" % numbers[i]
    i += 1
    print "At the bottom i is %d" % i

print "The numbers:"
for num in numbers:
    print num
```

结果运行后发现"Numbers now:" 打印出来的不一样，我只是把当前Numbers[i]打印出来了，需要的是整个Numbers数组

于是我将下行

```
print "Numbers now: %d" % numbers[i]
```

改为

```
print "Numbers now: %d" % numbers
```

结果报错了

```
TypeError: %d format: a number is required, not list
```

好吧，%d 是用于整型，numbers是个list, 那是不是可以用%r呢（任意格式）？于是改为%r, 成功：

```
Numbers now: [0, 1, 2, 3, 4, 5]
```

然后对照作者的源代码，咦，作者并没有用格式符，更简单：

```
print "Numbers now: ", numbers
```

