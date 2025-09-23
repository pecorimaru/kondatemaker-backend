from typing import Optional

from app.utils.api_utils import CamelModel
from app.models.display import RecipeDisp, RecipeIngredDisp


class SubmitAddRecipeRequest(CamelModel):
    recipe_nm: str
    recipe_nm_k: Optional[str] = None
    recipe_type: str
    recipe_url: Optional[str] = None


class SubmitAddRecipeResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_recipe: RecipeDisp


class SubmitEditRecipeRequest(CamelModel):
    recipe_id: int
    recipe_nm: str
    recipe_nm_k: Optional[str] = None
    recipe_type: str
    recipe_url: Optional[str] = None


class SubmitEditRecipeResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_recipe: RecipeDisp


class SubmitDeleteRecipeResponse(CamelModel):
    status_code: int
    message: Optional[str] = None


class SubmitAddRecipeIngredRequest(CamelModel):
    recipe_id: int
    ingred_nm: str
    qty: float
    unit_cd: str


class SubmitAddRecipeIngredResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_recipe_ingred: RecipeIngredDisp


class SubmitUpdateRecipeIngredRequest(CamelModel):
    recipe_ingred_id: int
    ingred_nm: str
    qty: float
    unit_cd: str


class SubmitUpdateRecipeIngredResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
    new_recipe_ingred: RecipeIngredDisp


class SubmitDeleteRecipeIngredRequest(CamelModel):
    recipe_ingred_id: int


class SubmitDeleteRecipeIngredResponse(CamelModel):
    status_code: int
    message: Optional[str] = None
