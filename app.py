from flask import Flask
from registration import registration_bp
from attendance import attendance_bp
from views import views_bp
from deletion import deletion_bp

app = Flask(__name__)

app.register_blueprint(views_bp)
app.register_blueprint(registration_bp, url_prefix='/register')
app.register_blueprint(attendance_bp, url_prefix='/attendance')
app.register_blueprint(deletion_bp, url_prefix='/delete')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)