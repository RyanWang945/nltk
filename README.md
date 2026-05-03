# Greetings

A minimal Python greetings package with a `Greeter` class supporting Chinese and English.

## Quick Start

```python
from greetings import Greeter

greeter = Greeter()
print(greeter.greet())
print(greeter.greet_by_time())
```

## User Types

```python
from greetings import Greeter

greeter = Greeter()
print(greeter.greet(user_type="new"))  # Welcome, new user! We are glad to serve you.
print(greeter.greet(user_type="vip"))  # Dear VIP user, welcome back!
```

## Run Tests

```bash
pytest -q
```

## 项目规划

本项目计划作为 [Jarvis](https://github.com/jarvis) 的测试项目使用。
