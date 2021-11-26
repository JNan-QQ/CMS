# 用户登录、登出模块

## 登录

3种类型的账号：管理员（1）、教师（100）、学生（1000）， 均使用该接口进行登录。

前端发送的登录请求中包含账号、密码。

后端接收后，对账号密码的正确性进行校验，进入不同的交互界面。

CMS系统使用session会话机制。

如果校验通过，服务端在响应消息头Set-Cookie 中存入session id ，该用户的后续请求头Cookie中必须携带session id。

### 请求

- 请求头

```http
POST /sign/
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "signin",
    "username" : "xxxx",
    "password" : "yyyy"
}
```

### 响应

- 响应头

```http
200 OK
Content-Type: application/json
Set-Cookie: sessionid=<sessionid数值>
```

- 消息体

如果校验通过，返回消息如下

```json
{
    "ret": 0,
    "usertype":1,
    "user_id":1,
    "realName":"管理员",
}
```

ret 为 0 表示登录成功

usertype 是用户类型。 1：管理员，100：教师，1000：学生

user_id 是用户在系统中的id

realname 是用户的姓名

登录成功后， 服务端在消息头Set-Cookie 中存入session id ，该用户的后续请求头Cookie中必须携带session id。

如果登录校验失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg":  "用户名或者密码错误"
}
```

ret 不为 0 表示登录失败， msg字段描述登录失败的原因



## 登出

### 请求

- 请求头

```http
POST /sign/
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "signout"
}
```

### 响应

后端应该根据session id清除掉session，然后返回响应消息

- 响应头

```http
200 OK
Content-Type: application/json
Set-Cookie: sessionid=""
```

- 消息体

```json
{
    "ret": 0
}
```



# 账号管理模块

## 用户注册

### 请求

- 请求头

```http
POST /account/
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "register",
    "username" : "xiaoming",
    "password" : "123456ll",
    "realName" :"小明",
    "usertype" :100
}
```

usertype为账号类型：100、1000；（管理员账号无法注册）

### 响应

- 响应头

```http
200 OK
Content-Type: application/json
```

- 消息体

```json
{
    "ret": 0,
    "user_id":20,
}
```

ret 为 0 表示注册成功

user_id 是用户在系统中的id



## 添加账号

### 请求

- 请求头

```http
POST /account/
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "add",
    "username" : "xiaoming",
    "password" : "123456",
    "realName" : "小明",
    "usertype" :100, 
    #以下字段可不填
    'studentNo':'',
    'classNo':'',
    'gradeNo':'',
    'major':'',
    'desc':''
}
```

password默认为123456

usertype为账号类型：1、100、1000

### 响应

- 响应头

```http
200 OK
Content-Type: application/json
```

- 消息体

```json
{
    "ret": 0,
    "user_id":20,
}
```

ret 为 0 表示添加成功

user_id 是用户在系统中的id



## 删除账号

### 请求

- 请求头

```
POST /account/
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```
{
    "action" : "delete",
    "user_id" : "20",
}
```

此操作仅管理员可用，后台加以判断

### 响应

- 响应头

```
200 OK
Content-Type: application/json
```

- 消息体

```
{
    "ret": 0,
}
```

ret 为 0 表示删除成功



## 修改账号

### 请求

- 请求头

