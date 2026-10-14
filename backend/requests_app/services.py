import smtplib
import logging
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid

from decouple import config as env
from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)

DEFAULT_RECIPIENTS = ('info@floksbox.ru', 'a.kim@floksbox.ru')


class NotificationService:
    """Письмо менеджерам о новой заявке с сайта."""

    @staticmethod
    def _email_settings():
        email_config = getattr(settings, 'EMAIL_CONFIG', {}) or {}
        host = env('EMAIL_SMTP_HOST', default=email_config.get('smtp_server') or 'smtp.yandex.ru')
        port = env('EMAIL_SMTP_PORT', default=email_config.get('smtp_port') or 465, cast=int)
        user = env('EMAIL_SMTP_USER', default=email_config.get('email') or 'info@floksbox.ru')
        password = env('EMAIL_SMTP_PASSWORD', default='') or email_config.get('password') or ''
        use_ssl = env('EMAIL_SMTP_USE_SSL', default='', cast=str).strip().lower()
        if use_ssl in {'1', 'true', 'yes'}:
            use_ssl = True
        elif use_ssl in {'0', 'false', 'no'}:
            use_ssl = False
        else:
            use_ssl = bool(email_config.get('use_ssl', port == 465))
        recipients = email_config.get('recipients') or DEFAULT_RECIPIENTS
        recipients = [item.strip() for item in recipients if item and item.strip()]
        return {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'use_ssl': use_ssl,
            'recipients': recipients or list(DEFAULT_RECIPIENTS),
        }

    @staticmethod
    def send_email_notification(user_request):
        """Отправка заявки на почту менеджеров."""
        try:
            email_config = NotificationService._email_settings()
            if not email_config['password']:
                logger.error('SMTP-пароль не задан, письмо по заявке %s не отправлено', user_request.id)
                return False

            created_at = timezone.localtime(user_request.created_at)
            subject = f'Новая заявка с сайта Floksbox от {user_request.name}'
            body = (
                'Поступила новая заявка с сайта Floksbox.\n\n'
                f'Номер заявки: {user_request.id}\n'
                f'Имя: {user_request.name}\n'
                f'Телефон: {user_request.phone or "Не указан"}\n'
                f'Email: {user_request.email or "Не указан"}\n'
                f'Страница: {user_request.source or "Сайт"}\n'
                f'Дата: {created_at.strftime("%d.%m.%Y %H:%M")}\n\n'
                'Сообщение:\n'
                f'{user_request.message or "Не указано"}\n'
            )

            msg = MIMEMultipart()
            msg['From'] = email_config['user']
            msg['To'] = ', '.join(email_config['recipients'])
            msg['Subject'] = Header(subject, 'utf-8')
            msg['Date'] = formatdate(localtime=True)
            msg['Message-ID'] = make_msgid(domain='floksbox.ru')
            if user_request.email:
                msg['Reply-To'] = user_request.email
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            if email_config['use_ssl']:
                server = smtplib.SMTP_SSL(email_config['host'], email_config['port'], timeout=20)
            else:
                server = smtplib.SMTP(email_config['host'], email_config['port'], timeout=20)
                server.ehlo()
                if email_config['port'] == 587:
                    server.starttls()
                    server.ehlo()
            try:
                server.login(email_config['user'], email_config['password'])
                server.sendmail(email_config['user'], email_config['recipients'], msg.as_string())
            finally:
                server.quit()

            logger.info(
                'Письмо по заявке %s отправлено: %s',
                user_request.id,
                ', '.join(email_config['recipients']),
            )
            return True
        except Exception as exc:
            logger.error('Ошибка отправки письма по заявке %s: %s', getattr(user_request, 'id', '?'), exc)
            return False

    @staticmethod
    def send_notifications(user_request):
        """Отправка заявки на почту."""
        return {
            'email': NotificationService.send_email_notification(user_request),
        }
