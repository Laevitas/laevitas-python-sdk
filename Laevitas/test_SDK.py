from unittest import TestCase
from laevitas import sdk

resp = sdk.api()
resp.configure('api-key')


class Testoptions(TestCase):
    def test_instruments(self):
        message = "Test value is not true."
        response = resp.realtime.options.instruments(market="deribit", currency="btc")
        self.assertTrue(response, message)
        self.assertListEqual(list(response["data"][0].keys()),
                             ["market", "currency", "maturity", "strike", "option_type", "instrument"])

    def test_get_atm(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.get_atm(market="deribit", currency="btc"), message)

    def test_gex_date(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.gex_date(market="deribit", currency="btc", maturity="30JUN23"), message)

    def test_gex_date_all(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.gex_date_all(market="deribit", currency="btc"), message)

    def test_maturities(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.maturities(market="deribit", currency="btc"), message)

    def test_oi_expiry(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.oi_expiry(market="deribit", currency="btc"), message)

    def test_oi_strike_all(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.oi_strike_all(market="deribit", currency="btc"), message)

    def test_oi_type(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.oi_type(market="deribit", currency="btc"), message)

    def test_top_traded_option(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.top_traded_option(market="deribit", currency="btc"), message)

    def test_v_expiry(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.v_expiry(market="deribit", currency="btc"), message)

    def test_v_strike_all(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.v_strike_all(market="deribit", currency="btc"), message)

    def test_volume_buy_sell_all(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.volume_buy_sell_all(market="deribit", currency="btc"), message)

    def test_iv_strike(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.iv_strike(market="deribit", currency="btc", strike="25000"), message)

    def test_oi_strike(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.oi_strike(market="deribit", currency="btc", maturity="30JUN23"), message)

    def test_oi_net_change_all(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.oi_net_change_all(market="deribit", currency="btc", hours="2"), message)

    def test_top_instrument_oi_change(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.top_instrument_oi_change(market="deribit", currency="btc", hours="2"),
                        message)

    def test_volume_buy_sell(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.volume_buy_sell(market="deribit", currency="btc", maturity="30JUN23"),
                        message)

    def test_v_strike(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.v_strike(market="deribit", currency="btc", maturity="30JUN23"), message)

    def test_summary_trades(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.summary_trades(market="deribit", currency="btc", hours="2"), message)

    def test_greeks(self):
        message = "Test value is not true."
        self.assertTrue(
            resp.realtime.options.greeks(market="deribit", currency="btc", maturity="30JUN23", optiontype="c"), message)

    def test_iv_all(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.iv_all(market="deribit", currency="btc", maturity="30JUN23", type="c"),
                        message)

    def test_iv_table(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.iv_table(market="deribit", currency="btc"), message)

    def test_oi_net_change(self):
        message = "Test value is not true."
        self.assertTrue(
            resp.realtime.options.oi_net_change(market="deribit", currency="btc", maturity="30JUN23", hour="2"),
            message)

    def test_snapshot(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.snapshot(market="deribit", currency="btc"), message)

    def test_oi_breakdown(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.oi_breakdown(), message)

    def test_sna(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.volume_breakdown(), message)

    def test_oi_breakdown_by_currency(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.oi_breakdown_by_currency(), message)

    def test_volume_breakdown_by_currency(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.options.volume_breakdown_by_currency(), message)


class Testfutures(TestCase):
    def test_instruments(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.futures.instruments(), message)

    def test_alt_currency(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.futures.alt_currency(), message)

    def test_perpetual_funding(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.futures.perpetual_funding(currency="btc"), message)

    def test_futures_yield(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.futures.futures_yield(currency="btc"), message)

    def test_futures_basis(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.futures.futures_basis(currency="btc"), message)

    def test_volume_breakdown(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.futures.volume_breakdown(currency="btc"), message)

    def test_oi_breakdown(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.futures.oi_breakdown(currency="btc"), message)

    def test_futures_curve(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.futures.futures_curve(currency="btc", market="deribit"), message)

    def test_markets_oi_gainers_and_losers(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.futures.markets_oi_gainers_and_losers(currency="btc", option="all", hour="2"),
                        message)

    def test_snapshot(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.futures.futures_yield(currency="btc"), message)


