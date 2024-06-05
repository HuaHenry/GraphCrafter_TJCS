# # import sys
# # import os
# # from flask import Flask, jsonify, request, render_template, url_for, send_from_directory
# # from flask_cors import CORS, cross_origin

# # from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
# # from sqlalchemy import func, cast, String, desc
# # from sqlalchemy.orm import relationship
# # from flask_bcrypt import Bcrypt     # 密码加密

# # from flask_socketio import SocketIO, emit, join_room
# # from datetime import datetime

# # # 用于数据库一键初始化 by hzq
# # from flask_migrate import Migrate


# # # 后端上传阿里云图床
# # import oss2
# # import os
# # from oss2.credentials import EnvironmentVariableCredentialsProvider

# # # 简单图像处理
# # import io
# # import numpy as np
# # import cv2
# # from simple_image_process.image_filtering import show_filtering
# # from simple_image_process.image_outline import show_outline
# # from simple_image_process.image_transformation import show_transformation
# # from simple_image_process.image_color import show_hsv
# # from simple_image_process.image_enhancement import show_enhancement

# # # 防止通信报错 by zyp
# # # import locale
# # # locale.setlocale(locale.LC_CTYPE,"chinese")

# # WIN = sys.platform.startswith('win')
# # if WIN:  # 如果是 Windows 系统，使用三个斜线
# #     prefix = 'sqlite:///'
# # else:  # 否则使用四个斜线
# #     prefix = 'sqlite:////'

# # app = Flask(__name__, static_url_path='/',
# #             static_folder='./../frontend/dist', template_folder='./../frontend/dist')
# # socketio = SocketIO(app, cors_allowed_origins="http://localhost:5173")

# # # 创建数据库
# # app.config['SQLALCHEMY_DATABASE_URI'] = prefix + \
# #     os.path.join(app.root_path, 'data.db')
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# # db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app
# # migrate = Migrate(app, db)


# # # 阿里云OSS相关信息
# # OSS_ACCESS_KEY_ID = 'LTAI5tR1c1uhFRfWxjq8BWT4'
# # OSS_ACCESS_KEY_SECRET = 'BdN5OIEdet7IO6KWOq7TJiivHOsC5B'
# # OSS_ENDPOINT = 'oss-cn-beijing.aliyuncs.com'
# # OSS_BUCKET_NAME = 'graphcrafter'
# # auth = oss2.Auth(OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET)
# # bucket = oss2.Bucket(auth, OSS_ENDPOINT, OSS_BUCKET_NAME)
# # bcrypt = Bcrypt(app)


# # class User(db.Model):  # 用户
# #     id = db.Column(db.Integer, primary_key=True)  # 主键，账号
# #     name = db.Column(db.String(20))  # 名字
# #     password = db.Column(db.String(20))  # 密码
# #     photo = db.Column(db.String(60))  # 头像
# #     email = db.Column(db.String(254))  # 邮箱
# #     age = db.Column(db.Integer)  # 年龄
# #     sex = db.Column(db.Boolean)  # 性别，1是男0是女
# #     is_admin = db.Column(db.Boolean, default=False)
# #     is_premium = db.Column(db.Boolean, default=False)
# #     description = db.Column(db.String(100))  # 一句话介绍自己
# #     status = db.Column(db.Boolean)  # 是否正常 0正常 1被封


# # class Post(db.Model):  # 帖子
# #     id = db.Column(db.Integer, primary_key=True)  # 主键
# #     author_id = db.Column(db.Integer)      # 作者id
# #     date = db.Column(db.DateTime)     # 日期
# #     picture1 = db.Column(db.String(60))     # 图片1，默认为封面
# #     picture2 = db.Column(db.String(60))     # 图片2
# #     picture3 = db.Column(db.String(60))     # 图片3
# #     picture4 = db.Column(db.String(60))     # 图片4
# #     picture5 = db.Column(db.String(60))     # 图片5
# #     title = db.Column(db.String(60))     # 标题
# #     body = db.Column(db.Text)  # 正文
# #     model = db.Column(db.Integer)  # 模型参数id
# #     status = db.Column(db.Boolean)  # 状态，0是正常 1是被禁


# # class Comment(db.Model):  # 评论
# #     id = db.Column(db.Integer, primary_key=True)  # 主键
# #     date = db.Column(db.DateTime)     # 日期
# #     content = db.Column(db.Text)  # 正文
# #     author_id = db.Column(db.Integer)      # 作者id
# #     post_id = db.Column(db.Integer)      # 文章id


# # class Like(db.Model):  # 点赞
# #     id = db.Column(db.Integer, primary_key=True)  # 主键
# #     date = db.Column(db.DateTime)     # 日期
# #     author_id = db.Column(db.Integer)      # 点赞者id
# #     post_id = db.Column(db.Integer)      # 文章id


# # class Collect(db.Model):  # 收藏
# #     id = db.Column(db.Integer, primary_key=True)  # 主键
# #     date = db.Column(db.DateTime)     # 日期
# #     user_id = db.Column(db.Integer)      # 作者id
# #     post_id = db.Column(db.Integer)      # 文章id


# # class Follow(db.Model):  # 关注
# #     id = db.Column(db.Integer, primary_key=True)  # 主键
# #     follower_id = db.Column(db.Integer)      # 粉丝id
# #     followed_id = db.Column(db.Integer)      # 被关注者id
# #     status = db.Column(db.Integer)      # 关注状态,0表示单独关注，1表示互相关注


# # class FeedBack(db.Model):  # 用户反馈
# #     id = db.Column(db.Integer, primary_key=True)  # 主键
# #     date = db.Column(db.DateTime)     # 日期
# #     user_id = db.Column(db.Integer)      # 用户id
# #     content = db.Column(db.Text)  # 正文
# #     processed = db.Column(db.Boolean)  # 是否已处理
# #     back_content = db.Column(db.Text)  # 反馈内容


# # class ModifyHistory(db.Model):  # 修图历史
# #     id = db.Column(db.Integer, primary_key=True)  # 主键
# #     date = db.Column(db.DateTime)     # 日期
# #     user_id = db.Column(db.Integer)      # 用户id
# #     pic_before = db.Column(db.String(60))     # 修改前图片
# #     pic_after = db.Column(db.String(60))     # 修改后图片
# #     prompt = db.Column(db.Text)  # 提示
# #     model_id = db.Column(db.Integer)  # 模型参数


# # class Message(db.Model):  # 单条消息记录
# #     __tablename__ = 'message'
# #     id = db.Column(db.Integer, primary_key=True)  # 主键
# #     type = db.Column(db.String(60))  # 消息的类型
# #     time = db.Column(db.DateTime)  # 发送时间
# #     show_time = db.Column(db.Boolean)  # 该条消息的时间是否显示
# #     content = db.Column(db.Text)  # 内容
# #     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 发送的用户id
# #     chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))  # 关联Chat模型的id


# # class Chat(db.Model):  # 会话
# #     __tablename__ = 'chat'
# #     id = db.Column(db.Integer, primary_key=True)  # 主键
# #     sender = db.Column(db.Integer)  # 发起者的id
# #     receiver = db.Column(db.Integer)  # 接收者的id
# #     unread_sender = db.Column(db.Boolean)  # 发起者是否已经阅读
# #     unread_receiver = db.Column(db.Boolean)  # 接收者是否已经阅读
# #     last_time = db.Column(db.DateTime)  # 最后一条消息的时间
# #     messages = relationship("Message", backref="chat",
# #                             cascade="all, delete-orphan")  # 包含的消息 一对多


# # class Draft(db.Model):  # 草稿箱
# #     __tablename__ = 'Draft'
# #     id = db.Column(db.Integer, primary_key=True)  # 主键
# #     date = db.Column(db.DateTime)     # 日期
# #     user_id = db.Column(db.Integer)      # 用户id
# #     picture = db.Column(db.String(60))     # 图片
# #     label = db.Column(db.Text)  # 标签


# # class Picture(db.Model):  # 图片
# #     id = db.Column(db.String(60), primary_key=True)  # 主键，即路由
# #     prompt = db.Column(db.Text)     # 修图的prompt，没有修图时为空
# #     Ptype = db.Column(db.Integer)   # 图片类型，0是原图，1是简单修图，2是对话修图


# # class Opencv(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)  # 主键
# #     description = db.Column(db.Text)  # 正文
# #     image = db.Column(db.String(60))
# #     type = db.Column(db.String(10))
# #     code = db.Column(db.Text)  # 代码


# # # app = Flask(__name__)
# # app.config.from_object(__name__)


# # CORS(app, resources={r'/*': {'origins': '*'}})


# # @app.route('/api/ping', methods=['GET'])
# # def ping_pong():
# #     return jsonify('pong!')


# # @app.route('/')
# # def index():
# #     return render_template('index.html')


# # @app.route('/<path:fallback>')
# # def fallback(fallback):       # Vue Router 的 mode 为 'hash' 时可移除该方法
# #     if fallback.startswith('css/') or fallback.startswith('js/')\
# #             or fallback.startswith('img/') or fallback == 'favicon.ico':
# #         return app.send_static_file(fallback)
# #     else:
# #         return app.send_static_file('index.html')


# # # 登录
# # @app.route('/login', methods=['POST', 'GET'])
# # @cross_origin(supports_credentials=True)
# # def login():
# #     data = request.form
# #     username = data.get('username')
# #     password = data.get('password')
# #     user_type = data.get('userType')
# #     print(username, password, user_type)

# #     # 查询用户（仅根据用户名查询）
# #     user = User.query.filter_by(name=username).first()

# #     # 加密密码匹配
# #     if user and bcrypt.check_password_hash(user.password, password):
# #         if user_type == 'admin' and not user.is_admin:
# #             return jsonify({'status': 'error', 'message': 'Unauthorized access for admin'}), 402
# #         return jsonify({'status': 'success', 'message': 'Login successful', "user_id": user.id}), 200
# #     else:
# #         return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401


# # # 注册
# # @app.route('/register', methods=['POST', 'GET'])
# # @cross_origin(supports_credentials=True)
# # def register():
# #     try:
# #         if request.method == 'POST':
# #             # 用户注册
# #             latest_user = User.query.order_by(User.id.desc()).first()
# #             id = latest_user.id + 1 if latest_user else 1
# #             username = request.form['username']
# #             password = request.form['password']
# #             email = request.form['email']
# #             user_type = request.form['userType']
# #             invite_code = None
# #             if user_type == "premium":
# #                 invite_code = request.form['inviteCode']
# #                 if invite_code not in ["kjk123456", "kjk654321", "kjk666888"]:
# #                     print("invalid")
# #                     return "error: invite code invalid", 401

# #             # 加密密码
# #             hashed_password = bcrypt.generate_password_hash(
# #                 password).decode('utf-8')

# #             default_avatar_url = 'http://graphcrafter.oss-cn-beijing.aliyuncs.com/avatars/1-default.webp'
# #             user_now = User(id=id, name=username, password=hashed_password, email=email, is_premium=(
# #                 user_type == 'premium'), photo=default_avatar_url)
# #             # 用户名已占用
# #             users = User.query.filter_by(name=username).all()
# #             if users:
# #                 return "error: username already taken", 400
# #             # 用户名未占用，可注册
# #             db.session.add(user_now)
# #             db.session.commit()
# #             return 'success', 200
# #         return '', 405
# #     except Exception as e:
# #         # 捕获异常并记录错误信息
# #         app.logger.error(f"Error during registration: {e}")
# #         return "Internal Server Error", 500


# # # @app.route('/api/opencvimages')
# # # def get_images():

# # #     images = Opencv.query.all()
# # #     response = [{
# # #         'id': img.id,
# # #         'description': img.description,
# # #         'image': img.image,
# # #         'code': img.code,
# # #     } for img in images]
# # #     return jsonify(response)


# # @app.route('/api/opencvimages', methods=['GET'])
# # def get_images():
# #     opencv_imgs = Opencv.query.all()
# #     print(opencv_imgs)

# #     ids = []
# #     pictures = []
# #     descriptions = []
# #     codes = []
# #     types = []

# #     for opencv_img in opencv_imgs:
# #         ids.append(opencv_img.id)
# #         pictures.append(opencv_img.image)
# #         descriptions.append(opencv_img.description)
# #         codes.append(opencv_img.code)
# #         types.append(opencv_img.type)

# #     response_json = jsonify({
# #         'ids': ids,
# #         'pictures': pictures,
# #         'descriptions': descriptions,
# #         'codes': codes,
# #         'types': types,
# #     })

# #     return response_json


# # # 示例用户资料
# # @app.route('/api/user/<int:user_id>', methods=['GET'])
# # def get_user_profile(user_id):
# #     user = User.query.get(user_id)
# #     if user:
# #         return jsonify({
# #             'id': user.id,
# #             'name': user.name,
# #             'photo': user.photo,
# #             'email': user.email,
# #             'age': user.age,
# #             'sex': user.sex,
# #             'is_premium': user.is_premium,
# #             # 'senior': user.senior,
# #             'bio': user.description
# #         })
# #     return jsonify({'error': 'User not found'}), 404


# # # 显示被点赞数量
# # def get_total_likes_count_for_user(user_id):
# #     # Query to count unique likes per post for a specific author
# #     likes_count = db.session.query(db.func.count(db.distinct(Like.id)))\
# #                     .join(Post, Post.id == Like.post_id)\
# #                     .filter(Post.author_id == user_id)\
# #                     .scalar()
# #     return likes_count

# # # 显示被收藏数量


# # def get_favorites_count_for_user(user_id):
# #     # Query to count unique likes per post for a specific author
# #     favorites_count = db.session.query(db.func.count(db.distinct(Collect.id)))\
# #         .join(Post, Post.id == Collect.post_id)\
# #         .filter(Post.author_id == user_id)\
# #         .scalar()
# #     return favorites_count


# # # 获取指定作者的帖子的获赞与收藏总数
# # @app.route('/api/user-stats/<int:user_id>')
# # def user_stats(user_id):
# #     likes_count = get_total_likes_count_for_user(user_id)
# #     favorites_count = get_favorites_count_for_user(
# #         user_id)  # Assuming you implement this
# #     return jsonify({
# #         'likes': likes_count,
# #         'favorites': favorites_count
# #     })


# # # 获取关注和粉丝数量
# # @app.route('/api/user/<int:user_id>/counts')
# # def get_follow_counts(user_id):
# #     # Count how many people the user is following
# #     following_count = Follow.query.filter_by(follower_id=user_id).count()

# #     # Count how many followers the user has
# #     followers_count = Follow.query.filter_by(followed_id=user_id).count()

# #     return jsonify({
# #         'following_count': following_count,
# #         'followers_count': followers_count
# #     })


# # # 得到我follow的人的列表
# # @app.route('/api/followings/<int:user_id>')
# # def get_followings(user_id):
# #     # Fetching all users that the given user_id is following
# #     followings = Follow.query.join(User, Follow.followed_id == User.id).filter(
# #         Follow.follower_id == user_id).all()

# #     # Preparing the data to return
# #     following_list = []
# #     for following in followings:
# #         user = User.query.get(following.followed_id)

# #         # Counting the followers of each followed user
# #         followers_count = Follow.query.filter_by(followed_id=user.id).count()

# #         # Counting the posts for each followed user
# #         posts_count = Post.query.filter_by(
# #             author_id=user.id, status=False).count()  # only counting active posts

# #         following_list.append({
# #             'id': user.id,
# #             'name': user.name,
# #             'avatar': user.photo,  # Assuming 'photo' is the correct field name for the user's avatar
# #             'followers': followers_count,
# #             'posts': posts_count
# #         })

# #     return jsonify({'followings': following_list})


# # # 得到我follow的人的列表
# # @app.route('/api/followers/<int:user_id>')
# # def get_followers(user_id):
# #     # Fetching all users that are following the given user_id
# #     followers = Follow.query.join(User, Follow.follower_id == User.id).filter(
# #         Follow.followed_id == user_id).all()

# #     # Preparing the data to return
# #     follower_list = []
# #     for follower in followers:
# #         user = User.query.get(follower.follower_id)

# #         followers_count = Follow.query.filter_by(followed_id=user.id).count()

# #         # Counting the active posts of this follower
# #         posts_count = Post.query.filter_by(
# #             author_id=user.id, status=False).count()

# #         follower_list.append({
# #             'id': user.id,
# #             'name': user.name,
# #             'avatar': user.photo,
# #             'followers': followers_count,
# #             'posts': posts_count
# #         })

# #     return jsonify({'followers': follower_list})

# # ###################################################################################################################################################################################################################################################################################
# # # 获取用户收藏


# # @cross_origin()
# # @app.route('/api/collection/<int:user_id>', methods=['GET'])
# # def get_collection(user_id):
# #     print(user_id, type(user_id))
# #     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
# #     collections = db.session.query(
# #         Post.picture1,
# #         Post.title,
# #         User.name,
# #         User.photo,
# #         func.count(Like.id).label('like'),
# #         Post.id
# #     ).join(Collect, Post.id == Collect.post_id).join(User, Post.author_id == User.id).outerjoin(Like, Post.id == Like.post_id).filter(Collect.user_id == user_id).group_by(Post.picture1, Post.title, User.name, User.photo).all()
# #     pictures = []
# #     titles = []
# #     authors = []
# #     avatars = []
# #     likes = []
# #     ids = []
# #     for collection in collections:
# #         pictures.append(collection[0])
# #         titles.append(collection[1])
# #         authors.append(collection[2])
# #         avatars.append(collection[3])
# #         likes.append(collection[4])
# #         ids.append(collection[5])
# #     response_json = jsonify({
# #         'pictures': pictures,
# #         'titles': titles,
# #         'authors': authors,
# #         'avatars': avatars,
# #         'likes': likes,
# #         'ids': ids
# #     })
# #     return response_json
# #     # return jsonify({'error': 'collect not found'}), 404

# # # 获取个人笔记


# # @cross_origin()
# # @app.route('/api/note/<int:user_id>', methods=['GET'])
# # def get_note(user_id):
# #     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
# #     # collections=db.session.query(
# #     #     Post.picture1,
# #     #     Post.title,
# #     #     User.name,
# #     #     User.photo,
# #     #     func.count(Like.id).label('like')
# #     # ).join(Collect, Post.id == Collect.post_id).join(User, Post.author_id == User.id).outerjoin(Like, Post.id == Like.post_id).filter(Collect.user_id == 1).group_by(Post.picture1, Post.title, User.name, User.photo).all()
# #     # 构建查询
# #     collections = db.session.query(
# #         Post.picture1,
# #         Post.title,
# #         User.name,
# #         User.photo,
# #         func.count(Like.id).label('like'),
# #         Post.id
# #     ).join(User, Post.author_id == User.id).filter(User.id == user_id).outerjoin(Like, Post.id == Like.post_id).group_by(Post.picture1, Post.title, User.name, User.photo).all()
# #     pictures = []
# #     titles = []
# #     authors = []
# #     avatars = []
# #     likes = []
# #     ids = []
# #     for collection in collections:
# #         pictures.append(collection[0])
# #         titles.append(collection[1])
# #         authors.append(collection[2])
# #         avatars.append(collection[3])
# #         likes.append(collection[4])
# #         ids.append(collection[5])
# #     response_json = jsonify({
# #         'pictures': pictures,
# #         'titles': titles,
# #         'authors': authors,
# #         'avatars': avatars,
# #         'likes': likes,
# #         'ids': ids
# #     })
# #     return response_json
# #     # return jsonify({'error': 'collect not found'}), 404

# # # 获取草稿箱


# # @cross_origin()
# # @app.route('/api/drafts/<int:user_id>', methods=['GET'])
# # def get_drafts(user_id):
# #     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
# #     drafts = db.session.query(
# #         Draft.picture,
# #         cast(Draft.date, String),
# #         Draft.label,
# #         Draft.id
# #     ).join(User, Draft.user_id == User.id).filter(User.id == user_id).all()
# #     pictures = []
# #     dates = []
# #     labels = []
# #     ids = []
# #     for draft in drafts:
# #         pictures.append(draft[0])
# #         dates.append(draft[1])
# #         labels.append(draft[2])
# #         ids.append(draft[3])
# #     response_json = jsonify({
# #         'pictures': pictures,
# #         'dates': dates,
# #         'labels': labels,
# #         'ids': ids
# #     })
# #     return response_json
# #     # return jsonify({'error': 'collect not found'}), 404

# # # 获取草稿箱


# # @cross_origin()
# # @app.route('/api/get_draft/<int:post_id>', methods=['GET'])
# # def get_draft(post_id):
# #     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
# #     draft = db.session.query(
# #         Draft.picture,
# #         cast(Draft.date, String),
# #         Draft.label,
# #         Draft.id
# #     ).join(User, Draft.user_id == User.id).filter(User.id == 1, Draft.id == post_id).first()
# #     response_json = jsonify({
# #         'pictures': draft[0],
# #         'dates': draft[1],
# #         'labels': draft[2],
# #         'ids': draft[3]
# #     })
# #     print({
# #         'pictures': draft[0],
# #         'dates': draft[1],
# #         'labels': draft[2],
# #         'ids': draft[3]
# #     })
# #     return response_json
# #     # return jsonify({'error': 'collect not found'}), 404

# # # 获取草稿箱标签


# # @cross_origin()
# # @app.route('/api/get_labels/<int:user_id>', methods=['GET'])
# # def get_labels(user_id):
# #     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
# #     drafts = db.session.query(
# #         Draft.label
# #     ).join(User, Draft.user_id == User.id).filter(User.id == user_id).distinct()
# #     labels = []
# #     for draft in drafts:
# #         labels.append(draft[0])
# #     return labels
# #     # return jsonify({'error': 'collect not found'}), 404

# # # 根据标签获取草稿箱


# # @cross_origin()
# # @app.route('/api/search_drafts/<selected_label>', methods=['GET'])
# # def search_drafts(selected_label):
# #     print(selected_label)
# #     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
# #     drafts = db.session.query(
# #         Draft.picture,
# #         cast(Draft.date, String),
# #         Draft.label,
# #         Draft.id
# #     ).join(User, Draft.user_id == User.id).filter(User.id == 1, Draft.label == selected_label).all()
# #     pictures = []
# #     dates = []
# #     labels = []
# #     ids = []
# #     for draft in drafts:
# #         pictures.append(draft[0])
# #         dates.append(draft[1])
# #         labels.append(draft[2])
# #         ids.append(draft[3])
# #     response_json = jsonify({
# #         'pictures': pictures,
# #         'dates': dates,
# #         'labels': labels,
# #         'ids': ids
# #     })
# #     return response_json
# #     # return jsonify({'error': 'collect not found'}), 404

# # # 草稿箱删除


