import asyncio
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from telegram import Bot
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class NotificationService:
    """Сервис для отправки уведомлений в Telegram и Email"""

    @staticmethod
    async def send_telegram_notification(user_request):
        """Отправка уведомления в Telegram"""
        try:
            bot_token = settings.TELEGRAM_CONFIG['bot_token']
            chat_id = settings.TELEGRAM_CONFIG['chat_id']

            if not bot_token or not chat_id or bot_token == "YOUR_TELEGRAM_BOT_TOKEN":
                logger.warning("Telegram bot token или chat_id не настроены")
                return False

            bot = Bot(token=bot_token)

            message = f"""🔔 Новая заявка с сайта FloksBox!
                    👤 Имя: {user_request.name}
                    📞 Телефон: {user_request.phone}
                    📧 Email: {user_request.email or 'Не указан'}
                    💬 Сообщение: {user_request.message or 'Не указано'}
                    
                    📅 Дата: {user_request.created_at.strftime('%d.%m.%Y %H:%M')}"""

            await bot.send_message(chat_id=chat_id, text=message)
            logger.info(f"Telegram уведомление отправлено для заявки {user_request.id}")
            return True

        except Exception as e:
            logger.error(f"Ошибка отправки в Telegram: {e}")
            return False

    @staticmethod
    def send_email_notification(user_request):
        """Отправка уведомления на Email"""
        try:
            email_config = settings.EMAIL_CONFIG

            if not email_config['email'] or email_config['email'] == "your-email@gmail.com":
                logger.warning("Email настройки не настроены")
                return False

            msg = MIMEMultipart()
            msg['From'] = email_config['email']
            msg['To'] = email_config['recipient']
            msg['Subject'] = f"Новая заявка с сайта FloksBox от {user_request.name}"

            body = f"""
                    Поступила новая заявка с сайта FloksBox:
                    
                    Имя: {user_request.name}
                    Телефон: {user_request.phone}
                    Email: {user_request.email or 'Не указан'}
                    Сообщение: {user_request.message or 'Не указано'}
                    
                    Дата создания: {user_request.created_at.strftime('%d.%m.%Y %H:%M')}
                    
                    ---
                    Это автоматическое уведомление с сайта FloksBox."""

            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            server = smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port'])
            server.starttls()
            server.login(email_config['email'], email_config['password'])
            text = msg.as_string()
            server.sendmail(email_config['email'], email_config['recipient'], text)
            server.quit()

            logger.info(f"Email уведомление отправлено для заявки {user_request.id}")
            return True

        except Exception as e:
            logger.error(f"Ошибка отправки Email: {e}")
            return False

    @staticmethod
    def send_notifications(user_request):
        """Отправка уведомлений в Telegram и Email"""
        results = {
            'telegram': False,
            'email': False
        }

        # Отправка в Telegram (асинхронно)
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            results['telegram'] = loop.run_until_complete(
                NotificationService.send_telegram_notification(user_request)
            )
            loop.close()
        except Exception as e:
            logger.error(f"Ошибка при отправке в Telegram: {e}")

        # Отправка Email
        results['email'] = NotificationService.send_email_notification(user_request)

        return results
