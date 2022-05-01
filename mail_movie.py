# -*- coding: utf-8 -*-
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email import Encoders
from email.mime.base import MIMEBase
import mimetypes

FROM_ADDRESS = 'SENDER EMAIL ADDRESS'
MY_PASSWORD = 'SENDER EMAIL PASSWORD'
TO_ADDRESS = 'RECEIVER EMAIL ADDRESS'
BCC = ''
SUBJECT = '異常検知'
BODY = ''


def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    mimetype, mimeencoding = mimetypes.guess_type(body)
    maintype, subtype = mimetype.split('/')
    with open(body, 'rb') as fp:
      attach = MIMEBase(mimetype, mimeencoding)
      attach.set_payload(fp.read())
      Encoders.encode_base64(attach)
      attach.add_header('Content-Disposition', 'attachment', filename=body)
      msg.attach(attach)
    return msg


def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


if __name__ == '__main__':

    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY

    msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, sys.argv[1])
    send(FROM_ADDRESS, to_addr, msg)