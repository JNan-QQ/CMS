import smtplib
from email.mime.text import MIMEText


class _Email:
    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.163.com'
    # 163用户名
    mail_user = 'jn896333574@163.com'
    # 密码(部分邮箱为授权码)
    mail_pass = 'QCIRGOCFFSFIYKVL'
    # 邮件发送方邮箱地址
    sender = 'jn896333574@163.com'

    def sendEmail(self, title, content, receivers):
        # 设置email信息
        # 邮件内容设置
        message = MIMEText(content, 'plain', 'utf-8')
        # 邮件主题
        message['Subject'] = title
        # 发送方信息
        message['From'] = self.sender

        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(self.mail_host, 25)
            # 登录到服务器
            smtpObj.login(self.mail_user, self.mail_pass)
            # 发送
            for receiver in receivers:
                message['To'] = receiver
                smtpObj.sendmail(self.sender, receiver, message.as_string())
            # 退出
            smtpObj.quit()
            return True
        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误
            return False


SendEmail = _Email()
