import sys
import os
from flask import Flask, jsonify, request, render_template, url_for, send_from_directory
from flask_cors import CORS, cross_origin

from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
from sqlalchemy import func
from sqlalchemy.orm import relationship

from flask_socketio import SocketIO, emit, join_room
from datetime import datetime

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
    senior = db.Column(db.Boolean)  # 是否为付费用户
    description = db.Column(db.String(100))  #一句话介绍自己
    
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
            'senior': user.senior,
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
        func.count(Like.id).label('like')
    ).join(Collect, Post.id == Collect.post_id).join(User, Post.author_id == User.id).outerjoin(Like, Post.id == Like.post_id).filter(Collect.user_id == 1).group_by(Post.picture1, Post.title, User.name, User.photo).all()
    pictures=[]
    titles=[]
    authors=[]
    avatars=[]
    likes=[]
    for collection in collections:
        pictures.append(collection[0])
        titles.append(collection[1])
        authors.append(collection[2])
        avatars.append(collection[3])
        likes.append(collection[4])
    response_json = jsonify({
        'pictures': pictures,
        'titles': titles,
        'authors': authors,
        'avatars': avatars,
        'likes': likes
    })
    print({
        'pictures': pictures,
        'titles': titles,
        'authors': authors,
        'avatars': avatars,
        'likes': likes
    })
    return response_json
    # return jsonify({'error': 'collect not found'}), 404

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

# 转换时间格式
def formatDateTime(time):
    return time.strftime("%Y年%m月%d日 %H:%M:%S").replace("年0", "年").replace("月0", "月").replace("日0", "日")
# 获取历史消息
@app.route('/api/chat/<int:user_id>', methods=['GET'])
def get_chats(user_id):
    chats = Chat.query.filter((Chat.sender == user_id) | (Chat.receiver == user_id)).all()
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

# 新增消息
@app.route('/api/save_message', methods=['POST'])
def receive_messages():
    data = request.json
    print(data)
    chat_id = data.get('chat_id')
    message = data.get('message')

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
            content=content,
            user_id=message.get('user')["id"],
            chat_id=chat.id
        )
        db.session.add(db_message)
        # 更新时间
        chat.last_time = message_datetime
        db.session.commit()

    return jsonify({'message': 'Messages received and saved successfully'}), 200

# 删去消息
@app.route('/api/delete_message', methods=['POST'])
def delete_message():
    message_id = request.json.get('message_id')
    if message_id:
        message = Message.query.get(message_id)
        if message:
            db.session.delete(message)
            db.session.commit()
            return 'Message deleted successfully', 200
        else:
            return 'Message not found', 404
    else:
        return 'No message ID provided', 400

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

if __name__ == '__main__':
    config = dict(
        host='0.0.0.0',
        port=9090,
        debug=True,
        allow_unsafe_werkzeug=True
    )
    socketio.run(app, **config)
