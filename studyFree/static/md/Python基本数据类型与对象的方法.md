# Python基本数据类型与对象的方法

## 一、字符串：Str

​	python 中的字符串字面量由单引号或双引号括起。

​	`'hello'` 等同于 `"hello"`等同于 `"""hello"""`。



### 1.	str + str

字符串的拼接：

```python
a = '我们喜欢打:'
b = "篮球,"
c = """你呢？"""
print(a+b+c)

####################
# 输出如下：
# 我们喜欢打:篮球,你呢？
####################
```



### 2.	len(str)

获取字符串的长度：

```python
a = '我们喜欢打:篮球,你呢？'
print(len(a))

####################
# 12
####################
```



### 3.	str.replace(old, new)

替换字符串中的指定字符old -> new, 并返回新的字符串：

```python
a = '我们喜欢打:篮球,你呢？'
b = a.replace('篮球','足球')
print(a)
print(b)

####################
# 输出如下：
# 我们喜欢打:篮球,你呢？
# 我们喜欢打:足球,你呢？
####################
```

- **replace() 的返回值是一个新的字符串，原字符串不会改变。**



### 4.	str.split('|')

以特定的字符分割字符串, 并返回一个列表：

```python
a = '我们喜欢打:篮球,你呢？'
print(a.split(':'))
print(a.split('篮球'))
print(a.split('？'))
print(a.split('ss'))
print(a.split())

####################
# 输出如下：
# ['我们喜欢打', '篮球,你呢？']
# ['我们喜欢打:', ',你呢？']
# ['我们喜欢打:篮球,你呢']
# ['我们喜欢打:篮球,你呢?']
# ['我们喜欢打:篮球,你呢?']
####################
```

- **作为分割的字符不会出现在列表中**
- **不能用 `''` 字符作为分割字符**



### 5.	str.index('|')

返回特定字符在字符串str中的索引下标：

```python
a = '我们喜欢打:篮球,你呢？'
print(a.index(':'))
print(a.inex('？'))

####################
# 输出如下：
# 5
# 11
####################
```

- **如果查找的字符不存在会报错：`ValueError: substring not found`**
- **查找 `''` 字符返回0**



### 6.	str.startswith('|') 、str.endswith('|')

判断字符串str是否以特定字符开头、结尾，并返回一个布尔值：

```python
a = '我们喜欢打:篮球,你呢？'
print(a.startswith('我们喜'))
print(a.startswith('们喜'))
print(a.endswith('？'))
print(a.endswith('你呢'))

####################
# 输出如下：
# True
# False
# True
# False
####################
```



### 7.	str.count('|')

统计字符串中指定字符出现的次数：

```python
a = '123114565'
print(a.count('1'))
print(a.count('6'))
print(a.count('9'))

####################
# 输出如下：
# 3
# 1
# 0
####################
```



### 8.	str.strip()

去除字符串首尾的空格，返回一个新的字符串：

```python
a = '  123456  '
print(a.strip())
print(a.lstrip())
print(a.rstrip())

b = '1135611'
print(b.strip('1'))

####################
# 输出如下：
# 123456
# 123456  #后面有两个空格
#   123456

# 356
####################
```

- **lstrip() 删除字符串开头的空格，rstrip() 删除字符串结尾的空格**
- **strip(chr) chr不为None是，删除首位指定字符chr**



### 9.	str.isxxx()

判断字符串的数据类型，还回布尔值：

```python
# 检测字符串是否只由数字组成
print('123'.isdigit())		# True
print('123abc'.isdigit())	# False

# 检测字符串是否由字母和数字组成
print('123abc'.isalnum())	# True
print('123 abc'.isalnum())	# False		

# 检测字符串是否只由字母组成
print('123abc'.isalpha())	# False
print('abc'.isalpha())		# True

# 检查字符串是否只由ASCII字符组成
print('Aa12<>'.isascii())	# True
print('你好'。isasscii()) 	  # False

# 检测字符串中的字母是否都是小写
print('你好Abc'.islower())   # False
print('你好abc'.islower())   # True

# 检测字符串中的字母是否都是大写
print('你好Abc'.isupper())   # False
print('你好ABC'.isupper())   # True

# 检测字符串是否只由空格组成
print('  '.isspace())		# True
print(' e '.isspace())		# False

# 检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
print('This Is String'.istitle())		# True
print('This is string'.istitle())		# False

```





### 10.	str[0]、str[1: 3]

