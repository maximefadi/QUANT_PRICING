from abc import ABC, abstractmethod
from src.pricing.products.european_call import EuropeanCall

class PricingModel(ABC):
    @abstractmethod
    def price(self, option: EuropeanCall) -> float:
        pass