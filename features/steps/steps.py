from behave import Given, When, Then, Step
from hamcrest import assert_that, equal_to, contains_string
import requests


@When('I call the Api "{api}" with the parameters "{params}"')
def step_impl(context, api, params):
    url = f"{context.config.userdata['base_url']}/{api}"
    params_dict = {}
    if str(params).upper() != 'NONE':
        params_list = str(params).split('&')
        params_tlist = []
        for item in params_list:
            key, value = str(item).split('=')
            params_tlist.append((key, value))
        params_dict = dict(params_tlist)

    context.response = requests.get(url=url, params=params_dict)


@Then('The response code is "{response_code}"')
def step_impl(context, response_code):
    assert_that(int(context.response.status_code), equal_to(int(response_code)))


@Then('The response message is "{message}"')
def step_impl(context, message):
    response_json = context.response.json()
    assert_that(response_json['message'], contains_string(str(message)))


@Then('The response schema matches {schema_file}')
def step_impl(context, schema_file):
    #TO DO
    pass
