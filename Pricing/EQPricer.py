import QuantLib as ql

def get_price(pricing_params):
    option_type = ql.Option.Call
    spot = float(pricing_params['spot'])
    strike = float(pricing_params['strike'])
    vol = float(pricing_params['vol'])/100
    rfr = float(pricing_params['rate'])/100
    maturity_date = pricing_params['detdate']
    maturity_date = ql.Date(int(maturity_date.split('/')[0]),int(maturity_date.split('/')[1]),int(maturity_date.split('/')[2]))
    valdate = pricing_params['valdate']
    valdate = ql.Date(int(valdate.split('/')[0]),int(valdate.split('/')[1]),int(valdate.split('/')[2]))
    ql.Settings.instance().evaluationDate = valdate
    day_count = ql.Actual365Fixed()
    calendar = ql.UnitedStates(ql.UnitedStates.NYSE)


    payoff = ql.PlainVanillaPayoff(option_type,strike)
    exercise = ql.EuropeanExercise(maturity_date)
    european_option = ql.VanillaOption(payoff,exercise)

    spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot))
    flat_ts = ql.YieldTermStructureHandle(ql.FlatForward(valdate,rfr,day_count))
    div_yield = ql.YieldTermStructureHandle(ql.FlatForward(valdate,0,day_count))
    flat_vol_ts = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(valdate,calendar,vol,day_count))

    bsm_process = ql.BlackScholesMertonProcess(spot_handle,div_yield,flat_ts,flat_vol_ts)
    european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
    bs_price = european_option.NPV()
    return round(bs_price,2)


