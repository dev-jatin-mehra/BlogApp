from flask import request,Blueprint,render_template,flash,redirect,url_for
from flask_login import login_user,current_user,logout_user,login_required
from app import db,bcrypt
from app.users.forms import RegistrationForm,RequestResetForm,ResetPasswordForm,LogInForm,UpdateAccountForm
from app.users.utils import save_picture,send_reset_email
from app.models import Post,User



users = Blueprint('users',__name__)


@users.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hash_pass)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created successfully !','success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title = 'Register' , form = form)



@users.route("/login",methods=['GET','POST'])
def login():
    form = LogInForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('LogIn Unsuccessful! Check The credentials','danger')
    return render_template('login.html', title = 'LogIn' , form = form)



@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('users.register'))


@users.route("/account",methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your Account has been updated !','success')
        return redirect(url_for('main.home'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static',filename = 'assets/' + current_user.image_file)
    return render_template('account.html', title = 'Account',image_file=image_file,form=form)



@users.route("/user/<string:username>")
def user_post(username):
    page = request.args.get('page',default=1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(per_page=5,page=page)
    return render_template('user_post.html',posts=posts,user=user)



@users.route("/resetpass",methods=['GET','POST'])
def reset_Request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset the password !','info')
        return redirect(url_for('users.login'))

    return render_template('reset_Request.html',title='Reset',form=form)



@users.route("/resetpass/<token>",methods=['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    user = User.verify_reset_token(token=token)
    if user is None:
        flash('That is an invalid/expired token','warning')
        return redirect(url_for('users.reset_Request'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hash_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hash_pass
        db.session.commit()
        flash('Your password has been updated successfully !','success')
        return redirect(url_for('users.login'))
    
    return render_template('reset_token.html',title='Reset',form=form)