import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


# 第三方 SMTP 服务
# mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1102065604@qq.com"  # 用户名
mail_pass = "byuvskoqrhxegaaj"  # 口令
mail_sender = "1102065604@qq.com"

repore=open(r"计算器.html", encoding="gbk")
email=repore.read()
def mail():
    ret = True
    try:
        msg = MIMEText(email,"html")
        msg['From'] = formataddr(["ヾ孤痞°", mail_user])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["ヾ孤痞°", mail_sender])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com")  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(mail_user,mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(mail_user, [mail_sender], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接

    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
    return ret
ret = mail()
