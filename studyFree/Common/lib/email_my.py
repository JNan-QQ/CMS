import os.path
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from config.settings import BASE_DIR

email_file_path = os.path.join(BASE_DIR, 'Common', 'templates', 'email.html')
with open(email_file_path, 'r', encoding='utf8') as fb:
    email_html = fb.read()


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

    # 修改邮箱通知邮件
    email_modify_email = 1
    email_modify_email_title = '你的 【StudyFree】 账户提醒你：你正在修改绑定邮箱！'

    # 用户注册通知邮件
    email_register = 2
    email_register_title = '【StudyFree】提醒你：你正在注册并绑定账号！'

    # 用户注册通知邮件
    email_modify_password = 3
    email_modify_password_title = '你的 【StudyFree】 账户提醒你：你正在修改账号密码！'

    # 消息通知邮件
    email_other = 4
    email_other_title = '来自 【StudyFree】 的通知！'

    def sendEmail(self, email_type, receivers, title='', content='', username='', code=''):

        # 添加邮件模板
        # 修改邮箱
        if email_type == self.email_modify_email:
            title = self.email_modify_email_title
            content = email_html.format(username, '修改绑定邮箱', code)

        # 注册账号
        elif email_type == self.email_register:
            title = self.email_register_title
            content = email_html.format('用户', '注册账号', code)

        elif email_type == self.email_modify_password:
            title = self.email_modify_password_title
            content = email_html.format(username, '修改密码', code)

        elif email_type == self.email_other:
            title = self.email_other_title

        # 设置email信息
        # 邮件内容设置
        message = MIMEText(content, 'html', 'utf-8')
        # 邮件主题
        message['Subject'] = Header(title, 'utf-8')
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
