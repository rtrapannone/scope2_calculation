def scope2(consumption,ef_location,ef_market):

  location_based=consumption*ef_location
  market_based=consumption*ef_market
  print("Location-based scope 2 emissions" + location_based)
  print("Market-based scope 2 emissions" + market_based)

## For running the function call the function by inserting the electricity consumption expressed in kWh and the two emission factors
