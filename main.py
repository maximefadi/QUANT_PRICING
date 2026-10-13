from src.pricing.models.black_scholes import BlackScholes
from src.pricing.engine.pricing_engine import PricingEngine
from src.pricing.products.european_call import EuropeanCall
from src.pricing.models.monte_carlo import MonteCarlo
call = EuropeanCall(S=100, K=100, T=1, r=0.05, sigma=0.2)
print(call.sigma)
print(call.S)

model = BlackScholes()
model = MonteCarlo(100000)
engine = PricingEngine(model)
price = engine.price(call)
print(f"The price of the European call option is: {price:.2f}")