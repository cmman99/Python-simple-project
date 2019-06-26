import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 邮件需要发送的信息
send_text = """你好，先生，我的发送者通过一个程序把我，噢，
                没错，就是“我,一封邮件，
                哈哈是不是很好笑”，发送给了您！祝您生活愉快！"
            """
message = MIMEText(send_text)
# 邮件发送人的名字
message['From'] = Header('蟒王python')
# 邮件接收人的名字
message['To'] = Header('爪哇')
# 邮件的标题
message['Subject'] = Header('来自蟒王python的问候!')
# 接受邮件的电子邮箱
recipient = ["xxxxx@163.com", "xxxxx@qq.com"]
email_user = "xxxxx@qq.com"
authorization_code = "stsgqxubjvfpdgid"

# 调用SMTP方法
mail = smtplib.SMTP()
# 连接qq邮箱的SMTP服务器
mail.connect('smtp.qq.com')
mail.login(email_user, authorization_code)
# 发送账号、接收账号和邮件信息
mail.sendmail(email_user, recipient, message.as_string())
