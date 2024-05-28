import sys
import os
from flask import Flask, jsonify, request, render_template, url_for, send_from_directory
from flask_cors import CORS, cross_origin

from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
from sqlalchemy import func, cast, String, desc
from sqlalchemy.orm import relationship

from flask_socketio import SocketIO, emit, join_room
from datetime import datetime

# 防止通信报错 by zyp
import locale
locale.setlocale(locale.LC_CTYPE,"chinese")

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__, static_url_path='/', static_folder='./../frontend/dist', template_folder='./../frontend/dist')
socketio = SocketIO(app, cors_allowed_origins="http://localhost:5173")

# 创建数据库
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app


class User(db.Model):  # 用户
    id = db.Column(db.Integer, primary_key=True)  # 主键，账号
    name = db.Column(db.String(20))  # 名字
    password=db.Column(db.String(20))  # 密码
    photo = db.Column(db.String(60))  # 头像
    email = db.Column(db.String(254))  # 邮箱
    age = db.Column(db.Integer)  # 年龄
    sex = db.Column(db.Boolean)  # 性别，1是男0是女
    is_admin = db.Column(db.Boolean, default=False)
    is_premium = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(100))  #一句话介绍自己
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
    author_id = db.Column(db.Integer)      # 作者id
    post_id = db.Column(db.Integer)      # 文章id

class Collect( db.Model):  # 收藏
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
    show_time = db.Column(db.Boolean) # 该条消息的时间是否显示
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
    messages = relationship("Message", backref="chat") # 包含的消息 一对多

class Draft(db.Model):  # 草稿箱
    __tablename__ = 'Draft'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    date = db.Column(db.DateTime)     # 日期
    user_id = db.Column(db.Integer)      # 用户id
    picture = db.Column(db.String(60))     # 图片
    label = db.Column(db.Text)  # 标签

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
    print("login")
    data = request.form
    username = data.get('username')
    password = data.get('password')
    user_type = data.get('userType')

    # 查询用户
    user = User.query.filter_by(name=username, password=password).first()

    if user:
        if user_type == 'admin' and not user.is_admin:
            return jsonify({'status': 'error', 'message': 'Unauthorized access for admin'}), 401
        if user_type == 'premium' and not user.is_premium:
            return jsonify({'status': 'error', 'message': 'Unauthorized access for premium user'}), 401
        return jsonify({'status': 'success', 'message': 'Login successful',"user_id":user.id}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401

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

            default_avatar_url = 'http://graphcrafter.oss-cn-beijing.aliyuncs.com/avatars/1-default.webp'
            user_now = User(id=id, name=username, password=password, email=email, is_premium=(user_type == 'premium'),photo=default_avatar_url)
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
            'is_premium':user.is_premium,
            #'senior': user.senior,
            'bio': user.description
        })
    return jsonify({'error': 'User not found'}), 404

# 获取用户收藏
@cross_origin()
@app.route('/api/collection', methods=['GET'])
def get_collection():
    # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
    collections=db.session.query(
        Post.picture1,
        Post.title,
        User.name,
        User.photo,
        func.count(Like.id).label('like'),
        Post.id
    ).join(Collect, Post.id == Collect.post_id).join(User, Post.author_id == User.id).outerjoin(Like, Post.id == Like.post_id).filter(Collect.user_id == 1).group_by(Post.picture1, Post.title, User.name, User.photo).all()
    pictures=[]
    titles=[]
    authors=[]
    avatars=[]
    likes=[]
    ids=[]
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
        'ids':ids
    })
    return response_json
    # return jsonify({'error': 'collect not found'}), 404

# 获取用户收藏
@cross_origin()
@app.route('/api/note', methods=['GET'])
def get_note():
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
    ).join(User, Post.author_id == User.id).filter(User.id == 1).outerjoin(Like, Post.id == Like.post_id).group_by(Post.picture1, Post.title, User.name, User.photo).all()
    pictures=[]
    titles=[]
    authors=[]
    avatars=[]
    likes=[]
    ids=[]
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
        'ids':ids
    })
    return response_json
    # return jsonify({'error': 'collect not found'}), 404

