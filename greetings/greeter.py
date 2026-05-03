from datetime import datetime


class Greeter:
    def __init__(self, lang="zh", fallback_lang="zh"):
        self.lang = lang
        self.fallback_lang = fallback_lang
        self._templates = {}

    def register_template(self, name, message):
        if name not in self._templates:
            self._templates[name] = {}
        self._templates[name][self.lang] = message

    def greet(self, user_type=None, template=None):
        if template and template in self._templates:
            tpl = self._templates[template]
            return tpl.get(self.lang, tpl.get(self.fallback_lang, ""))

        defaults = {
            "zh": {
                "default": "你好！欢迎使用我们的服务。",
                "new": "欢迎新用户！我们很高兴为您服务。",
                "vip": "尊敬的 VIP 用户，欢迎回来！",
            },
            "en": {
                "default": "Hello! Welcome to our service.",
                "new": "Welcome, new user! We are glad to serve you.",
                "vip": "Dear VIP user, welcome back!",
            },
        }

        lang_map = defaults.get(self.lang, defaults.get(self.fallback_lang, {}))
        key = user_type if user_type else "default"
        return lang_map.get(key, lang_map.get("default", ""))

    def greet_by_time(self):
        hour = datetime.now().hour

        if 5 <= hour < 12:
            period = "morning"
        elif 12 <= hour < 18:
            period = "afternoon"
        else:
            period = "evening"

        messages = {
            "zh": {
                "morning": "早上好！祝您今天充满活力。",
                "afternoon": "下午好！希望您度过愉快的一天。",
                "evening": "晚上好！感谢您的使用。",
            },
            "en": {
                "morning": "Good morning! Wishing you a vibrant day.",
                "afternoon": "Good afternoon! Have a pleasant day.",
                "evening": "Good evening! Thank you for using our service.",
            },
        }

        lang_map = messages.get(self.lang, messages.get(self.fallback_lang, {}))
        return lang_map.get(period, "")
