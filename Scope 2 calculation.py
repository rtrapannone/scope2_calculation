def scope2(electricity,ef_location,ef_market):
    location_based=electricity*ef_location/1000
    market_based=electricity*ef_market/1000
    print("Location-based scope 2 electricity emissions: " + str(location_based) + " tCO2eq")
    print("Market-based scope 2 electricity emissions: " + str(market_based) + " tCO2eq")

## For running the function call the function by inserting the electricity consumption expressed in kWh during the reporting year 
## and the two emission factors expressed in kgCO2eq/kWh
## It returns the scope2 CO2eq realted to electricity expressed in tCO2eq
## Example: scope2(5000,0.3,0.2) -> Returns: Location-based scope 2 electricity emissions: 1.5 tCO2eq; Market-based scope 2 electricity emissions: 1.0 tC




