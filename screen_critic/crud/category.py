from screen_critic.crud.base import CRUDBase
from screen_critic.models import Category
from screen_critic.schemas.category import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    pass


category = CRUDCategory(Category)