# # @cross_origin()
# # @app.route('/api/del_draft/<int:post_id>', methods=['GET'])
# # def del_draft(post_id):
# #     draft_to_del = Draft.query.get(post_id)
# #     db.session.delete(draft_to_del)
# #     db.session.commit()
# #     return jsonify({'message': 'Delete successfully'})

# # # 暂存草稿


# # @cross_origin()
# # @app.route('/api/post_draft/', methods=['POST','GET'])
# # def post_draft():
# #     img = request.json.get('img')
# #     user_id = request.json.get('user_id')
# #     label = request.json.get('label')
# #     from datetime import datetime
# #     date = datetime.now()
# #     if img:
# #         new_draft = Draft(user_id=user_id, picture=img, date=date, label='1')
# #         db.session.add(new_draft)
# #         db.session.commit()
# #     return jsonify({'message': 'Post draft successfully'})


# # # 上传头像
# # @app.route('/api/upload-avatar', methods=['POST'])
# # def upload_avatar():
# #     if 'file' not in request.files:
# #         return jsonify({'error': 'No file uploaded'}), 400
# #     file = request.files['file']
# #     if file.filename == '':
# #         return jsonify({'error': 'No selected file'}), 400

# #     # 保存头像文件
# #     filename = file.filename
# #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

# #     # 返回文件路径给前端
# #     photo_url = url_for('serve_avatar', filename=filename)
# #     return jsonify({'photo': photo_url})


# # @app.route('/uploads/<filename>')
# # def serve_avatar(filename):
# #     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# # # 查看要改的用户名是否已存在，要确保所有都是unique
# # @app.route('/check-username', methods=['GET'])
# # def check_username():
# #     username = request.args.get('username')
# #     user_id = request.args.get('user_id')
# #     existing_user = User.query.filter(
# #         User.name == username, User.id != user_id).first()
# #     return jsonify(is_unique=existing_user is None)


# # # 更新用户资料
# # @app.route('/api/update-profile', methods=['POST'])
# # def update_profile():
# #     data = request.json
# #     user = User.query.get(data.get('id'))
# #     if not user:
# #         return jsonify({'error': 'User not found'}), 404

# #     user.name = data.get('name', user.name)
# #     user.photo = data.get('photo', user.photo)
# #     user.email = data.get('email', user.email)
# #     user.sex = data.get('sex', user.sex)
# #     user.age = data.get('age', user.age)
# #     print(user.age)
# #     user.description = data.get('bio', user.description)

# #     db.session.commit()
# #     return jsonify({'message': 'Profile updated successfully'})

# # # 更新用户头像 URL


# # @app.route('/api/update-avatar', methods=['POST'])
# # def update_avatar():
# #     data = request.json
# #     user_id = data.get('user_id')
# #     avatar_url = data.get('photo')

# #     user = User.query.get(user_id)
# #     if not user:
# #         return jsonify({'error': 'User not found'}), 404

# #     # 更新用户的头像 URL
# #     user.photo = avatar_url
# #     db.session.commit()

# #     return jsonify({'message': 'Avatar updated successfully'})

# # # 转换User格式


# # def transUserData(user):
# #     return {'id': user.id,
# #             'name': user.name,
# #             'avatar': user.photo,
# #             }


# # @app.route('/api/get-user-info/<int:user_id>', methods=['GET'])
# # def get_user_info(user_id):
# #     if user_id >= 0:
# #         user = User.query.filter_by(id=user_id).first()
# #         if user:
# #             response = {
# #                 'name': user.name,
# #                 'avatar': user.photo
# #             }
# #             return jsonify(response), 200
# #         else:
# #             return jsonify({'error': 'User not found'}), 404
# #     else:
# #         return jsonify({'error': 'Userid parameter is required'}), 400

# # # 转换时间格式


# # def formatDateTime(time):
# #     return time.strftime("%Y年%m月%d日 %H:%M:%S").replace("年0", "年").replace("月0", "月").replace("日0", "日")


# # def parse_last_time(last_time_str):
# #     return datetime.strptime(last_time_str, '%Y年%m月%d日 %H:%M:%S')

# # # 获取历史消息


# # @app.route('/api/chat/<int:user_id>', methods=['GET'])
# # def get_chats(user_id):
# #     print("get chats user:", user_id)
# #     stuff_id = 0
# #     chats = Chat.query.filter((Chat.receiver == user_id) | (
# #         (Chat.sender == user_id) & (Chat.receiver != stuff_id))).all()
# #     data = []
# #     for chat in chats:
# #         messages = Message.query.filter_by(
# #             chat_id=chat.id).order_by(Message.id).all()
# #         chat_data = {
# #             'id': chat.id,
# #             'sender': transUserData(User.query.get(chat.sender)),
# #             'receiver': transUserData(User.query.get(chat.receiver)),
# #             'unread_sender': chat.unread_sender,
# #             'unread_receiver': chat.unread_receiver,
# #             'last_time': formatDateTime(chat.last_time),
# #             'messages': []
# #         }
# #         for message in messages:
# #             user = User.query.get(message.user_id)
# #             message_data = {
# #                 'id': message.id,
# #                 'type': message.type,
# #                 'time': formatDateTime(message.time),
# #                 'show_time': message.show_time,
# #                 'content': message.content,
# #                 'user': transUserData(user)
# #             }
# #             chat_data['messages'].append(message_data)
# #         data.append(chat_data)
# #     data.sort(key=lambda x: parse_last_time(
# #         x['last_time']), reverse=True)  # 按最后一条消息的时间降序排序
# #     print("chats data:", data)
# #     return jsonify(data)


# # @app.route('/api/chat-feedback/<int:user_id>', methods=['GET'])
# # def get_chats_feedback(user_id):
# #     print("get chats user:", user_id)
# #     stuff_id = 0
# #     if user_id != stuff_id:
# #         chats = Chat.query.filter(
# #             ((Chat.sender == user_id) & (Chat.receiver == stuff_id))).all()
# #     else:
# #         chats = Chat.query.filter((Chat.receiver == stuff_id)).all()
# #     data = []
# #     for chat in chats:
# #         messages = Message.query.filter_by(
# #             chat_id=chat.id).order_by(Message.id).all()
# #         chat_data = {
# #             'id': chat.id,
# #             'sender': transUserData(User.query.get(chat.sender)),
# #             'receiver': transUserData(User.query.get(chat.receiver)),
# #             'unread_sender': chat.unread_sender,
# #             'unread_receiver': chat.unread_receiver,
# #             'last_time': formatDateTime(chat.last_time),
# #             'messages': []
# #         }
# #         for message in messages:
# #             user = User.query.get(message.user_id)
# #             message_data = {
# #                 'id': message.id,
# #                 'type': message.type,
# #                 'time': formatDateTime(message.time),
# #                 'show_time': message.show_time,
# #                 'content': message.content,
# #                 'user': transUserData(user)
# #             }
# #             chat_data['messages'].append(message_data)
# #         data.append(chat_data)
# #     data.sort(key=lambda x: parse_last_time(
# #         x['last_time']), reverse=True)  # 按最后一条消息的时间降序排序
# #     print("chats data:", len(data))
# #     return jsonify(data)

# # # 新增会话


# # @app.route('/create_chat', methods=['POST'])
# # def create_chat():
# #     data = request.get_json()
# #     sender_id = data.get('sender_id')
# #     receiver_id = data.get('receiver_id')

# #     if sender_id == None or receiver_id == None:
# #         return jsonify({"error": "Sender ID and Receiver ID are required"}), 400

# #     # 查找是否已经存在包含 sender_id 和 receiver_id 的会话
# #     chat = Chat.query.filter(
# #         (Chat.sender == sender_id) & (Chat.receiver == receiver_id) |
# #         (Chat.sender == receiver_id) & (Chat.receiver == sender_id)
# #     ).first()

# #     if chat:
# #         # 如果会话已存在，更新 last_time
# #         chat.last_time = datetime.now()
# #         db.session.commit()
# #         return jsonify({"message": "Chat updated successfully", "chat_id": chat.id}), 200
# #     else:
# #         # 获取当前数据库中最大的id值
# #         max_id = db.session.query(db.func.max(Chat.id)).scalar()
# #         new_id = (max_id or 0) + 1

# #         new_chat = Chat(
# #             id=new_id,
# #             sender=sender_id,
# #             receiver=receiver_id,
# #             unread_sender=True,
# #             unread_receiver=True,
# #             last_time=datetime.now()
# #         )
# #         db.session.add(new_chat)
# #         db.session.commit()

# #     return jsonify({"message": "Chat created successfully", "chat_id": new_id}), 201

# # # 删除指定会话


# # @app.route('/api/delete_chat/<int:chat_id>', methods=['DELETE'])
# # def delete_chat(chat_id):
# #     chat = Chat.query.get(chat_id)
# #     if not chat:
# #         return jsonify({"error": "Chat not found"}), 404

# #     db.session.delete(chat)
# #     db.session.commit()

# #     return jsonify({"message": "Chat and associated messages deleted successfully"}), 200


# # # 检查对话是否为空，空则删去
# # @app.route('/api/check_empty_chat', methods=['POST'])
# # def check_empty_chat():
# #     # 查询没有消息的聊天记录
# #     empty_chats = Chat.query.filter(~Chat.messages.any()).all()

# #     for chat in empty_chats:
# #         db.session.delete(chat)
# #     db.session.commit()

# #     return jsonify({"message": f"Deleted {len(empty_chats)} empty chats."}), 200

# # # 新增消息


# # @app.route('/api/save_message', methods=['POST'])
# # def receive_messages():
# #     data = request.json
# #     print(data)
# #     chat_id = data.get('chat_id')
# #     message = data.get('message')
# #     show_time = data.get('show_time')
# #     if not chat_id or not message:
# #         return jsonify({'error': 'Invalid data provided'}), 400

# #     chat = Chat.query.get(chat_id)
# #     if not chat:
# #         return jsonify({'error': 'Chat not found'}), 404

# #     content = message.get('content')
# #     if content:
# #         message_datetime = datetime.strptime(
# #             message.get('time'), '%Y年%m月%d日 %H:%M:%S')
# #         max_message_id = db.session.query(func.max(Message.id)).scalar() or 0
# #         next_message_id = max_message_id + 1
# #         db_message = Message(
# #             id=next_message_id,
# #             type=message.get('type'),
# #             time=message_datetime,
# #             show_time=show_time,
# #             content=content,
# #             user_id=message.get('user')["id"],
# #             chat_id=chat.id,
# #         )
# #         db.session.add(db_message)
# #         # 更新时间
# #         chat.last_time = message_datetime
# #         db.session.commit()

# #     return jsonify({'message_id': next_message_id}), 200

# # # 删去消息


# # @app.route('/api/delete_message', methods=['POST'])
# # def delete_message():
# #     message_id = request.json.get('message_id')
# #     print("msg id:", message_id)
# #     if message_id:
# #         message = Message.query.get(message_id)
# #         if message:
# #             db.session.delete(message)
# #             db.session.commit()
# #             return 'Delete successfully', 200
# #         else:
# #             return 'Message not found', 404
# #     else:
# #         return 'No message ID provided', 400

# # # 查询反馈


# # @app.route('/api/feedback/<int:user_id>', methods=['GET'])
# # def get_feedback(user_id):
# #     stuff_id = 0  # 客服id
# #     chats = Chat.query.filter((Chat.sender == user_id)
# #                               & (Chat.receiver == stuff_id)).all()
# #     data = []
# #     for chat in chats:
# #         messages = Message.query.filter_by(
# #             chat_id=chat.id).order_by(Message.id).all()
# #         chat_data = {
# #             'id': chat.id,
# #             'sender': transUserData(User.query.get(chat.sender)),
# #             'receiver': transUserData(User.query.get(chat.receiver)),
# #             'unread_sender': chat.unread_sender,
# #             'unread_receiver': chat.unread_receiver,
# #             'last_time': formatDateTime(chat.last_time),
# #             'messages': []
# #         }
# #         for message in messages:
# #             user = User.query.get(message.user_id)
# #             message_data = {
# #                 'id': message.id,
# #                 'type': message.type,
# #                 'time': formatDateTime(message.time),
# #                 'content': message.content,
# #                 'user': transUserData(user)
# #             }
# #             chat_data['messages'].append(message_data)
# #         data.append(chat_data)

# #     return jsonify(data)

# # # 添加收藏


# # @app.route('/api/add_collect', methods=['GET', 'POST'])
# # def add_collect():
# #     post_id = request.json.get('postId')  # 获取文章 ID
# #     user_id = request.json.get('userId')  # 获取用户 ID
# #     isAdd = request.json.get('add')
# #     from datetime import datetime, timezone
# #     date = datetime.now()
# #     if isAdd and post_id and user_id:
# #         new_Collect = Collect(date=date, user_id=user_id, post_id=post_id)
# #         db.session.add(new_Collect)
# #         db.session.commit()
# #         return jsonify({'message': '收藏成功'})
# #     elif not isAdd and post_id and user_id:
# #         Collect.query.filter(
# #             Collect.post_id == post_id and Collect.user_id == user_id).delete()
# #         db.session.commit()
# #         return jsonify({'message': '取消收藏成功'})
# #     else:
# #         return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400

# # # 添加点赞


# # @app.route('/api/add_like', methods=['GET', 'POST'])
# # def add_like():
# #     post_id = request.json.get('postId')  # 获取文章 ID
# #     user_id = request.json.get('userId')  # 获取用户 ID
# #     isAdd = request.json.get('add')
# #     from datetime import datetime, timezone
# #     date = datetime.now()
# #     if isAdd and post_id and user_id:
# #         new_Like = Like(date=date, author_id=user_id, post_id=post_id)
# #         db.session.add(new_Like)
# #         db.session.commit()
# #         return jsonify({'message': '点赞成功'})
# #     elif not isAdd and post_id and user_id:
# #         Like.query.filter(
# #             Like.post_id == post_id and Like.author_id == user_id).delete()
# #         db.session.commit()
# #         return jsonify({'message': '取消点赞成功'})
# #     else:
# #         return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400

# # # 获取点赞和收藏的状态


# # @app.route('/api/get_status/<int:post_id>/<int:userId>', methods=['GET'])
# # def get_status(post_id, userId):
# #     # post_id = request.json.get('postId')  # 获取文章 ID
# #     # user_id = request.json.get('userId')  # 获取用户 ID
# #     print('post:{},user:{}'.format(post_id, userId))
# #     isLiked = db.session.query(
# #         Like.id
# #     ).filter(Like.post_id == post_id and Like.author_id == userId) \
# #         .first()
# #     isCollected = db.session.query(
# #         Collect.id
# #     ).filter(Collect.post_id == post_id and Collect.user_id == userId) \
# #         .first()
# #     if isLiked:
# #         isLiked = '1'
# #     else:
# #         isLiked = '0'
# #     if isCollected:
# #         isCollected = '1'
# #     else:
# #         isCollected = '0'
# #     response_json = jsonify({
# #         'isLiked': isLiked,
# #         'isCollected': isCollected
# #     })
# #     print({
# #         'isLiked': isLiked,
# #         'isCollected': isCollected
# #     })
# #     return response_json

# # # 提交评论


# # @app.route('/api/submit_comment', methods=['GET', 'POST'])
# # def add_comment():
# #     content = request.json.get('content')
# #     post_id = request.json.get('postId')  # 获取文章 ID
# #     user_id = request.json.get('userId')  # 获取用户 ID
# #     post_id = int(post_id)
# #     from datetime import datetime, timezone
# #     date = datetime.now()
# #     # date = date.strftime('%Y-%m-%d %H:%M:%S')
# #     print(content)
# #     # from datetime import datetime
# #     # date = datetime.strptime(date, "%Y/%m/%d, %H:%M:%S")
# #     if content and post_id:
# #         new_comment = Comment(content=content,
# #                               author_id=user_id,
# #                               post_id=post_id,
# #                               date=date)
# #         db.session.add(new_comment)
# #         db.session.commit()
# #         newComment = db.session.query(
# #             Comment.id,
# #             # Comment.date,
# #             cast(Comment.date, String),
# #             Comment.content,
# #             User.name,
# #             User.photo
# #         ).join(User, Comment.author_id == User.id) \
# #             .outerjoin(Post, Comment.post_id == Post.id) \
# #             .filter(Post.id == post_id) \
# #             .order_by(desc(Comment.id)) \
# #             .first()
# #         response_json = jsonify({
# #             'ids': newComment[0],
# #             'dates': newComment[1],
# #             'contents': newComment[2],
# #             'authors': newComment[3],
# #             'avatars': newComment[4]
# #         })
# #         print({
# #             'ids': newComment[0],
# #             'dates': newComment[1],
# #             'contents': newComment[2],
# #             'authors': newComment[3],
# #             'avatars': newComment[4]
# #         })
# #         return response_json
# #     else:
# #         return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400

# # # 获取帖子评论


# # @app.route('/api/post_comments/<int:post_id>', methods=['GET'])
# # def get_postComment(post_id):
# #     # 首先是文章信息，包括内容、作者等
# #     print(post_id)
# #     comments = db.session.query(
# #         Comment.id,
# #         # Comment.date,
# #         cast(Comment.date, String),
# #         Comment.content,
# #         User.name,
# #         User.photo
# #     ).join(User, Comment.author_id == User.id) \
# #         .outerjoin(Post, Comment.post_id == Post.id) \
# #         .filter(Post.id == post_id) \
# #         .order_by(desc(Comment.id)) \
# #         .all()
# #     ids = []
# #     dates = []
# #     contents = []
# #     authors = []
# #     avatars = []
# #     for comment in comments:
# #         ids.append(comment[0])
# #         dates.append(comment[1][:19])
# #         contents.append(comment[2])
# #         authors.append(comment[3])
# #         avatars.append(comment[4])
# #     response_json = jsonify({
# #         'ids': ids,
# #         'dates': dates,
# #         'contents': contents,
# #         'authors': authors,
# #         'avatars': avatars
# #     })
# #     print({
# #         'ids': ids,
# #         'dates': dates,
# #         'contents': contents,
# #         'authors': authors,
# #         'avatars': avatars
# #     })
# #     return response_json

# # # 获取帖子评论


# # @app.route('/api/all_comments/<int:user_id>', methods=['GET'])
# # def get_allComment(user_id):
# #     # 获取用户发表的所有帖子
# #     posts = db.session.query(Post.id).filter(Post.author_id == user_id).all()
# #     post_ids = [post.id for post in posts]

# #     # 获取这些帖子的评论，以及评论的作者信息和帖子的第一张图片
# #     comments = db.session.query(
# #         Comment.id,
# #         cast(Comment.date, String),
# #         Comment.content,
# #         User.name,
# #         User.photo,
# #         Post.picture1
# #     ).join(User, Comment.author_id == User.id) \
# #         .join(Post, Comment.post_id == Post.id) \
# #         .filter(Post.id.in_(post_ids)) \
# #         .order_by(desc(Comment.date)) \
# #         .all()
# #     ids = []
# #     dates = []
# #     contents = []
# #     authors = []
# #     avatars = []
# #     pictures = []
# #     for comment in comments:
# #         ids.append(comment[0])
# #         dates.append(comment[1][:19])
# #         contents.append(comment[2])
# #         authors.append(comment[3])
# #         avatars.append(comment[4])
# #         pictures.append(comment[5])
# #     response_json = jsonify({
# #         'ids': ids,
# #         'dates': dates,
# #         'contents': contents,
# #         'authors': authors,
# #         'avatars': avatars,
# #         'pictures': pictures
# #     })
# #     print({
# #         'ids': ids,
# #         'dates': dates,
# #         'contents': contents,
# #         'authors': authors,
# #         'avatars': avatars,
# #         'pictures': pictures
# #     })
# #     return response_json


# # @app.route('/api/post_content/<int:post_id>', methods=['GET'])
# # def get_postContent(post_id):
# #     print(post_id)
# #     # Expanded query to include User.id
# #     contents = db.session.query(
# #         Post.picture1,
# #         Post.picture2,
# #         Post.picture3,
# #         Post.picture4,
# #         Post.picture5,
# #         cast(Post.date, String),
# #         Post.title,
# #         Post.body,
# #         User.name,
# #         User.photo,
# #         User.id,  # Adding this to capture the author's ID
# #         func.count(Like.id.distinct()).label('like'),
# #         func.count(Comment.id.distinct()).label('comment'),
# #         func.count(Collect.id.distinct()).label('collect'),
# #         Post.id
# #     ).join(User, Post.author_id == User.id) \
# #         .outerjoin(Like, Post.id == Like.post_id) \
# #         .outerjoin(Comment, Post.id == Comment.post_id) \
# #         .outerjoin(Collect, Post.id == Collect.post_id) \
# #         .filter(Post.id == post_id) \
# #         .group_by(Post.id, User.id, User.name, User.photo) \
# #         .order_by(desc(Post.id)) \
# #         .all()

# #     if contents:
# #         content = contents[0]
# #         pictures = [pic for pic in content[:5] if pic]
# #         response_json = jsonify({
# #             'pictures': pictures,
# #             'date': content[5][:19],
# #             'title': content[6],
# #             'body': content[7],
# #             'author': content[8],
# #             'avatar': content[9],
# #             'author_id': content[10],  # Using the fetched author ID
# #             'likes_num': content[11],
# #             'comments_num': content[12],
# #             'collects_num': content[13]
# #         })
# #         # This will print the JSON response in your server logs
# #         print(response_json.get_json())
# #         return response_json
# #     else:
# #         return jsonify({'error': 'Post not found'}), 404


# # # 互相关注
# # @app.route('/api/follow', methods=['POST'])
# # def follow_user():
# #     data = request.get_json()
# #     follower_id = data.get('follower_id')
# #     followed_id = data.get('followed_id')
# #     # print(follower_id)
# #     if follower_id == followed_id:
# #         return jsonify({'error': 'Cannot follow yourself'}), 400

# #     follow = Follow.query.filter_by(
# #         follower_id=follower_id, followed_id=followed_id).first()
# #     if follow:
# #         # 已经存在关注记录，检查是否已经是互相关注
# #         return jsonify({'message': 'Already followed', 'status': follow.status}), 409
# #     else:
# #         # 创建新的关注关系
# #         new_follow = Follow(follower_id=follower_id,
# #                             followed_id=followed_id, status=0)
# #        # print(follower_id)
# #         db.session.add(new_follow)

# #         # 检查对方是否已关注当前用户，实现互相关注
# #         reverse_follow = Follow.query.filter_by(
# #             follower_id=followed_id, followed_id=follower_id).first()
# #         if reverse_follow:
# #             new_follow.status = 1
# #             reverse_follow.status = 1
# #             db.session.add(reverse_follow)

# #         db.session.commit()
# #         return jsonify({'message': 'Followed successfully', 'status': new_follow.status}), 200

