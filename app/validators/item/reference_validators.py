from fastapi import HTTPException, status
from app.crud.app_const_crud import AppConstCrud
from app.models import MenuPlanDet, RecipeIngred
from app.utils import message_utils as msg
from app.utils import constants as const


def check_recipe_unreferenced(menu_plan_det_list: list[MenuPlanDet]):
    """レシピ非参照チェック"""
    if menu_plan_det_list:
        menu_plan_example = menu_plan_det_list[0].rel_t_menu_plan.menu_plan_nm
        menu_plan_other = "など" if len(menu_plan_det_list) > 1 else ""
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=msg.get_message(
                msg.ME0012_NOT_DELETABLE_FOREIGN_KEY, 
                menu_plan_det_list[0].rel_t_recipe.recipe_nm, 
                "献立プラン", 
                menu_plan_example, 
                menu_plan_other
            ),
        )


def check_ingred_unreferenced(recipe_ingred_list: list[RecipeIngred]):
    """食材非参照チェック"""
    if recipe_ingred_list:
        recipe_example = recipe_ingred_list[0].rel_t_recipe.recipe_nm
        recipe_other = "など" if len(recipe_ingred_list) > 1 else ""
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=msg.get_message(
                msg.ME0012_NOT_DELETABLE_FOREIGN_KEY, 
                recipe_ingred_list[0].rel_m_ingred.ingred_nm, 
                "レシピ", 
                recipe_example, 
                recipe_other
            ),
        ) 


def check_ingred_unit_conv_unreferenced(recipe_ingred_list: list[RecipeIngred], app_const_crud: AppConstCrud):
    """食材非参照チェック"""
    if recipe_ingred_list:
        recipe_example = recipe_ingred_list[0].rel_t_recipe.recipe_nm
        recipe_other = "など" if len(recipe_ingred_list) > 1 else ""
        app_const = app_const_crud.get_app_const_from_val(const.APP_CONST_C0002_UNIT_TYPE, recipe_ingred_list[0].rel_m_ingred_unit_conv.conv_unit_cd)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=msg.get_message(
                msg.ME0012_NOT_DELETABLE_FOREIGN_KEY, 
                app_const.val_content, 
                "レシピ", 
                recipe_example, 
                recipe_other
            ),
        ) 