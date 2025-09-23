from typing import Optional

from app.utils.api_utils import CamelModel
from app.models.display import IngredDisp, IngredUnitConvDisp


class SubmitAddIngredRequest(CamelModel):
    ingred_nm: str
    ingred_nm_k: Optional[str] = None
    parent_ingred_nm: str
    buy_unit_cd: str
    sales_area_type: Optional[str] = None


class SubmitAddIngredResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_ingred: IngredDisp


class SubmitEditIngredRequest(CamelModel):
    ingred_id: int
    ingred_nm: str
    ingred_nm_k: Optional[str] = None
    parent_ingred_nm: str
    buy_unit_cd: str
    sales_area_type: Optional[str] = None


class SubmitEditIngredResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    edit_ingred: IngredDisp


class SubmitDeleteIngredResponse(CamelModel):
    status_code: int
    message: Optional[str] = None


class SubmitAddIngredUnitConvRequest(CamelModel):
    ingred_id: int
    conv_unit_cd: str
    conv_rate: float


class SubmitAddIngredUnitConvResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_ingred_unit_conv: IngredUnitConvDisp


class SubmitUpdateIngredUnitConvRequest(CamelModel):
    ingred_unit_conv_id: int
    ingred_id: int
    conv_unit_cd: str
    conv_rate: float


class SubmitUpdateIngredUnitConvResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_ingred_unit_conv: IngredUnitConvDisp


class SubmitDeleteIngredUnitConvRequest(CamelModel):
    ingred_unit_conv_id: int


class SubmitDeleteIngredUnitConvResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