# # # 取消关注


# # @app.route('/api/unfollow', methods=['POST'])
# # def unfollow_user():
# #     data = request.get_json()
# #     follower_id = data.get('follower_id')
# #     followed_id = data.get('followed_id')

# #     if follower_id == followed_id:
# #         return jsonify({'error': 'Cannot unfollow yourself'}), 400

# #     # 查询是否存在关注记录
# #     follow = Follow.query.filter_by(
# #         follower_id=follower_id, followed_id=followed_id).first()
# #     if not follow:
# #         return jsonify({'message': 'No follow relation found'}), 404

# #     # 存在关注记录，进行取消
# #     db.session.delete(follow)

# #     # 检查是否需要更新互相关注状态
# #     reverse_follow = Follow.query.filter_by(
# #         follower_id=followed_id, followed_id=follower_id).first()
# #     if reverse_follow and reverse_follow.status == 1:
# #         reverse_follow.status = 0  # 更新为非互相关注状态
# #         db.session.add(reverse_follow)

# #     db.session.commit()
# #     return jsonify({'message': 'Unfollowed successfully'}), 200

# # # 查看，来显示


# # @app.route('/api/check-follow/<int:follower_id>/<int:followed_id>', methods=['GET'])
# # def check_follow(follower_id, followed_id):
# #     follow = Follow.query.filter_by(
# #         follower_id=follower_id, followed_id=followed_id).first()
# #     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# #     print(follow)
# #     if follow:
# #         return jsonify({'isFollowed': True, 'status': follow.status}), 200
# #     else:
# #         return jsonify({'isFollowed': False, 'status': 0}), 200


# # # 广场页获取帖子
# # # @cross_origin()
# # @app.route('/api/posts', methods=['GET'])
# # def get_posts():
# #     posts = db.session.query(
# #         Post.id,
# #         Post.picture1,
# #         Post.title,
# #         User.name,
# #         User.photo,
# #         func.count(Like.id).label('like')
# #     ).join(User, Post.author_id == User.id) \
# #         .outerjoin(Like, Post.id == Like.post_id) \
# #         .group_by(Post.picture1,
# #                   Post.title,
# #                   User.name,
# #                   User.photo) \
# #         .all()
# #     ids = []
# #     pictures = []
# #     titles = []
# #     authors = []
# #     avatars = []
# #     likes = []
# #     for post in posts:
# #         ids.append(post[0])
# #         pictures.append(post[1])
# #         titles.append(post[2])
# #         authors.append(post[3])
# #         avatars.append(post[4])
# #         likes.append(post[5])
# #     response_json = jsonify({
# #         'ids': ids,
# #         'pictures': pictures,
# #         'titles': titles,
# #         'authors': authors,
# #         'avatars': avatars,
# #         'likes': likes
# #     })
# #     # print({
# #     #     'ids': ids,
# #     #     'pictures': pictures,
# #     #     'titles': titles,
# #     #     'authors': authors,
# #     #     'avatars': avatars,
# #     #     'likes': likes
# #     # })
# #     return response_json

# # # 广场页获取关注帖子
# # # @cross_origin()


# # @app.route('/api/follow_posts/<int:user_id>', methods=['GET'])
# # def get_followposts(user_id):
# #     # user_id = 1  # Replace with the current logged in user's ID
# #     posts = db.session.query(
# #         Post.id,
# #         Post.picture1,
# #         Post.title,
# #         User.name,
# #         User.photo,
# #         func.count(Like.id).label('like')
# #     ).join(User, Post.author_id == User.id) \
# #         .outerjoin(Like, Post.id == Like.post_id) \
# #         .join(Follow, Follow.followed_id == Post.author_id) \
# #         .filter(Follow.follower_id == user_id) \
# #         .group_by(Post.picture1,
# #                   Post.title,
# #                   User.name,
# #                   User.photo) \
# #         .all()
# #     ids = []
# #     pictures = []
# #     titles = []
# #     authors = []
# #     avatars = []
# #     likes = []
# #     for post in posts:
# #         ids.append(post[0])
# #         pictures.append(post[1])
# #         titles.append(post[2])
# #         authors.append(post[3])
# #         avatars.append(post[4])
# #         likes.append(post[5])
# #     response_json = jsonify({
# #         'ids': ids,
# #         'pictures': pictures,
# #         'titles': titles,
# #         'authors': authors,
# #         'avatars': avatars,
# #         'likes': likes
# #     })
# #     # print({
# #     #     'ids': ids,
# #     #     'pictures': pictures,
# #     #     'titles': titles,
# #     #     'authors': authors,
# #     #     'avatars': avatars,
# #     #     'likes': likes
# #     # })
# #     return response_json


# # @socketio.on('connect')
# # def handle_connect():
# #     print('Client connected')


# # @socketio.on('disconnect')
# # def handle_disconnect():
# #     print('Client disconnected')


# # @socketio.on('join')
# # def handle_join(data):
# #     print("join:", data)
# #     chat_id = data['chat_id']
# #     join_room(chat_id)


# # @socketio.on('message')
# # def handle_message(data):
# #     chat_id = data['chat_id']
# #     print("chat:", chat_id)
# #     emit('message', {'message': data['message']}, room=chat_id)

# # # 管理员相关函数
# # # 获取所有用户


# # @app.route('/api/get-all-user', methods=['GET'])
# # def get_all_users():
# #     users = User.query.all()
# #     users_data = []

# #     for user in users:
# #         if user.is_admin:
# #             continue
# #         user_data = {
# #             'id': user.id,
# #             'name': user.name,
# #             'password': user.password,
# #             'avatar': user.photo,
# #             'email': user.email,
# #             'age': user.age,
# #             'sex': user.sex,
# #             'senior': user.is_premium,
# #             'description': user.description,
# #             'status': user.status
# #         }
# #         users_data.append(user_data)

# #     return jsonify({'userList': users_data})


# # # 获取用户和帖子总数
# # @app.route('/api/get-user-post-num', methods=['GET'])
# # def get_user_post_num():
# #     users = User.query.all()
# #     posts = Post.query.all()
# #     return jsonify({'userNum': len(users), 'postNum': len(posts)})

# # # 获取所有帖子


# # @app.route('/api/get-all-post', methods=['GET'])
# # def get_all_posts():
# #     posts = Post.query.all()
# #     posts_data = []

# #     for post in posts:
# #         post_data = {
# #             'id': post.id,
# #             'author_id': post.author_id,
# #             'date': formatDateTime(post.date),
# #             'pics': [post.picture1, post.picture2, post.picture3, post.picture4, post.picture5],
# #             'title': post.title,
# #             'content': post.body,
# #             'status': post.status
# #         }
# #         posts_data.append(post_data)

# #     return jsonify({'dataList': posts_data})

# # # 更新用户状态 禁用和正常来回切换


# # @app.route('/api/update-user-status/<int:user_id>', methods=['POST'])
# # def update_user_status(user_id):
# #     user = User.query.get(user_id)
# #     if user is None:
# #         return jsonify({'error': 'User not found'}), 404

# #     # 切换帖子状态
# #     user.status = not user.status
# #     db.session.commit()

# #     return jsonify({'success': 'User status updated successfully', 'new_status': user.status})

# # # 更新帖子状态 禁用和正常来回切换


# # @app.route('/api/update-post-status/<int:post_id>', methods=['POST'])
# # def update_post_status(post_id):
# #     print(post_id)
# #     post = Post.query.get(post_id)
# #     if post is None:
# #         return jsonify({'error': 'Post not found'}), 404

# #     post.status = not post.status
# #     db.session.commit()

# #     return jsonify({'success': 'Post status updated successfully', 'new_status': post.status})

# # # 发布动态


# # @app.route('/api/postnotes', methods=['GET', 'POST'])
# # def postnotes():
# #     dataform = request.json.get('pics')
# #     title = request.json.get('title')
# #     description = request.json.get('description')
# #     user_id = request.json.get('userId')  # 获取用户 ID
# #     # user_id = 1
# #     # 获取dataform的实际大小
# #     cnt = len(dataform)
# #     pic1 = ''
# #     pic2 = ''
# #     pic3 = ''
# #     pic4 = ''
# #     pic5 = ''
# #     if cnt >= 1:
# #         pic1 = dataform[0]
# #     if cnt >= 2:
# #         pic2 = dataform[1]
# #     if cnt >= 3:
# #         pic3 = dataform[2]
# #     if cnt >= 4:
# #         pic4 = dataform[3]
# #     if cnt >= 5:
# #         pic5 = dataform[4]
# #     # 谁定义的数据表，表项名字那么长...pic不好么
# #     dateToday = datetime.now()
# #     print(dateToday)
# #     post = Post(date=dateToday, author_id=user_id, title=title, body=description,
# #                 picture1=pic1, picture2=pic2, picture3=pic3, picture4=pic4, picture5=pic5)
# #     db.session.add(post)
# #     db.session.commit()
# #     return jsonify({'message': 'Post created successfully'})

# # # 后端调用修图指令
# # # 参数：img_url(原图URL) + img_select(对应的模板url，用于寻找prompt)
# # # 本地调试请注释该函数！！！！！！！

# # @app.route('/api/call_P2P', methods=['GET', 'POST'])
# # def call_P2P():
# #     img_old = request.json.get('img_url')
# #     img_select = request.json.get('img_select')
# #     user_id = request.json.get('user_id')
# #     print(img_old, img_select, user_id)
# #     if img_old is None or img_select is None or user_id is None:
# #         return jsonify({'img': 'Invalid data provided'}), 400
# #     # 查询Picture数据表，找到对应的prompt
# #     pic_tmp = Picture(id=img_select, prompt='turn it yellow.')
# #     db.session.add(pic_tmp)
# #     db.session.commit()
# #     prompt = Picture.query.filter_by(id=img_select).first().prompt
# #     if prompt is None:
# #         print("prompt is None")
# #         return jsonify({'img': 'Prompt not found'})
# #     # 调用修图指令
# #     # img_new = os.system("python /root/Code/Models/P2P/P2P.py --img_url "+img_old+" --prompt "+prompt)
# #     # 函数调用修图命令，存储为/mod/{prompt+"_modify_"+img_old}
# #     sys.path.append(r'/root/Code/Models/P2P')
# #     import P2P
# #     P2P.modify_pic(img_old, prompt)
# #     # 上传阿里云图床
# #     # OSS_ACCESS_KEY_ID = "LTAI5tR1c1uhFRfWxjq8BWT4"
# #     # OSS_ACCESS_KEY_SECRET = "BdN5OIEdet7IO6KWOq7TJiivHOsC5B"
# #     auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
# #     bucket = oss2.Bucket(
# #         auth, 'https://oss-cn-beijing.aliyuncs.com', 'graphcrafter')
# #     # /root/Code/Models/P2P/weights
# #     prompt = prompt.replace(" ", "")
# #     mod_img_url = prompt + "_modify_" + img_old.split("/")[-1]
# #     with open(mod_img_url, mode="rb") as fileobj:
# #         fileobj.seek(0, os.SEEK_SET)
# #         current = fileobj.tell()
# #         bucket_url = user_id+'/'+prompt + "_modify_" + img_old.split("/")[-1]
# #         bucket.put_object(bucket_url, fileobj)
# #         # 删除文件夹中的图片
# #         os.remove(mod_img_url)
# #         print("https://graphcrafter.oss-cn-beijing.aliyuncs.com/" + bucket_url)
# #         return jsonify({'img': "https://graphcrafter.oss-cn-beijing.aliyuncs.com/" + bucket_url})
# #     return jsonify({'img': None})

# # # 删除帖子的接口
# # @app.route('/api/delete-post/<int:post_id>', methods=['DELETE'])
# # def delete_post(post_id):
# #     post = Post.query.get_or_404(post_id)

# #     # 删除相关的评论
# #     Comment.query.filter_by(post_id=post_id).delete()

# #     # 删除相关的点赞
# #     Like.query.filter_by(post_id=post_id).delete()

# #     # 删除相关的收藏
# #     Collect.query.filter_by(post_id=post_id).delete()

# #     # 删除帖子
# #     db.session.delete(post)
# #     db.session.commit()

# #     return jsonify({'message': 'Post deleted successfully'}), 200

# # # 基本图像处理


# # @app.route('/api/simple-image-process', methods=['POST'])
# # def process_image_simple():
# #     print(request.files)
# #     print("form:", request.form)
# #     if 'file' not in request.files:
# #         return jsonify({'error': 'No file uploaded'}), 400
# #     file = request.files['file']
# #     if file.filename == '':
# #         return jsonify({'error': 'No selected file'}), 400

# #     # 读取参数
# #     user_id = request.form.get('user_id')
# #     # 处理的类别 eg.图像色彩，图像变换...
# #     process_category = request.form.get('process_category')
# #     process_type = request.form.get('process_type')  # 具体的处理类型 eg.色调

# #     if not user_id or not process_category or not process_type:
# #         return jsonify({'error': 'Missing processing parameters'}), 400

# #     # 读取图片文件
# #     file_stream = io.BytesIO(file.read())
# #     file_bytes = np.frombuffer(file_stream.read(), np.uint8)
# #     origin = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
# #     height, width, channels = origin.shape
# #     img_size = [width, height]
# #     print("image size:", height, width)

# #     if origin is None:
# #         return jsonify({'error': 'Failed to read the uploaded image'}), 500

# #     # 进行图像处理
# #     # 处理后的图片暂存为tmp.png
# #     if process_category == "color":
# #         show_hsv(origin, process_type, img_size)
# #     elif process_category == "transform":
# #         show_transformation(origin, process_type, img_size)
# #     elif process_category == "filter":
# #         show_filtering(origin, process_type, img_size)
# #     elif process_category == "outline":
# #         show_outline(origin, process_type, img_size)
# #     elif process_category == "enhance":
# #         show_enhancement(origin, process_type, img_size)
# #     else:
# #         return jsonify({'error': 'Process category chosen does not exits'}), 400

# #     # 上传到阿里云OSS
# #     tmp_file_path = './img_tmp/tmp.png'
# #     current_time = datetime.now().strftime('%Y%m%d%H%M%S')
# #     oss_file_path = f'simple_image_process/{user_id}-{current_time}.png'
# #     with open(tmp_file_path, 'rb') as file:
# #         bucket.put_object(oss_file_path, file)
# #     img_url = f'http://{OSS_BUCKET_NAME}.{OSS_ENDPOINT}/{oss_file_path}'
# #     print(img_url)

# #     return jsonify({'imgUrl': img_url})


# # if __name__ == '__main__':
# #     config = dict(
# #         host='0.0.0.0',
# #         port=3306,
# #         debug=True,
# #         allow_unsafe_werkzeug=True
# #     )
# #     socketio.run(app, **config)

# import sys
# import os
# from flask import Flask, jsonify, request, render_template, url_for, send_from_directory
# from flask_cors import CORS, cross_origin

# from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
# from sqlalchemy import func, cast, String, desc
# from sqlalchemy.orm import relationship
# from flask_bcrypt import Bcrypt     # 密码加密

# from flask_socketio import SocketIO, emit, join_room
# from datetime import datetime

# # 用于数据库一键初始化 by hzq
# from flask_migrate import Migrate


# # 后端上传阿里云图床
# import oss2
# import os
# from oss2.credentials import EnvironmentVariableCredentialsProvider

# # 简单图像处理
# import io
# import numpy as np
# import cv2
# from simple_image_process.image_filtering import show_filtering
# from simple_image_process.image_outline import show_outline
# from simple_image_process.image_transformation import show_transformation
# from simple_image_process.image_color import show_hsv
# from simple_image_process.image_enhancement import show_enhancement

# # 防止通信报错 by zyp
# # import locale
# # locale.setlocale(locale.LC_CTYPE,"chinese")

# WIN = sys.platform.startswith('win')
# if WIN:  # 如果是 Windows 系统，使用三个斜线
#     prefix = 'sqlite:///'
# else:  # 否则使用四个斜线
#     prefix = 'sqlite:////'

# app = Flask(__name__, static_url_path='/',
#             static_folder='./../frontend/dist', template_folder='./../frontend/dist')
# socketio = SocketIO(app, cors_allowed_origins="http://localhost:5173")

# # 创建数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = prefix + \
#     os.path.join(app.root_path, 'data.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 关闭对模型修改的监控
# db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app
# migrate = Migrate(app, db)


# # 阿里云OSS相关信息
# OSS_ACCESS_KEY_ID = 'LTAI5tR1c1uhFRfWxjq8BWT4'
# OSS_ACCESS_KEY_SECRET = 'BdN5OIEdet7IO6KWOq7TJiivHOsC5B'
# OSS_ENDPOINT = 'oss-cn-beijing.aliyuncs.com'
# OSS_BUCKET_NAME = 'graphcrafter'
# auth = oss2.Auth(OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET)
# bucket = oss2.Bucket(auth, OSS_ENDPOINT, OSS_BUCKET_NAME)
# bcrypt = Bcrypt(app)


# class User(db.Model):  # 用户
#     id = db.Column(db.Integer, primary_key=True)  # 主键，账号
#     name = db.Column(db.String(20))  # 名字
#     password = db.Column(db.String(20))  # 密码
#     photo = db.Column(db.String(60))  # 头像
#     email = db.Column(db.String(254))  # 邮箱
#     age = db.Column(db.Integer)  # 年龄
#     sex = db.Column(db.Boolean)  # 性别，1是男0是女
#     is_admin = db.Column(db.Boolean, default=False)
#     is_premium = db.Column(db.Boolean, default=False)
#     description = db.Column(db.String(100))  # 一句话介绍自己
#     status = db.Column(db.Boolean)  # 是否正常 0正常 1被封


# class Post(db.Model):  # 帖子
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     author_id = db.Column(db.Integer)      # 作者id
#     date = db.Column(db.DateTime)     # 日期
#     picture1 = db.Column(db.String(60))     # 图片1，默认为封面
#     picture2 = db.Column(db.String(60))     # 图片2
#     picture3 = db.Column(db.String(60))     # 图片3
#     picture4 = db.Column(db.String(60))     # 图片4
#     picture5 = db.Column(db.String(60))     # 图片5
#     title = db.Column(db.String(60))     # 标题
#     body = db.Column(db.Text)  # 正文
#     model = db.Column(db.Integer)  # 模型参数id
#     status = db.Column(db.Boolean)  # 状态，0是正常 1是被禁


# class Comment(db.Model):  # 评论
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     date = db.Column(db.DateTime)     # 日期
#     content = db.Column(db.Text)  # 正文
#     author_id = db.Column(db.Integer)      # 作者id
#     post_id = db.Column(db.Integer)      # 文章id


# class Like(db.Model):  # 点赞
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     date = db.Column(db.DateTime)     # 日期
#     author_id = db.Column(db.Integer)      # 点赞者id
#     post_id = db.Column(db.Integer)      # 文章id


# class Collect(db.Model):  # 收藏
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     date = db.Column(db.DateTime)     # 日期
#     user_id = db.Column(db.Integer)      # 作者id
#     post_id = db.Column(db.Integer)      # 文章id


# class Follow(db.Model):  # 关注
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     follower_id = db.Column(db.Integer)      # 粉丝id
#     followed_id = db.Column(db.Integer)      # 被关注者id
#     status = db.Column(db.Integer)      # 关注状态,0表示单独关注，1表示互相关注


# class FeedBack(db.Model):  # 用户反馈
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     date = db.Column(db.DateTime)     # 日期
#     user_id = db.Column(db.Integer)      # 用户id
#     content = db.Column(db.Text)  # 正文
#     processed = db.Column(db.Boolean)  # 是否已处理
#     back_content = db.Column(db.Text)  # 反馈内容


# class ModifyHistory(db.Model):  # 修图历史
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     date = db.Column(db.DateTime)     # 日期
#     user_id = db.Column(db.Integer)      # 用户id
#     pic_before = db.Column(db.String(60))     # 修改前图片
#     pic_after = db.Column(db.String(60))     # 修改后图片
#     prompt = db.Column(db.Text)  # 提示
#     model_id = db.Column(db.Integer)  # 模型参数


# class Message(db.Model):  # 单条消息记录
#     __tablename__ = 'message'
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     type = db.Column(db.String(60))  # 消息的类型
#     time = db.Column(db.DateTime)  # 发送时间
#     show_time = db.Column(db.Boolean)  # 该条消息的时间是否显示
#     content = db.Column(db.Text)  # 内容
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 发送的用户id
#     chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))  # 关联Chat模型的id


# class Chat(db.Model):  # 会话
#     __tablename__ = 'chat'
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     sender = db.Column(db.Integer)  # 发起者的id
#     receiver = db.Column(db.Integer)  # 接收者的id
#     unread_sender = db.Column(db.Boolean)  # 发起者是否已经阅读
#     unread_receiver = db.Column(db.Boolean)  # 接收者是否已经阅读
#     last_time = db.Column(db.DateTime)  # 最后一条消息的时间
#     messages = relationship("Message", backref="chat",
#                             cascade="all, delete-orphan")  # 包含的消息 一对多


# class Draft(db.Model):  # 草稿箱
#     __tablename__ = 'Draft'
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     date = db.Column(db.DateTime)     # 日期
#     user_id = db.Column(db.Integer)      # 用户id
#     picture = db.Column(db.String(60))     # 图片
#     label = db.Column(db.Text)  # 标签


# class Picture(db.Model):  # 图片
#     id = db.Column(db.String(60), primary_key=True)  # 主键，即路由
#     prompt = db.Column(db.Text)     # 修图的prompt，没有修图时为空
#     Ptype = db.Column(db.Integer)   # 图片类型，0是原图，1是简单修图，2是对话修图


# class Opencv(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     description = db.Column(db.Text)  # 正文
#     image = db.Column(db.String(60))
#     type = db.Column(db.String(10))
#     code = db.Column(db.Text)  # 代码


# # app = Flask(__name__)
# app.config.from_object(__name__)


# CORS(app, resources={r'/*': {'origins': '*'}})


# @app.route('/api/ping', methods=['GET'])
# def ping_pong():
#     return jsonify('pong!')


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/<path:fallback>')
# def fallback(fallback):       # Vue Router 的 mode 为 'hash' 时可移除该方法
#     if fallback.startswith('css/') or fallback.startswith('js/')\
#             or fallback.startswith('img/') or fallback == 'favicon.ico':
#         return app.send_static_file(fallback)
#     else:
#         return app.send_static_file('index.html')


# # 登录
# @app.route('/login', methods=['POST', 'GET'])
# @cross_origin(supports_credentials=True)
# def login():
#     data = request.form
#     username = data.get('username')
#     password = data.get('password')
#     user_type = data.get('userType')
#     print(username, password, user_type)