# 获取草稿箱
@cross_origin()
@app.route('/api/drafts', methods=['GET'])
def get_drafts():
    # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
    drafts=db.session.query(
        Draft.picture,
        cast(Draft.date,String),
        Draft.label,
        Draft.id
    ).join(User, Draft.user_id == User.id).filter(User.id == 1).all()
    pictures=[]
    dates=[]
    labels=[]
    ids=[]
    for draft in drafts:
        pictures.append(draft[0])
        dates.append(draft[1])
        labels.append(draft[2])
        ids.append(draft[3])
    response_json = jsonify({
        'pictures': pictures,
        'dates': dates,
        'labels': labels,
        'ids':ids
    })
    return response_json
    # return jsonify({'error': 'collect not found'}), 404

# 获取草稿箱
@cross_origin()
@app.route('/api/get_draft/<int:post_id>', methods=['GET'])
def get_draft(post_id):
    # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
    draft=db.session.query(
        Draft.picture,
        cast(Draft.date,String),
        Draft.label,
        Draft.id
    ).join(User, Draft.user_id == User.id).filter(User.id == 1, Draft.id==post_id).first()
    response_json = jsonify({
        'pictures': draft[0],
        'dates': draft[1],
        'labels': draft[2],
        'ids':draft[3]
    })
    print({
        'pictures': draft[0],
        'dates': draft[1],
        'labels': draft[2],
        'ids':draft[3]
    })
    return response_json
    # return jsonify({'error': 'collect not found'}), 404

# 获取草稿箱标签
@cross_origin()
@app.route('/api/get_labels', methods=['GET'])
def get_labels():
    # user = db.session.query(Post.picture1,Post.title,User.name,User.photo,func.count(Like.id).label('like')).filter(Post.id==Collect.post_id and Collect.user_id==1 and Post.author_id==User.id and Like.post_id==Post.id).all()
    drafts=db.session.query(
        Draft.label
    ).join(User, Draft.user_id == User.id).filter(User.id == 1).distinct()
    labels=[]
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
    drafts=db.session.query(
        Draft.picture,
        cast(Draft.date,String),
        Draft.label,
        Draft.id
    ).join(User, Draft.user_id == User.id).filter(User.id == 1,Draft.label==selected_label).all()
    pictures=[]
    dates=[]
    labels=[]
    ids=[]
    for draft in drafts:
        pictures.append(draft[0])
        dates.append(draft[1])
        labels.append(draft[2])
        ids.append(draft[3])
    response_json = jsonify({
        'pictures': pictures,
        'dates': dates,
        'labels': labels,
        'ids':ids
    })
    return response_json
    # return jsonify({'error': 'collect not found'}), 404

# 草稿箱删除
@cross_origin()
@app.route('/api/del_draft/<int:post_id>', methods=['GET'])
def del_draft(post_id):
    draft_to_del=Draft.query.get(post_id)
    db.session.delete(draft_to_del)
    db.session.commit()
    return jsonify({'message': 'Delete successfully'})

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

#查看要改的用户名是否已存在，要确保所有都是unique
# @app.route('/check-username', methods=['GET'])
# def check_username():
#     username = request.args.get('username')
#     existing_user = User.query.filter_by(name=username).first()
#     return jsonify(is_unique=existing_user is None)

