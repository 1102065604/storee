# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.utils import formataddr
#
#
# sender = "1102065604@qq.com"
# receiver = "1102065604@qq.com"
#
# repore=open(r"计算器.html", encoding="utf-8")
# email=repore.read()
#
# message = MIMEText(email, "utf-8")
# message["From"] = formataddr(["鲁皓", sender])
# message["To"] = formataddr(["鲁皓", receiver])
#
# # subject = "python SMTP 邮件测试"
# # message["Subject"] = Header(subject, "utf-8")
# # message[subject]="python SMTP 邮件测试"
# server=smtplib.SMTP_SSL("smtp.qq.com",465)
# server.login(sender,"byuvskoqrhxegaaj")
# server.sendmail(sender,[receiver],message.as_string())
# server.quit()
#
# try:
#     # smtp0bj = smtplib.SMTP("smtp.qq.com")
#     # smtp0bj.sendmail(sender, receiver, message.as_string())
#     print("邮件发送成功!")
#
# except smtplib.SMTPException:
#     print("Error:无法发送邮件")

import smtplib
#发送字符串的邮件
# from SendEmail.mime.text import MIMEText
#处理多种形态的邮件主体我们需要 MIMEMultipart 类
# from SendEmail.mime.multipart import MIMEMultipart
#处理图片需要 MIMEImage 类
# from SendEmail.mime.image import MIMEImage


#from youjian.mime.application import MIMEApplication



# if __name__ == '__main__':
#     fromaddr = '2743638431@qq.com'
#     password = 'pqvvankpbntidedh'
#     toaddrs = ['2743638431@qq.com']
#
#     content = '你好这是我的测试报告'
#     textApart = MIMEText(content)
#
#
#     htmlFile='计算器.html'
#     htmlApart=MIMEText(open(htmlFile, 'rb').read(), _subtype='html', _charset='utf-8')
#     htmlApart.add_header('content-Disposition','attachment',filename=htmlFile)
#
#     m = MIMEMultipart()
#     m.attach(textApart)
#     # m.attach(imageApart)
#     # m.attach(pdfApart)
#     # m.attach(zipApart)
#     m.attach(htmlApart)
#
#     m['Subject']='测试报告'
#     m['From'] = fromaddr
#     # 接受方信息
#     m['To'] = toaddrs[0]
#     try:
#         server = smtplib.SMTP('smtp.qq.com')
#         server.login(fromaddr, password)
#         server.sendmail(fromaddr, toaddrs, m.as_string())
#         print('success')
#         server.quit()
#     except smtplib.SMTPException as e:
#         print('error:', e)  # 打印错误

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
#
# # 第三方 SMTP 服务
# mail_host = "smtp.qq.com"  # 设置服务器
# mail_user = "2291494711@qq.com"  # 用户名
# mail_pass = "easokwbixrxldiai"  # 口令
#
# sender = '2291494711@qq.com'
# receivers = ['2291494711@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# # 创建一个带附件的实例
# message = MIMEMultipart()
# message['From'] = Header("蔚超慧", 'utf-8')  # 发件人
# message['To'] = Header("蔚大白", 'utf-8')   # 收件人
#
# subject = 'Python发送带附件的邮件示例'
# message['Subject'] = Header(subject, 'utf-8')
#
# # 邮件正文内容
# send_content = 'hi man，你收到附件了吗？'
# content_obj = MIMEText(send_content, 'plain', 'utf-8')  # 第一个参数为邮件内容
# message.attach(content_obj)
#
# # 构造附件1，发送当前目录下的 t1.txt 文件
# att1 = MIMEApplication(open('计算器.html', 'rb').read(), _subtype='html', _charset='utf-8')
# # att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件附件中显示什么名字
# att1.add_header("Content-Disposition" , 'attachment', filename="计算器.html")
# message.attach(att1)
#
# try:
#     smtpObj = smtplib.SMTP_SSL(mail_host)  # 25 为 SMTP 端口号
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
#     smtpObj.quit()
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")


# !/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '1102065604@qq.com'  # 发件人邮箱账号
my_pass = 'byuvskoqrhxegaaj'  # 发件人邮箱密码
my_user = '1102065604@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["ヾ孤痞°", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["ヾ孤痞°", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")