> #### i. 字符串元素索引	[字符串 | 白月黑羽 (byhy.net)](https://www.byhy.net/tut/py/basic/04/#字符串元素索引)
>
> ```python
> a = '刘总你好啊'
> ```
>
> 大家从字符串内容就可以看出，里面有5个字符，每个字符都是这个字符串的一个**元素**。
>
> 像这种由一个个 元素依次组成的字符串， Python语言里面，把这种特性的数据称之为 **sequence**，翻译成中文就是**序列**。
>
> 序列里面的元素都是有索引的。 所谓索引就是元素的下标，如下图所示
>
> ![](https://data.waiyutong.org/ocr/4caf80bcf90d8e12f581b3c964808e51.png)
>
> 特别特别要注意的是，字符串元素的索引是从 **0** 开始，而不是从1 开始。
>
> **刘** 这个字符的索引是 0 ，
>
> **总** 这个字符的索引是 1 ，
>
> **你** 这个字符的索引是 2 ，
>
> **好** 这个字符的索引是 3 ，
>
> **啊** 这个字符的索引是 4 ，
>
> 
>
> **刘** 这个字符可以这样获取a[0] ， 运行如下代码看看
>
> ```python
> print(a[0])
> print(a[1])
> print(a[4])
> 
> ##########
> # 刘
> # 总
> # 啊
> ##########
> ```
>
> 一个长度为 n 的字符串， 它的最后一个字符的下标是n - 1。
>
> 由于并不存在一个下标索引为5 的元素， 就会报下面这样的错误
>
> ```python
> print(a[5])
> 
> IndexError: string index out of range
> ```
>
> ------
>
> 
>
> 而且Python还支持 `用负数表示字符串的索引` ， 最后一个字符的索引是 -1, 倒数第二个是 -2， 如上图：
>
> **啊** 这个字符的索引是 -1 ， 可以这样获取 a[-1] ，
>
> **好** 这个字符的索引是 -2 ， 可以这样获取 a[-2] ，
>
> **你** 这个字符的索引是 -3 ， 可以这样获取 a[-3] ，
>
> **总** 这个字符的索引是 -4 ， 可以这样获取 a[-4] ，
>
> **刘** 这个字符的索引是 -5 ， 可以这样获取 a[-5] ，
>
> 
>
> #### ii. 字符串切片	[字符串 | 白月黑羽 (byhy.net)](https://www.byhy.net/tut/py/basic/04/#字符串切片)
>
> sequence特性的数据对象 都支持 `切片操作` ， 字符串是具有sequence特性的，当然也支持切片。
>
> 什么是切片， 形象的说，好像用刀切出其中的一部分
>
> 比如我要把
>
> ```python
> a = '刘总你好啊'
> ```
>
> 这个字符串切出其中 `你好` 这部分内容，
>
> 假想我们手里有把刀，要从下面的字符串中切出 `你好`，就应该在箭头所示的地方切两刀，就得到 `你好` 这个 子字符串了
>
> ![](https://data.waiyutong.org/ocr/15a85c2e8217b1c7948f4a9937ee0190.png)
>
> 那么我们看看这两刀 对应的索引的位置。
>
> 如果用正数表示就是 2 和 4 ， Python中可以用 `a[2:4]` 这样的切片表达式来得到该字符串。 
>
> ```python
> a = '刘总你好啊'
> print(a[2:4])
> ```
>
> 当然也可以用负数表示， 就是 -3 和 -1 ， Python中可以用 `a[-3:-1]` 这样的切片表达式来得到该字符串。 
>
> ```python
> a = '刘总你好啊'
> print(a[-3:-1])
> ```
>
> 字符串切片前面的索引是切片开始的元素的 索引，后面的索引是切片结束的元素的 **索引 + 1**
>
> 
>
> **省略一个切片索引**
>
> 如果要得到’刘总你好啊' 当中 **你好啊** 这3个字 :
>
> 可以用 `a[2:5]`
>
> 我们发现，要切出的内容一直到字符串的结尾，这时还可以用 `a[2:]` ，**后面的索引** 空着不写，**表示到整个字符串的结束** 。
>
> 相应的，如果 **前面的索引** 不写，可以表示 **从字符串的开头切片**， 比如 `a[:2]` ，就是切出 **刘总** 这两个字





### 11.	字符串格式化：% 、format

#### i. %，关于字符串的输出

```python
print("字符串：%s,%s,%s,%s。" % (1, 22.22, [1, 2],'你好'))
print("字符串不足5位，左边补空格：%5s。" % '2')
print("字符串不足5位，右边补空格：%-5s。" % '2', "end")
print("字符串宽10位，截取两位：%10.2s。" % "hello.world")


####################
# 字符串：1,22.22,[1, 2],你好。
# 字符串不足5位，左边补空格：     2。
# 字符串不足5位，右边补空格：2        。end
# 字符串宽10位，截取两位：           he。
####################
```

- **可以传入任意类型的数据，譬如整数、浮点数、列表、元组甚至字典，他都会自动转成字符串类型**



**补充：**

 %，关于整数的输出

- %o：oct 八进制
- %d：dec 十进制
- %x：hex 十六进制

```python
print("整数：%d,%d,%d。" % (1, 22.22, 33))
print("整数不足5位，左边补空格：%5d。" % 22)
print("整数不足5位，左边补0：%05d。" % 22)
print("整数不足5位，右边补空格：%-5d。" % 22, "end")
print("八进制：%o" % 222)
print("十六进制：%x" % 12)


####################
# 整数：1,22,33。
# 整数不足5位，左边补空格：22。
# 整数不足5位，左边补0：00022。
# 整数不足5位，右边补空格：22       。end
# 八进制：336
# 十六进制：c
####################
```



%，关于浮点数的输出

```python
print("浮点数：%f,%f" % (1, 22.22))
print("浮点数保留两位小数：%.2f" % 22.222)
print("浮点数保留两位小数，宽5位，不足补0：%05.2f" % 2.222)

####################
# 浮点数：1.000000,22.220000
# 浮点数保留两位小数：22.22
# 浮点数保留两位小数，宽5位，不足补0：02.22
####################
```

- **默认保留6位小数，可通过  这种形式指定小数位，2代表保留两位**



#### ii. format，位置匹配

-  不带编号，即“{}” 
-  带数字编号，可调换顺序，即“{1}”、“{2}” 
-  带关键字，即“{a}”、“{tom}”

```python
print("今天是{}的{}生日会".format("帅哥", 18))

print("今天是{1}的{0}生日会".format("帅哥", 18))

print("今天是{0}的{1}生日会".format("帅哥", 18))

print("今天是{name}的{key}生日会".format(22, 11, name="帅哥", key=18))

print("今天是{name}的{key}生日会，接着上{}".format("test", name="帅哥", key=18))


####################
# 今天是帅哥的18生日会
# 今天是18的帅哥生日会
# 今天是帅哥的18生日会
# 今天是帅哥的18生日会
# 今天是帅哥的19生日会，接着上test
####################




# 以下会报错
print("今天是{0}的{}生日会".format("帅哥", 18))

print("今天是{name}的{key}生日会，接着上{}".format( name="帅哥", key=18,"test"))
```

- **当你只写了{} 时，默认按传入的值的顺序读取**
- **{}和 {1} 是不能共存的**
- **{}和{key}共存时，你传入带有关键字指定的值必须写在后面，类似函数（形参在前，实参在后）**



## 二、列表：List



列表是一个有序且可更改的集合。在 Python 中，列表用方括号编写。

```python
a = [1, '2', 'apple', ['你好'，'world'], ' ']
```



### 1.	append(n)、extend(_iterable)、insert(index, n)、+

```python
base = [1, '2', 'apple', ['你好'，'world'], ' ']

# + :将两个列表中的元素按前后顺序构建一个新的列表，并返回。
# 原列表不会发生改变
a = base
b = ['255']
c = a + b
d = b + a

print(c)			# [1, '2', 'apple', ['你好'，'world'], ' ', '255']
print(d)			# ['255', 1, '2', 'apple', ['你好'，'world'], ' ']
print(a)			# [1, '2', 'apple', ['你好'，'world'], ' ']
print(b)			# ['255']




# append :将一个新的元素（列表、字符串、字典......）添加到原列表的末尾。
# 该方法没有返回值，原列表会改变
a = base
a.append(b)
print(a)					# [1, '2', 'apple', ['你好'，'world'], ' ', ['255']]

a = base
a.append('255')
print(a)					# [1, '2', 'apple', ['你好'，'world'], ' ', '255']

a = base
a.append(255)
print(a)					# [1, '2', 'apple', ['你好'，'world'], ' ', 255]

a = base
a.append({'name':'Tome'})
print(a)					# [1, '2', 'apple', ['你好'，'world'], ' ', {'name':'Tome'}]




# extend :将一个可迭代对象里的元素按顺序添加到列表末尾
a = base
a.extend(['extend', 'end'])
print(a)						# [1, '2', 'apple', ['你好'，'world'], ' ', 'extend', 'end']

a = base
a.extend({'name':'Tome', 'age':18})
print(a)						# [1, '2', 'apple', ['你好'，'world'], ' ', 'name', 'age']

a = base
a.extend('255')
print(a)						# [1, '2', 'apple', ['你好'，'world'], ' ', '2', '5', '5']





# insert :在列表指定位置(index)添加一个新元素，该位置后的元素依次后移
# 该方法没有返回值，原列表会改变
a = base
a.insert(0,'你好！')
print(a)					# ['你好！', 0, 1, 2, 3, 4, 5]

a = base
a.insert(2,'你好！')
print(a)					# [0, 1, '你好！', 2, 3, 4, 5]

# 如果index > 列表最大索引（len(list) - 1）,则将元素添加到原列表的末尾同append
a = base
a.insert(6,'你好！')
print(a)					# [0, 1, 2, 3, 4, 5, '你好！']

a = base
a.insert(100,'你好！')
print(a)					# [0, 1, 2, 3, 4, 5, '你好！']
```



### 2.	index(n)、count(n)

```python
a = ['你好', 1, 2, 3, 5, 1, 5, 0, '你好']

# index :查询元素在列表中的位置索引
# 如果查询的元素在列表中有多个，仅会返回第一个位置
print(a.index('你好'))			# 0
print(a.index(5))				 # 4

# 如果index(n, start, stop) 中，start/stop不为空，则在列表指定范围内查找
print(a.index('你好',1))			# 8
print(a.index(5,5))				 # 6

# 如果查找的元素不在列表中，会报错
print(a.index('不好'))			# ValueError: '不好' is not in list	




# count :统计列表中指定元素出现的个数
print(a.count('你好'))			# 2
print(a.count(0))				 # 1
print(a.count(5))				 # 2
print(a.count('不好'))		    # 0
```



### 3.	pop(index)、remove(n)、del、clear()

```python
base = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

# pop :通过列表索引删除元素，并返回删除的元素
a = base
b = a.pop(1)
print(a)						# [0, 2, 3, 4, 0, 1, 2, 3, 4]
print(b)						# 1

a.pop(100)						# IndexError: pop index out of range




# remove :在列表中从左——》右，查找指定元素并将找到的第一个元素删除，无返回值
a = base
a.remove(1)
print(a)						# [0, 2, 3, 4, 0, 1, 2, 3, 4]
a.remove(4)
print(a)						# [0, 2, 3, 0, 1, 2, 3, 4]

a.remove(1000)					# ValueError: list.remove(x): x not in list




# del :通过列表索引删除元素，可以切片删除
a = base
del a[1]						
print(a)						# [0, 2, 3, 4, 0, 1, 2, 3, 4]

a = base
del a[3:6]						
print(a)						# [0, 1, 2, 1, 2, 3, 4]



# clear :清空列表
a = base
a.clear()
print(a)						# []

```



### 4.	reverse()

```python
# 列表反转、倒叙
a = [0, 1, 2, 3, 4]
a.reverse()
print(a)						# [4, 3, 2, 1, 0]
```



### 5.	sort()

```python
# 对列表内的元素排序
# list.sort(reverse=True|False, key=myFunc)
# reverse：可选。reverse=True 将对列表进行降序排序。默认是 reverse=False。
# key：可选。指定排序标准的函数。


# 默认升序排序,0-9-A-Z-a-z-拼音
a = ['Porsche', 'BMW', 'Volvo', '0', '1', '2', 'app', 'lcss', '你好', '不好', 'Book']
a.sort()
print(a)			
# ['0', '1', '2', 'BMW', 'Book', 'Porsche', 'Volvo', 'app', 'lcss', '不好', '你好']



# 按元素长度排序
# 返回值的长度的函数：
def myFunc(e):
  return len(e)

a = ['Porsche', 'Audi', 'BMW', 'Volvo']
a.sort(key=myFunc)
print(a)										# ['BMW', 'Audi', 'Volvo', 'Porsche']

a = ['Porsche', 'Audi', 'BMW', 'Volvo']
a.sort(reverse=True, key=myFunc)
print(a)										# ['Porsche', 'Volvo', 'Audi', 'BMW']



# 根据字典的 "year" 值对字典列表进行排序：
# 返回 'year' 值的函数：
def myFunc(e):
  return e['year']

a = [
  {'car': 'Porsche', 'year': 1963},
  {'car': 'Audi', 'year': 2010},
  {'car': 'BMW', 'year': 2019},
  {'car': 'Volvo', 'year': 2013}
]

a.sort(key=myFunc)
print(a)										# [
                                                #    {'car': 'Audi', 'year': 2000}, 
                                                #    {'car': 'Porsche', 'year': 2005}, 
                                                #    {'car': 'VW', 'year': 2011}, 
                                                #    {'car': 'BMW', 'year': 2019}
                                                # ]

```

- 列表中同时存在字符串与number无法排序 `TypeError: '<' not supported between instances of 'int' and 'str'`



### 6.	列表切片

[列表、元组 | 白月黑羽 (byhy.net)](https://www.byhy.net/tut/py/basic/07/#列表的sequence操作)



