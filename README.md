# 图匠 - 对话式图像创意室

> **项目名称**： 图匠 —— 对话式图像创意室
>
> **项目性质**： 同济大学软件工程课程项目
>
> **开发团队**：同济大学 锟斤拷



## 1、首页

进入部署网址，首页 URL 为`/Demo`。（此时为未登录状态，未登录不能进入各功能界面）

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/b368223261df91153ff3d52b486f6a0.png" alt="b368223261df91153ff3d52b486f6a0" style="zoom:20%;" />

下拉为模板推荐展示：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/f681d2438f0a243720c9a17624c5d1e.png" alt="f681d2438f0a243720c9a17624c5d1e" style="zoom:20%;" />



## 2、注册登录

### 2.1 进入注册登录界面

点击首页右上角 `LOG IN` 按钮，跳转登录界面。未注册用户需先注册。

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605231800164.png" alt="image-20240605231800164" style="zoom:40%;" />



### 2.2 用户类型说明

系统用户分为普通用户`Normal User`、高级用户`Premium User`和管理员`admin`。

- 普通用户可直接注册；
- 高级用户注册需要填写邀请码`Invite Code`，目前指定邀请码包括`kjk123456`、`kjk654321`、`kjk666888`；
- 管理员不可注册，由开发人员指定，账号为`客服1`，密码为`Service`；



### 2.3 注册登录信息说明

不符合以下规范会出错提示。

- 用户名不可重复；
- 邮箱需符合格式，含@；
- 密码必须包含大写字母、小写字母、数字中的至少两种；



### 2.4 登录系统

#### 2.4.1 `User`用户登录（普通用户和高级用户）

登录成功后进入系统首页，首页三个功能导航进入对应页面：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605150135234.png" alt="image-20240605150135234" style="zoom:20%;" />

#### 2.4.2 `Admin`管理员登录

登录成功后进入管理员界面：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605145052037.png" alt="image-20240605145052037" style="zoom:20%;" />



## 3、图像评估

点击修图，可看到三个图像处理模块，选择“图像评估”：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605163957062.png" alt="image-20240605163957062" style="zoom:20%;" />

点击上传图片，选择一张想要修改的图片：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605165347784-17175776398452.png" alt="image-20240605165347784-17175776398452" style="zoom:20%;" />

输入指令，询问图匠对这张图片的美学评估：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605165849597.png" alt="image-20240605165849597" style="zoom:20%;" />

稍等片刻，图匠给出 `IAA`（Image Artificial Assessment，图像质量评估）评分和内容理解：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605170031725.png" alt="image-20240605170031725" style="zoom:20%;" />

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605170052190.png" alt="image-20240605170052190" style="zoom:20%;" />

继续追问图片有什么可以改进的地方，图匠给出回答：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605170413276.png" alt="image-20240605170413276" style="zoom:20%;" />

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605170427386.png" alt="image-20240605170427386" style="zoom:20%;" />

可以移除图片，上传新的图片进行问答：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605170619501.png" alt="image-20240605170619501" style="zoom:20%;" />

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240605170654809.png" alt="image-20240605170654809" style="zoom:40%;" />

通过点击“清空历史”来清空会话内容：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606000103640.png" alt="image-20240606000103640" style="zoom:20%;" />





## 4、简单修图

简单修图基于 OpenCV 实现，不使用指令修改图像模型推理，缩短处理速度的同时为降低能源消耗、减少碳排放与碳中和做出贡献。

### 4.1 进入简单修图页面

点击侧边栏修图 $\rightarrow$ 简单修图，进入界面。 

点击上方选择栏的不同选项，如图像色彩、图像变换等，可以查看对应分类的图像处理。

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606000919189.png" alt="image-20240606000919189" style="zoom: 25%;" />

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606001039094.png" alt="image-20240606001039094" style="zoom: 25%;" />

### 4.2 选择修图方法并上传图片

鼠标悬浮在某个修图方法上，会出现立即使用按钮，点击按钮进行图片上传：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606001141770.png" alt="image-20240606001141770" style="zoom:25%;" />