#     # 查询用户（仅根据用户名查询）
#     user = User.query.filter_by(name=username).first()

#     # 加密密码匹配
#     if user and bcrypt.check_password_hash(user.password, password):
#         if user_type == 'admin' and not user.is_admin:
#             return jsonify({'status': 'error', 'message': 'Unauthorized access for admin'}), 402
#         return jsonify({'status': 'success', 'message': 'Login successful', "user_id": user.id}), 200
#     else:
#         return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401


# # 注册
# @app.route('/register', methods=['POST', 'GET'])
# @cross_origin(supports_credentials=True)
# def register():
#     try:
#         if request.method == 'POST':
#             # 用户注册
#             latest_user = User.query.order_by(User.id.desc()).first()
#             id = latest_user.id + 1 if latest_user else 1
#             username = request.form['username']
#             password = request.form['password']
#             email = request.form['email']
#             user_type = request.form['userType']
#             invite_code = None
#             if user_type == "premium":
#                 invite_code = request.form['inviteCode']
#                 if invite_code not in ["kjk123456", "kjk654321", "kjk666888"]:
#                     print("invalid")
#                     return "error: invite code invalid", 401

#             # 加密密码
#             hashed_password = bcrypt.generate_password_hash(
#                 password).decode('utf-8')

#             default_avatar_url = 'http://graphcrafter.oss-cn-beijing.aliyuncs.com/avatars/1-default.webp'
#             user_now = User(id=id, name=username, password=hashed_password, email=email, is_premium=(
#                 user_type == 'premium'), photo=default_avatar_url)
#             # 用户名已占用
#             users = User.query.filter_by(name=username).all()
#             if users:
#                 return "error: username already taken", 400
#             # 用户名未占用，可注册
#             db.session.add(user_now)
#             db.session.commit()
#             return 'success', 200
#         return '', 405
#     except Exception as e:
#         # 捕获异常并记录错误信息
#         app.logger.error(f"Error during registration: {e}")
#         return "Internal Server Error", 500


# # @app.route('/api/opencvimages')
# # def get_images():

# #     images = Opencv.query.all()
# #     response = [{
# #         'id': img.id,
# #         'description': img.description,
# #         'image': img.image,
# #         'code': img.code,
# #     } for img in images]
# #     return jsonify(response)


# # 广场页模糊搜索帖子
# @app.route('/api/posts/search', methods=['GET'])
# @cross_origin(supports_credentials=True)
# def search_posts():
#     query = request.args.get('query', '')
#     if not query:
#         return jsonify({'posts': []})

#     posts = db.session.query(
#         Post.id,
#         Post.picture1,
#         Post.title,
#         User.name,
#         User.photo,
#         func.count(Like.id).label('like')
#     ).join(User, Post.author_id == User.id) \
#         .outerjoin(Like, Post.id == Like.post_id) \
#         .filter(Post.title.ilike(f'%{query}%')) \
#         .group_by(Post.picture1,
#                   Post.title,
#                   User.name,
#                   User.photo,
#                   Post.id) \
#         .all()

#     results = [{
#         'id': post[0],
#         'picture1': post[1],
#         'title': post[2],
#         'author': post[3],
#         'avatar': post[4],
#         'likes': post[5]
#     } for post in posts]

#     print(results)

#     return jsonify({'posts': results})


# @app.route('/api/opencvimages', methods=['GET'])
# def get_images():
#     opencv_imgs = Opencv.query.all()
#     print(opencv_imgs)

#     ids = []
#     pictures = []
#     descriptions = []
#     codes = []
#     types = []

#     for opencv_img in opencv_imgs:
#         ids.append(opencv_img.id)
#         pictures.append(opencv_img.image)
#         descriptions.append(opencv_img.description)
#         codes.append(opencv_img.code)
#         types.append(opencv_img.type)

#     response_json = jsonify({
#         'ids': ids,
#         'pictures': pictures,
#         'descriptions': descriptions,
#         'codes': codes,
#         'types': types,
#     })

#     return response_json


# # 示例用户资料
# @app.route('/api/user/<int:user_id>', methods=['GET'])
# def get_user_profile(user_id):
#     user = User.query.get(user_id)
#     if user:
#         return jsonify({
#             'id': user.id,
#             'name': user.name,
#             'photo': user.photo,
#             'email': user.email,
#             'age': user.age,
#             'sex': user.sex,
#             'is_premium': user.is_premium,
#             # 'senior': user.senior,
#             'bio': user.description
#         })
#     return jsonify({'error': 'User not found'}), 404


# # 显示被点赞数量
# def get_total_likes_count_for_user(user_id):
#     # Query to count unique likes per post for a specific author
#     likes_count = db.session.query(db.func.count(db.distinct(Like.id)))\
#                     .join(Post, Post.id == Like.post_id)\
#                     .filter(Post.author_id == user_id)\
#                     .scalar()
#     return likes_count

# # 显示被收藏数量


# def get_favorites_count_for_user(user_id):
#     # Query to count unique likes per post for a specific author
#     favorites_count = db.session.query(db.func.count(db.distinct(Collect.id)))\
#         .join(Post, Post.id == Collect.post_id)\
#         .filter(Post.author_id == user_id)\
#         .scalar()
#     return favorites_count


# # 获取指定作者的帖子的获赞与收藏总数
# @app.route('/api/user-stats/<int:user_id>')
# def user_stats(user_id):
#     likes_count = get_total_likes_count_for_user(user_id)
#     favorites_count = get_favorites_count_for_user(
#         user_id)  # Assuming you implement this
#     return jsonify({
#         'likes': likes_count,
#         'favorites': favorites_count
#     })


# # 获取关注和粉丝数量
# @app.route('/api/user/<int:user_id>/counts')
# def get_follow_counts(user_id):
#     # Count how many people the user is following
#     following_count = Follow.query.filter_by(follower_id=user_id).count()

#     # Count how many followers the user has
#     followers_count = Follow.query.filter_by(followed_id=user_id).count()

#     return jsonify({
#         'following_count': following_count,
#         'followers_count': followers_count
#     })


# # 得到我follow的人的列表
# @app.route('/api/followings/<int:user_id>')
# def get_followings(user_id):
#     # Fetching all users that the given user_id is following
#     followings = Follow.query.join(User, Follow.followed_id == User.id).filter(
#         Follow.follower_id == user_id).all()

#     # Preparing the data to return
#     following_list = []
#     for following in followings:
#         user = User.query.get(following.followed_id)

#         # Counting the followers of each followed user
#         followers_count = Follow.query.filter_by(followed_id=user.id).count()

#         # Counting the posts for each followed user
#         posts_count = Post.query.filter_by(
#             author_id=user.id, status=False).count()  # only counting active posts

#         following_list.append({
#             'id': user.id,
#             'name': user.name,
#             'avatar': user.photo,  # Assuming 'photo' is the correct field name for the user's avatar
#             'followers': followers_count,
#             'posts': posts_count
#         })

#     return jsonify({'followings': following_list})


# # 得到我follow的人的列表
# @app.route('/api/followers/<int:user_id>')
# def get_followers(user_id):
#     # Fetching all users that are following the given user_id
#     followers = Follow.query.join(User, Follow.follower_id == User.id).filter(
#         Follow.followed_id == user_id).all()

#     # Preparing the data to return
#     follower_list = []
#     for follower in followers:
#         user = User.query.get(follower.follower_id)

#         followers_count = Follow.query.filter_by(followed_id=user.id).count()

#         # Counting the active posts of this follower
#         posts_count = Post.query.filter_by(
#             author_id=user.id, status=False).count()

#         follower_list.append({
#             'id': user.id,
#             'name': user.name,
#             'avatar': user.photo,
#             'followers': followers_count,
#             'posts': posts_count
#         })

#     return jsonify({'followers': follower_list})

# ###################################################################################################################################################################################################################################################################################
# # 获取用户收藏


# @cross_origin()
# @app.route('/api/collection/<int:user_id>', methods=['GET'])
# def get_collection(user_id):
#     print(user_id, type(user_id))
#     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
#     collections = db.session.query(
#         Post.picture1,
#         Post.title,
#         User.name,
#         User.photo,
#         func.count(Like.id).label('like'),
#         Post.id
#     ).join(Collect, Post.id == Collect.post_id).join(User, Post.author_id == User.id).outerjoin(Like, Post.id == Like.post_id).filter(Collect.user_id == user_id).group_by(Post.picture1, Post.title, User.name, User.photo).all()
#     pictures = []
#     titles = []
#     authors = []
#     avatars = []
#     likes = []
#     ids = []
#     for collection in collections:
#         pictures.append(collection[0])
#         titles.append(collection[1])
#         authors.append(collection[2])
#         avatars.append(collection[3])
#         likes.append(collection[4])
#         ids.append(collection[5])
#     response_json = jsonify({
#         'pictures': pictures,
#         'titles': titles,
#         'authors': authors,
#         'avatars': avatars,
#         'likes': likes,
#         'ids': ids
#     })
#     return response_json
#     # return jsonify({'error': 'collect not found'}), 404

# # 获取个人笔记


# @cross_origin()
# @app.route('/api/note/<int:user_id>', methods=['GET'])
# def get_note(user_id):
#     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
#     # collections=db.session.query(
#     #     Post.picture1,
#     #     Post.title,
#     #     User.name,
#     #     User.photo,
#     #     func.count(Like.id).label('like')
#     # ).join(Collect, Post.id == Collect.post_id).join(User, Post.author_id == User.id).outerjoin(Like, Post.id == Like.post_id).filter(Collect.user_id == 1).group_by(Post.picture1, Post.title, User.name, User.photo).all()
#     # 构建查询
#     collections = db.session.query(
#         Post.picture1,
#         Post.title,
#         User.name,
#         User.photo,
#         func.count(Like.id).label('like'),
#         Post.id
#     ).join(User, Post.author_id == User.id).filter(User.id == user_id).outerjoin(Like, Post.id == Like.post_id).group_by(Post.picture1, Post.title, User.name, User.photo).all()
#     pictures = []
#     titles = []
#     authors = []
#     avatars = []
#     likes = []
#     ids = []
#     for collection in collections:
#         pictures.append(collection[0])
#         titles.append(collection[1])
#         authors.append(collection[2])
#         avatars.append(collection[3])
#         likes.append(collection[4])
#         ids.append(collection[5])
#     response_json = jsonify({
#         'pictures': pictures,
#         'titles': titles,
#         'authors': authors,
#         'avatars': avatars,
#         'likes': likes,
#         'ids': ids
#     })
#     return response_json
#     # return jsonify({'error': 'collect not found'}), 404

# # 获取草稿箱


# @cross_origin()
# @app.route('/api/drafts/<int:user_id>', methods=['GET'])
# def get_drafts(user_id):
#     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
#     drafts = db.session.query(
#         Draft.picture,
#         cast(Draft.date, String),
#         Draft.label,
#         Draft.id
#     ).join(User, Draft.user_id == User.id).filter(User.id == user_id).all()
#     pictures = []
#     dates = []
#     labels = []
#     ids = []
#     for draft in drafts:
#         pictures.append(draft[0])
#         dates.append(draft[1])
#         labels.append(draft[2])
#         ids.append(draft[3])
#     response_json = jsonify({
#         'pictures': pictures,
#         'dates': dates,
#         'labels': labels,
#         'ids': ids
#     })
#     return response_json
#     # return jsonify({'error': 'collect not found'}), 404

# # 获取草稿箱


# @cross_origin()
# @app.route('/api/get_draft/<int:post_id>', methods=['GET'])
# def get_draft(post_id):
#     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
#     draft = db.session.query(
#         Draft.picture,
#         cast(Draft.date, String),
#         Draft.label,
#         Draft.id
#     ).join(User, Draft.user_id == User.id).filter(User.id == 1, Draft.id == post_id).first()
#     response_json = jsonify({
#         'pictures': draft[0],
#         'dates': draft[1],
#         'labels': draft[2],
#         'ids': draft[3]
#     })
#     print({
#         'pictures': draft[0],
#         'dates': draft[1],
#         'labels': draft[2],
#         'ids': draft[3]
#     })
#     return response_json
#     # return jsonify({'error': 'collect not found'}), 404

# # 获取草稿箱标签


# @cross_origin()
# @app.route('/api/get_labels/<int:user_id>', methods=['GET'])
# def get_labels(user_id):
#     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
#     drafts = db.session.query(
#         Draft.label
#     ).join(User, Draft.user_id == User.id).filter(User.id == user_id).distinct()
#     labels = []
#     for draft in drafts:
#         labels.append(draft[0])
#     return labels
#     # return jsonify({'error': 'collect not found'}), 404

# # 根据标签获取草稿箱


# @cross_origin()
# @app.route('/api/search_drafts/<selected_label>', methods=['GET'])
# def search_drafts(selected_label):
#     print(selected_label)
#     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
#     drafts = db.session.query(
#         Draft.picture,
#         cast(Draft.date, String),
#         Draft.label,
#         Draft.id
#     ).join(User, Draft.user_id == User.id).filter(User.id == 1, Draft.label == selected_label).all()
#     pictures = []
#     dates = []
#     labels = []
#     ids = []
#     for draft in drafts:
#         pictures.append(draft[0])
#         dates.append(draft[1])
#         labels.append(draft[2])
#         ids.append(draft[3])
#     response_json = jsonify({
#         'pictures': pictures,
#         'dates': dates,
#         'labels': labels,
#         'ids': ids
#     })
#     return response_json
#     # return jsonify({'error': 'collect not found'}), 404

# # 草稿箱删除


# @cross_origin()
# @app.route('/api/del_draft/<int:post_id>', methods=['GET'])
# def del_draft(post_id):
#     draft_to_del = Draft.query.get(post_id)
#     db.session.delete(draft_to_del)
#     db.session.commit()
#     return jsonify({'message': 'Delete successfully'})

# # 暂存草稿


# @cross_origin()
# @app.route('/api/post_draft/', methods=['POST', 'GET'])
# def post_draft():
#     img = request.json.get('img')
#     user_id = request.json.get('user_id')
#     label = request.json.get('label')
#     from datetime import datetime
#     date = datetime.now()
#     if img:
#         new_draft = Draft(user_id=user_id, picture=img, date=date, label='1')
#         db.session.add(new_draft)
#         db.session.commit()
#     return jsonify({'message': 'Post draft successfully'})


# # 上传头像
# @app.route('/api/upload-avatar', methods=['POST'])
# def upload_avatar():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file uploaded'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     # 保存头像文件
#     filename = file.filename
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#     # 返回文件路径给前端
#     photo_url = url_for('serve_avatar', filename=filename)
#     return jsonify({'photo': photo_url})


# @app.route('/uploads/<filename>')
# def serve_avatar(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# # 查看要改的用户名是否已存在，要确保所有都是unique
# @app.route('/check-username', methods=['GET'])
# def check_username():
#     username = request.args.get('username')
#     user_id = request.args.get('user_id')
#     existing_user = User.query.filter(
#         User.name == username, User.id != user_id).first()
#     return jsonify(is_unique=existing_user is None)


# # 更新用户资料
# @app.route('/api/update-profile', methods=['POST'])
# def update_profile():
#     data = request.json
#     user = User.query.get(data.get('id'))
#     if not user:
#         return jsonify({'error': 'User not found'}), 404

#     user.name = data.get('name', user.name)
#     user.photo = data.get('photo', user.photo)
#     user.email = data.get('email', user.email)
#     user.sex = data.get('sex', user.sex)
#     user.age = data.get('age', user.age)
#     print(user.age)
#     user.description = data.get('bio', user.description)

#     db.session.commit()
#     return jsonify({'message': 'Profile updated successfully'})

# # 更新用户头像 URL


# @app.route('/api/update-avatar', methods=['POST'])
# def update_avatar():
#     data = request.json
#     user_id = data.get('user_id')
#     avatar_url = data.get('photo')

#     user = User.query.get(user_id)
#     if not user:
#         return jsonify({'error': 'User not found'}), 404

#     # 更新用户的头像 URL
#     user.photo = avatar_url
#     db.session.commit()

#     return jsonify({'message': 'Avatar updated successfully'})

# # 转换User格式


# def transUserData(user):
#     return {'id': user.id,
#             'name': user.name,
#             'avatar': user.photo,
#             }


# @app.route('/api/get-user-info/<int:user_id>', methods=['GET'])
# def get_user_info(user_id):
#     if user_id >= 0:
#         user = User.query.filter_by(id=user_id).first()
#         if user:
#             response = {
#                 'name': user.name,
#                 'avatar': user.photo
#             }
#             return jsonify(response), 200
#         else:
#             return jsonify({'error': 'User not found'}), 404
#     else:
#         return jsonify({'error': 'Userid parameter is required'}), 400

# # 转换时间格式


# def formatDateTime(time):
#     return time.strftime("%Y年%m月%d日 %H:%M:%S").replace("年0", "年").replace("月0", "月").replace("日0", "日")


# def parse_last_time(last_time_str):
#     return datetime.strptime(last_time_str, '%Y年%m月%d日 %H:%M:%S')

# # 获取历史消息


# @app.route('/api/chat/<int:user_id>', methods=['GET'])
# def get_chats(user_id):
#     print("get chats user:", user_id)
#     stuff_id = 0
#     chats = Chat.query.filter((Chat.receiver == user_id) | (
#         (Chat.sender == user_id) & (Chat.receiver != stuff_id))).all()
#     data = []
#     for chat in chats:
#         messages = Message.query.filter_by(
#             chat_id=chat.id).order_by(Message.id).all()
#         chat_data = {
#             'id': chat.id,
#             'sender': transUserData(User.query.get(chat.sender)),
#             'receiver': transUserData(User.query.get(chat.receiver)),
#             'unread_sender': chat.unread_sender,
#             'unread_receiver': chat.unread_receiver,
#             'last_time': formatDateTime(chat.last_time),
#             'messages': []
#         }
#         for message in messages:
#             user = User.query.get(message.user_id)
#             message_data = {
#                 'id': message.id,
#                 'type': message.type,
#                 'time': formatDateTime(message.time),
#                 'show_time': message.show_time,
#                 'content': message.content,
#                 'user': transUserData(user)
#             }
#             chat_data['messages'].append(message_data)
#         data.append(chat_data)
#     data.sort(key=lambda x: parse_last_time(
#         x['last_time']), reverse=True)  # 按最后一条消息的时间降序排序
#     print("chats data:", data)
#     return jsonify(data)


# @app.route('/api/chat-feedback/<int:user_id>', methods=['GET'])
# def get_chats_feedback(user_id):
#     print("get chats user:", user_id)
#     stuff_id = 0
#     if user_id != stuff_id:
#         chats = Chat.query.filter(
#             ((Chat.sender == user_id) & (Chat.receiver == stuff_id))).all()
#     else:
#         chats = Chat.query.filter((Chat.receiver == stuff_id)).all()
#     data = []
#     for chat in chats:
#         messages = Message.query.filter_by(
#             chat_id=chat.id).order_by(Message.id).all()
#         chat_data = {
#             'id': chat.id,
#             'sender': transUserData(User.query.get(chat.sender)),
#             'receiver': transUserData(User.query.get(chat.receiver)),
#             'unread_sender': chat.unread_sender,
#             'unread_receiver': chat.unread_receiver,
#             'last_time': formatDateTime(chat.last_time),
#             'messages': []
#         }
#         for message in messages:
#             user = User.query.get(message.user_id)
#             message_data = {
#                 'id': message.id,
#                 'type': message.type,
#                 'time': formatDateTime(message.time),
#                 'show_time': message.show_time,
#                 'content': message.content,
#                 'user': transUserData(user)
#             }
#             chat_data['messages'].append(message_data)
#         data.append(chat_data)
#     data.sort(key=lambda x: parse_last_time(
#         x['last_time']), reverse=True)  # 按最后一条消息的时间降序排序
#     print("chats data:", len(data))
#     return jsonify(data)

# # 新增会话


# @app.route('/create_chat', methods=['POST'])
# def create_chat():
#     data = request.get_json()
#     sender_id = data.get('sender_id')
#     receiver_id = data.get('receiver_id')

#     if sender_id == None or receiver_id == None:
#         return jsonify({"error": "Sender ID and Receiver ID are required"}), 400

#     # 查找是否已经存在包含 sender_id 和 receiver_id 的会话
#     chat = Chat.query.filter(
#         (Chat.sender == sender_id) & (Chat.receiver == receiver_id) |
#         (Chat.sender == receiver_id) & (Chat.receiver == sender_id)
#     ).first()

#     if chat:
#         # 如果会话已存在，更新 last_time
#         chat.last_time = datetime.now()
#         db.session.commit()
#         return jsonify({"message": "Chat updated successfully", "chat_id": chat.id}), 200
#     else:
#         # 获取当前数据库中最大的id值
#         max_id = db.session.query(db.func.max(Chat.id)).scalar()
#         new_id = (max_id or 0) + 1

#         new_chat = Chat(
#             id=new_id,
#             sender=sender_id,
#             receiver=receiver_id,
#             unread_sender=True,
#             unread_receiver=True,
#             last_time=datetime.now()
#         )
#         db.session.add(new_chat)
#         db.session.commit()

#     return jsonify({"message": "Chat created successfully", "chat_id": new_id}), 201

# # 删除指定会话


# @app.route('/api/delete_chat/<int:chat_id>', methods=['DELETE'])
# def delete_chat(chat_id):
#     chat = Chat.query.get(chat_id)
#     if not chat:
#         return jsonify({"error": "Chat not found"}), 404

#     db.session.delete(chat)
#     db.session.commit()

#     return jsonify({"message": "Chat and associated messages deleted successfully"}), 200


# # 检查对话是否为空，空则删去
# @app.route('/api/check_empty_chat', methods=['POST'])
# def check_empty_chat():
#     # 查询没有消息的聊天记录
#     empty_chats = Chat.query.filter(~Chat.messages.any()).all()

#     for chat in empty_chats:
#         db.session.delete(chat)
#     db.session.commit()

#     return jsonify({"message": f"Deleted {len(empty_chats)} empty chats."}), 200

# # 新增消息


# @app.route('/api/save_message', methods=['POST'])
# def receive_messages():
#     data = request.json
#     print(data)
#     chat_id = data.get('chat_id')
#     message = data.get('message')
#     show_time = data.get('show_time')
#     if not chat_id or not message:
#         return jsonify({'error': 'Invalid data provided'}), 400

#     chat = Chat.query.get(chat_id)
#     if not chat:
#         return jsonify({'error': 'Chat not found'}), 404

