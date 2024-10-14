from enum import StrEnum


class PM10IndexEnum(StrEnum):
    VERY_GOOD = "Very good"
    GOOD = "Good"
    MODERATE = "Moderate"
    SUFFICIENT = "Sufficient"
    BAD = "Bad"
    VERY_BAD = "Very bad"

    @staticmethod
    def from_pm10_value(pm10_value: float) -> "PM10IndexEnum":
        if pm10_value <= 20:
            return PM10IndexEnum.VERY_GOOD
        elif 21 <= pm10_value <= 60:
            return PM10IndexEnum.GOOD
        elif 61 <= pm10_value <= 100:
            return PM10IndexEnum.MODERATE
        elif 101 <= pm10_value <= 140:
            return PM10IndexEnum.SUFFICIENT
        elif 141 <= pm10_value <= 200:
            return PM10IndexEnum.BAD
        else:
            return PM10IndexEnum.VERY_BAD