稍等片刻，会显示处理后的图像：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606001515097.png" alt="image-20240606001515097" style="zoom:25%;" />

点击保存，可将图片保存至草稿箱。



### 4.3 查看保存的处理后图片

点击侧边栏的个人选项，选择草稿箱，可查看刚刚保存的图片：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606001555321.png" alt="image-20240606001555321" style="zoom:25%;" />

所有简单修图类型效果展示 见 **附录**

## 5、智能修图

### 5.1 对话修图

点击对话修图，跳转到对话修图界面：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606000148559.png" alt="image-20240606000148559" style="zoom:20%;" />

上传图片，可以根据图像评估给出的修改意见或自己的想法，输入指令，进行AI修图：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606000208666.png" alt="image-20240606000208666" style="zoom:20%;" />

注意每次提交的图片都是基于上次的结果的。

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606000239962.png" alt="image-20240606000239962" style="zoom:20%;" />

风景照修图效果更佳 :smiley:：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606000331859.png" alt="image-20240606000331859" style="zoom:20%;" />

同“图像评估”，可以移除图片、清空历史。请注意每一次页面跳转，“对话修图”模块都会清空历史。



### 5.2 图像生成

进入对话修图界面，输入一段生成图片的指令（含有关键词 `生成` 或 `Generate`），即可调用百度文心大模型实时生成图像：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/7d134378cf56cfbb2c79770f55de021.png" alt="7d134378cf56cfbb2c79770f55de021" style="zoom:20%;" />

生成结果可以进一步使用指令修图进行修改。



## 6、分享广场

### 6.1 展示帖子

#### 6.1.1 展示所有用户公开发送的帖子

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606002042743.png" alt="image-20240606002042743" style="zoom: 20%;" />

#### 6.1.2 展示关注用户发送的帖子

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606002140249.png" alt="image-20240606002140249" style="zoom:20%;" />

### 6.2 搜索

在搜索栏中输入关键词，可以进行帖子的搜索和用户的搜索：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606002253141.png" alt="image-20240606002253141" style="zoom:20%;" />

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606002305886.png" alt="image-20240606002305886" style="zoom:20%;" />

### 6.3 帖子详情

#### 6.3.1 评论

在帖子右下方输入栏输入评论：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606002346556.png" alt="image-20240606002346556" style="zoom:20%;" />

点击发送，评论会显示在评论中：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606002405022.png" alt="image-20240606002405022" style="zoom:20%;" />

#### 6.3.2 点赞与收藏

点击爱心图标可以点赞这一篇帖子，点击五角星图标可以收藏这一篇帖子：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606002450565.png" alt="image-20240606002450565" style="zoom:20%;" />

当已经收藏以及点赞的时候，图标会显示为实心。此时，如果再次点击图标，则会取消收藏，取消点赞。

#### 6.3.3 关注用户

点击发帖者用户名旁的关注按钮，即可关注这一名发帖者。

再次点击已关注/互相关注按钮，会出现取消关注的确认弹窗。在此弹窗中，点击确认即可取关这一名发帖者。

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606002552761.png" alt="image-20240606002552761" style="zoom:20%;" />

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606002603389.png" alt="image-20240606002603389" style="zoom:20%;" />

#### 6.3.4 浏览发帖者的主页

点击发帖者的头像(下图绿框)，可以浏览发帖者的主页。

发帖者的主页显示了他的相关个人资料以及发过的帖子。

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606002712899.png" alt="image-20240606002712899" style="zoom:20%;" />

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606002724867.png" alt="image-20240606002724867" style="zoom:20%;" />

点击下图绿框中的对话按钮，可以跳转至与其的对话窗口：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606011842329.png" alt="image-20240606011842329" style="zoom:20%;" />

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606011904243.png" alt="image-20240606011904243" style="zoom:20%;" />

### 6.4 发布帖子

点击空白的方形区域，即可从本地选中图片上传：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606012012740.png" alt="image-20240606012012740" style="zoom:20%;" />

对于已经上传的图片，鼠标移动在其上时，可以选择查看大图或者删除该图片。