```
POST /account/
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```
{
    "action" : "modify",
    "user_id" : "20",
    "字段key" :"字段value",
}
```

usertype不可修改

管理员可以修改所有用户信息

教师、学生只能修改自己的用户信息（用户名、密码、昵称）

### 响应

- 响应头

```
200 OK
Content-Type: application/json
```

- 消息体

```
{
    "ret": 0,
}
```

ret 为 0 表示修改成功



## 列出账号

### 请求

- 请求头

```
POST /account/
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "list",
    "pagenum":2,
    "pagesize":5,
    "search_items":{key1:value1},
}
```

仅管理员可以操作

pagenum:显示的页数；pagesize:每页显示的数据个数；如果为空则默认为1，5

### 响应

- 响应头

```
200 OK
Content-Type: application/json
```

- 消息体

```
{
    "ret": 0,
    "retlist":[
    {
    "user_id":20,
    "username":"**",
    "usertype":1000,
    },{...}
    ]
}
```

ret 为 0 表示列出成功









# 新闻与通知管理

新闻只有管理员可以编辑、发布；新闻分为三种状态：0（禁用、不显示）、1（发布中）、2（热点）;

通知管理员可以同时给全体用户发信息

## 新闻

### 添加新闻

#### 请求

- 请求头

```http
POST /notice/news
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "add",
    "author_id" : "1",
    "title" : "****",
    "content" : "**************",
    "status" :1,
    "news_type":"校园、社会、竞赛。。。。",
}
```

author_id : 创建者id，暂时默认为1

title ：新闻标题

content ：新闻内容

status ：新闻状态

new_type ：新闻类型根据实际需要填写



#### 响应

- 响应头

```http
200 OK
Content-Type: application/json
```

- 消息体

```json
{
    "ret": 0,
    "news_id":5,
}
```

ret 为 0 表示添加成功

new_id 是新闻在系统中的id

### 修改新闻

#### 请求

- 请求头

```http
POST /notice/news
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "modify",
    "news_id" : "5",
    "title" : "new_title",
    "content" : "new_content",
    "status" :0\1\2,
    "new_type":"校园、社会、竞赛。。。。",
}
```

new_id : 要修改的新闻id



#### 响应

- 响应头

```http
200 OK
Content-Type: application/json
```

- 消息体

```json
{
    "ret": 0,
}
```

ret 为 0 表示修改成功

### 删除新闻

#### 请求

- 请求头

```http
POST /notice/news
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "delete",
    "news_id" : "5",
}
```

new_id : 要删除的新闻id



#### 响应

- 响应头

```http
200 OK
Content-Type: application/json
```

- 消息体

```json
{
    "ret": 0,
}
```

ret 为 0 表示删除成功

### 列出新闻

#### 请求

- 请求头

```django
POST /notice/news
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "list",
    "pagenum":2,
    "pagesize":5,
    "news_type":"新闻类型"
}
```

pagenum:显示的页数；pagesize:每页显示的数据个数；如果为空则默认为1，5

new_type  ： ALL为所有新闻

#### 响应

- 响应头

```
200 OK
Content-Type: application/json
```

- 消息体

```json
{
    "ret": 0,
    "retlist":[
    {
    "new_id":5,
    "title":"**",
    "content":"****",
    "status":1\2\0,
    },{...}
    ]
}
```

ret 为 0 表示列出成功



## 通知

### 添加通知

#### 请求

- 请求头

```http
POST /notice/message
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "add",
    "author_id" : "3",
    "title" : "****",
    "content" : "**************",
    "status" :1,
    "receive_user_id":[2,3,5],
}
```

author_id : 创建者id

title ：通知标题

content ：通知内容

status ：通知状态 0：禁用；1：发布

new_type ：新闻类型根据实际需要填写

receive_user_id：接收者的id



#### 响应

- 响应头

```http
200 OK
Content-Type: application/json
```

- 消息体

```json
{
    "ret": 0,
    "message_id":5,
}
```

ret 为 0 表示添加成功

message_id 是新闻在系统中的id

### 修改通知

#### 请求

- 请求头

```http
POST /notice/message
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "modify",
    "message_id" : "5",
    "title" : "new_title",
    "content" : "new_content",
    "status" :0\1\2,
}
```

new_id : 要修改的新闻id



#### 响应

- 响应头

```http
200 OK
Content-Type: application/json
```

- 消息体

```json
{
    "ret": 0,
}
```

ret 为 0 表示修改成功

### 删除通知

#### 请求

- 请求头

```http
POST /notice/message
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "delete",
    "message_id" : "5",
}
```

new_id : 要删除的新闻id



#### 响应

- 响应头

```http
200 OK
Content-Type: application/json
```

- 消息体

```json
{
    "ret": 0,
}
```

ret 为 0 表示删除成功

### 列出通知

#### 请求

- 请求头

```django
POST /notice/message
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "list",
}
```

根据用户类型列出通知：

管理员-》列出所有通知

教师-》列出名下通知 和 接收到的通知

学生-》列出接收到的通知

#### 响应

- 响应头

```
200 OK
Content-Type: application/json
```

- 消息体

```json
{
    "ret": 0,
    "retlist":[
    {
    "message_id":5,
    "title":"**",
    "content":"****",
    "author_id":5,
    },{...}
    ]
}
```

ret 为 0 表示列出成功









