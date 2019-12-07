from flask import render_template
from . import main
from flask import request
from flask_login import login_required
from flask_login import login_user,current_user




@main.route('/',methods=['GET','POST']) #index 叫做试图函数
def index():
    userid = request.args.get('id')
    return render_template('index.html',title='homepage',uid=userid)


