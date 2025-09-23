from typing import Optional

from app.utils.api_utils import CamelModel
from app.models.display import GroupDisp


class SubmitEditUserNmRequest(CamelModel):
    edit_user_nm: str


class SubmitEditUserNmResponse(CamelModel):
    status_code: int
    message: Optional[str] = None


class SubmitChangePasswordRequest(CamelModel):
    current_password: str
    new_password: str


class SubmitChangePasswordResponse(CamelModel):
    status_code: int
    message: Optional[str] = None


class SubmitDeleteUserResponse(CamelModel):
    status_code: int
    message: Optional[str] = None


class SubmitEditGroupNmRequest(CamelModel):
    edit_group_nm: str


class SubmitEditGroupNmResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    edit_group: GroupDisp


class SubmitMemberInviteRequest(CamelModel):
    to_email: str


class SubmitMemberInviteResponse(CamelModel):
    status_code: int
    message: Optional[str] = None


class JoinGroupRequest(CamelModel):
    token: str


class JoinGroupResponse(CamelModel):
    status_code: int
    message: Optional[str] = None


class ChangeGroupRequest(CamelModel):
    group_id: int


class ChangeGroupResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    access_token: Optional[str] = None


class ExitGroupResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    access_token: Optional[str] = None


class LogoutResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
