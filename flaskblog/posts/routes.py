from flask import (render_template, url_for, request,
                   redirect, abort, flash, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm, UpdatePostForm
from flaskblog.posts.utils import save_gpx, create_map, download_file

import os
from flask import url_for, current_app, send_from_directory, flash


posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    map_html = None
    gpx_file = None
    if form.validate_on_submit():
        post = Post(title = form.title.data,
                    content = form.content.data,
                    author = current_user)
        if form.gpx.data:
            gpx_file = save_gpx(form.gpx.data)
            post.gpx_file = gpx_file
            map_html = create_map(gpx_file)
        else:
            post.gpx_file = None
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        # return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                            form=form, legend='New Post', folium_map=map_html)


@posts.route("/post/new/<int:post_id>")
def post(post_id):
    """
    pip install flask-download-btn

    for the gpx download button
    """
    post = Post.query.get_or_404(post_id)
    if post.gpx_file:
        map_html = create_map(post.gpx_file)
    else: 
        map_html = None
    return render_template('post.html', title=post.title, post=post, folium_map=map_html)


@posts.route("/post/new/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.gpx_file:
        map_html = create_map(post.gpx_file)
    else: 
        map_html = None
    if post.author != current_user:
        abort(403)
    form = UpdatePostForm()
    if form.validate_on_submit():
        if form.gpx.data:
            gpx_file = save_gpx(form.gpx.data)
            post.gpx_file = gpx_file
            map_html = create_map(post.gpx_file)
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        #return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.gpx.data = post.gpx_file 
    return render_template('create_post.html', title='Update Post',
                            form=form, legend='Update Post', folium_map=map_html)


@posts.route("/post/new/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

@posts.route("/post/new/<int:post_id>/download", methods=['POST','GET'])
@login_required
def download_post(post_id):
    post = Post.query.get_or_404(post_id)
    gpx_directory = os.path.join(current_app.root_path,'static/route_gpx')
    flash(f"GPX file downloaded! {gpx_directory}", 'success')
    filename = post.gpx_file
    return send_from_directory(gpx_directory, filename, as_attachment=True, download_name="route.gpx")
    # download_file(post.gpx_file)
    #flash(f"GPX file downloaded! {post.gpx_file}", 'success')
    return redirect(url_for('posts.post', post_id=post.id))


# @posts.route("/post/new/<int:post_id>/map",methods=['POST'])
# def upload_gpx(post_id):
#     post = Post.query.get_or_404(post_id)
#     form = PostForm()
#     if form.validate_on_submit():
#         if form.gpx.data:
#             gpx_file = save_gpx(form.picture.data)
#             current_user.image_file = gpx_file
#         # post.title = form.title.data
#         # post.content = form.content.data
#         # db.session.commit()
#         flash('GPX file has been uploaded!', 'success')
#         return redirect(url_for('posts.post', post_id=post.id))

#     return render_template('upload.html', form=form)
