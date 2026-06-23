
class NotWearingMaskError(Exception):

    def __str__(self) -> str:
        return "Have no mask"


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):

    def __str__(self) -> str:
        return "Have no vaccine"


class OutdatedVaccineError(VaccineError):

    def __str__(self) -> str:
        return "Vaccine is outdated"
