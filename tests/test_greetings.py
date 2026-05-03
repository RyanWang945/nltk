from datetime import datetime
from unittest.mock import patch

import pytest

from greetings import Greeter


class TestGreeterGreet:
    def test_greet_default_zh(self):
        greeter = Greeter(lang="zh")
        assert greeter.greet() == "你好！欢迎使用我们的服务。"

    def test_greet_default_en(self):
        greeter = Greeter(lang="en")
        assert greeter.greet() == "Hello! Welcome to our service."

    def test_greet_new_user_zh(self):
        greeter = Greeter(lang="zh")
        assert greeter.greet(user_type="new") == "欢迎新用户！我们很高兴为您服务。"

    def test_greet_new_user_en(self):
        greeter = Greeter(lang="en")
        assert greeter.greet(user_type="new") == "Welcome, new user! We are glad to serve you."

    def test_greet_vip_user_zh(self):
        greeter = Greeter(lang="zh")
        assert greeter.greet(user_type="vip") == "尊敬的 VIP 用户，欢迎回来！"

    def test_greet_vip_user_en(self):
        greeter = Greeter(lang="en")
        assert greeter.greet(user_type="vip") == "Dear VIP user, welcome back!"

    def test_greet_custom_template(self):
        greeter = Greeter(lang="zh")
        greeter.register_template("holiday", "节日快乐！祝您度过美好的假期。")
        assert greeter.greet(template="holiday") == "节日快乐！祝您度过美好的假期。"

    def test_greet_template_priority_over_user_type(self):
        greeter = Greeter(lang="zh")
        greeter.register_template("holiday", "节日快乐！")
        assert greeter.greet(user_type="vip", template="holiday") == "节日快乐！"

    def test_greet_fallback_lang(self):
        greeter = Greeter(lang="fr", fallback_lang="zh")
        assert greeter.greet() == "你好！欢迎使用我们的服务。"


class TestGreeterGreetByTime:
    @patch("greetings.greeter.datetime")
    def test_greet_by_time_morning_zh(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 1, 8, 0, 0)
        mock_datetime.hour = property(lambda self: 8)
        greeter = Greeter(lang="zh")
        assert greeter.greet_by_time() == "早上好！祝您今天充满活力。"

    @patch("greetings.greeter.datetime")
    def test_greet_by_time_afternoon_zh(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 1, 14, 0, 0)
        mock_datetime.hour = property(lambda self: 14)
        greeter = Greeter(lang="zh")
        assert greeter.greet_by_time() == "下午好！希望您度过愉快的一天。"

    @patch("greetings.greeter.datetime")
    def test_greet_by_time_evening_zh(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 1, 20, 0, 0)
        mock_datetime.hour = property(lambda self: 20)
        greeter = Greeter(lang="zh")
        assert greeter.greet_by_time() == "晚上好！感谢您的使用。"

    @patch("greetings.greeter.datetime")
    def test_greet_by_time_morning_en(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 1, 8, 0, 0)
        mock_datetime.hour = property(lambda self: 8)
        greeter = Greeter(lang="en")
        assert greeter.greet_by_time() == "Good morning! Wishing you a vibrant day."

    @patch("greetings.greeter.datetime")
    def test_greet_by_time_afternoon_en(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 1, 14, 0, 0)
        mock_datetime.hour = property(lambda self: 14)
        greeter = Greeter(lang="en")
        assert greeter.greet_by_time() == "Good afternoon! Have a pleasant day."

    @patch("greetings.greeter.datetime")
    def test_greet_by_time_evening_en(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 1, 20, 0, 0)
        mock_datetime.hour = property(lambda self: 20)
        greeter = Greeter(lang="en")
        assert greeter.greet_by_time() == "Good evening! Thank you for using our service."

    @patch("greetings.greeter.datetime")
    def test_greet_by_time_fallback_lang(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 1, 8, 0, 0)
        mock_datetime.hour = property(lambda self: 8)
        greeter = Greeter(lang="fr", fallback_lang="zh")
        assert greeter.greet_by_time() == "早上好！祝您今天充满活力。"
