from app.admin.models.AdmPage import AdmPage
from typing import Dict


class AdmPageForm:
    description: str
    url: str

    def __init__(self, admPage: Dict):
        self.description=admPage["description"]
        self.url=admPage["url"]

    def to_AdmPage(self):
        newAdmPage = AdmPage(
            description=self.description,
            url=self.url
        )
        return newAdmPage

    def from_AdmPage(self, admPage: AdmPage):
        admPage.description=self.description
        admPage.url=self.url

        return admPage
