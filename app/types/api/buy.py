from typing import Optional

from app.utils.api_utils import CamelModel
from app.models.display import BuyIngredDisp


class SwitchCompletionStateRequest(CamelModel):
    buy_ingred_id: int
    bought_flg: str


class SwitchCompletionStateResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_buy_ingred: BuyIngredDisp


class SubmitAddBuyIngredRequest(CamelModel):
    ingred_nm: str
    qty: Optional[float] = None
    unit_cd: str
    sales_area_type: str
    is_buy_every_week: bool


class SubmitAddBuyIngredResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_buy_ingred: BuyIngredDisp


class SubmitEditBuyIngredRequest(CamelModel):
    buy_ingred_id: int
    ingred_nm: str
    qty: Optional[float] = None
    unit_cd: str
    sales_area_type: str
    is_buy_every_week: bool


class SubmitEditBuyIngredResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_buy_ingred: BuyIngredDisp


class SubmitDeleteBuyIngredResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
