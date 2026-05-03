from fastapi import APIRouter

from greetings.greeter import Greeter


router = APIRouter()


@router.get("/")
@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/greet")
def greet(name=None, language="en", user_type=None):
    greeting = Greeter(lang=language).greet(user_type=user_type)
    return {"greeting": greeting, "name": name, "language": language}


@router.get("/greet-by-time")
def greet_by_time(name=None, language="en"):
    greeting = Greeter(lang=language).greet_by_time()
    return {"greeting": greeting, "name": name, "language": language}