#     content = message.get('content')
#     if content:
#         message_datetime = datetime.strptime(
#             message.get('time'), '%Y年%m月%d日 %H:%M:%S')
#         max_message_id = db.session.query(func.max(Message.id)).scalar() or 0
#         next_message_id = max_message_id + 1
#         db_message = Message(
#             id=next_message_id,
#             type=message.get('type'),
#             time=message_datetime,
#             show_time=show_time,
#             content=content,
#             user_id=message.get('user')["id"],
#             chat_id=chat.id,
#         )
#         db.session.add(db_message)
#         # 更新时间
#         chat.last_time = message_datetime
#         db.session.commit()

#     return jsonify({'message_id': next_message_id}), 200

# # 删去消息


# @app.route('/api/delete_message', methods=['POST'])
# def delete_message():
#     message_id = request.json.get('message_id')
#     print("msg id:", message_id)
#     if message_id:
#         message = Message.query.get(message_id)
#         if message:
#             db.session.delete(message)
#             db.session.commit()
#             return 'Delete successfully', 200
#         else:
#             return 'Message not found', 404
#     else:
#         return 'No message ID provided', 400

# # 查询反馈


# @app.route('/api/feedback/<int:user_id>', methods=['GET'])
# def get_feedback(user_id):
#     stuff_id = 0  # 客服id
#     chats = Chat.query.filter((Chat.sender == user_id)
#                               & (Chat.receiver == stuff_id)).all()
#     data = []
#     for chat in chats:
#         messages = Message.query.filter_by(
#             chat_id=chat.id).order_by(Message.id).all()
#         chat_data = {
#             'id': chat.id,
#             'sender': transUserData(User.query.get(chat.sender)),
#             'receiver': transUserData(User.query.get(chat.receiver)),
#             'unread_sender': chat.unread_sender,
#             'unread_receiver': chat.unread_receiver,
#             'last_time': formatDateTime(chat.last_time),
#             'messages': []
#         }
#         for message in messages:
#             user = User.query.get(message.user_id)
#             message_data = {
#                 'id': message.id,
#                 'type': message.type,
#                 'time': formatDateTime(message.time),
#                 'content': message.content,
#                 'user': transUserData(user)
#             }
#             chat_data['messages'].append(message_data)
#         data.append(chat_data)

#     return jsonify(data)

# # 添加收藏


# @app.route('/api/add_collect', methods=['GET', 'POST'])
# def add_collect():
#     post_id = request.json.get('postId')  # 获取文章 ID
#     user_id = request.json.get('userId')  # 获取用户 ID
#     isAdd = request.json.get('add')
#     from datetime import datetime, timezone
#     date = datetime.now()
#     if isAdd and post_id and user_id:
#         new_Collect = Collect(date=date, user_id=user_id, post_id=post_id)
#         db.session.add(new_Collect)
#         db.session.commit()
#         return jsonify({'message': '收藏成功'})
#     elif not isAdd and post_id and user_id:
#         Collect.query.filter(
#             Collect.post_id == post_id and Collect.user_id == user_id).delete()
#         db.session.commit()
#         return jsonify({'message': '取消收藏成功'})
#     else:
#         return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400

# # 添加点赞


# @app.route('/api/add_like', methods=['GET', 'POST'])
# def add_like():
#     post_id = request.json.get('postId')  # 获取文章 ID
#     user_id = request.json.get('userId')  # 获取用户 ID
#     isAdd = request.json.get('add')
#     from datetime import datetime, timezone
#     date = datetime.now()
#     if isAdd and post_id and user_id:
#         new_Like = Like(date=date, author_id=user_id, post_id=post_id)
#         db.session.add(new_Like)
#         db.session.commit()
#         return jsonify({'message': '点赞成功'})
#     elif not isAdd and post_id and user_id:
#         Like.query.filter(
#             Like.post_id == post_id and Like.author_id == user_id).delete()
#         db.session.commit()
#         return jsonify({'message': '取消点赞成功'})
#     else:
#         return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400

# # 获取点赞和收藏的状态


# @app.route('/api/get_status/<int:post_id>/<int:userId>', methods=['GET'])
# def get_status(post_id, userId):
#     # post_id = request.json.get('postId')  # 获取文章 ID
#     # user_id = request.json.get('userId')  # 获取用户 ID
#     print('post:{},user:{}'.format(post_id, userId))
#     isLiked = db.session.query(
#         Like.id
#     ).filter(Like.post_id == post_id and Like.author_id == userId) \
#         .first()
#     isCollected = db.session.query(
#         Collect.id
#     ).filter(Collect.post_id == post_id and Collect.user_id == userId) \
#         .first()
#     if isLiked:
#         isLiked = '1'
#     else:
#         isLiked = '0'
#     if isCollected:
#         isCollected = '1'
#     else:
#         isCollected = '0'
#     response_json = jsonify({
#         'isLiked': isLiked,
#         'isCollected': isCollected
#     })
#     print({
#         'isLiked': isLiked,
#         'isCollected': isCollected
#     })
#     return response_json

# # 提交评论


# @app.route('/api/submit_comment', methods=['GET', 'POST'])
# def add_comment():
#     content = request.json.get('content')
#     post_id = request.json.get('postId')  # 获取文章 ID
#     user_id = request.json.get('userId')  # 获取用户 ID
#     post_id = int(post_id)
#     from datetime import datetime, timezone
#     date = datetime.now()
#     # date = date.strftime('%Y-%m-%d %H:%M:%S')
#     print(content)
#     # from datetime import datetime
#     # date = datetime.strptime(date, "%Y/%m/%d, %H:%M:%S")
#     if content and post_id:
#         new_comment = Comment(content=content,
#                               author_id=user_id,
#                               post_id=post_id,
#                               date=date)
#         db.session.add(new_comment)
#         db.session.commit()
#         newComment = db.session.query(
#             Comment.id,
#             # Comment.date,
#             cast(Comment.date, String),
#             Comment.content,
#             User.name,
#             User.photo
#         ).join(User, Comment.author_id == User.id) \
#             .outerjoin(Post, Comment.post_id == Post.id) \
#             .filter(Post.id == post_id) \
#             .order_by(desc(Comment.id)) \
#             .first()
#         response_json = jsonify({
#             'ids': newComment[0],
#             'dates': newComment[1],
#             'contents': newComment[2],
#             'authors': newComment[3],
#             'avatars': newComment[4]
#         })
#         print({
#             'ids': newComment[0],
#             'dates': newComment[1],
#             'contents': newComment[2],
#             'authors': newComment[3],
#             'avatars': newComment[4]
#         })
#         return response_json
#     else:
#         return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400

# # 获取帖子评论


# @app.route('/api/post_comments/<int:post_id>', methods=['GET'])
# def get_postComment(post_id):
#     # 首先是文章信息，包括内容、作者等
#     print(post_id)
#     comments = db.session.query(
#         Comment.id,
#         # Comment.date,
#         cast(Comment.date, String),
#         Comment.content,
#         User.name,
#         User.photo
#     ).join(User, Comment.author_id == User.id) \
#         .outerjoin(Post, Comment.post_id == Post.id) \
#         .filter(Post.id == post_id) \
#         .order_by(desc(Comment.id)) \
#         .all()
#     ids = []
#     dates = []
#     contents = []
#     authors = []
#     avatars = []
#     for comment in comments:
#         ids.append(comment[0])
#         dates.append(comment[1][:19])
#         contents.append(comment[2])
#         authors.append(comment[3])
#         avatars.append(comment[4])
#     response_json = jsonify({
#         'ids': ids,
#         'dates': dates,
#         'contents': contents,
#         'authors': authors,
#         'avatars': avatars
#     })
#     print({
#         'ids': ids,
#         'dates': dates,
#         'contents': contents,
#         'authors': authors,
#         'avatars': avatars
#     })
#     return response_json

# # 获取帖子评论


# @app.route('/api/all_comments/<int:user_id>', methods=['GET'])
# def get_allComment(user_id):
#     # 获取用户发表的所有帖子
#     posts = db.session.query(Post.id).filter(Post.author_id == user_id).all()
#     post_ids = [post.id for post in posts]

#     # 获取这些帖子的评论，以及评论的作者信息和帖子的第一张图片
#     comments = db.session.query(
#         Comment.id,
#         cast(Comment.date, String),
#         Comment.content,
#         User.name,
#         User.photo,
#         Post.picture1
#     ).join(User, Comment.author_id == User.id) \
#         .join(Post, Comment.post_id == Post.id) \
#         .filter(Post.id.in_(post_ids)) \
#         .order_by(desc(Comment.date)) \
#         .all()
#     ids = []
#     dates = []
#     contents = []
#     authors = []
#     avatars = []
#     pictures = []
#     for comment in comments:
#         ids.append(comment[0])
#         dates.append(comment[1][:19])
#         contents.append(comment[2])
#         authors.append(comment[3])
#         avatars.append(comment[4])
#         pictures.append(comment[5])
#     response_json = jsonify({
#         'ids': ids,
#         'dates': dates,
#         'contents': contents,
#         'authors': authors,
#         'avatars': avatars,
#         'pictures': pictures
#     })
#     print({
#         'ids': ids,
#         'dates': dates,
#         'contents': contents,
#         'authors': authors,
#         'avatars': avatars,
#         'pictures': pictures
#     })
#     return response_json

# # 获取帖子 （新增获取图片角标内容 by hzq）


# @app.route('/api/post_content/<int:post_id>', methods=['GET'])
# def get_postContent(post_id):
#     print(post_id)
#     # Expanded query to include User.id
#     contents = db.session.query(
#         Post.picture1,
#         Post.picture2,
#         Post.picture3,
#         Post.picture4,
#         Post.picture5,
#         cast(Post.date, String),
#         Post.title,
#         Post.body,
#         User.name,
#         User.photo,
#         User.id,  # Adding this to capture the author's ID
#         func.count(Like.id.distinct()).label('like'),
#         func.count(Comment.id.distinct()).label('comment'),
#         func.count(Collect.id.distinct()).label('collect'),
#         Post.id
#     ).join(User, Post.author_id == User.id) \
#         .outerjoin(Like, Post.id == Like.post_id) \
#         .outerjoin(Comment, Post.id == Comment.post_id) \
#         .outerjoin(Collect, Post.id == Collect.post_id) \
#         .filter(Post.id == post_id) \
#         .group_by(Post.id, User.id, User.name, User.photo) \
#         .order_by(desc(Post.id)) \
#         .all()

#     if contents:
#         content = contents[0]
#         pictures = [pic for pic in content[:5] if pic]
#         pic_types = []
#         # 查询 Picture 数据库获得每张图片的Ptype
#         for pic in pictures:
#             pic_type = Picture.query.filter_by(id=pic).first()
#             if not pic_type:
#                 pic_types.append(-1)
#             else:
#                 # 如果不存在，就置0
#                 pic_type = pic_type.Ptype
#                 if not pic_type:
#                     pic_types.append(-1)
#                 else:
#                     pic_types.append(pic_type)
#         print("pic_types", pic_types)
#         response_json = jsonify({
#             'pictures': pictures,
#             'date': content[5][:19],
#             'title': content[6],
#             'body': content[7],
#             'author': content[8],
#             'avatar': content[9],
#             'author_id': content[10],  # Using the fetched author ID
#             'likes_num': content[11],
#             'comments_num': content[12],
#             'collects_num': content[13],
#             'pic_tabs': pic_types,
#         })
#         print(response_json.get_json())
#         return response_json
#     else:
#         return jsonify({'error': 'Post not found'}), 404


# # 互相关注
# @app.route('/api/follow', methods=['POST'])
# def follow_user():
#     data = request.get_json()
#     follower_id = data.get('follower_id')
#     followed_id = data.get('followed_id')
#     # print(follower_id)
#     if follower_id == followed_id:
#         return jsonify({'error': 'Cannot follow yourself'}), 400

#     follow = Follow.query.filter_by(
#         follower_id=follower_id, followed_id=followed_id).first()
#     if follow:
#         # 已经存在关注记录，检查是否已经是互相关注
#         return jsonify({'message': 'Already followed', 'status': follow.status}), 409
#     else:
#         # 创建新的关注关系
#         new_follow = Follow(follower_id=follower_id,
#                             followed_id=followed_id, status=0)
#        # print(follower_id)
#         db.session.add(new_follow)

#         # 检查对方是否已关注当前用户，实现互相关注
#         reverse_follow = Follow.query.filter_by(
#             follower_id=followed_id, followed_id=follower_id).first()
#         if reverse_follow:
#             new_follow.status = 1
#             reverse_follow.status = 1
#             db.session.add(reverse_follow)

#         db.session.commit()
#         return jsonify({'message': 'Followed successfully', 'status': new_follow.status}), 200

# # 取消关注


# @app.route('/api/unfollow', methods=['POST'])
# def unfollow_user():
#     data = request.get_json()
#     follower_id = data.get('follower_id')
#     followed_id = data.get('followed_id')

#     if follower_id == followed_id:
#         return jsonify({'error': 'Cannot unfollow yourself'}), 400

#     # 查询是否存在关注记录
#     follow = Follow.query.filter_by(
#         follower_id=follower_id, followed_id=followed_id).first()
#     if not follow:
#         return jsonify({'message': 'No follow relation found'}), 404

#     # 存在关注记录，进行取消
#     db.session.delete(follow)

#     # 检查是否需要更新互相关注状态
#     reverse_follow = Follow.query.filter_by(
#         follower_id=followed_id, followed_id=follower_id).first()
#     if reverse_follow and reverse_follow.status == 1:
#         reverse_follow.status = 0  # 更新为非互相关注状态
#         db.session.add(reverse_follow)

#     db.session.commit()
#     return jsonify({'message': 'Unfollowed successfully'}), 200

# # 查看，来显示


# @app.route('/api/check-follow/<int:follower_id>/<int:followed_id>', methods=['GET'])
# def check_follow(follower_id, followed_id):
#     follow = Follow.query.filter_by(
#         follower_id=follower_id, followed_id=followed_id).first()
#     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     print(follow)
#     if follow:
#         return jsonify({'isFollowed': True, 'status': follow.status}), 200
#     else:
#         return jsonify({'isFollowed': False, 'status': 0}), 200


# # 广场页获取帖子
# # @cross_origin()
# @app.route('/api/posts', methods=['GET'])
# def get_posts():
#     posts = db.session.query(
#         Post.id,
#         Post.picture1,
#         Post.title,
#         User.name,
#         User.photo,
#         func.count(Like.id).label('like')
#     ).join(User, Post.author_id == User.id) \
#         .outerjoin(Like, Post.id == Like.post_id) \
#         .group_by(Post.picture1,
#                   Post.title,
#                   User.name,
#                   User.photo) \
#         .all()
#     ids = []
#     pictures = []
#     titles = []
#     authors = []
#     avatars = []
#     likes = []
#     for post in posts:
#         ids.append(post[0])
#         pictures.append(post[1])
#         titles.append(post[2])
#         authors.append(post[3])
#         avatars.append(post[4])
#         likes.append(post[5])
#     response_json = jsonify({
#         'ids': ids,
#         'pictures': pictures,
#         'titles': titles,
#         'authors': authors,
#         'avatars': avatars,
#         'likes': likes
#     })
#     # print({
#     #     'ids': ids,
#     #     'pictures': pictures,
#     #     'titles': titles,
#     #     'authors': authors,
#     #     'avatars': avatars,
#     #     'likes': likes
#     # })
#     return response_json

# # 广场页获取关注帖子
# # @cross_origin()


# @app.route('/api/follow_posts/<int:user_id>', methods=['GET'])
# def get_followposts(user_id):
#     # user_id = 1  # Replace with the current logged in user's ID
#     posts = db.session.query(
#         Post.id,
#         Post.picture1,
#         Post.title,
#         User.name,
#         User.photo,
#         func.count(Like.id).label('like')
#     ).join(User, Post.author_id == User.id) \
#         .outerjoin(Like, Post.id == Like.post_id) \
#         .join(Follow, Follow.followed_id == Post.author_id) \
#         .filter(Follow.follower_id == user_id) \
#         .group_by(Post.picture1,
#                   Post.title,
#                   User.name,
#                   User.photo) \
#         .all()
#     ids = []
#     pictures = []
#     titles = []
#     authors = []
#     avatars = []
#     likes = []
#     for post in posts:
#         ids.append(post[0])
#         pictures.append(post[1])
#         titles.append(post[2])
#         authors.append(post[3])
#         avatars.append(post[4])
#         likes.append(post[5])
#     response_json = jsonify({
#         'ids': ids,
#         'pictures': pictures,
#         'titles': titles,
#         'authors': authors,
#         'avatars': avatars,
#         'likes': likes
#     })
#     # print({
#     #     'ids': ids,
#     #     'pictures': pictures,
#     #     'titles': titles,
#     #     'authors': authors,
#     #     'avatars': avatars,
#     #     'likes': likes
#     # })
#     return response_json


# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')


# @socketio.on('disconnect')
# def handle_disconnect():
#     print('Client disconnected')


# @socketio.on('join')
# def handle_join(data):
#     print("join:", data)
#     chat_id = data['chat_id']
#     join_room(chat_id)


# @socketio.on('message')
# def handle_message(data):
#     chat_id = data['chat_id']
#     print("chat:", chat_id)
#     emit('message', {'message': data['message']}, room=chat_id)

# # 管理员相关函数
# # 获取所有用户


# @app.route('/api/get-all-user', methods=['GET'])
# def get_all_users():
#     users = User.query.all()
#     users_data = []

#     for user in users:
#         if user.is_admin:
#             continue
#         user_data = {
#             'id': user.id,
#             'name': user.name,
#             'password': user.password,
#             'avatar': user.photo,
#             'email': user.email,
#             'age': user.age,
#             'sex': user.sex,
#             'senior': user.is_premium,
#             'description': user.description,
#             'status': user.status
#         }
#         users_data.append(user_data)

#     return jsonify({'userList': users_data})


# # 获取用户和帖子总数
# @app.route('/api/get-user-post-num', methods=['GET'])
# def get_user_post_num():
#     users = User.query.all()
#     posts = Post.query.all()
#     return jsonify({'userNum': len(users), 'postNum': len(posts)})

# # 获取所有帖子


# @app.route('/api/get-all-post', methods=['GET'])
# def get_all_posts():
#     posts = Post.query.all()
#     posts_data = []

#     for post in posts:
#         post_data = {
#             'id': post.id,
#             'author_id': post.author_id,
#             'date': formatDateTime(post.date),
#             'pics': [post.picture1, post.picture2, post.picture3, post.picture4, post.picture5],
#             'title': post.title,
#             'content': post.body,
#             'status': post.status
#         }
#         posts_data.append(post_data)

#     return jsonify({'dataList': posts_data})

# # 更新用户状态 禁用和正常来回切换


# @app.route('/api/update-user-status/<int:user_id>', methods=['POST'])
# def update_user_status(user_id):
#     user = User.query.get(user_id)
#     if user is None:
#         return jsonify({'error': 'User not found'}), 404

#     # 切换帖子状态
#     user.status = not user.status
#     db.session.commit()

#     return jsonify({'success': 'User status updated successfully', 'new_status': user.status})

# # 更新帖子状态 禁用和正常来回切换


# @app.route('/api/update-post-status/<int:post_id>', methods=['POST'])
# def update_post_status(post_id):
#     print(post_id)
#     post = Post.query.get(post_id)
#     if post is None:
#         return jsonify({'error': 'Post not found'}), 404

#     post.status = not post.status
#     db.session.commit()

#     return jsonify({'success': 'Post status updated successfully', 'new_status': post.status})

# # 发布动态


# @app.route('/api/postnotes', methods=['GET', 'POST'])
# def postnotes():
#     dataform = request.json.get('pics')
#     title = request.json.get('title')
#     description = request.json.get('description')
#     user_id = request.json.get('userId')  # 获取用户 ID
#     # user_id = 1
#     # 获取dataform的实际大小
#     cnt = len(dataform)
#     pic1 = ''
#     pic2 = ''
#     pic3 = ''
#     pic4 = ''
#     pic5 = ''
#     if cnt >= 1:
#         pic1 = dataform[0]
#     if cnt >= 2:
#         pic2 = dataform[1]
#     if cnt >= 3:
#         pic3 = dataform[2]
#     if cnt >= 4:
#         pic4 = dataform[3]
#     if cnt >= 5:
#         pic5 = dataform[4]
#     # 谁定义的数据表，表项名字那么长...pic不好么
#     dateToday = datetime.now()
#     print(dateToday)
#     post = Post(date=dateToday, author_id=user_id, title=title, body=description,
#                 picture1=pic1, picture2=pic2, picture3=pic3, picture4=pic4, picture5=pic5)
#     db.session.add(post)
#     db.session.commit()
#     return jsonify({'message': 'Post created successfully'})

# # 后端一键修图指令
# # 参数：img_url(原图URL) + img_select(对应的模板url，用于寻找prompt)
# # 本地调试请注释该函数！！！！！！！


# @app.route('/api/call_P2P', methods=['GET', 'POST'])
# def call_P2P():
#     img_old = request.json.get('img_url')
#     img_select = request.json.get('img_select')
#     user_id = request.json.get('user_id')
#     print(img_old, img_select, user_id)
#     # if img_old is None or img_select is None or user_id is None:
#     #     return jsonify({'img': 'Invalid data provided'}), 400
#     # 查询Picture数据表，找到对应的prompt
#     pic_tmp = Picture(id=img_select, prompt='turn it yellow.')
#     db.session.add(pic_tmp)
#     db.session.commit()
#     prompt = Picture.query.filter_by(id=img_select).first().prompt
#     if prompt is None:
#         print("prompt is None")
#         return jsonify({'img': 'Prompt not found'})
#     # 调用修图指令
#     # img_new = os.system("python /root/Code/Models/P2P/P2P.py --img_url "+img_old+" --prompt "+prompt)
#     # 函数调用修图命令，存储为/mod/{prompt+"_modify_"+img_old}
#     sys.path.append(r'/root/Code/Models/P2P')
#     import P2P
#     P2P.modify_pic(img_old, prompt)
#     # 上传阿里云图床
#     # OSS_ACCESS_KEY_ID = "LTAI5tR1c1uhFRfWxjq8BWT4"
#     # OSS_ACCESS_KEY_SECRET = "BdN5OIEdet7IO6KWOq7TJiivHOsC5B"
#     auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
#     bucket = oss2.Bucket(
#         auth, 'https://oss-cn-beijing.aliyuncs.com', 'graphcrafter')
#     # /root/Code/Models/P2P/weights
#     prompt = prompt.replace(" ", "")
#     mod_img_url = prompt + "_modify_" + img_old.split("/")[-1]
#     with open(mod_img_url, mode="rb") as fileobj:
#         fileobj.seek(0, os.SEEK_SET)
#         current = fileobj.tell()
#         bucket_url = user_id+'/'+prompt + "_modify_" + img_old.split("/")[-1]
#         bucket.put_object(bucket_url, fileobj)
#         # 删除文件夹中的图片
#         os.remove(mod_img_url)
#         print("https://graphcrafter.oss-cn-beijing.aliyuncs.com/" + bucket_url)
#         return jsonify({'img': "https://graphcrafter.oss-cn-beijing.aliyuncs.com/" + bucket_url})
#     return jsonify({'img': None})

