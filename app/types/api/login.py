from typing import Optional

from app.utils.api_utils import CamelModel


class LoginRequest(CamelModel):
    email: str
    password: Optional[str] = None


class GoogleLoginRequest(CamelModel):
    google_token: str


class LoginResponse(CamelModel):
    status_code: int
    message: str
    user_nm: Optional[str] = None
    access_token: Optional[str] = None


class VerifyRequest(CamelModel):
    token: str


class VerifyResponse(CamelModel):
    status_code: int


class RefreshRequest(CamelModel):
    refresh_token: str


class RefreshResponse(CamelModel):
    status_code: int
    new_access_token: str


class ResetPasswordRequest(CamelModel):
    email: str


class ResetPasswordResponse(CamelModel):
    status_code: int
    message: str


class CreateUserRequest(CamelModel):
    email: str
    password: str


class CreateUserResponse(CamelModel):
    status_code: int
    message: str


class ActivateRequest(CamelModel):
    token: str


class ActivateResponse(CamelModel):
    status_code: int
    message: str
