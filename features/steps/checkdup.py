from behave import *
#from features.steps.env import *
from features.env import kishore


@given(u"connect to mysql")
def step_impl(context):
    kishore.new_round()


@when(u"validate the data in msql")
def step_impl(context):
    kishore.new_round()



@then(u"show me duplicate values")
def step_impl(context):
    kishore.new_round()
