from app.api import bp


@bp.route("/hello")
def index():
    return "Hello world!"
