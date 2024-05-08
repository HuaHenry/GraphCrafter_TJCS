import sys,os
from flask import Flask, jsonify, request, render_template, url_for, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
import os

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__, static_url_path='/', static_folder='./../frontend/dist', template_folder='./../frontend/dist')
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
    user.description = data.get('bio', user.description)

    db.session.commit()
    return jsonify({'message': 'Profile updated successfully'})



if __name__ == '__main__':

    app.run()
