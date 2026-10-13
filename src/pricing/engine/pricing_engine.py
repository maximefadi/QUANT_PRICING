from src.pricing.models.base import PricingModel
from src.pricing.products.european_call import EuropeanCall

class PricingEngine:
    def __init__(self, model: PricingModel):
        self.model = model

    def price(self, option: EuropeanCall) -> float:
        return self.model.price(option)