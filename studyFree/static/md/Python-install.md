# Python安装、环境配置

## 一、python安装

### 1、下载python

​		官网：[Download Python | Python.org](https://www.python.org/downloads/)

​		淘宝镜像：[CNPM Binaries Mirror (npmmirror.com)](https://registry.npmmirror.com/binary.html?path=python/)

​		<img src="https://data.waiyutong.org/ocr/1094574a8088d641eb3479fac33cbcc4.png" alt="image-20220302155636293" style="zoom:80%;" />	

​		根据需求选择对应版本下载即可。

​		<img src="https://data.waiyutong.org/ocr/8f6f0d4bf29a46c4fd78d94bc9d3a2b8.png" alt="image-20220302160413665" style="zoom:80%;" />



### 2、安装

①	勾选**`Add Python 3.9 to PATH`**  并选择自定义安装

![image-20220302165817578](https://data.waiyutong.org/ocr/c79c4f84b04fc2f8a367fec15f66f884.png)

②	点击下一步

![image-20220302171046542](https://data.waiyutong.org/ocr/edc90739b0ccc3e7d597b41a642d0904.png)

③	选择安装位置 - *最好不要选择默认安装位置*，点击`install`开始安装

![image-20220302171326760](https://data.waiyutong.org/ocr/1f28943b74f96d29bc446b14ae78e81e.png)

④	等待安装完成

![image-20220302171454345](https://data.waiyutong.org/ocr/300c171afec4a06ea231ef5c16d34dc6.png)





## 二、验证配置环境

### 1、打开 **CMD** 命令行窗口，输入命令 **`python`** 并回车。

验证失败 ：

![image-20220302172605615](https://data.waiyutong.org/ocr/7e3e7dc3dbe558935baeea23b6b67923.png)



原因 1： 安装时未勾选`Add Python 3.9 to PATH`，导致未自动配置环境变量。

解决：①	在控制面板>系统和安全>系统下，选择“高级系统设置”。

![](https://img-blog.csdnimg.cn/20190927170837666.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzIyMjQ3Ng==,size_16,color_FFFFFF,t_70)



​		②	选择环境变量。

![](https://img-blog.csdnimg.cn/20190927171421235.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzIyMjQ3Ng==,size_16,color_FFFFFF,t_70)



​		③	如果变量中没有 <font color=red>**Path**</font>，则选择 `新建`，如果已经有 <font color=red>**Path**</font>，则选择 `编辑`。

​				在 <font color=red>**PATH**</font> 中添加python安装路径，及python包路径。如下：

![image-20220303092911609](https://data.waiyutong.org/ocr/f87a15636db7b8b248b07e2204c75909.png)

```
C:\Python\Python39\
C:\Python\Python39\Scripts\
```



​	④	如果 `CMD` 中输入`python`,继续报不是内部命令......，请尝试重启电脑。



验证成功：

![image-20220303093522673](https://data.waiyutong.org/ocr/862efa2eff48751fb6beed8e22c36679.png)



## 三、其他设置

### 1、设备中安装了多个版本的 `Python` ,运行 `.py` 文件时无法调用指定版本的`python`

解决：

​	①	idea 可以选择指定版本的解释器（不过多叙述）

​	②	将 `python.exe` 执行文件重命名。

![python38](https://data.waiyutong.org/ocr/e69173880b514035e7d9ca43e2199673.png)



![image-20220303095936551](https://data.waiyutong.org/ocr/2444ccf465f8cc5b01bf977f34ccd075.png)



​		③	 通过文件名运行`python解释器`,可以保留常用的python解释器执行程序名称为`python.exe`

![image-20220303100154882](https://data.waiyutong.org/ocr/cf66beac19ad1ddf7febe3972b7705b2.png)



## 四、pip国内源配置



常用国内源：

```http
pypi 清华源：https://pypi.tuna.tsinghua.edu.cn/simple
pypi 豆瓣源：http://pypi.douban.com/simple
pypi 腾讯源：http://mirrors.cloud.tencent.com/pypi/simple
pypi 阿里源：https://mirrors.aliyun.com/pypi/simple
```



①	临时使用国内源：`pip install [包名] -i [国内源地址]`

```bash
pip install markdown -i https://pypi.tuna.tsinghua.edu.cn/simple
```

②	把国内源设为默认：

```python
#清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
#阿里源
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
#腾讯源
pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple
#豆瓣源
pip config set global.index-url http://pypi.douban.com/simple/

```

