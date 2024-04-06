def calculate_aum_revenue(total_clients, initial_avg_asset_value, growth_rate, years):
    aum_fee_rate = 0.01  # 1% AUM fee
    aum_revenue_projection = []
    current_asset_value = initial_avg_asset_value

    for year in range(years):
        annual_aum_revenue = total_clients * current_asset_value * aum_fee_rate
        aum_revenue_projection.append(annual_aum_revenue)
        current_asset_value *= (1 + growth_rate)  # Update asset value for next year

    return aum_revenue_projection

def calculate_total_assets_value(initial_avg_asset_value, growth_rate, years, total_clients):
    total_assets_projection = []
    current_asset_value = initial_avg_asset_value

    for year in range(years):
        total_assets_value = total_clients * current_asset_value
        total_assets_projection.append(total_assets_value)
        current_asset_value *= (1 + growth_rate)  # Update asset value for next year

    return total_assets_projection

def main():
    # Hypothetical input values
    total_clients = 100  # Number of clients
    initial_avg_asset_value = 50000  # Initial average asset value per client
    growth_rate = 0.05  # Annual asset growth rate (5%)
    years = 10  # Number of years for the projection

    # Calculate revenue and total assets
    revenue_projection = calculate_aum_revenue(total_clients, initial_avg_asset_value, growth_rate, years)
    total_assets_projection = calculate_total_assets_value(initial_avg_asset_value, growth_rate, years, total_clients)

    # Display the results
    print("\nAUM Revenue Projection:")
    for year, revenue in enumerate(revenue_projection, 1):
        print(f"Year {year}: ${revenue:,.2f}")

    print("\nTotal Assets Under Management:")
    for year, total_assets in enumerate(total_assets_projection, 1):
        print(f"Year {year}: ${total_assets:,.2f}")

if __name__ == "__main__":
    main()