#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Create Time    : 2019/7/29 17:59
# @Author  : LucasHuang
# @Email: 84457593@qq.com


import os
# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite1.settings'

if __name__ == '__main__':

    # send_mail(
    #     '来自AmazingHuang的测试邮件',
    #     '欢迎访问AmazingHuang的博客',
    #     'from_user@example.com',
    #     ['to_user@example.com'],
    #     fail_silently=False,
    # )

    subject, from_email, to = '来自AmazingHuang的测试邮件', 'from_user@example.com', 'to_user@example.com'
    text_content = '欢迎访问AmazingHuang的博客！'
    html_content = '<p>欢迎访问<a href="http://www.AmazingHuang.com" target=blank>www.AmazingHuang.com</a>，欢迎访问AmazingHuang的博客！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
