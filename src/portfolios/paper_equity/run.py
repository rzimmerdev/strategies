import dxlib as dx
import pandas as pd
from dxlib.markets.alpaca_markets import AlpacaPortfolio, AlpacaOrder, AlpacaMarket


class PaperPortfolio(dx.Portfolio):
    def __init__(self, api):
        super().__init__(api)

        self._portfolio = AlpacaPortfolio(api)
        self._order = AlpacaOrder(api)
        self._market = AlpacaMarket(api)
        self.security_manager = dx.SecurityManager()

    def process_signals(self, signals: pd.Series):
        for security in signals.index:
            signal = signals[security]

            order_data = dx.OrderData(
                security=security,
                quantity=signal.quantity,
                side=signal.side,
                price=signal.price
            )

            self._order.post(order_data, self._market)

    def get_position(self):
        pass
        # TODO: Add market snapshot function
        # return self.value(self._market.price(self.security_manager.get()))
