from typing import Optional, Dict

from app.utils.api_utils import CamelModel


class SubmitRecreateToweekPlanRequest(CamelModel):
    selected_plan_id: int


class SubmitRecreateToweekPlanResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_toweek_menu_plan_det_list_dict: Dict[str, list]


class SubmitAddToweekMenuPlanDetRequest(CamelModel):
    recipe_nm: str
    weekday_cd: str


class SubmitAddToweekMenuPlanDetResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    toweek_menu_plan_det_list_dict: Dict[str, list]


class SubmitEditToweekMenuPlanDetRequest(CamelModel):
    toweek_menu_plan_det_id: int
    recipe_nm: str


class SubmitEditToweekMenuPlanDetResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    toweek_menu_plan_det_list_dict: Dict[str, list]


class SubmitDeleteToweekMenuPlanDetResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