class Testmove(TestCase):
    def test_oi_group(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.oi_group(), message)

    def test_oi_expiry(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.oi_expiry(), message)

    def test_volume_expiry(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.volume_expiry(), message)

    def test_volume_group(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.volume_group(), message)

    def test_volume_expiry_buy_sell(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.volume_expiry_buy_sell(), message)

    def test_volume_contract_buy_sell(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.volume_contract_buy_sell(), message)

    def test_volume_top_contract(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.volume_top_contract(), message)

    def test_volume_type_buy_sell(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.volume_type_buy_sell(), message)

    def test_oi_top_contract(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.volume_top_contract(), message)

    def test_big_trades(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.big_trades(), message)

    def test_contract_name(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.contract_name(), message)

    def test_expirations(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.expirations(), message)

    def test_ftx_vs_deribit(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.ftx_vs_deribit(), message)

    def test_live(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.move.live(), message)


class Testdefi(TestCase):
    def test_dovs(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.defi.dovs(), message)

    def test_ribbon(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.defi.ribbon(), message)

    def test_friktion(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.defi.friktion(), message)

    def test_squeeth(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.defi.squeeth(), message)

    def test_thetanuts(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.defi.thetanuts(), message)


class Testderivs(TestCase):
    def test_futures(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.derivs.futures(market="deribit", currency="btc", maturity="30JUN23"), message)

    def test_perpetuals(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.derivs.perpetuals(market="deribit", currency="btc"), message)

    def test_summary(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.derivs.summary(currency="btc"), message)

    def test_oi_gainers(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.derivs.oi_gainers(market="deribit", oitype="future", period="2"), message)

    def test_price_gainers(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.derivs.price_gainers(market="deribit", oitype="future", period="2"), message)

    def test_top_funding(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.derivs.top_funding(market="deribit"), message)

    def test_top_gainers_losers(self):
        message = "Test value is not true."
        self.assertTrue(resp.realtime.derivs.top_gainers_losers(change="2", type="gainers"), message)


