from app.admin.models.AdmParameterCategory import AdmParameterCategory
from typing import Dict


class AdmParameterCategoryForm:
    description: str
    order: int

    def __init__(self, admParameterCategory: Dict):
        self.description = admParameterCategory["description"]
        self.order = admParameterCategory["order"]"

    def to_AdmParameterCategory(self):
        newAdmParameterCategory = AdmParameterCategory(
            description=self.description,
            order=self.order
        )
        return newAdmParameterCategory

    def from_AdmParameterCategory(self, admParameterCategory: AdmParameterCategory):
        admParameterCategory.description=self.description
        admParameterCategory.order=self.order

        return admParameterCategory