# # 对话修图指令
# @app.route('/api/chat_P2P', methods=['GET', 'POST'])
# def chat_P2P():
#     img_old = request.json.get('img_url')
#     # img_select = request.json.get('img_select')
#     prompt = request.json.get('prompt')
#     user_id = request.json.get('user_id')
#     # print(img_old, img_select, user_id)
#     if img_old is None or prompt is None or user_id is None:
#         return jsonify({'img': 'Invalid data provided'}), 400
#     # 查询Picture数据表，找到对应的prompt
#     # pic_tmp = Picture(id=img_select, prompt='turn it yellow.')
#     # db.session.add(pic_tmp)
#     # db.session.commit()
#     # prompt = Picture.query.filter_by(id=img_select).first().prompt
#     # if prompt is None:
#     #     print("prompt is None")
#     #     return jsonify({'img': 'Prompt not found'})
#     # 调用修图指令
#     # img_new = os.system("python /root/Code/Models/P2P/P2P.py --img_url "+img_old+" --prompt "+prompt)
#     # 函数调用修图命令，存储为/mod/{prompt+"_modify_"+img_old}
#     sys.path.append(r'/root/Code/Models/P2P')
#     import P2P
#     print("promptpromptpromptpromptprompt ",prompt)
#     P2P.modify_pic(img_old, prompt)
#     # 上传阿里云图床
#     # OSS_ACCESS_KEY_ID = "LTAI5tR1c1uhFRfWxjq8BWT4"
#     # OSS_ACCESS_KEY_SECRET = "BdN5OIEdet7IO6KWOq7TJiivHOsC5B"
#     auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
#     bucket = oss2.Bucket(
#         auth, 'https://oss-cn-beijing.aliyuncs.com', 'graphcrafter')
#     # /root/Code/Models/P2P/weights
#     prompt = prompt.replace(" ", "")
#     mod_img_url = prompt + "_modify_" + img_old.split("/")[-1]
#     with open(mod_img_url, mode="rb") as fileobj:
#         fileobj.seek(0, os.SEEK_SET)
#         current = fileobj.tell()
#         bucket_url = user_id+'/'+prompt + "_modify_" + img_old.split("/")[-1]
#         bucket.put_object(bucket_url, fileobj)
#         # 删除文件夹中的图片
#         os.remove(mod_img_url)
#         print("https://graphcrafter.oss-cn-beijing.aliyuncs.com/" + bucket_url)
#         return jsonify({'img': "https://graphcrafter.oss-cn-beijing.aliyuncs.com/" + bucket_url})
#     return jsonify({'img': None})

# # 删除帖子的接口
# @app.route('/api/delete-post/<int:post_id>', methods=['DELETE'])
# def delete_post(post_id):
#     post = Post.query.get_or_404(post_id)

#     # 删除相关的评论
#     Comment.query.filter_by(post_id=post_id).delete()

#     # 删除相关的点赞
#     Like.query.filter_by(post_id=post_id).delete()

#     # 删除相关的收藏
#     Collect.query.filter_by(post_id=post_id).delete()

#     # 删除帖子
#     db.session.delete(post)
#     db.session.commit()

#     return jsonify({'message': 'Post deleted successfully'}), 200

# # 基本图像处理
# @app.route('/api/simple-image-process', methods=['POST'])
# def process_image_simple():
#     print(request.files)
#     print("form:", request.form)
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file uploaded'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     # 读取参数
#     user_id = request.form.get('user_id')
#     # 处理的类别 eg.图像色彩，图像变换...
#     process_category = request.form.get('process_category')
#     process_type = request.form.get('process_type')  # 具体的处理类型 eg.色调

#     if not user_id or not process_category or not process_type:
#         return jsonify({'error': 'Missing processing parameters'}), 400

#     # 读取图片文件
#     file_stream = io.BytesIO(file.read())
#     file_bytes = np.frombuffer(file_stream.read(), np.uint8)
#     origin = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#     height, width, channels = origin.shape
#     img_size = [width, height]
#     print("image size:", height, width)

#     if origin is None:
#         return jsonify({'error': 'Failed to read the uploaded image'}), 500

#     # 进行图像处理
#     # 处理后的图片暂存为tmp.png
#     if process_category == "color":
#         show_hsv(origin, process_type, img_size)
#     elif process_category == "transform":
#         show_transformation(origin, process_type, img_size)
#     elif process_category == "filter":
#         show_filtering(origin, process_type, img_size)
#     elif process_category == "outline":
#         show_outline(origin, process_type, img_size)
#     elif process_category == "enhance":
#         show_enhancement(origin, process_type, img_size)
#     else:
#         return jsonify({'error': 'Process category chosen does not exits'}), 400

#     # 上传到阿里云OSS
#     tmp_file_path = './img_tmp/tmp.png'
#     current_time = datetime.now().strftime('%Y%m%d%H%M%S')
#     oss_file_path = f'simple_image_process/{user_id}-{current_time}.png'
#     with open(tmp_file_path, 'rb') as file:
#         bucket.put_object(oss_file_path, file)
#     img_url = f'http://{OSS_BUCKET_NAME}.{OSS_ENDPOINT}/{oss_file_path}'
#     print(img_url)

#     return jsonify({'imgUrl': img_url})

# # 对话功能中的信息预获取
# @app.route('/api/get_info', methods=['POST','GET'])
# def get_personal_info():
#     personal_id = request.json.get('user_id')
#     # 查询用户数据库获取头像
#     person_avatar = User.query.filter_by(id=personal_id).first().photo
#     return jsonify({'info':person_avatar})

# if __name__ == '__main__':
#     config = dict(
#         host='0.0.0.0',
#         port=3306,
#         debug=True,
#         allow_unsafe_werkzeug=True
#     )
#     socketio.run(app, **config)

from io import BytesIO
import base64
import openai
from flask import redirect
import sys
import os
from flask import Flask, jsonify, request, render_template, url_for, send_from_directory
from flask_cors import CORS, cross_origin

from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
from sqlalchemy import func, cast, String, desc
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt     # 密码加密

from flask_socketio import SocketIO, emit, join_room
from datetime import datetime

# 用于数据库一键初始化 by hzq
from flask_migrate import Migrate


# 后端上传阿里云图床
import oss2
import os
from oss2.credentials import EnvironmentVariableCredentialsProvider

# 简单图像处理
import io
import numpy as np
import cv2
from simple_image_process.image_filtering import show_filtering
from simple_image_process.image_outline import show_outline
from simple_image_process.image_transformation import show_transformation
from simple_image_process.image_color import show_hsv
from simple_image_process.image_enhancement import show_enhancement
import requests

# 防止通信报错 by zyp
# import locale
# locale.setlocale(locale.LC_CTYPE, "chinese")

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__, static_url_path='/',
            static_folder='./../frontend/dist', template_folder='./../frontend/dist')
# socketio = SocketIO(app, cors_allowed_origins="http://localhost:5173") http://10.80.42.173/Demo
socketio = SocketIO(app, cors_allowed_origins="http://10.80.42.173/message")

# 创建数据库
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + \
    os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 关闭对模型修改的监控
db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app
migrate = Migrate(app, db)


# 阿里云OSS相关信息
OSS_ACCESS_KEY_ID = 'LTAI5tR1c1uhFRfWxjq8BWT4'
OSS_ACCESS_KEY_SECRET = 'BdN5OIEdet7IO6KWOq7TJiivHOsC5B'
OSS_ENDPOINT = 'oss-cn-beijing.aliyuncs.com'
OSS_BUCKET_NAME = 'graphcrafter'
auth = oss2.Auth(OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET)
bucket = oss2.Bucket(auth, OSS_ENDPOINT, OSS_BUCKET_NAME)
bcrypt = Bcrypt(app)


class User(db.Model):  # 用户
    id = db.Column(db.Integer, primary_key=True)  # 主键，账号
    name = db.Column(db.String(20))  # 名字
    password = db.Column(db.String(20))  # 密码
    photo = db.Column(db.String(60))  # 头像
    email = db.Column(db.String(254))  # 邮箱
    age = db.Column(db.Integer)  # 年龄
    sex = db.Column(db.Boolean)  # 性别，1是男0是女
    is_admin = db.Column(db.Boolean, default=False)
    is_premium = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(100))  # 一句话介绍自己
    status = db.Column(db.Boolean)  # 是否正常 0正常 1被封


class Post(db.Model):  # 帖子
    id = db.Column(db.Integer, primary_key=True)  # 主键
    author_id = db.Column(db.Integer)      # 作者id
    date = db.Column(db.DateTime)     # 日期
    picture1 = db.Column(db.String(60))     # 图片1，默认为封面
    picture2 = db.Column(db.String(60))     # 图片2
    picture3 = db.Column(db.String(60))     # 图片3
    picture4 = db.Column(db.String(60))     # 图片4
    picture5 = db.Column(db.String(60))     # 图片5
    title = db.Column(db.String(60))     # 标题
    body = db.Column(db.Text)  # 正文
    model = db.Column(db.Integer)  # 模型参数id
    status = db.Column(db.Boolean)  # 状态，0是正常 1是被禁


class Comment(db.Model):  # 评论
    id = db.Column(db.Integer, primary_key=True)  # 主键
    date = db.Column(db.DateTime)     # 日期
    content = db.Column(db.Text)  # 正文
    author_id = db.Column(db.Integer)      # 作者id
    post_id = db.Column(db.Integer)      # 文章id


class Like(db.Model):  # 点赞
    id = db.Column(db.Integer, primary_key=True)  # 主键
    date = db.Column(db.DateTime)     # 日期
    author_id = db.Column(db.Integer)      # 点赞者id
    post_id = db.Column(db.Integer)      # 文章id


class Collect(db.Model):  # 收藏
    id = db.Column(db.Integer, primary_key=True)  # 主键
    date = db.Column(db.DateTime)     # 日期
    user_id = db.Column(db.Integer)      # 作者id
    post_id = db.Column(db.Integer)      # 文章id


class Follow(db.Model):  # 关注
    id = db.Column(db.Integer, primary_key=True)  # 主键
    follower_id = db.Column(db.Integer)      # 粉丝id
    followed_id = db.Column(db.Integer)      # 被关注者id
    status = db.Column(db.Integer)      # 关注状态,0表示单独关注，1表示互相关注


class FeedBack(db.Model):  # 用户反馈
    id = db.Column(db.Integer, primary_key=True)  # 主键
    date = db.Column(db.DateTime)     # 日期
    user_id = db.Column(db.Integer)      # 用户id
    content = db.Column(db.Text)  # 正文
    processed = db.Column(db.Boolean)  # 是否已处理
    back_content = db.Column(db.Text)  # 反馈内容


class ModifyHistory(db.Model):  # 修图历史
    id = db.Column(db.Integer, primary_key=True)  # 主键
    date = db.Column(db.DateTime)     # 日期
    user_id = db.Column(db.Integer)      # 用户id
    pic_before = db.Column(db.String(60))     # 修改前图片
    pic_after = db.Column(db.String(60))     # 修改后图片
    prompt = db.Column(db.Text)  # 提示
    model_id = db.Column(db.Integer)  # 模型参数


class Message(db.Model):  # 单条消息记录
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    type = db.Column(db.String(60))  # 消息的类型
    time = db.Column(db.DateTime)  # 发送时间
    show_time = db.Column(db.Boolean)  # 该条消息的时间是否显示
    content = db.Column(db.Text)  # 内容
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 发送的用户id
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))  # 关联Chat模型的id


class Chat(db.Model):  # 会话
    __tablename__ = 'chat'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    sender = db.Column(db.Integer)  # 发起者的id
    receiver = db.Column(db.Integer)  # 接收者的id
    unread_sender = db.Column(db.Boolean)  # 发起者是否已经阅读
    unread_receiver = db.Column(db.Boolean)  # 接收者是否已经阅读
    last_time = db.Column(db.DateTime)  # 最后一条消息的时间
    messages = relationship("Message", backref="chat",
                            cascade="all, delete-orphan")  # 包含的消息 一对多


class Draft(db.Model):  # 草稿箱
    __tablename__ = 'Draft'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    date = db.Column(db.DateTime)     # 日期
    user_id = db.Column(db.Integer)      # 用户id
    picture = db.Column(db.String(60))     # 图片
    label = db.Column(db.Text)  # 标签


class Picture(db.Model):  # 图片
    id = db.Column(db.String(60), primary_key=True)  # 主键，即路由
    prompt = db.Column(db.Text)     # 修图的prompt，没有修图时为空
    Ptype = db.Column(db.Integer)   # 图片类型，0是原图，1是简单修图，2是对话修图


