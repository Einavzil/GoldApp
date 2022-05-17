from behave import *
# import sys, os
# sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
# from LoginScreen.LoginScreen import Ui_MainWindow as main_win
# import main
# import login

@Given("I have an account already created")
def before_login(context):
    pass
    
# @When("I login to goldapp with '{email}' and '{password}'")
# def step_implpy(context, email, password):    
    # print("Username for login: {}".format(email))
    # print("Password for login: {}".format(password))
    # context.model = main_win
    # context.password = main_win.password_box.setText("pass")
    # context.email = main_win.email_box.setText("liis@gmail.com")
    # context = main_win.open_login()
    # context.log = main_win.login_button(clicked=True)
    pass

@Then("login is successful")
def after_login(context):
    pass