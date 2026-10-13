from src.pricing.engine.pricing_engine import PricingEngine
from src.pricing.products.european_call import EuropeanCall
import numpy as np

class MonteCarlo(PricingEngine):
    def __init__(self, n_simulations):
        self.n_simulation = n_simulations

    def price(self, option : EuropeanCall) -> float:
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        sigma = option.sigma

        z = np.random.standard_normal(self.n_simulation)

        ST = S * np.exp((r - 0.5 * sigma **2) * T + sigma * np.sqrt(T) * z

        )
        payoff = np.maximum(ST - K, 0)
        expected_payoff = np.mean(payoff)
        price = np.exp(-r * T) * expected_payoff
        return float(price)
            