@app.route('/check-username', methods=['GET'])
def check_username():
    username = request.args.get('username')
    user_id = request.args.get('user_id')
    existing_user = User.query.filter(User.name == username, User.id != user_id).first()
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
    if user_id:
        user = User.query.filter_by(id=user_id).first()
        if user:
            # If user found, construct response
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
# 获取历史消息
@app.route('/api/chat/<int:user_id>', methods=['GET'])
def get_chats(user_id):
    print("get chats user:",user_id)
    stuff_id = 0
    chats = Chat.query.filter((Chat.receiver == user_id) | ((Chat.sender == user_id) & (Chat.receiver != stuff_id))).all()
    data = []
    for chat in chats:
        messages = Message.query.filter_by(chat_id=chat.id).order_by(Message.id).all()
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
                'show_time':message.show_time,
                'content': message.content,
                'user': transUserData(user)
            }
            chat_data['messages'].append(message_data)
        data.append(chat_data)

    return jsonify(data)

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
        message_datetime = datetime.strptime(message.get('time'), '%Y年%m月%d日 %H:%M:%S')
        max_message_id = db.session.query(func.max(Message.id)).scalar() or 0
        next_message_id = max_message_id + 1
        db_message = Message(
            id = next_message_id,
            type=message.get('type'),
            time= message_datetime,
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
    print("msg id:",message_id)
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
    stuff_id=0# 客服id
    chats = Chat.query.filter((Chat.sender == user_id) & (Chat.receiver == stuff_id)).all()
    data = []
    for chat in chats:
        messages = Message.query.filter_by(chat_id=chat.id).order_by(Message.id).all()
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
@app.route('/api/add_collect', methods=['GET','POST'])
def add_collect():
    post_id = request.json.get('postId')  # 获取文章 ID
    user_id = request.json.get('userId')  # 获取用户 ID
    isAdd = request.json.get('add')
    from datetime import datetime, timezone
    date = datetime.now()
    if isAdd and post_id and user_id:
        new_Collect = Collect(date=date,user_id=user_id,post_id=post_id)
        db.session.add(new_Collect)
        db.session.commit()
        return  jsonify({'message': '收藏成功'})
    elif not isAdd and post_id and user_id:
        Collect.query.filter(Collect.post_id==post_id and Collect.user_id==user_id).delete()
        db.session.commit()
        return  jsonify({'message': '取消收藏成功'})
    else:
        return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400

# 添加点赞
@app.route('/api/add_like', methods=['GET','POST'])
def add_like():
    post_id = request.json.get('postId')  # 获取文章 ID
    user_id = request.json.get('userId')  # 获取用户 ID
    isAdd = request.json.get('add')
    from datetime import datetime, timezone
    date = datetime.now()
    if isAdd and post_id and user_id:
        new_Like = Like(date=date,author_id=user_id,post_id=post_id)
        db.session.add(new_Like)
        db.session.commit()
        return  jsonify({'message': '点赞成功'})
    elif not isAdd and post_id and user_id:
        Like.query.filter(Like.post_id==post_id and Like.author_id==user_id).delete()
        db.session.commit()
        return  jsonify({'message': '取消点赞成功'})
    else:
        return jsonify({'message': '评论内容或文章 ID 不能为空'}), 400

# 获取点赞和收藏的状态
@app.route('/api/get_status/<int:post_id>/<int:userId>', methods=['GET'])
def get_status(post_id,userId):
    # post_id = request.json.get('postId')  # 获取文章 ID
    # user_id = request.json.get('userId')  # 获取用户 ID
    print('post:{},user:{}'.format(post_id,userId))
    isLiked = db.session.query(
                    Like.id
                    ).filter(Like.post_id==post_id and Like.author_id==userId) \
                    .first()
    isCollected = db.session.query(
                    Collect.id
                    ).filter(Collect.post_id==post_id and Collect.user_id==userId) \
                    .first()
    if isLiked:
        isLiked='1'
    else:
        isLiked='0'
    if isCollected: 
        isCollected='1'
    else:   
        isCollected='0'
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
@app.route('/api/submit_comment', methods=['GET','POST'])
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
        newComment=db.session.query(
                    Comment.id,
                    # Comment.date,
                    cast(Comment.date, String),
                    Comment.content,
                    User.name,
                    User.photo
                    ).join(User, Comment.author_id == User.id) \
                        .outerjoin(Post, Comment.post_id == Post.id) \
                        .filter(Post.id==post_id) \
                        .order_by(desc(Comment.id)) \
                        .first()
        response_json = jsonify({
            'ids'  : newComment[0],
            'dates': newComment[1],
            'contents': newComment[2],
            'authors': newComment[3],  
            'avatars': newComment[4]
            })
        print({
            'ids'  : newComment[0],
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
    comments=db.session.query(
        Comment.id,
        # Comment.date,
        cast(Comment.date, String),
        Comment.content,
        User.name,
        User.photo
    ).join(User, Comment.author_id == User.id) \
        .outerjoin(Post, Comment.post_id == Post.id) \
        .filter(Post.id==post_id) \
        .order_by(desc(Comment.id)) \
        .all() 
    ids=[]
    dates=[]
    contents=[]
    authors=[]
    avatars=[]
    for comment in comments:
        ids.append(comment[0])
        dates.append(comment[1])
        contents.append(comment[2])
        authors.append(comment[3])
        avatars.append(comment[4])
    response_json = jsonify({
        'ids'  : ids,
        'dates': dates,
        'contents': contents,
        'authors': authors,  
        'avatars': avatars
    })
    print({
        'ids'  : ids,
        'dates': dates,
        'contents': contents,
        'authors': authors,  
        'avatars': avatars
    })
    return response_json

# 获取帖子详情
@app.route('/api/post_content/<int:post_id>', methods=['GET'])
def get_postContent(post_id):
    # 首先是文章信息，包括内容、作者等
    print(post_id)
    contents=db.session.query(
        Post.picture1,
        Post.picture2,
        Post.picture3,
        Post.picture4,
        Post.picture5,
        # Post.date,
        cast(Post.date, String),
        Post.title,
        Post.body,
        User.name,
        User.photo,
        func.count(Like.id.distinct()).label('like'),
        func.count(Comment.id.distinct()).label('comment'),
        func.count(Collect.id.distinct()).label('collect'),
        Post.id
    ).join(User, Post.author_id == User.id) \
        .outerjoin(Like, Post.id == Like.post_id) \
        .outerjoin(Comment, Post.id == Comment.post_id) \
        .outerjoin(Collect, Post.id == Collect.post_id) \
        .filter(Post.id==post_id) \
        .order_by(desc(Post.id)) \
        .all() 
    content=contents[0]
    pictures=[]
    print(content)
    # titles=[]
    # authors=[]
    # avatars=[]
    # likes=[]
    for i in range(5):
        # print(("this is id {}").format(i))
        if content[i]:
            pictures.append(content[i])
    # print(pictures)
    response_json = jsonify({
        'pictures': pictures,
        'date': content[5],
        'title': content[6],
        'body': content[7],
        'author': content[8],
        'avatar': content[9],
        'likes_num': content[10],
        'comments_num': content[11],
        'collects_num': content[12]
    })
    print({
        'pictures': pictures,
        'date': content[5],
        'title': content[6],
        'body': content[7],
        'author': content[8],
        'avatar': content[9],
        'likes_num': content[10],
        'comments_num': content[11],
        'collects_num': content[12]
    })
    return response_json

# 广场页获取帖子
# @cross_origin()
@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts=db.session.query(
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
    ids=[] 
    pictures=[]
    titles=[]
    authors=[]
    avatars=[]
    likes=[]
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
    print("join:",data)
    chat_id = data['chat_id']
    join_room(chat_id)

@socketio.on('message')
def handle_message(data):
    chat_id = data['chat_id']
    print("chat:",chat_id)
    emit('message', {'message': data['message']}, room=chat_id)

# 管理员相关函数
# 获取所有用户
@app.route('/api/get-all-user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_data = []

    for user in users:
        user_data = {
            'id': user.id,
            'name': user.name,
            'password': user.password,
            'avatar': user.photo,
            'email': user.email,
            'age': user.age,
            'sex': user.sex,
            'senior': user.senior,
            'description': user.description,
            'status':user.status
        }
        users_data.append(user_data)

    return jsonify({'userList': users_data})


# 获取用户和帖子总数
@app.route('/api/get-user-post-num', methods=['GET'])
def get_user_post_num():
    users = User.query.all()
    posts = Post.query.all()
    return jsonify({'userNum':len(users),'postNum':len(posts)})

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
            'pics':[post.picture1,post.picture2,post.picture3,post.picture4,post.picture5],
            'title': post.title,
            'content': post.body,
            'status':post.status
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
    # 获取dataform的实际大小
    cnt = len(dataform)
    # 下面这坨也许可以改进，但是能跑
    pic1 = ''
    pic2 = ''
    pic3 = ''
    pic4 = ''
    pic5 = ''
    if cnt>=1:
        pic1 = dataform[0]
    if cnt>=2:
        pic2 = dataform[1]
    if cnt>=3:
        pic3 = dataform[2]
    if cnt>=4:
        pic4 = dataform[3]
    if cnt>=5:
        pic5 = dataform[4]
    # 谁定义的数据表，表项名字那么长...pic不好么
    post = Post(author_id=user_id, title=title, body=description, picture1=pic1, picture2=pic2, picture3=pic3, picture4=pic4, picture5=pic5)
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'})

if __name__ == '__main__':
    config = dict(
        host='0.0.0.0',
        port=8080,
        debug=True,
        allow_unsafe_werkzeug=True
    )
    socketio.run(app, **config)
