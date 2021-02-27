import os
import yagmail
from jinja2 import Template, Environment, FileSystemLoader
from config import config


class Mailer:

    PREFIX='[Pyworks Mailer]'
    TEMPLATES_ROOT_DIR = 'templates'
    TEMPLATE_USER_REGISTERED = 'user_registered.minify.html'
    TEMPLATE_ORDER_CREATED = 'order_created.minify.html'
    TEMPLATE_NEWSLETTER = 'newsletter.minify.html'

    def __init__(self):
        pass 

    def send(self, subject, body):
        yag = yagmail.SMTP(config.MAIL_USERNAME, config.MAIL_PASSWORD)
        yag.send(
            to=config.MAIL_RECEIVERS,
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

    def send_order_created(self, data):
        try:
            subject = self._get_subject('Order Successfully')
            self.send(subject=subject, body=self._get_body(data, self.TEMPLATE_ORDER_CREATED))
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
    # mail.send_newsletter(data)
    mail.send_order_created(data)
    