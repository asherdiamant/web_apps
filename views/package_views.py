import flask

from infrastructure.view_modifiers import response
from services import package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
# @response(template_file='packages/details.html')
def package_details(package_name: str):
    return f'package details for {package_name}'


@blueprint.route('/<int:rank>')
def popular(rank: int):
    return f'Package details for the {rank}th most popular package'