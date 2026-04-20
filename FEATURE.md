# Greetings Feature

## Feature 描述

Greetings Feature 提供了一个标准化的问候工作流，用于在应用启动或用户交互时展示友好的欢迎信息。该功能支持多种问候语模板，可根据不同场景（如时间、用户类型）动态选择最合适的问候方式。

## 功能说明

- **多场景问候**：支持早安、午安、晚安等基于时间的问候语
- **用户类型适配**：可根据普通用户、VIP 用户、新用户等身份展示不同问候
- **多语言支持**：内置中英文问候语模板，易于扩展其他语言
- **自定义模板**：允许开发者注册自定义问候语模板
- **静默模式**：支持在特定场景下关闭问候输出

## 使用方法（Usage 示例）

### 基础用法

```python
from greetings import Greeter

greeter = Greeter()
print(greeter.greet())  # 输出: 你好！欢迎使用我们的服务。
```

### 根据时间问候

```python
from greetings import Greeter

greeter = Greeter()
print(greeter.greet_by_time())
# 早上输出: 早上好！祝您今天充满活力。
# 下午输出: 下午好！希望您度过愉快的一天。
# 晚上输出: 晚上好！感谢您的使用。
```

### 按用户类型问候

```python
from greetings import Greeter

greeter = Greeter()

# 新用户
print(greeter.greet(user_type="new"))
# 输出: 欢迎新用户！我们很高兴为您服务。

# VIP 用户
print(greeter.greet(user_type="vip"))
# 输出: 尊敬的 VIP 用户，欢迎回来！
```

### 自定义问候模板

```python
from greetings import Greeter

greeter = Greeter()
greeter.register_template("holiday", "节日快乐！祝您度过美好的假期。")
print(greeter.greet(template="holiday"))
```

### 在 CLI 工具中使用

```python
import sys
from greetings import Greeter

def main():
    greeter = Greeter(lang="en")
    print(greeter.greet())
    # 继续执行其他业务逻辑...

if __name__ == "__main__":
    main()
```

## 注意事项

1. **时区问题**：`greet_by_time()` 默认使用系统本地时间，如需指定时区，请在初始化时传入 `timezone` 参数
2. **模板优先级**：当同时指定 `template` 和 `user_type` 时，`template` 参数优先级更高
3. **性能考虑**：频繁创建 `Greeter` 实例可能影响性能，建议在应用启动时初始化一次并复用
4. **语言回退**：如果指定的语言模板不存在，会自动回退到默认语言（中文），可通过 `fallback_lang` 参数修改
5. **线程安全**：`Greeter` 实例是线程安全的，但 `register_template()` 方法应在初始化阶段调用，避免运行时并发修改
