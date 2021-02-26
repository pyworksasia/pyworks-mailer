import os
import yagmail
from jinja2 import Template, Environment, FileSystemLoader
from dotenv import load_dotenv

load_dotenv()

MAIL_HOST = os.getenv('MAIL_HOST')
MAIL_PORT = os.getenv('MAIL_PORT')
MAIL_TLS = os.getenv('MAIL_TLS', True)
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_RECEIVERS = os.getenv('MAIL_RECEIVERS')

if MAIL_RECEIVERS is not None and MAIL_RECEIVERS.find(',') > -1:
    MAIL_RECEIVERS = MAIL_RECEIVERS.split(',')


class Mailer:

    PREFIX='[Pyworks Mailer]'
    TEMPLATES_ROOT_DIR = 'templates'
    TEMPLATE_USER_REGISTERED = 'user_registered.minify.html'
    TEMPLATE_ORDER_CREATED = 'order_created.minify.html'
    TEMPLATE_NEWSLETTER = 'newsletter.minify.html'

    def __init__(self):
        pass 

    def send(self, subject, body):
        yag = yagmail.SMTP(MAIL_USERNAME, MAIL_PASSWORD)
        yag.send(
            to=MAIL_RECEIVERS,
            subject=subject,
            contents=body, 
        )

    
    def send_user_registered(self, data):
        try:
            subject = self._get_subject('Thank you for register awesome website')
            self.send(subject=subject, body=self._get_body(data, self.TEMPLATE_USER_REGISTERED))
        except Exception as e:
            raise e

    def send_newsletter(self, data):
        try:
            subject = self._get_subject('New Content Publishing API, PyWorks Community Blog, and more')
            self.send(subject=subject, body=self._get_body(data, self.TEMPLATE_NEWSLETTER))
        except Exception as e:
            raise e

    def _get_subject(self, subject):
        return '{prefix} {subject}'.format(prefix=self.PREFIX, subject=subject)

    def _get_body(self, data, template):                    
        return self._render_from_template(data, template_file=template)

    def _render_from_template(self, data, template_file):
        file_loader = FileSystemLoader(self.TEMPLATES_ROOT_DIR)
        env = Environment(loader=file_loader)
        template = env.get_template(template_file)
        output = template.render(data)
        return output
        

if __name__ == '__main__':
    data = {
        "user": {
            "fullname": "Brian Lee"
        }
    }
    mail = Mailer()
    # mail.send_user_registered(data)
    mail.send_newsletter(data)
    