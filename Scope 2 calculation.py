def scope2(electricity,heat,ef_location,ef_market):
    consumption=electricity+heat
    location_based=consumption*ef_location
    market_based=consumption*ef_market
    print("Location-based scope 2 emissions: " + str(location_based))
    print("Market-based scope 2 emissions: " + str(market_based))

## For running the function call the function by inserting the electricity and heat consumption expressed in kWh during the reporting year 
## and the two emission factors expressed in kgCO2eq/kWh
## It returns the scope2 CO2eq expressed in kg
## Example: scope2(5000,2000,0.3,0.2) -> Returns: Location-based scope 2 emissions: 2100.0 kgCO2eq; Market-based scope 2 emissions: 4000.0 kgCO2eq