图片下方可以输入帖子的标题和内容。

一个帖子可以上传 0~5 张图片，标题和内容不得为空。

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606012139272.png" alt="image-20240606012139272" style="zoom:20%;" />



## 7、个人中心

### 7.1 个人资料卡

#### 7.1.1 资料卡展示

显示基本个人资料，包括用户名，头像，id号，权限(高级/普通)， 简介，性别，关注列表，粉丝列表，获赞数，被收藏数：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606012351164.png" alt="image-20240606012351164" style="zoom:20%;" />

#### 7.1.2 资料编辑

点击头像旁的编辑按钮，可以进入个人资料编辑页面。

点击头像，上传并预览头像。

所有资料都可编辑 (用户名不能与其他用户重名)。

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606012440879.png" alt="image-20240606012440879" style="zoom:20%;" />

#### 7.1.3 关注和粉丝列表

点击下图绿框中的关注/粉丝，可以展示用户的关注列表和粉丝列表：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606012523137.png" alt="image-20240606012523137" style="zoom:20%;" />

关注列表展示，点击"已关注"按钮，进行相应操作可以实现取消操作：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606012550696.png" alt="image-20240606012550696" style="zoom:20%;" />

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606012600831.png" alt="image-20240606012600831" style="zoom:20%;" />

粉丝列表展示，点击关注按钮，可以进行回关：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606012623481.png" alt="image-20240606012623481" style="zoom:20%;" />



### 7.2 个人收藏

之前在分享广场收藏的帖子会在个人收藏模块展示。点击帖子，同样会显示帖子的详情等：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606012705697.png" alt="image-20240606012705697" style="zoom:20%;" />

### 7.3 个人笔记

自己发过的笔记会在个人中心的笔记栏中显示。点击删除按钮可以进行帖子的删除。

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606012800295.png" alt="image-20240606012800295" style="zoom:20%;" />

### 7.4 草稿箱

用户使用简单修图、对话修图的所有图片都会被存储在草稿箱中：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606015652471.png" alt="image-20240606015652471" style="zoom:25%;" />

点击任意一张草稿箱的图片，可以一键发布动态至广场页面：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606015743000.png" alt="image-20240606015743000" style="zoom:25%;" />



### 7.5 一键使用模板

对于所有从草稿箱发布的动态，自动存储其修图 prompt，可以在动态详情界面一键使用模板进行修图：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606015910106.png" alt="image-20240606015910106" style="zoom:25%;" />

快捷上传图片，确认后自动应用模板进行修图：

<img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/image-20240606015941967.png" alt="image-20240606015941967" style="zoom:25%;" />



## 附录

### 简单修图类型

