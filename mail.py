import smtplib
import ssl
from email.message import EmailMessage

port = 587
# Enter your email provider smtp server
smtp_server = "smtp.server.com"
# Enter your sender email address
sender_email = "sender@server.com"
# Enter your receiver email address
receiver_email = "receiver@server.com"
# Enter your password when prompted
password = input("Type your password and press enter: ")


def send_ej_numbers(nums, win):
    try:
        context = ssl.create_default_context()
        msg = EmailMessage()
        if win:
            msg['Subject'] = "Eurojackpot WIIIIIIIN"
        else:
            msg['Subject'] = "Eurojackpot"
        msg['From'] = sender_email
        msg['To'] = receiver_email
        nums_s = ""
        nums_s += create_string_from_list(nums)
        msg.set_content(nums_s)
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.send_message(msg)
    except Exception as e:
        print("Check smtp server values and your password then try again.")
        print("Exception: ", e)


def create_string_from_list(nums):
    string = ""
    for i in range(0, len(nums)):
        string += str(nums[i])
        if i == 4:
            string += " joker: "
        elif i == 6:
            string += ""
        else:
            string += ", "

    return string
