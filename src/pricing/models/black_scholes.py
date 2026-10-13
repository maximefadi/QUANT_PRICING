import math
from scipy.stats import norm
from src.pricing.models.base import PricingModel
from src.pricing.products.european_call import EuropeanCall

class BlackScholes(PricingModel):
    def price(self, option: EuropeanCall) -> float:
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        sigma = option.sigma

        d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)

        call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        return call_price