class Opencv(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    description = db.Column(db.Text)  # 正文
    image = db.Column(db.String(60))
    type = db.Column(db.String(10))
    code = db.Column(db.Text)  # 代码


class History(db.Model):  # 图像评估聊天历史
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    role = db.Column(db.String(60))  # 消息方
    time = db.Column(db.String(60))
    content = db.Column(db.Text)  # 内容
    user_id = db.Column(db.Integer)  # 用户id
    picture = db.Column(db.String(60))  # 图片


# app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:fallback>')
def fallback(fallback):       # Vue Router 的 mode 为 'hash' 时可移除该方法
    if fallback.startswith('css/') or fallback.startswith('js/')\
            or fallback.startswith('img/') or fallback == 'favicon.ico':
        return app.send_static_file(fallback)
    else:
        return app.send_static_file('index.html')


# 登录
@app.route('/login', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    user_type = data.get('userType')
    print(username, password, user_type)

    # 查询用户（仅根据用户名查询）
    user = User.query.filter_by(name=username).first()

    # 加密密码匹配
    if user and bcrypt.check_password_hash(user.password, password):
        if user_type == 'admin' and not user.is_admin:
            return jsonify({'status': 'error', 'message': 'Unauthorized access for admin'}), 402
        return jsonify({'status': 'success', 'message': 'Login successful', "user_id": user.id, "isAdmin": user.is_admin}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401


# 注册
@app.route('/register', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def register():
    try:
        if request.method == 'POST':
            # 用户注册
            latest_user = User.query.order_by(User.id.desc()).first()
            id = latest_user.id + 1 if latest_user else 1
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            user_type = request.form['userType']
            invite_code = None
            if user_type == "premium":
                invite_code = request.form['inviteCode']
                if invite_code not in ["kjk123456", "kjk654321", "kjk666888"]:
                    print("invalid")
                    return "error: invite code invalid", 401

            # 加密密码
            hashed_password = bcrypt.generate_password_hash(
                password).decode('utf-8')

            default_avatar_url = 'http://graphcrafter.oss-cn-beijing.aliyuncs.com/avatars/1-default.webp'
            user_now = User(id=id, name=username, password=hashed_password, email=email, is_premium=(
                user_type == 'premium'), photo=default_avatar_url)
            # 用户名已占用
            users = User.query.filter_by(name=username).all()
            if users:
                return "error: username already taken", 400
            # 用户名未占用，可注册
            db.session.add(user_now)
            db.session.commit()
            return 'success', 200
        return '', 405
    except Exception as e:
        # 捕获异常并记录错误信息
        app.logger.error(f"Error during registration: {e}")
        return "Internal Server Error", 500


# @app.route('/api/opencvimages')
# def get_images():

#     images = Opencv.query.all()
#     response = [{
#         'id': img.id,
#         'description': img.description,
#         'image': img.image,
#         'code': img.code,
#     } for img in images]
#     return jsonify(response)


# 广场页模糊搜索帖子
@app.route('/api/posts/search', methods=['GET'])
@cross_origin(supports_credentials=True)
def search_posts():
    query = request.args.get('query', '')
    if not query:
        return jsonify({'posts': []})

    posts = db.session.query(
        Post.id,
        Post.picture1,
        Post.title,
        User.name,
        User.photo,
        func.count(Like.id).label('like')
    ).join(User, Post.author_id == User.id) \
        .outerjoin(Like, Post.id == Like.post_id) \
        .filter(Post.title.ilike(f'%{query}%')) \
        .group_by(Post.picture1,
                  Post.title,
                  User.name,
                  User.photo,
                  Post.id) \
        .all()

    results = [{
        'id': post[0],
        'picture1': post[1],
        'title': post[2],
        'author': post[3],
        'avatar': post[4],
        'likes': post[5]
    } for post in posts]

    print(results)

    return jsonify({'posts': results})


# 广场页模糊搜索用户
@app.route('/api/users/search', methods=['GET'])
@cross_origin(supports_credentials=True)
def search_users():
    query = request.args.get('query', '')
    current_user_id = request.args.get('userId')  # 获取前端传来的当前用户 ID
    if not query:
        return jsonify({'users': []})

    users = User.query.filter(User.name.ilike(f'%{query}%')).all()
    results = []

    for user in users:
        is_followed = Follow.query.filter_by(
            follower_id=current_user_id, followed_id=user.id).first() is not None
        followers_count = Follow.query.filter_by(followed_id=user.id).count()
        posts_count = Post.query.filter_by(author_id=user.id).count()
        is_follower = Follow.query.filter_by(
            followed_id=current_user_id, follower_id=user.id).first() is not None
        results.append({
            'id': user.id,
            'name': user.name,
            'photo': user.photo,
            'followers': followers_count,
            'posts': posts_count,
            'is_followed': is_followed,
            'is_follower': is_follower
        })
    print(results)
    return jsonify({'users': results})


@app.route('/api/opencvimages', methods=['GET'])
def get_images():
    opencv_imgs = Opencv.query.all()
    print(opencv_imgs)

    ids = []
    pictures = []
    descriptions = []
    codes = []
    types = []

    for opencv_img in opencv_imgs:
        ids.append(opencv_img.id)
        pictures.append(opencv_img.image)
        descriptions.append(opencv_img.description)
        codes.append(opencv_img.code)
        types.append(opencv_img.type)

    response_json = jsonify({
        'ids': ids,
        'pictures': pictures,
        'descriptions': descriptions,
        'codes': codes,
        'types': types,
    })

    return response_json


# 示例用户资料
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'photo': user.photo,
            'email': user.email,
            'age': user.age,
            'sex': user.sex,
            'is_premium': user.is_premium,
            # 'senior': user.senior,
            'bio': user.description
        })
    return jsonify({'error': 'User not found'}), 404


# 显示被点赞数量
def get_total_likes_count_for_user(user_id):
    # Query to count unique likes per post for a specific author
    likes_count = db.session.query(db.func.count(db.distinct(Like.id)))\
                    .join(Post, Post.id == Like.post_id)\
                    .filter(Post.author_id == user_id)\
                    .scalar()
    return likes_count

# 显示被收藏数量


def get_favorites_count_for_user(user_id):
    # Query to count unique likes per post for a specific author
    favorites_count = db.session.query(db.func.count(db.distinct(Collect.id)))\
        .join(Post, Post.id == Collect.post_id)\
        .filter(Post.author_id == user_id)\
        .scalar()
    return favorites_count


# 获取指定作者的帖子的获赞与收藏总数
@app.route('/api/user-stats/<int:user_id>')
def user_stats(user_id):
    likes_count = get_total_likes_count_for_user(user_id)
    favorites_count = get_favorites_count_for_user(
        user_id)  # Assuming you implement this
    return jsonify({
        'likes': likes_count,
        'favorites': favorites_count
    })


# 获取关注和粉丝数量
@app.route('/api/user/<int:user_id>/counts')
def get_follow_counts(user_id):
    # Count how many people the user is following
    following_count = Follow.query.filter_by(follower_id=user_id).count()

    # Count how many followers the user has
    followers_count = Follow.query.filter_by(followed_id=user_id).count()

    return jsonify({
        'following_count': following_count,
        'followers_count': followers_count
    })


# 得到我follow的人的列表
@app.route('/api/followings/<int:user_id>')
def get_followings(user_id):
    # Fetching all users that the given user_id is following
    followings = Follow.query.join(User, Follow.followed_id == User.id).filter(
        Follow.follower_id == user_id).all()

    # Preparing the data to return
    following_list = []
    for following in followings:
        user = User.query.get(following.followed_id)

        # Counting the followers of each followed user
        followers_count = Follow.query.filter_by(followed_id=user.id).count()

        # Counting the posts for each followed user
        posts_count = Post.query.filter_by(
            author_id=user.id, status=False).count()  # only counting active posts

        following_list.append({
            'id': user.id,
            'name': user.name,
            'avatar': user.photo,  # Assuming 'photo' is the correct field name for the user's avatar
            'followers': followers_count,
            'posts': posts_count
        })

    return jsonify({'followings': following_list})


# 得到我follow的人的列表
@app.route('/api/followers/<int:user_id>')
def get_followers(user_id):
    # Fetching all users that are following the given user_id
    followers = Follow.query.join(User, Follow.follower_id == User.id).filter(
        Follow.followed_id == user_id).all()

    # Preparing the data to return
    follower_list = []
    for follower in followers:
        user = User.query.get(follower.follower_id)

        followers_count = Follow.query.filter_by(followed_id=user.id).count()

        # Counting the active posts of this follower
        posts_count = Post.query.filter_by(
            author_id=user.id, status=False).count()

        follower_list.append({
            'id': user.id,
            'name': user.name,
            'avatar': user.photo,
            'followers': followers_count,
            'posts': posts_count
        })

    return jsonify({'followers': follower_list})

###################################################################################################################################################################################################################################################################################
# 获取用户收藏


@cross_origin()
@app.route('/api/collection/<int:user_id>', methods=['GET'])
def get_collection(user_id):
    print(user_id, type(user_id))
    # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
    collections = db.session.query(
        Post.picture1,
        Post.title,
        User.name,
        User.photo,
        func.count(Like.id).label('like'),
        Post.id
    ).join(Collect, Post.id == Collect.post_id).join(User, Post.author_id == User.id).outerjoin(Like, Post.id == Like.post_id).filter(Collect.user_id == user_id).group_by(Post.picture1, Post.title, User.name, User.photo).all()
    pictures = []
    titles = []
    authors = []
    avatars = []
    likes = []
    ids = []
    for collection in collections:
        pictures.append(collection[0])
        titles.append(collection[1])
        authors.append(collection[2])
        avatars.append(collection[3])
        likes.append(collection[4])
        ids.append(collection[5])
    response_json = jsonify({
        'pictures': pictures,
        'titles': titles,
        'authors': authors,
        'avatars': avatars,
        'likes': likes,
        'ids': ids
    })
    return response_json
    # return jsonify({'error': 'collect not found'}), 404

# 获取个人笔记


@cross_origin()
@app.route('/api/note/<int:user_id>', methods=['GET'])
def get_note(user_id):
    # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
    # collections=db.session.query(
    #     Post.picture1,
    #     Post.title,
    #     User.name,
    #     User.photo,
    #     func.count(Like.id).label('like')
    # ).join(Collect, Post.id == Collect.post_id).join(User, Post.author_id == User.id).outerjoin(Like, Post.id == Like.post_id).filter(Collect.user_id == 1).group_by(Post.picture1, Post.title, User.name, User.photo).all()
    # 构建查询
    collections = db.session.query(
        Post.picture1,
        Post.title,
        User.name,
        User.photo,
        func.count(Like.id).label('like'),
        Post.id
    ).join(User, Post.author_id == User.id).filter(User.id == user_id).outerjoin(Like, Post.id == Like.post_id).group_by(Post.picture1, Post.title, User.name, User.photo).all()
    pictures = []
    titles = []
    authors = []
    avatars = []
    likes = []
    ids = []
    for collection in collections:
        pictures.append(collection[0])
        titles.append(collection[1])
        authors.append(collection[2])
        avatars.append(collection[3])
        likes.append(collection[4])
        ids.append(collection[5])
    response_json = jsonify({
        'pictures': pictures,
        'titles': titles,
        'authors': authors,
        'avatars': avatars,
        'likes': likes,
        'ids': ids
    })
    return response_json
    # return jsonify({'error': 'collect not found'}), 404

# 获取草稿箱


@cross_origin()
@app.route('/api/drafts/<int:user_id>', methods=['GET'])
def get_drafts(user_id):
    # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
    drafts = db.session.query(
        Draft.picture,
        cast(Draft.date, String),
        Draft.label,
        Draft.id
    ).join(User, Draft.user_id == User.id).filter(User.id == user_id).all()
    pictures = []
    dates = []
    labels = []
    ids = []
    for draft in drafts:
        pictures.append(draft[0])
        dates.append(draft[1])
        labels.append(draft[2])
        ids.append(draft[3])
    response_json = jsonify({
        'pictures': pictures,
        'dates': dates,
        'labels': labels,
        'ids': ids
    })
    return response_json
    # return jsonify({'error': 'collect not found'}), 404

# 获取草稿箱


@cross_origin()
@app.route('/api/get_draft/<int:post_id>', methods=['GET'])
def get_draft(post_id):
    # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
    draft = db.session.query(
        Draft.picture,
        cast(Draft.date, String),
        Draft.label,
        Draft.id
    ).join(User, Draft.user_id == User.id).filter(User.id == 1, Draft.id == post_id).first()
    response_json = jsonify({
        'pictures': draft[0],
        'dates': draft[1],
        'labels': draft[2],
        'ids': draft[3]
    })
    print({
        'pictures': draft[0],
        'dates': draft[1],
        'labels': draft[2],
        'ids': draft[3]
    })
    return response_json
    # return jsonify({'error': 'collect not found'}), 404

# 获取草稿箱标签


@cross_origin()
@app.route('/api/get_labels/<int:user_id>', methods=['GET'])
def get_labels(user_id):
    # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
    drafts = db.session.query(
        Draft.label
    ).join(User, Draft.user_id == User.id).filter(User.id == user_id).distinct()
    labels = []
    for draft in drafts:
        labels.append(draft[0])
    return labels
    # return jsonify({'error': 'collect not found'}), 404

# 根据标签获取草稿箱


@cross_origin()
@app.route('/api/search_drafts/<selected_label>', methods=['GET'])
def search_drafts(selected_label):
    print(selected_label)
    # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
    drafts = db.session.query(
        Draft.picture,
        cast(Draft.date, String),
        Draft.label,
        Draft.id
    ).join(User, Draft.user_id == User.id).filter(User.id == 1, Draft.label == selected_label).all()
    pictures = []
    dates = []
    labels = []
    ids = []
    for draft in drafts:
        pictures.append(draft[0])
        dates.append(draft[1])
        labels.append(draft[2])
        ids.append(draft[3])
    response_json = jsonify({
        'pictures': pictures,
        'dates': dates,
        'labels': labels,
        'ids': ids
    })
    return response_json
    # return jsonify({'error': 'collect not found'}), 404

# 草稿箱删除


@cross_origin()
@app.route('/api/del_draft/<int:post_id>', methods=['GET'])
def del_draft(post_id):
    draft_to_del = Draft.query.get(post_id)
    db.session.delete(draft_to_del)
    db.session.commit()
    return jsonify({'message': 'Delete successfully'})

# 暂存草稿


@cross_origin()
@app.route('/api/post_draft/', methods=['POST', 'GET'])
def post_draft():
    img = request.json.get('img')
    user_id = request.json.get('user_id')
    label = request.json.get('label')
    from datetime import datetime
    date = datetime.now()
    if img:
        new_draft = Draft(user_id=user_id, picture=img, date=date, label='1')
        db.session.add(new_draft)
        db.session.commit()
    return jsonify({'message': 'Post draft successfully'})


# 上传头像
@app.route('/api/upload-avatar', methods=['POST'])
def upload_avatar():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 保存头像文件
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # 返回文件路径给前端
    photo_url = url_for('serve_avatar', filename=filename)
    return jsonify({'photo': photo_url})


@app.route('/uploads/<filename>')
def serve_avatar(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# 查看要改的用户名是否已存在，要确保所有都是unique
@app.route('/check-username', methods=['GET'])
def check_username():
    username = request.args.get('username')
    user_id = request.args.get('user_id')
    existing_user = User.query.filter(
        User.name == username, User.id != user_id).first()
    return jsonify(is_unique=existing_user is None)


# 更新用户资料
@app.route('/api/update-profile', methods=['POST'])
def update_profile():
    data = request.json
    user = User.query.get(data.get('id'))
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.name = data.get('name', user.name)
    user.photo = data.get('photo', user.photo)
    user.email = data.get('email', user.email)
    user.sex = data.get('sex', user.sex)
    user.age = data.get('age', user.age)
    print(user.age)
    user.description = data.get('bio', user.description)

    db.session.commit()
    return jsonify({'message': 'Profile updated successfully'})

# 更新用户头像 URL


@app.route('/api/update-avatar', methods=['POST'])
def update_avatar():
    data = request.json
    user_id = data.get('user_id')
    avatar_url = data.get('photo')

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # 更新用户的头像 URL
    user.photo = avatar_url
    db.session.commit()

    return jsonify({'message': 'Avatar updated successfully'})

# 转换User格式


def transUserData(user):
    return {'id': user.id,
            'name': user.name,
            'avatar': user.photo,
            }


@app.route('/api/get-user-info/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    if user_id >= 0:
        user = User.query.filter_by(id=user_id).first()
        if user:
            response = {
                'name': user.name,
                'avatar': user.photo
            }
            return jsonify(response), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Userid parameter is required'}), 400

# 转换时间格式


def formatDateTime(time):
    return time.strftime("%Y年%m月%d日 %H:%M:%S").replace("年0", "年").replace("月0", "月").replace("日0", "日")


def parse_last_time(last_time_str):
    return datetime.strptime(last_time_str, '%Y年%m月%d日 %H:%M:%S')

# 获取历史消息


@app.route('/api/chat/<int:user_id>', methods=['GET'])
def get_chats(user_id):
    print("get chats user:", user_id)
    stuff_id = 0
    chats = Chat.query.filter((Chat.receiver == user_id) | (
        (Chat.sender == user_id) & (Chat.receiver != stuff_id))).all()
    data = []
    for chat in chats:
        messages = Message.query.filter_by(
            chat_id=chat.id).order_by(Message.id).all()
        chat_data = {
            'id': chat.id,
            'sender': transUserData(User.query.get(chat.sender)),
            'receiver': transUserData(User.query.get(chat.receiver)),
            'unread_sender': chat.unread_sender,
            'unread_receiver': chat.unread_receiver,
            'last_time': formatDateTime(chat.last_time),
            'messages': []
        }
        for message in messages:
            user = User.query.get(message.user_id)
            message_data = {
                'id': message.id,
                'type': message.type,
                'time': formatDateTime(message.time),
                'show_time': message.show_time,
                'content': message.content,
                'user': transUserData(user)
            }
            chat_data['messages'].append(message_data)
        data.append(chat_data)
    data.sort(key=lambda x: parse_last_time(
        x['last_time']), reverse=True)  # 按最后一条消息的时间降序排序
    print("chats data:", data)
    return jsonify(data)


@app.route('/api/chat-feedback/<int:user_id>', methods=['GET'])
def get_chats_feedback(user_id):
    print("get chats user:", user_id)
    stuff_id = 0
    if user_id != stuff_id:
        chats = Chat.query.filter(
            ((Chat.sender == user_id) & (Chat.receiver == stuff_id))).all()
    else:
        chats = Chat.query.filter((Chat.receiver == stuff_id)).all()
    data = []
    for chat in chats:
        messages = Message.query.filter_by(
            chat_id=chat.id).order_by(Message.id).all()
        chat_data = {
            'id': chat.id,
            'sender': transUserData(User.query.get(chat.sender)),
            'receiver': transUserData(User.query.get(chat.receiver)),
            'unread_sender': chat.unread_sender,
            'unread_receiver': chat.unread_receiver,
            'last_time': formatDateTime(chat.last_time),
            'messages': []
        }
        for message in messages:
            user = User.query.get(message.user_id)
            message_data = {
                'id': message.id,
                'type': message.type,
                'time': formatDateTime(message.time),
                'show_time': message.show_time,
                'content': message.content,
                'user': transUserData(user)
            }
            chat_data['messages'].append(message_data)
        data.append(chat_data)
    data.sort(key=lambda x: parse_last_time(
        x['last_time']), reverse=True)  # 按最后一条消息的时间降序排序
    print("chats data:", len(data))
    return jsonify(data)

# 新增会话


@app.route('/create_chat', methods=['POST'])
def create_chat():
    data = request.get_json()
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')

    if sender_id == None or receiver_id == None:
        return jsonify({"error": "Sender ID and Receiver ID are required"}), 400

    # 查找是否已经存在包含 sender_id 和 receiver_id 的会话
    chat = Chat.query.filter(
        (Chat.sender == sender_id) & (Chat.receiver == receiver_id) |
        (Chat.sender == receiver_id) & (Chat.receiver == sender_id)
    ).first()

    if chat:
        # 如果会话已存在，更新 last_time
        chat.last_time = datetime.now()
        db.session.commit()
        return jsonify({"message": "Chat updated successfully", "chat_id": chat.id}), 200
    else:
        # 获取当前数据库中最大的id值
        max_id = db.session.query(db.func.max(Chat.id)).scalar()
        new_id = (max_id or 0) + 1

        new_chat = Chat(
            id=new_id,
            sender=sender_id,
            receiver=receiver_id,
            unread_sender=True,
            unread_receiver=True,
            last_time=datetime.now()
        )
        db.session.add(new_chat)
        db.session.commit()

    return jsonify({"message": "Chat created successfully", "chat_id": new_id}), 201

# 删除指定会话


@app.route('/api/delete_chat/<int:chat_id>', methods=['DELETE'])
def delete_chat(chat_id):
    chat = Chat.query.get(chat_id)
    if not chat:
        return jsonify({"error": "Chat not found"}), 404

    db.session.delete(chat)
    db.session.commit()

    return jsonify({"message": "Chat and associated messages deleted successfully"}), 200


# 检查对话是否为空，空则删去
@app.route('/api/check_empty_chat', methods=['POST'])
def check_empty_chat():
    # 查询没有消息的聊天记录
    empty_chats = Chat.query.filter(~Chat.messages.any()).all()

    for chat in empty_chats:
        db.session.delete(chat)
    db.session.commit()

    return jsonify({"message": f"Deleted {len(empty_chats)} empty chats."}), 200

# 新增消息


@app.route('/api/save_message', methods=['POST'])
def receive_messages():
    data = request.json
    print(data)
    chat_id = data.get('chat_id')
    message = data.get('message')
    show_time = data.get('show_time')
    if not chat_id or not message:
        return jsonify({'error': 'Invalid data provided'}), 400

    chat = Chat.query.get(chat_id)
    if not chat:
        return jsonify({'error': 'Chat not found'}), 404

    content = message.get('content')
    if content:
        message_datetime = datetime.strptime(
            message.get('time'), '%Y年%m月%d日 %H:%M:%S')
        max_message_id = db.session.query(func.max(Message.id)).scalar() or 0
        next_message_id = max_message_id + 1
        db_message = Message(
            id=next_message_id,
            type=message.get('type'),
            time=message_datetime,
            show_time=show_time,
            content=content,
            user_id=message.get('user')["id"],
            chat_id=chat.id,
        )
        db.session.add(db_message)
        # 更新时间
        chat.last_time = message_datetime
        db.session.commit()

    return jsonify({'message_id': next_message_id}), 200

# 删去消息


@app.route('/api/delete_message', methods=['POST'])
def delete_message():
    message_id = request.json.get('message_id')
    print("msg id:", message_id)
    if message_id:
        message = Message.query.get(message_id)
        if message:
            db.session.delete(message)
            db.session.commit()
            return 'Delete successfully', 200
        else:
            return 'Message not found', 404
    else:
        return 'No message ID provided', 400

# 查询反馈


@app.route('/api/feedback/<int:user_id>', methods=['GET'])
def get_feedback(user_id):
    stuff_id = 0  # 客服id
    chats = Chat.query.filter((Chat.sender == user_id)
                              & (Chat.receiver == stuff_id)).all()
    data = []
    for chat in chats:
        messages = Message.query.filter_by(
            chat_id=chat.id).order_by(Message.id).all()
        chat_data = {
            'id': chat.id,
            'sender': transUserData(User.query.get(chat.sender)),
            'receiver': transUserData(User.query.get(chat.receiver)),
            'unread_sender': chat.unread_sender,
            'unread_receiver': chat.unread_receiver,
            'last_time': formatDateTime(chat.last_time),
            'messages': []
        }
        for message in messages:
            user = User.query.get(message.user_id)
            message_data = {
                'id': message.id,
                'type': message.type,
                'time': formatDateTime(message.time),
                'content': message.content,
                'user': transUserData(user)
            }
            chat_data['messages'].append(message_data)
        data.append(chat_data)

    return jsonify(data)

# 添加收藏


@app.route('/api/add_collect', methods=['GET', 'POST'])
def add_collect():
    post_id = request.json.get('postId')  # 获取文章 ID
    user_id = request.json.get('userId')  # 获取用户 ID
    isAdd = request.json.get('add')
    from datetime import datetime, timezone
    date = datetime.now()
    if isAdd and post_id and user_id:
        new_Collect = Collect(date=date, user_id=user_id, post_id=post_id)
        db.session.add(new_Collect)
        db.session.commit()
        return jsonify({'message': '收藏成功'})
    elif not isAdd and post_id and user_id:
        Collect.query.filter(
            Collect.post_id == post_id and Collect.user_id == user_id).delete()
        db.session.commit()
        return jsonify({'message': '取消收藏成功'})
    else:
        return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400

# 添加点赞


@app.route('/api/add_like', methods=['GET', 'POST'])
def add_like():
    post_id = request.json.get('postId')  # 获取文章 ID
    user_id = request.json.get('userId')  # 获取用户 ID
    isAdd = request.json.get('add')
    from datetime import datetime, timezone
    date = datetime.now()
    if isAdd and post_id and user_id:
        new_Like = Like(date=date, author_id=user_id, post_id=post_id)
        db.session.add(new_Like)
        db.session.commit()
        return jsonify({'message': '点赞成功'})
    elif not isAdd and post_id and user_id:
        Like.query.filter(
            Like.post_id == post_id and Like.author_id == user_id).delete()
        db.session.commit()
        return jsonify({'message': '取消点赞成功'})
    else:
        return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400

# 获取点赞和收藏的状态


@app.route('/api/get_status/<int:post_id>/<int:userId>', methods=['GET'])
def get_status(post_id, userId):
    # post_id = request.json.get('postId')  # 获取文章 ID
    # user_id = request.json.get('userId')  # 获取用户 ID
    print('post:{},user:{}'.format(post_id, userId))
    isLiked = db.session.query(
        Like.id
    ).filter(Like.post_id == post_id and Like.author_id == userId) \
        .first()
    isCollected = db.session.query(
        Collect.id
    ).filter(Collect.post_id == post_id and Collect.user_id == userId) \
        .first()
    if isLiked:
        isLiked = '1'
    else:
        isLiked = '0'
    if isCollected:
        isCollected = '1'
    else:
        isCollected = '0'
    response_json = jsonify({
        'isLiked': isLiked,
        'isCollected': isCollected
    })
    print({
        'isLiked': isLiked,
        'isCollected': isCollected
    })
    return response_json

# 提交评论


@app.route('/api/submit_comment', methods=['GET', 'POST'])
def add_comment():
    content = request.json.get('content')
    post_id = request.json.get('postId')  # 获取文章 ID
    user_id = request.json.get('userId')  # 获取用户 ID
    post_id = int(post_id)
    from datetime import datetime, timezone
    date = datetime.now()
    # date = date.strftime('%Y-%m-%d %H:%M:%S')
    print(content)
    # from datetime import datetime
    # date = datetime.strptime(date, "%Y/%m/%d, %H:%M:%S")
    if content and post_id:
        new_comment = Comment(content=content,
                              author_id=user_id,
                              post_id=post_id,
                              date=date)
        db.session.add(new_comment)
        db.session.commit()
        newComment = db.session.query(
            Comment.id,
            # Comment.date,
            cast(Comment.date, String),
            Comment.content,
            User.name,
            User.photo
        ).join(User, Comment.author_id == User.id) \
            .outerjoin(Post, Comment.post_id == Post.id) \
            .filter(Post.id == post_id) \
            .order_by(desc(Comment.id)) \
            .first()
        response_json = jsonify({
            'ids': newComment[0],
            'dates': newComment[1],
            'contents': newComment[2],
            'authors': newComment[3],
            'avatars': newComment[4]
        })
        print({
            'ids': newComment[0],
            'dates': newComment[1],
            'contents': newComment[2],
            'authors': newComment[3],
            'avatars': newComment[4]
        })
        return response_json
    else:
        return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400

# 获取帖子评论


@app.route('/api/post_comments/<int:post_id>', methods=['GET'])
def get_postComment(post_id):
    # 首先是文章信息，包括内容、作者等
    print(post_id)
    comments = db.session.query(
        Comment.id,
        # Comment.date,
        cast(Comment.date, String),
        Comment.content,
        User.name,
        User.photo
    ).join(User, Comment.author_id == User.id) \
        .outerjoin(Post, Comment.post_id == Post.id) \
        .filter(Post.id == post_id) \
        .order_by(desc(Comment.id)) \
        .all()
    ids = []
    dates = []
    contents = []
    authors = []
    avatars = []
    for comment in comments:
        ids.append(comment[0])
        dates.append(comment[1][:19])
        contents.append(comment[2])
        authors.append(comment[3])
        avatars.append(comment[4])
    response_json = jsonify({
        'ids': ids,
        'dates': dates,
        'contents': contents,
        'authors': authors,
        'avatars': avatars
    })
    print({
        'ids': ids,
        'dates': dates,
        'contents': contents,
        'authors': authors,
        'avatars': avatars
    })
    return response_json

# 获取帖子评论


@app.route('/api/all_comments/<int:user_id>', methods=['GET'])
def get_allComment(user_id):
    # 获取用户发表的所有帖子
    posts = db.session.query(Post.id).filter(Post.author_id == user_id).all()
    post_ids = [post.id for post in posts]

    # 获取这些帖子的评论，以及评论的作者信息和帖子的第一张图片
    comments = db.session.query(
        Comment.id,
        cast(Comment.date, String),
        Comment.content,
        User.name,
        User.photo,
        Post.picture1
    ).join(User, Comment.author_id == User.id) \
        .join(Post, Comment.post_id == Post.id) \
        .filter(Post.id.in_(post_ids)) \
        .order_by(desc(Comment.date)) \
        .all()
    ids = []
    dates = []
    contents = []
    authors = []
    avatars = []
    pictures = []
    for comment in comments:
        ids.append(comment[0])
        dates.append(comment[1][:19])
        contents.append(comment[2])
        authors.append(comment[3])
        avatars.append(comment[4])
        pictures.append(comment[5])
    response_json = jsonify({
        'ids': ids,
        'dates': dates,
        'contents': contents,
        'authors': authors,
        'avatars': avatars,
        'pictures': pictures
    })
    print({
        'ids': ids,
        'dates': dates,
        'contents': contents,
        'authors': authors,
        'avatars': avatars,
        'pictures': pictures
    })
    return response_json

# 获取帖子 （新增获取图片角标内容 by hzq）


@app.route('/api/post_content/<int:post_id>', methods=['GET'])
def get_postContent(post_id):
    print(post_id)
    # Expanded query to include User.id
    contents = db.session.query(
        Post.picture1,
        Post.picture2,
        Post.picture3,
        Post.picture4,
        Post.picture5,
        cast(Post.date, String),
        Post.title,
        Post.body,
        User.name,
        User.photo,
        User.id,  # Adding this to capture the author's ID
        func.count(Like.id.distinct()).label('like'),
        func.count(Comment.id.distinct()).label('comment'),
        func.count(Collect.id.distinct()).label('collect'),
        Post.id
    ).join(User, Post.author_id == User.id) \
        .outerjoin(Like, Post.id == Like.post_id) \
        .outerjoin(Comment, Post.id == Comment.post_id) \
        .outerjoin(Collect, Post.id == Collect.post_id) \
        .filter(Post.id == post_id) \
        .group_by(Post.id, User.id, User.name, User.photo) \
        .order_by(desc(Post.id)) \
        .all()

    if contents:
        content = contents[0]
        pictures = [pic for pic in content[:5] if pic]
        pic_types = []
        # 查询 Picture 数据库获得每张图片的Ptype
        for pic in pictures:
            pic_type = Picture.query.filter_by(id=pic).first()
            if not pic_type:
                pic_types.append(-1)
            else:
                # 如果不存在，就置0
                pic_type = pic_type.Ptype
                if not pic_type:
                    pic_types.append(-1)
                else:
                    pic_types.append(pic_type)
        print("pic_types", pic_types)
        response_json = jsonify({
            'pictures': pictures,
            'date': content[5][:19],
            'title': content[6],
            'body': content[7],
            'author': content[8],
            'avatar': content[9],
            'author_id': content[10],  # Using the fetched author ID
            'likes_num': content[11],
            'comments_num': content[12],
            'collects_num': content[13],
            'pic_tabs': pic_types,
        })
        print(response_json.get_json())
        return response_json
    else:
        return jsonify({'error': 'Post not found'}), 404


# 互相关注
@app.route('/api/follow', methods=['POST'])
def follow_user():
    data = request.get_json()
    follower_id = data.get('follower_id')
    followed_id = data.get('followed_id')
    print(follower_id)
    print(followed_id)

    if follower_id == followed_id:
        return jsonify({'error': 'Cannot follow yourself'}), 400

    follow = Follow.query.filter_by(
        follower_id=follower_id, followed_id=followed_id).first()
    if follow:
        # 已经存在关注记录，检查是否已经是互相关注
        return jsonify({'message': 'Already followed', 'status': follow.status}), 409
    else:
        # 创建新的关注关系
        new_follow = Follow(follower_id=follower_id,
                            followed_id=followed_id, status=0)
       # print(follower_id)
        db.session.add(new_follow)

        # 检查对方是否已关注当前用户，实现互相关注
        reverse_follow = Follow.query.filter_by(
            follower_id=followed_id, followed_id=follower_id).first()
        if reverse_follow:
            new_follow.status = 1
            reverse_follow.status = 1
            db.session.add(reverse_follow)

        db.session.commit()
        return jsonify({'message': 'Followed successfully', 'status': new_follow.status}), 200

# 取消关注


@app.route('/api/unfollow', methods=['POST'])
def unfollow_user():
    data = request.get_json()
    follower_id = data.get('follower_id')
    followed_id = data.get('followed_id')

    if follower_id == followed_id:
        return jsonify({'error': 'Cannot unfollow yourself'}), 400

    # 查询是否存在关注记录
    follow = Follow.query.filter_by(
        follower_id=follower_id, followed_id=followed_id).first()
    if not follow:
        return jsonify({'message': 'No follow relation found'}), 404

    # 存在关注记录，进行取消
    db.session.delete(follow)

    # 检查是否需要更新互相关注状态
    reverse_follow = Follow.query.filter_by(
        follower_id=followed_id, followed_id=follower_id).first()
    if reverse_follow and reverse_follow.status == 1:
        reverse_follow.status = 0  # 更新为非互相关注状态
        db.session.add(reverse_follow)

    db.session.commit()
    return jsonify({'message': 'Unfollowed successfully'}), 200

# 查看，来显示
@app.route('/api/check-follow/<int:follower_id>/<int:followed_id>', methods=['GET'])
def check_follow(follower_id, followed_id):
    follow = Follow.query.filter_by(
        follower_id=follower_id, followed_id=followed_id).first()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(follow)
    if follow:
        return jsonify({'isFollowed': True, 'status': follow.status}), 200
    else:
        return jsonify({'isFollowed': False, 'status': 0}), 200


# 广场页获取帖子
# @cross_origin()
@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = db.session.query(
        Post.id,
        Post.picture1,
        Post.title,
        User.name,
        User.photo,
        func.count(Like.id).label('like')
    ).join(User, Post.author_id == User.id) \
        .outerjoin(Like, Post.id == Like.post_id) \
        .group_by(Post.picture1,
                  Post.title,
                  User.name,
                  User.photo) \
        .all()
    ids = []
    pictures = []
    titles = []
    authors = []
    avatars = []
    likes = []
    for post in posts:
        ids.append(post[0])
        pictures.append(post[1])
        titles.append(post[2])
        authors.append(post[3])
        avatars.append(post[4])
        likes.append(post[5])
    response_json = jsonify({
        'ids': ids,
        'pictures': pictures,
        'titles': titles,
        'authors': authors,
        'avatars': avatars,
        'likes': likes
    })
    # print({
    #     'ids': ids,
    #     'pictures': pictures,
    #     'titles': titles,
    #     'authors': authors,
    #     'avatars': avatars,
    #     'likes': likes
    # })
    return response_json

# 广场页获取关注帖子
# @cross_origin()


@app.route('/api/follow_posts/<int:user_id>', methods=['GET'])
def get_followposts(user_id):
    # user_id = 1  # Replace with the current logged in user's ID
    posts = db.session.query(
        Post.id,
        Post.picture1,
        Post.title,
        User.name,
        User.photo,
        func.count(Like.id).label('like')
    ).join(User, Post.author_id == User.id) \
        .outerjoin(Like, Post.id == Like.post_id) \
        .join(Follow, Follow.followed_id == Post.author_id) \
        .filter(Follow.follower_id == user_id) \
        .group_by(Post.picture1,
                  Post.title,
                  User.name,
                  User.photo) \
        .all()
    ids = []
    pictures = []
    titles = []
    authors = []
    avatars = []
    likes = []
    for post in posts:
        ids.append(post[0])
        pictures.append(post[1])
        titles.append(post[2])
        authors.append(post[3])
        avatars.append(post[4])
        likes.append(post[5])
    response_json = jsonify({
        'ids': ids,
        'pictures': pictures,
        'titles': titles,
        'authors': authors,
        'avatars': avatars,
        'likes': likes
    })
    # print({
    #     'ids': ids,
    #     'pictures': pictures,
    #     'titles': titles,
    #     'authors': authors,
    #     'avatars': avatars,
    #     'likes': likes
    # })
    return response_json


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on('join')
def handle_join(data):
    print("join:", data)
    chat_id = data['chat_id']
    join_room(chat_id)


@socketio.on('message')
def handle_message(data):
    chat_id = data['chat_id']
    print("chat:", chat_id)
    emit('message', {'message': data['message']}, room=chat_id)

# 管理员相关函数
# 获取所有用户


@app.route('/api/get-all-user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_data = []

    for user in users:
        if user.is_admin:
            continue
        user_data = {
            'id': user.id,
            'name': user.name,
            'password': user.password,
            'avatar': user.photo,
            'email': user.email,
            'age': user.age,
            'sex': user.sex,
            'senior': user.is_premium,
            'description': user.description,
            'status': user.status
        }
        users_data.append(user_data)

    return jsonify({'userList': users_data})


# 获取用户和帖子总数
@app.route('/api/get-user-post-num', methods=['GET'])
def get_user_post_num():
    users = User.query.all()
    posts = Post.query.all()
    return jsonify({'userNum': len(users), 'postNum': len(posts)})

# 获取所有帖子


@app.route('/api/get-all-post', methods=['GET'])
def get_all_posts():
    posts = Post.query.all()
    posts_data = []

    for post in posts:
        post_data = {
            'id': post.id,
            'author_id': post.author_id,
            'date': formatDateTime(post.date),
            'pics': [post.picture1, post.picture2, post.picture3, post.picture4, post.picture5],
            'title': post.title,
            'content': post.body,
            'status': post.status
        }
        posts_data.append(post_data)

    return jsonify({'dataList': posts_data})

# 更新用户状态 禁用和正常来回切换


@app.route('/api/update-user-status/<int:user_id>', methods=['POST'])
def update_user_status(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    # 切换帖子状态
    user.status = not user.status
    db.session.commit()

    return jsonify({'success': 'User status updated successfully', 'new_status': user.status})

# 更新帖子状态 禁用和正常来回切换


@app.route('/api/update-post-status/<int:post_id>', methods=['POST'])
def update_post_status(post_id):
    print(post_id)
    post = Post.query.get(post_id)
    if post is None:
        return jsonify({'error': 'Post not found'}), 404

    post.status = not post.status
    db.session.commit()

    return jsonify({'success': 'Post status updated successfully', 'new_status': post.status})

# 发布动态


@app.route('/api/postnotes', methods=['GET', 'POST'])
def postnotes():
    dataform = request.json.get('pics')
    title = request.json.get('title')
    description = request.json.get('description')
    user_id = request.json.get('userId')  # 获取用户 ID
    # user_id = 1
    # 获取dataform的实际大小
    cnt = len(dataform)
    pic1 = ''
    pic2 = ''
    pic3 = ''
    pic4 = ''
    pic5 = ''
    if cnt >= 1:
        pic1 = dataform[0]
    if cnt >= 2:
        pic2 = dataform[1]
    if cnt >= 3:
        pic3 = dataform[2]
    if cnt >= 4:
        pic4 = dataform[3]
    if cnt >= 5:
        pic5 = dataform[4]
    # 谁定义的数据表，表项名字那么长...pic不好么
    dateToday = datetime.now()
    print(dateToday)
    post = Post(date=dateToday, author_id=user_id, title=title, body=description,
                picture1=pic1, picture2=pic2, picture3=pic3, picture4=pic4, picture5=pic5)
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'})

# 后端一键修图指令
# 参数：img_url(原图URL) + img_select(对应的模板url，用于寻找prompt)
# 本地调试请注释该函数！！！！！！！


@app.route('/api/call_P2P', methods=['GET', 'POST'])
@app.route('/api/call_P2P', methods=['GET', 'POST'])
def call_P2P():
    img_old = request.json.get('img_url')
    img_select = request.json.get('img_select')
    user_id = request.json.get('user_id')
    print(img_old, img_select, user_id)
    # if img_old is None or img_select is None or user_id is None:
    #     return jsonify({'img': 'Invalid data provided'}), 400
    # 查询Picture数据表，找到对应的prompt
    # pic_tmp = Picture(id=img_select, prompt='turn it yellow.')
    # db.session.add(pic_tmp)
    # db.session.commit()
    prompt = Picture.query.filter_by(id=img_select).first().prompt
    if prompt is None:
        print("prompt is None")
        return jsonify({'img': 'Prompt not found'})
    # 调用修图指令
    # img_new = os.system("python /root/Code/Models/P2P/P2P.py --img_url "+img_old+" --prompt "+prompt)
    # 函数调用修图命令，存储为/mod/{prompt+"_modify_"+img_old}
    sys.path.append(r'/root/Code/Models/P2P')
    import P2P
    P2P.modify_pic(img_old, prompt)
    # 上传阿里云图床
    # OSS_ACCESS_KEY_ID = "LTAI5tR1c1uhFRfWxjq8BWT4"
    # OSS_ACCESS_KEY_SECRET = "BdN5OIEdet7IO6KWOq7TJiivHOsC5B"
    auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
    bucket = oss2.Bucket(
        auth, 'https://oss-cn-beijing.aliyuncs.com', 'graphcrafter')
    # /root/Code/Models/P2P/weights
    prompt = prompt.replace(" ", "")
    mod_img_url = prompt + "_modify_" + img_old.split("/")[-1]
    with open(mod_img_url, mode="rb") as fileobj:
        fileobj.seek(0, os.SEEK_SET)
        current = fileobj.tell()
        bucket_url = user_id+'/'+prompt + "_modify_" + img_old.split("/")[-1]
        bucket.put_object(bucket_url, fileobj)
        # 删除文件夹中的图片
        os.remove(mod_img_url)
        current_url = 'https://graphcrafter.oss-cn-beijing.aliyuncs.com/' + bucket_url
        new_pic = Picture(id=current_url, prompt=prompt, Ptype=2)
        db.session.add(new_pic)
        db.session.commit()
        return jsonify({'img': "https://graphcrafter.oss-cn-beijing.aliyuncs.com/" + bucket_url})

    return jsonify({'img': None})

# 删除帖子的接口


@app.route('/api/delete-post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    # 删除相关的评论
    Comment.query.filter_by(post_id=post_id).delete()

    # 删除相关的点赞
    Like.query.filter_by(post_id=post_id).delete()

    # 删除相关的收藏
    Collect.query.filter_by(post_id=post_id).delete()

    # 删除帖子
    db.session.delete(post)
    db.session.commit()

    return jsonify({'message': 'Post deleted successfully'}), 200

# 基本图像处理


@app.route('/api/simple-image-process', methods=['POST'])
def process_image_simple():
    print(request.files)
    print("form:", request.form)
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 读取参数
    user_id = request.form.get('user_id')
    # 处理的类别 eg.图像色彩，图像变换...
    process_category = request.form.get('process_category')
    process_type = request.form.get('process_type')  # 具体的处理类型 eg.色调

    if not user_id or not process_category or not process_type:
        return jsonify({'error': 'Missing processing parameters'}), 400

    # 读取图片文件
    file_stream = io.BytesIO(file.read())
    file_bytes = np.frombuffer(file_stream.read(), np.uint8)
    origin = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    height, width, channels = origin.shape
    img_size = [width, height]
    print("image size:", height, width)

    if origin is None:
        return jsonify({'error': 'Failed to read the uploaded image'}), 500

    # 进行图像处理
    # 处理后的图片暂存为tmp.png
    if process_category == "color":
        show_hsv(origin, process_type, img_size)
    elif process_category == "transform":
        show_transformation(origin, process_type, img_size)
    elif process_category == "filter":
        show_filtering(origin, process_type, img_size)
    elif process_category == "outline":
        show_outline(origin, process_type, img_size)
    elif process_category == "enhance":
        show_enhancement(origin, process_type, img_size)
    else:
        return jsonify({'error': 'Process category chosen does not exits'}), 400

    # 上传到阿里云OSS
    tmp_file_path = './img_tmp/tmp.png'
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    oss_file_path = f'simple_image_process/{user_id}-{current_time}.png'
    with open(tmp_file_path, 'rb') as file:
        bucket.put_object(oss_file_path, file)
    img_url = f'http://{OSS_BUCKET_NAME}.{OSS_ENDPOINT}/{oss_file_path}'
    print(img_url)

    return jsonify({'imgUrl': img_url})

###################################################


# Chat 界面


####################################
from IAA_main import get_score_one_image

# Set your OpenAI API key here
openai.api_key = 'sk-75C7ruBi5U7ts0Yi55BeDb4576Cd41EbA68bDbF1344f9f5e'

# Set base URL for OpenAI API
openai.api_base = "https://tb.plus7.plus/v1"

history = []
image_list = []

# Define a route for clearing chat history


@app.route('/clear_history/<int:user_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def clear_history(user_id):
    History.query.filter(History.user_id == user_id).delete()
    db.session.commit()
    return {}


@app.route('/api/getmsg/<int:user_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def getMessageList(user_id):
    chats = db.session.query(
        History.id,
        History.role,
        History.time,
        History.content,
        History.user_id,
        History.picture,
        User.photo
    ).join(User, History.user_id == User.id).filter(User.id == user_id).all()
    data = []
    for chat in chats:
        chat_data = {
            'id': chat[0],
            'role': chat[1],
            # 'time': formatDateTime(chat.time),
            'time': chat[2],
            'content': chat[3],
            'user_id': chat[4],
            'picture': chat[5],
            'photo': chat[6]
        }
        data.append(chat_data)
    # data.sort(key=lambda x: parse_last_time(x['time']), reverse=True) # 按最后一条消息的时间降序排序
    print("chats data:", data)
    return jsonify({"data": data})


@app.route('/api/get_info', methods=['POST', 'GET'])
def get_personal_info():
    personal_id = request.json.get('user_id')
    # 查询用户数据库获取头像
    person_avatar = User.query.filter_by(id=personal_id).first().photo
    return jsonify({'info': person_avatar})

@app.route('/upload_photo', methods=['POST'])
@cross_origin(supports_credentials=True)
def photo():
    if "img_score" not in globals():
        global img_score
    image = request.files['file']
    # Convert image to base64
    image_read = image.read()
    image_stream = BytesIO(image_read)
    # img_score = get_score_one_image(image_stream)
    img_score = 8.2
    img_score = round(min(img_score*1.2, 10), 2)
    img_base64 = base64.b64encode(image_read).decode('utf-8')
    # global_image_data = image_data #更新global_image_data
    image_list.append(f"data:image/jpeg;base64,{img_base64}")
    return "success"

# 对话修图指令
@app.route('/api/chat_P2P', methods=['GET', 'POST'])
def chat_P2P():
    img_old = request.json.get('img_url')
    # img_select = request.json.get('img_select')
    prompt = request.json.get('prompt')
    user_id = request.json.get('user_id')
    # print(img_old, img_select, user_id)
    if img_old is None or prompt is None or user_id is None:
        return jsonify({'img': 'Invalid data provided'}), 400
    # 查询Picture数据表，找到对应的prompt
    # pic_tmp = Picture(id=img_select, prompt='turn it yellow.')
    # db.session.add(pic_tmp)
    # db.session.commit()
    # prompt = Picture.query.filter_by(id=img_select).first().prompt
    # if prompt is None:
    #     print("prompt is None")
    #     return jsonify({'img': 'Prompt not found'})
    # 调用修图指令
    # img_new = os.system("python /root/Code/Models/P2P/P2P.py --img_url "+img_old+" --prompt "+prompt)
    # 函数调用修图命令，存储为/mod/{prompt+"_modify_"+img_old}
    sys.path.append(r'/root/Code/Models/P2P')
    import P2P
    print("promptpromptpromptpromptprompt ",prompt)
    P2P.modify_pic(img_old, prompt)
    # 上传阿里云图床
    # OSS_ACCESS_KEY_ID = "LTAI5tR1c1uhFRfWxjq8BWT4"
    # OSS_ACCESS_KEY_SECRET = "BdN5OIEdet7IO6KWOq7TJiivHOsC5B"
    auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
    bucket = oss2.Bucket(
        auth, 'https://oss-cn-beijing.aliyuncs.com', 'graphcrafter')
    # /root/Code/Models/P2P/weights
    prompt = prompt.replace(" ", "")
    mod_img_url = prompt + "_modify_" + img_old.split("/")[-1]
    with open(mod_img_url, mode="rb") as fileobj:
        fileobj.seek(0, os.SEEK_SET)
        current = fileobj.tell()
        bucket_url = user_id+'/'+prompt + "_modify_" + img_old.split("/")[-1]
        bucket.put_object(bucket_url, fileobj)
        # 删除文件夹中的图片
        os.remove(mod_img_url)
        print("https://graphcrafter.oss-cn-beijing.aliyuncs.com/" + bucket_url)
        return jsonify({'img': "https://graphcrafter.oss-cn-beijing.aliyuncs.com/" + bucket_url})
    return jsonify({'img': None})

# 图像评估
@app.route('/gpt', methods=['POST'])
@cross_origin(supports_credentials=True)
def gpt():
    user_id = request.json.get('user_id')
    question = request.json.get('question')
    img_url = request.json.get('img_url')
    time = request.json.get('time')

    # if question=="":
    #     post = History(user_id=user_id,role="warn",content="请输入问题")
    #     db.session.add(post)
    #     db.session.commit()
    #     return {}
    chats = db.session.query(
        History.role,
        History.content,
        History.picture,
    ).join(User, History.user_id == User.id).filter(User.id == user_id, History.role != 'warn').all()
    chat_history = []
    # last_picture=None
    for chat in chats:
        chat_data = {
            'role': chat[0],
            'content': chat[1]
        }
        chat_history.append(chat_data)
        # last_picture=chat[2]

    # data.sort(key=lambda x: parse_last_time(x['time']), reverse=True) # 按最后一条消息的时间降序排序
    # if picture==None:
    #     if last_picture is not None:
    #         picture=last_picture
    #     else:
    #         post = History(user_id=user_id,role="warn",content="请上传一张照片")
    #         db.session.add(post)
    #         db.session.commit()
    #         return {}
    file = requests.get(img_url).content
    print(file)
    image_read = file  # .read()
    image_stream = BytesIO(image_read)
    img_score = get_score_one_image(image_stream)
    # img_score = 8.2
    img_score = round(min(img_score*1.2, 10), 2)
    img_base64 = base64.b64encode(image_read).decode('utf-8')
    # global_image_data = image_data #更新global_image_data
    image_data = f"data:image/jpeg;base64,{img_base64}"

    rate_msg = f"这张图片的IAA评分是{img_score}/10分，"
    response = send_gpt(rate_msg+question, image_data, chat_history)
    response = rate_msg + response

    q = History(user_id=user_id, role="user",
                content=question, picture=img_url, time=time)
    a = History(user_id=user_id, role="assistant",
                content=response, picture=img_url, time=time)
    db.session.add(q)
    db.session.add(a)
    db.session.commit()
    return {"score": img_score}
    #     # question = request.form['question']
    #     # print("所有：",request.get_data(as_text=True))
    #     question = eval(request.get_data(as_text=True))["content"]
    #     print("问题：",question)
    #     # print(request.files.get('image'))
    #     # image = request.files.get('image')
    #     if(len(image_list)==0):
    #         image=None
    #         img_score=0
    #     elif(up==False):
    #         image=image_list[-1]
    #         img_score=0
    #     else:
    #         image=image_list[-1]
    #     print("image:",image)
    #     # Handle image file if uploaded
    #     # img_score = 0
    #     if image:
    #         # # Convert image to base64
    #         # image_read = image.read()
    #         # image_stream = BytesIO(image_read)
    #         # img_score = get_score_one_image(image_stream)
    #         # img_score = round(min(img_score*1.2,10),2)
    #         # img_base64 = base64.b64encode(image_read).decode('utf-8')
    #         # image_data = f"data:image/jpeg;base64,{img_base64}"
    #         # global_image_data = image_data #更新global_image_data
    #         image_data=image
    #     else:
    #         image_data = None

    #     # Send data to GPT and get response
    #     if img_score:
    #         rate_msg = f"这张图片的IAA评分是{img_score}/10分，"
    #     else:
    #         rate_msg = ""

    #     response = send_gpt(rate_msg+question, image_data)
    #     response = rate_msg + response
    #     print(up)
    #     history.append({"q":question,"a":response,"p":image_data if up==True else None})
    #     up=False
    #     return ""#render_template('index.html', question=question, response=response,ch=history)
    # else:
    #     # Display the form for user input on GET requests
    #     return render_template('index.html', question=None, response=None)

# Function to send data to OpenAI's GPT including text and optional image


def send_gpt(prompt, image_data=None, chat_history=[]):
    try:
        # 构建消息
        message = {"role": "user", "content": prompt}

        # 如果本轮没有传图片 - 用以前的
        if image_data == None:
            image_data = image_data

        if image_data:
            message["content"] = [{"type": "text", "text": prompt}, {
                "type": "image_url", "image_url": image_data}]

        # Limit the chat history to the last 3 exchanges to ensure the conversation does not exceed 3 turns
        if len(chat_history) >= 6:
            chat_history = chat_history[-6:]

        chat_history.insert(0, message)

        print(chat_history)

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model='gpt-4-vision-preview',
            messages=chat_history,
            max_tokens=4096
        )

        # Extract and return the response
        reply = response["choices"][0]['message']['content']
        chat_history.insert(0, {"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return str(e)


'''


CREATE TABLE history (
    id INTEGER PRIMARY KEY,
    role VARCHAR(60),
    time VARCHAR(60),
    content TEXT,
    user_id INTEGER,
    picture VARCHAR(60)
);


'''

if __name__ == '__main__':
    config = dict(
        host='0.0.0.0',
        port=3306,
        debug=True,
        allow_unsafe_werkzeug=True
    )
    socketio.run(app, **config)
