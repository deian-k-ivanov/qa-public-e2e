from enum import Enum


class SortProductMenuOptions(str, Enum):
    NAME_ASC = ("az", "Name (A to Z)")
    NAME_DESC = ("za", "Name (Z to A)")
    PRICE_LOW_TO_HIGH = ("lohi", "Price (low to high)")
    PRICE_HIGH_TO_LOW = ("hilo", "Price (high to low)")

    def __new__(cls, value: str, label: str):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.label = label

        return obj