class TestoptionsH(TestCase):
    def test_option(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.option(market="deribit",
                                                       instrument="BTC-30JUN23-80000-C",
                                                       start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_iv(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.iv(market="deribit",
                                                   instrument="BTC-30JUN23-80000-C",
                                                   start="2022-08-30", end="2022-09-06", limit="10", page="1"), message)

    def test_price(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.price(market="deribit",
                                                      instrument="BTC-30JUN23-80000-C",
                                                      start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_oi_volume(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.oi_volume(market="deribit",
                                                          instrument="BTC-30JUN23-80000-C",
                                                          start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_underlying_price(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.underlying_price(market="deribit",
                                                                 instrument="BTC-30JUN23-80000-C",
                                                                 start="2022-08-30", end="2022-09-06", limit="10",
                                                                 page="1"),
                        message)

    def test_oi_strike(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.oi_strike(market="deribit", currency="BTC", maturity="30JUN23",
                                                          date="2022-07-24T01"), message)

    def test_volume_strike(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.volume_strike(market="deribit", currency="BTC", maturity="30JUN23",
                                                              date="2022-07-24T01"), message)

    def test_oi_by_market(self):
        message = "Test value is not true."
        self.assertTrue(
            resp.historical.options.oi_by_market(market="deribit", start="2022-08-30", end="2022-09-06", limit="10",
                                                 page="1"), message)

    def test_volume_by_market(self):
        message = "Test value is not true."
        self.assertTrue(
            resp.historical.options.volume_by_market(market="deribit", start="2022-08-30", end="2022-09-06", limit="10",
                                                     page="1"), message)

    def test_oi_by_currency(self):
        message = "Test value is not true."
        self.assertTrue(
            resp.historical.options.oi_by_currency(currency="btc", start="2022-08-30", end="2022-09-06", limit="10",
                                                   page="1"), message)

    def test_volume_by_currency(self):
        message = "Test value is not true."
        self.assertTrue(
            resp.historical.options.volume_by_currency(currency="btc", start="2022-08-30", end="2022-09-06", limit="10",
                                                       page="1"), message)

    def test_iv_rv(self):
        message = "Test value is not true."
        self.assertTrue(
            resp.historical.options.iv_rv(market="deribit", currency="btc", start="2022-08-30", end="2022-09-06",
                                          limit="10",
                                          page="1"), message)

    def test_volume_pc_ratio(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.volume_pc_ratio(market="deribit",
                                                                currency="BTC",
                                                                start="2022-08-30", end="2022-09-06", limit="10",
                                                                page="1"),
                        message)

    def test_gex_index(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.gex_index(market="deribit",
                                                          currency="BTC",
                                                          start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_max_pain(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.max_pain(market="deribit",
                                                         currency="BTC",
                                                         start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_atm_iv(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.atm_iv(market="deribit",
                                                       currency="BTC",
                                                       start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_volume_total(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.volume_total(market="deribit",
                                                             currency="BTC",
                                                             start="2022-08-30", end="2022-09-06", limit="10",
                                                             page="1"),
                        message)

    def test_oi_pc_ratio(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.oi_pc_ratio(market="deribit",
                                                            currency="BTC",
                                                            start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_oi_total(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.oi_total(market="deribit",
                                                         currency="BTC",
                                                         start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_vix(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.vix(market="deribit",
                                                    currency="BTC",
                                                    start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_dvol(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.dvol(market="deribit",
                                                     currency="BTC",
                                                     start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_atm_iv_model(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.atm_iv_model(market="deribit",
                                                             currency="BTC", type="25p",
                                                             start="2022-08-30", end="2022-09-06", limit="10",
                                                             page="1"),
                        message)

    def test_butterfly(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.butterfly(market="deribit",
                                                          currency="BTC", type="25d",
                                                          start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_butterfly_model(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.butterfly_model(market="deribit",
                                                                currency="BTC", type="25d",
                                                                start="2022-08-30", end="2022-09-06", limit="10",
                                                                page="1"),
                        message)

    def test_skew(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.skew(market="deribit",
                                                     currency="BTC", type="25d",
                                                     start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_skew_model(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.skew_model(market="deribit",
                                                           currency="BTC", type="25d",
                                                           start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_risk_reversal(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.risk_reversal(market="deribit",
                                                              currency="BTC", type="25d",
                                                              start="2022-08-30", end="2022-09-06", limit="10",
                                                              page="1"),
                        message)

    def test_risk_reversal_model(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.risk_reversal_model(market="deribit",
                                                                    currency="BTC", type="25d",
                                                                    start="2022-08-30", end="2022-09-06", limit="10",
                                                                    page="1"),
                        message)

    def test_gamma_bands(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.gamma_bands(market="deribit",
                                                            currency="BTC", type="1d",
                                                            start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_iv_bid_ask(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.iv_bid_ask(market="deribit",
                                                           currency="BTC", type="p_25",
                                                           start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_total_oi(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.total_oi(market="deribit",
                                                         currency="BTC", maturity="30JUN23",
                                                         start="2022-08-30", end="2022-09-06", limit="10", page="1"),
                        message)

    def test_total_volume(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.total_volume(market="deribit",
                                                             currency="BTC", maturity="30JUN23",
                                                             start="2022-08-30", end="2022-09-06", limit="10",
                                                             page="1"),
                        message)

    def test_volume_oi_by_exchange(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.options.volumeOiByExchange(currency="BTC", maturity="30JUN23",
                                                                   start="2022-08-30", end="2022-09-06", limit="10",
                                                                   page="1"),
                        message)


class TestfuturesH(TestCase):
    def test_oi_weighted_funding(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.oi_weighted_funding(currency="BTC",
                                                                    start="2022-08-30", end="2022-09-06", limit="10",
                                                                    page="1"), message)

    def test_oi_weighted_volume_funding(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.oi_weighted_volume_funding(currency="BTC",
                                                                           start="2022-08-30", end="2022-09-06",
                                                                           limit="10",
                                                                           page="1"), message)

    def test_oi_weighted_basis(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.oi_weighted_basis(currency="BTC",
                                                                  start="2022-08-30", end="2022-09-06", limit="10",
                                                                  page="1"), message)

    def test_total_oi(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.total_oi(currency="BTC",
                                                         start="2022-08-30", end="2022-09-06", limit="10",
                                                         page="1"), message)

    def test_total_oi_by_margin(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.total_oi_by_margin(currency="BTC",
                                                                   start="2022-08-30", end="2022-09-06", limit="10",
                                                                   page="1"), message)

    def test_total_volume(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.total_volume(currency="BTC",
                                                             start="2022-08-30", end="2022-09-06", limit="10",
                                                             page="1"), message)

    def test_total_volume_by_margin(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.total_volume_by_margin(currency="BTC",
                                                                       start="2022-08-30", end="2022-09-06", limit="10",
                                                                       page="1"), message)

    def test_realized_volatility(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.realized_volatility(currency="BTC",
                                                                    start="2022-08-30", end="2022-09-06", limit="10",
                                                                    page="1"), message)

    def test_alt_summary(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.alt_summary(currency="BTC",
                                                            start="2022-08-30", end="2022-09-06", limit="10",
                                                            page="1"), message)

    def test_alt_markets(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.alt_markets(currency="BTC",
                                                            start="2022-08-30", end="2022-09-06", limit="10",
                                                            page="1"), message)

    def test_market_index(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.market_index(currency="BTC",
                                                             start="2022-08-30", end="2022-09-06", limit="10",
                                                             page="1"), message)

    def test_indices_price(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.indices_price(currency="BTC",
                                                              start="2022-08-30", end="2022-09-06", limit="10",
                                                              page="1"), message)

    def test_futures_annualized_basis(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.futures_annualized_basis(currency="BTC", period="7",
                                                                         start="2022-08-30", end="2022-09-06",
                                                                         limit="10",
                                                                         page="1"), message)

    def test_perpetual_funding_exchange(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.perpetual_funding_exchange(currency="BTC", option="C",
                                                                           start="2022-08-30", end="2022-09-06",
                                                                           limit="10",
                                                                           page="1"), message)

    def test_total_oi_by_exchange(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.total_oi_by_exchange(currency="BTC", option="C",
                                                                     start="2022-08-30", end="2022-09-06", limit="10",
                                                                     page="1"), message)

    def test_total_volume_by_exchange(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.total_volume_by_exchange(currency="BTC", option="C",
                                                                         start="2022-08-30", end="2022-09-06",
                                                                         limit="10",
                                                                         page="1"), message)

    def test_perpetual_yield(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.perpetual_yield(market="DERIBIT", currency="BTC",
                                                                start="2022-08-30", end="2022-09-06", limit="10",
                                                                page="1"), message)

    def test_perpetual_funding(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.futures.perpetual_funding(market="DERIBIT", currency="BTC",
                                                                  start="2022-08-30", end="2022-09-06", limit="10",
                                                                  page="1"), message)


class TestmoveH(TestCase):
    def test_total_oi(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.move.total_oi(market="FTX", currency="BTC",
                                                      start="2022-09-02", end="2022-09-09", limit="10",
                                                      page="1"), message)

    def test_volume_buy_sell(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.move.volume_buy_sell(market="FTX", currency="BTC",
                                                             start="2022-08-30", end="2022-09-06", limit="10",
                                                             page="1"), message)

    def test_iv_type(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.move.iv_type(market="FTX", currency="BTC", type="weekly",
                                                     start="2022-08-30", end="2022-09-06", limit="10",
                                                     page="1"), message)

    def test_iv_historical_open_future(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.move.iv_historical_open_future(market="FTX", currency="BTC", is_open="true",
                                                                       start="2022-08-30", end="2022-09-06", limit="10",
                                                                       page="1"), message)

    def test_total_volume(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.move.total_volume(market="FTX", currency="BTC",
                                                          start="2022-08-30", end="2022-09-06", limit="10",
                                                          page="1"), message)

    def test_historical_iv(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.move.historical_iv(market="FTX", contract_name="BTC-MOVE-2022Q4",
                                                           start="2022-08-30", end="2022-09-06", limit="10",
                                                           page="1"), message)

    def test_historical_oi(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.move.historical_oi(market="FTX", contract_name="BTC-MOVE-2022Q4",
                                                           start="2022-08-30", end="2022-09-06", limit="10",
                                                           page="1"), message)

    def test_historical_price(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.move.historical_price(market="FTX", contract_name="BTC-MOVE-2022Q4",
                                                              start="2022-08-30", end="2022-09-06", limit="10",
                                                              page="1"), message)

    def test_historical_volume(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.move.historical_volume(market="FTX", contract_name="BTC-MOVE-2022Q4",
                                                               start="2022-08-30", end="2022-09-06", limit="10",
                                                               page="1"), message)

    def test_open_future(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.move.open_future(contract_type="daily"), message)


class TestdefiH(TestCase):
    def test_dovs_auctions(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.defi.dovs_auctions(protocol="ribbon", currency="BTC",
                                                           start="2022-08-30", end="2022-09-06", limit="10",
                                                           page="1"), message)


class TestderivsH(TestCase):
    def test_perpetuals(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.derivs.perpetuals(symbol="ETHUSDTH22", market="DERIBIT",
                                                          start="2022-08-30", end="2022-09-06", limit="10",
                                                          page="1"), message)

    def test_futures(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.derivs.futures(symbol="ETHUSDTH22", market="DERIBIT",
                                                       start="2022-08-30", end="2022-09-06", limit="10",
                                                       page="1"), message)

    def test_summary(self):
        message = "Test value is not true."
        self.assertTrue(resp.historical.derivs.summary(currency="BTC",
                                                       start="2022-08-30", end="2022-09-06", limit="10",
                                                       page="1"), message)