| 修图方法                                               | 修前                                                         | 修后                                                         |
| ------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Hue                                                    | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Hue.png" alt="Hue" style="zoom:25%;" /> |
| Saturation                                             | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Saturation.png" alt="Saturation" style="zoom:25%;" /> |
| Value                                                  | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Value.png" alt="Value" style="zoom:25%;" /> |
| Fixed Hue                                              | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Fixed Hue.png" alt="Fixed Hue" style="zoom:25%;" /> |
| Fixed Saturation                                       | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Fixed Saturation.png" alt="Fixed Saturation" style="zoom:25%;" /> |
| Fixed Value                                            | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Fixed Value.png" alt="Fixed Value" style="zoom:25%;" /> |
| Fixed Hue & Saturation                                 | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Fixed Hue & Saturation.png" alt="Fixed Hue & Saturation" style="zoom:25%;" /> |
| Fixed Hue & Value                                      | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Fixed Hue & Value.png" alt="Fixed Hue & Value" style="zoom:25%;" /> |
| Fixed Saturation & Value                               | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Fixed Saturation & Value.png" alt="Fixed Saturation & Value" style="zoom:25%;" /> |
| eroded                                                 | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/eroded.png" alt="eroded" style="zoom:25%;" /> |
| dilated 3 times                                        | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/dilated 3 times.png" alt="dilated 3 times" style="zoom:25%;" /> |
| eroded 7x7                                             | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/eroded 7x7.png" alt="eroded 7x7" style="zoom:25%;" /> |
| eroded 3 times                                         | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/eroded 3 times.png" alt="eroded 3 times" style="zoom:25%;" /> |
| closed                                                 | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/closed.png" alt="closed" style="zoom:25%;" /> |
| opened                                                 | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/opened.png" alt="opened" style="zoom:25%;" /> |
| Closed 2 Opened                                        | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Closed 2 Opened.png" alt="Closed 2 Opened" style="zoom:25%;" /> |
| Opened 2 Closed                                        | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Opened 2 Closed-171757388316143.png" alt="Opened 2 Closed" style="zoom:25%;" /> |
| Gradient or Edge                                       | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Gradient or Edge.png" alt="Gradient or Edge" style="zoom:25%;" /> |
| Gradient or Edge 2 Thresh Binary or Edge               | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Gradient or Edge 2 Thresh Binary or Edge.png" alt="Gradient or Edge 2 Thresh Binary or Edge" style="zoom:25%;" /> |
| 7x7 Black Top-hat                                      | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/7x7 Black Top-hat.png" alt="7x7 Black Top-hat" style="zoom:25%;" /> |
| 7x7 Black Top-hat 2 Thresh Binary or Edge              | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/7x7 Black Top-hat 2 Thresh Binary or Edge.png" alt="7x7 Black Top-hat 2 Thresh Binary or Edge" style="zoom:25%;" /> |
| 7x7 Black Top-hat 2 Closed                             | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/7x7 Black Top-hat 2 Closed.png" alt="7x7 Black Top-hat 2 Closed" style="zoom:25%;" /> |
| Mean filtered (5x5)                                    | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Mean filtered (5x5).png" alt="Mean filtered (5x5)" style="zoom:25%;" /> |
| Mean filtered (9x9)                                    | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Mean filtered (9x9).png" alt="Mean filtered (9x9)" style="zoom:25%;" /> |
| Gaussian filtered Image (9x9)                          | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Gaussian filtered Image (9x9).png" alt="Gaussian filtered Image (9x9)" style="zoom:25%;" /> |
| resize CUBIC 0.25                                      | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/resize CUBIC 0.25.png" alt="resize CUBIC 0.25" style="zoom:25%;" /> |
| resize NEAREST x4                                      | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/resize NEAREST x4.png" alt="resize NEAREST x4" style="zoom:25%;" /> |
| resize LINEAR x4                                       | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/resize LINEAR x4.png" alt="resize LINEAR x4" style="zoom:25%;" /> |
| Median filtered                                        | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Median filtered.png" alt="Median filtered" style="zoom:25%;" /> |
| Sobel X                                                | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Sobel X.png" alt="Sobel X" style="zoom:25%;" /> |
| Sobel Y                                                | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Sobel Y.png" alt="Sobel Y" style="zoom:25%;" /> |
| abs Sobel X+Y                                          | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="C:/Users/h1585/Desktop/%E7%AE%80%E5%8D%95%E4%BF%AE%E5%9B%BE%E8%AF%B4%E6%98%8E.assets/abs%20Sobel%20X+Y.png" alt="abs Sobel X+Y" style="zoom:25%;" /> |
| cv2.convertScaleAbs Sobel X+Y                          | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="C:/Users/h1585/Desktop/%E7%AE%80%E5%8D%95%E4%BF%AE%E5%9B%BE%E8%AF%B4%E6%98%8E.assets/cv2.convertScaleAbs%20Sobel%20X+Y.png" alt="cv2.convertScaleAbs Sobel X+Y" style="zoom:25%;" /> |
| Sobel X (7x7)                                          | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Sobel X (7x7).png" alt="Sobel X (7x7)" style="zoom:25%;" /> |
| uint8 sobel_1                                          | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/uint8 sobel_1.png" alt="uint8 sobel_1" style="zoom:25%;" /> |
| uint8 sobel_2                                          | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/uint8 sobel_2.png" alt="uint8 sobel_2" style="zoom:25%;" /> |
| int8 sobel_1                                           | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/int8 sobel_1.png" alt="int8 sobel_1" style="zoom:25%;" /> |
| int8 sobel_2                                           | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/int8 sobel_2.png" alt="int8 sobel_2" style="zoom:25%;" /> |
| Binary Sobel (low)  cv2.threshold uint8_sobel_1        | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Binary Sobel (low)  cv2.threshold uint8_sobel_1.png" alt="Binary Sobel (low)  cv2.threshold uint8_sobel_1" style="zoom:25%;" /> |
| Binary Sobel (low)  cv2.threshold uint8_sobel_2        | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Binary Sobel (low)  cv2.threshold uint8_sobel_2.png" alt="Binary Sobel (low)  cv2.threshold uint8_sobel_2" style="zoom:25%;" /> |
| Binary Sobel Image (high)  cv2.threshold uint8_sobel_1 | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Binary Sobel Image (high)  cv2.threshold uint8_sobel_1.png" alt="Binary Sobel Image (high)  cv2.threshold uint8_sobel_1" style="zoom:25%;" /> |
| Binary Sobel Image (high)  cv2.threshold uint8_sobel_2 | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Binary Sobel Image (high)  cv2.threshold uint8_sobel_2-171757414631970.png" alt="Binary Sobel Image (high)  cv2.threshold uint8_sobel_2" style="zoom:25%;" /> |
| cv2.addWeighted abs                                    | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/cv2.addWeighted abs.png" alt="cv2.addWeighted abs" style="zoom:25%;" /> |
| Rescaled                                               | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Rescaled.png" alt="Rescaled" style="zoom:25%;" /> |
| cv2.subtract                                           | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/cv2.subtract.png" alt="cv2.subtract" style="zoom:25%;" /> |
| cv2.subtract gauss15 - gauss05                         | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/cv2.subtract gauss15 - gauss05.png" alt="cv2.subtract gauss15 - gauss05" style="zoom:25%;" /> |
| cv2.subtract gauss22 - gauss20                         | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/cv2.subtract gauss22 - gauss20.png" alt="cv2.subtract gauss22 - gauss20" style="zoom:25%;" /> |
| Canny Contours                                         | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Canny Contours.png" alt="Canny Contours" style="zoom:25%;" /> |
| Canny Contours Gray                                    | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Canny Contours Gray.png" alt="Canny Contours Gray" style="zoom:25%;" /> |
| Contours with RETR_LIST                                | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Contours with RETR_LIST.png" alt="Contours with RETR_LIST" style="zoom:25%;" /> |
| White Balance 1                                        | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/White Balance 1.png" alt="White Balance 1" style="zoom:25%;" /> |
| White Balance 2                                        | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/White Balance 2.png" alt="White Balance 2" style="zoom:25%;" /> |
| White Balance 3                                        | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/White Balance 3.png" alt="White Balance 3" style="zoom:25%;" /> |
| Single Scale Retinex 1                                 | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Single Scale Retinex 1.png" alt="Single Scale Retinex 1" style="zoom:25%;" /> |
| Single Scale Retinex 2                                 | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Single Scale Retinex 2.png" alt="Single Scale Retinex 2" style="zoom:25%;" /> |
| Multi Scale Retinex 1                                  | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Multi Scale Retinex 1.png" alt="Multi Scale Retinex 1" style="zoom:25%;" /> |
| Multi Scale Retinex 2                                  | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Multi Scale Retinex 2.png" alt="Multi Scale Retinex 2" style="zoom:25%;" /> |
| Multi Scale Retinex With Color Restoration 1           | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Multi Scale Retinex With Color Restoration 1.png" alt="Multi Scale Retinex With Color Restoration 1" style="zoom:25%;" /> |
| Automatic White Balance                                | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Origin.png" alt="Origin" style="zoom:25%;" /> | <img src="http://henry-typora.oss-cn-beijing.aliyuncs.com/img/Automatic White Balance.png" alt="Automatic White Balance" style="zoom:25%;" /> |



