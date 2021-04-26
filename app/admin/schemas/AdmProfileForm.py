from app.admin.models.AdmProfile import AdmProfile
from typing import Dict


class AdmProfileForm:
    administrator: str
    description: str
    general: str

    def __init__(self, admProfile: Dict):
        self.administrator=admProfile["administrator"]
        self.description=admProfile["description"]
        self.general=admProfile["general"]

    def to_AdmProfile(self):
        newAdmProfile = AdmProfile(
            administrator=self.administrator,
            description=self.description,
            general=self.general
        )
        return newAdmProfile

    def from_AdmProfile(self, admProfile: AdmProfile):
        admProfile.administrator=self.administrator
        admProfile.description=self.description
        admProfile.general=self.general

        return admProfile
