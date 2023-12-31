import rest
from app import application
from flask import render_template
from flask import Flask


@application.route('/')
def home_page():
    return render_template('index.html')


@application.route('/<string:area>/<string:issue>')
def posts(area, issue):
    return render_template('posts.html', post_left=rest.retrieve_posts_left(area,issue), post_right=rest.retrieve_posts_right(area,issue))

@application.route('/areas')
def areas_page():
    return render_template('areas.html', areas=rest.retrieve_areas())

@application.route('/<string:area>')
def issues_page(area):
    return render_template('issues.html', issues=rest.retrieve_issues(area))


@application.route('/about/page')
def about_page():
    return render_template('about.html')


@application.route('/contact/page')
def contact_page():
    return render_template('contact.html')

@application.route('/local/page')
def local_page():
    return render_template('local.html')


@application.route('/login/page')
def login_page():
    return render_template('login.html')


@application.route('/politicians/page')
def politicians_page():
    return render_template('politicians.html', postdict_left=rest.retrieve_thread_left(), postdict_right=rest.retrieve_thread_right())


@application.route('/signup/page')
def signup_page():
    return render_template('signup.html')


@application.route('/faq/page')
def faq_page():
    return render_template('faq.html')


@application.route('/user_profile/page')
def user_profile_page():
    return render_template('user_profile.html')


@application.route('/post/page/<int:post_id>')
def post_page(post_id):
    return render_template('post.html', post_id=post_id, postdict=rest.retrieve_thread(post_id=post_id), postcomments=rest.retrieve_post_comments(post_id=post_id))


@application.route('/make_post/page')
def make_post_page():
    return render_template('make_post.html')


if __name__ == "__main__":
    application.debug = True
    application.run(port=8000)
