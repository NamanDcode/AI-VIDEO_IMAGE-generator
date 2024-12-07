from flask import Flask, render_template
from db import session, UserContent

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the AI Video and Image Generator!"

@app.route('/user/<user_id>')
def user_dashboard(user_id):
    # Query the database for user content
    content = session.query(UserContent).filter_by(user_id=user_id).first()
    if content:
        if content.status == "Completed":
            videos = content.video_paths.split(',')
            images = content.image_paths.split(',')
            return render_template("dashboard.html", videos=videos, images=images)
        else:
            return "Your content is still processing. Please check back later."
    else:
        return "No content found for this user."

if __name__ == '__main__':
    app.run(debug=True)
