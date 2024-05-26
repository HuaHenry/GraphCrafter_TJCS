import sys, os
from flask import Flask, jsonify, request, render_template, url_for, send_from_directory
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
import os
from sqlalchemy import func, cast, String, desc

# WIN = sys.platform.startswith('win')
# if WIN:  # 如果是 Windows 系统，使用三个斜线
#     prefix = 'sqlite:///'
# else:  # 否则使用四个斜线
#     prefix = 'sqlite:////'

# app = Flask(__name__, static_url_path='/', static_folder='./../frontend/dist', template_folder='./../frontend/dist')
# # 创建数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app


app = Flask(__name__, static_url_path='/s',
            static_folder='static', template_folder='templates')

CORS(app, resources=r'/*', supports_credentials=True) 

# 连接数据库
HOSTNAME = "127.0.0.1"  # MySQL所在主机名
PORT = 3306  # MySQL监听的端口号，默认3306
USERNAME = "root"  # 连接MySQL的用户名，自己设置
PASSWORD = "212300"  # 连接MySQL的密码，自己设置
DATABASE = "tujiang"  # MySQL上创建的数据库名称
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class User(db.Model):  # 用户
    id = db.Column(db.Integer, primary_key=True)  # 主键，账号
    name = db.Column(db.String(20))  # 名字
    password = db.Column(db.String(20))  # 密码
    photo = db.Column(db.String(60))  # 头像
    email = db.Column(db.String(254))  # 邮箱
    age = db.Column(db.Integer)  # 年龄
    sex = db.Column(db.Boolean)  # 性别，1是男0是女
    senior = db.Column(db.Boolean)  # 是否为付费用户
    description = db.Column(db.String(100))  # 一句话介绍自己


# 登录
@app.route('/login', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def login():
    with app.app_context():
        if (request.method == 'POST'):
            username = request.form['username']
            password = request.form['password']
            users = User.query.filter_by(name=username).all()
            for item in users:
                if password == item.password:
                    print(password)
                    return "success"
            else:
                print("Error!!")
                return 'error'
        else:
            return ''

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#     user = User.query.filter_by(name=username, password=password).first()
#     if user:
#         return jsonify({'status': 'success', 'message': 'Login successful', 'user': user.id}), 200
#     else:
#         return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401


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
            if user_type == "admin":
                invite_code = request.form['inviteCode']
            user_now = User(id=id, name=username, password=password, email=email, senior=(user_type == 'admin'))
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



# @app.route('/api/ping', methods=['GET'])
# def ping_pong():
#     return jsonify('pong!')


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/<path:fallback>')
# def fallback(fallback):  # Vue Router 的 mode 为 'hash' 时可移除该方法
#     if fallback.startswith('css/') or fallback.startswith('js/') \
#             or fallback.startswith('img/') or fallback == 'favicon.ico':
#         return app.send_static_file(fallback)
#     else:
#         return app.send_static_file('index.html')


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
#             'senior': user.senior,
#             'bio': user.description
#         })
#     return jsonify({'error': 'User not found'}), 404


# # 获取用户收藏
# @cross_origin()
# @app.route('/api/collection', methods=['GET'])
# def get_collection():
#     # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
#     collections = db.session.query(
#         Post.picture1,
#         Post.title,
#         User.name,
#         User.photo,
#         func.count(Like.id).label('like')
#     ).join(Collect, Post.id == Collect.post_id) \
#         .join(User, Post.author_id == User.id) \
#         .outerjoin(Like, Post.id == Like.post_id) \
#         .filter(Collect.user_id == 1) \
#         .group_by(Post.picture1, Post.title, User.name, User.photo) \
#         .all()
#     pictures = []
#     titles = []
#     authors = []
#     avatars = []
#     likes = []
#     for collection in collections:
#         pictures.append(collection[0])
#         titles.append(collection[1])
#         authors.append(collection[2])
#         avatars.append(collection[3])
#         likes.append(collection[4])
#     response_json = jsonify({
#         'pictures': pictures,
#         'titles': titles,
#         'authors': authors,
#         'avatars': avatars,
#         'likes': likes
#     })
#     print({
#         'pictures': pictures,
#         'titles': titles,
#         'authors': authors,
#         'avatars': avatars,
#         'likes': likes
#     })
#     return response_json
#     # return jsonify({'error': 'collect not found'}), 404


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


# # 更新用户资料s
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

#     # return jsonify({'error': 'collect not found'}), 404


# # 获取帖子详情
# @app.route('/api/post_content/<int:post_id>', methods=['GET'])
# def get_postContent(post_id):
#     # 首先是文章信息，包括内容、作者等
#     print(post_id)
#     contents = db.session.query(
#         Post.picture1,
#         Post.picture2,
#         Post.picture3,
#         Post.picture4,
#         Post.picture5,
#         # Post.date,
#         cast(Post.date, String),
#         Post.title,
#         Post.body,
#         User.name,
#         User.photo,
#         func.count(Like.id.distinct()).label('like'),
#         func.count(Comment.id.distinct()).label('comment'),
#         func.count(Collect.id.distinct()).label('collect'),
#         Post.id
#     ).join(User, Post.author_id == User.id) \
#         .outerjoin(Like, Post.id == Like.post_id) \
#         .outerjoin(Comment, Post.id == Comment.post_id) \
#         .outerjoin(Collect, Post.id == Collect.post_id) \
#         .filter(Post.id == post_id) \
#         .order_by(desc(Post.id)) \
#         .all()
#     content = contents[0]
#     pictures = []
#     print(content)
#     # titles=[]
#     # authors=[]
#     # avatars=[]
#     # likes=[]
#     for i in range(5):
#         # print(("this is id {}").format(i))
#         if content[i]:
#             pictures.append(content[i])
#     # print(pictures)
#     response_json = jsonify({
#         'pictures': pictures,
#         'date': content[5],
#         'title': content[6],
#         'body': content[7],
#         'author': content[8],
#         'avatar': content[9],
#         'likes_num': content[10],
#         'comments_num': content[11],
#         'collects_num': content[12]
#     })
#     print({
#         'pictures': pictures,
#         'date': content[5],
#         'title': content[6],
#         'body': content[7],
#         'author': content[8],
#         'avatar': content[9],
#         'likes_num': content[10],
#         'comments_num': content[11],
#         'collects_num': content[12]
#     })
#     return response_json


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
#         dates.append(comment[1])
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
#         Like.query.filter(Like.post_id == post_id and Like.author_id == user_id).delete()
#         db.session.commit()
#         return jsonify({'message': '取消点赞成功'})
#     else:
#         return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400


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
#         Collect.query.filter(Collect.post_id == post_id and Collect.user_id == user_id).delete()
#         db.session.commit()
#         return jsonify({'message': '取消收藏成功'})
#     else:
#         return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400


if __name__ == '__main__':
    app.run()
