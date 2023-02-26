# send emails via django

[article](https://www.abstractapi.com/guides/django-send-email)

## What is an SMTP Backend?
SMTP (or Simple Mail Transfer Protocol) is the communication network layer that sends and receives email. Just as the HTTP (Hyper Text Transfer Protocol) handles app-related data traffic, SMTP handles email traffic.

## Why Use SMTP?
1. handles SMTP traffic. 
2. prevent spam 
3. provide a secure environment.


## How Does an SMTP Server Work?

1. The server receives the email information from the mail client (usually on Port 25.) 
2. It breaks the email address of both sender and recipient into two pieces: the name and the domain. 
3. In the email address abstractapi@gmail.com, the name is abstractapi and the domain is gmail.com
4. The SMTP backend examines the domain of the sender and the domain of the recipient. If they both belong to the same domain (i.e. gmail.com) it uses that domain's sending agent to send the email.
5. If the domain of the sender and recipient are different, the server checks whether the sender’s email address is an active and valid email. This is done to prevent spam.
6. If the sender’s address is active, the SMTP server hands over the email data to the recipient’s SMTP server. The recipient's SMTP server handles delivering the email to the recipient's email client

### notes:
- in django we can check if the send email feature is work fine by: `python manage.py sendtestemail`
