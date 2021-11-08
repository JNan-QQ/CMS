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
POST /sign
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
    "realname":"管理员",
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
POST /sign
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
POST /account
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "register",
    "username" : "小明",
    "password" : "123456ll",
    "usertype" :100
}
```

usertype未账号类型：100、1000

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
POST /account
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```json
{
    "action" : "add",
    "username" : "小明",
    "password" : "123456",
    "usertype" :100
}
```

password默认为123456

usertype未账号类型：1、100、1000

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
POST /account
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
POST /account
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
POST /account
Cookie: sessionid=<sessionid数值>
Content-Type: application/json
```

- 消息体

为json格式

```
{
    "action" : "list",
}
```

仅管理员可以操作

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



