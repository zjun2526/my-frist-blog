# Django Girls



## Python



### 列表

- 排序(大到小)

```shell
lottery.sort()
```

- 倒序

```shell
lottery.recerse()
```

- 末尾追加

```shell
lottery.append(199)
```

- 删除元素 pop(index)

```shell
lottery.pop(0)
```



### 字典

- 查找 key 获取 value
- add

```shell
participant['favorite_language'] = 'Python'
```

- 删除 pop('key')
- 修改 

```shell
participant['country'] = 'US'
```



### Range

- Range 函数产生一个列表数字
- 半开区间，包含第一个值，但不包含最后一个值



## Django 是什么



### 项服务器请求一个网站，发生什么？

#### UrlResolver URL 解析器

- URL 统一资源定位器
- URLResolver 接受一个模式列表，逐个匹配URL，如果匹配上，Django会将请求传递给相关的函数（视图函数）
- 视图函数 操作数据库，然后生成响应发送给用户



### Django 模型

#### 对象

- 面向对象编程：思想是与其用无聊的一连串的程序指令方式写程序，不如为失误建立模型，然后定义他们怎样相互交互。
- 对象：属性和操作的集合。思想是用包含属性的代码来描述真实的东西（对象属性）和操作（方法）
- 博客帖子模型：文本（title、text），作者（author），时间（created_date、published_date），发布(方法 publish)



#### Django 模型

- Django里的模型是一种特殊的对象，它保存在数据库中。数据库是数据的集合。存储有关用户、博客文章等信息的地方
- 数据库中的模型看作是电子表格中的 列（字段） 和 行（数据）



#### 创建应用程序

#### 创建一个博客文章模型

