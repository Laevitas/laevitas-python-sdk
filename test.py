from laevitas import sdk

resp = sdk.api()
resp.configure('your-api-key')
test1 = resp.historical.move.total_oi(market="FTX", currency="BTC",
                                                      start="2022-09-02", end="2022-09-09", limit="10",
                                                      page="1")

test2 = resp.realtime.options.instruments(market="deribit", currency="btc")
print(test2)




