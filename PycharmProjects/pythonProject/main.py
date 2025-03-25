import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email:
    def __init__(self, sender_email, sender_password, recipient, subject, body):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send(self):
        try:
            # Создаем MIME-сообщение
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = self.recipient
            msg["Subject"] = self.subject
            msg.attach(MIMEText(self.body, "plain"))

            # Подключаемся к SMTP-серверу Gmail
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()  # Шифрование соединения
            server.login(self.sender_email, self.sender_password)  # Авторизация
            server.sendmail(self.sender_email, self.recipient, msg.as_string())  # Отправка письма
            server.quit()

            return "Email отправлен успешно!"
        except Exception as e:
            return f"Ошибка при отправке: {e}"

if __name__ == "__main__":
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"  # Используй пароль приложения, а не обычный пароль Gmail
    recipient = "test@example.com"
    subject = "Привет!"
    body = "Это тестовое письмо."

    email = Email(sender_email, sender_password, recipient, subject, body)
    print(email.send())
