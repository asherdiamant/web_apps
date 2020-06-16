import flask
from flask import url_for

from infrastructure import request_dict
from infrastructure.view_modifiers import response
from services import user_service
import infrastructure.cookie_auth as cookie_auth
from viewmodels.account.Index_viewmodel import IndexViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ################## INDEX ######################

@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    if not vm.user:
        return flask.redirect(url_for('account.login_get'))
    return vm.to_dict()


# ################## REGISTER ####################

@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    vm = RegisterViewModel()
    return vm.to_dict()


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    vm = RegisterViewModel()
    vm.validate()

    if vm.error:
        return vm.to_dict()

    user = user_service.create_user(vm.name, vm.email, vm.password)
    if not user:
        vm.error = 'The account could not be created'
        return vm.to_dict()

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)
    return resp


# #################### LOGIN ######################

@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():

    data = request_dict.create(default_val='')

    email = data.email.lower().strip()
    password = data.password.strip()

    if not email or not password:
        return {
            'email': email,
            'password': password,
            'error': "Some required fields are missing"
        }

    # TODO: Validate the user
    user = user_service.login_user(email, password)
    if not user:
        return {
            'email': email,
            'password': password,
            'error': "The account does not exist or the password is incorrect"
        }

    resp = flask.redirect(url_for('account.index'))
    cookie_auth.set_auth(resp, user.id)
    return resp


# #################### LOGOUT ######################

@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect(url_for('home.index'))
    cookie_auth.logout(resp)
    return resp
