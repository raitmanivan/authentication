class UserNotFound(Exception):
    pass
class UserAlreadyExists(Exception):
    pass
class InvalidCredentials(Exception):
    pass
class InvalidParams(Exception):
    pass
class InvalidPasswordPolicy(Exception):
    pass
class SecretNotLoaded(Exception):
    pass