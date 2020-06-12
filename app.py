import flask


app = flask.Flask(__name__)


def register_blueprints():
    from views import home_views
    from views import package_views
    from views import cms_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


def main():
    register_blueprints()
    app.run(debug=True)
    

if __name__ == '__main__':
    main()