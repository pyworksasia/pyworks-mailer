# Test mailer

from mailer.mailer import Mailer


class TestSendMail:

    def test_send(self):
        mail = Mailer(provider='gmail')    
        subject = "Reset your password"
        data = {
            "user": {
                "fullname": "Brian Lee"
            }
        }
        body = mail.render_from_template(data=data, template_name='forgot_password')
        is_sent_mail = mail.send(subject=subject, body=body)
        assert is_sent_mail