from flask_mail import Message
from app import app, mail


def send_email_reg(sender, username, password):
    s = [sender]
    msg = Message("Registration in Sea Battle Online", recipients=s)
    msg.body = "An account in Sea Battle Online was registered to this mail.\nIf you did not do this, please send " \
               "an answer.\nIf it was you, then do not reply to this message.\nYour " \
               "login: " + username + "\nYour password: " + password
    mail.send(msg)


def send_email_del(sender, username):
    s = [sender]
    msg = Message("Deleting account in Sea Battle Online", recipients=s)
    msg.body = "Your account '" + username + "' in Sea Battle Online has been deleted." + \
               "\nIf it wasn’t you, send an answer"
    mail.send(msg)
