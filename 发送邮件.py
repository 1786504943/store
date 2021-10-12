import smtplib
from email.mime.text import MIMEText      # MIMRText()定义邮件正文
from email.mime.multipart import MIMEMultipart  # MIMEMulipart模块构造带附件
# 发送邮件的服务器
smtpserver = 'smtp.qq.com'
# 发送邮件用户和密码
user ="1786504943@qq.com"
password = "dmmxuzfcenkvbbjc"
# 发送者
sender = "1786504943@qq.com"
# 接收者
receiver = "1786504943@qq.com"
# 邮件主题
subject = "加减乘除"
# 发送附件
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
file = open(r"C:\Users\ASUS\PycharmProjects\单元测试\计算器.html", encoding="utf-8").read()
att = MIMEText(file, "html", "utf-8")
att["Content-Type"] = "application/octet-stream"
att.add_header("Content-Disposition", "attachment", filename='计算器.html')  # 邮件显示名称
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender,receiver, msgRoot.as_string())
smtp.quit()

