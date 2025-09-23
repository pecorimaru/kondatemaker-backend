from typing import Optional

from app.utils.api_utils import CamelModel
from app.models.display import MenuPlanDisp, MenuPlanDetDisp


class SubmitAddMenuPlanRequest(CamelModel):
    menu_plan_nm: str
    menu_plan_nm_k: str


class SubmitAddMenuPlanResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_menu_plan: MenuPlanDisp


class SubmitEditMenuPlanRequest(CamelModel):
    menu_plan_id: int
    menu_plan_nm: str
    menu_plan_nm_k: str


class SubmitEditMenuPlanResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_menu_plan: MenuPlanDisp


class SubmitDeleteMenuPlanResponse(CamelModel):
    status_code: int
    message: Optional[str] = None


class SubmitAddMenuPlanDetRequest(CamelModel):
    menu_plan_id: int
    weekday_cd: str
    recipe_nm: str


class SubmitAddMenuPlanDetResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_menu_plan_det: MenuPlanDetDisp


class SubmitEditMenuPlanDetRequest(CamelModel):
    menu_plan_det_id: int
    weekday_cd: str
    recipe_nm: str


class SubmitEditMenuPlanDetResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_menu_plan_det: MenuPlanDetDisp


class SubmitDeleteMenuPlanDetResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
