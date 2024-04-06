# Re-defining the function after reset and running the calculation

def email_campaign_calculator(daily_email_limit, days_in_a_year, sequence_length_days, unsubscribe_rate, response_rate, meeting_rate, opportunity_rate, deals_closed_rate, average_deal_value):
    new_sequences_initiated = 0
    active_sequences = [0] * sequence_length_days  # To track active sequences
    expected_responses = 0
    expected_meetings = 0
    opportunities_in_pipeline = 0
    opportunities_in_pipeline_value = 0
    expected_deals = 0
    revenue = 0
    
    for day in range(days_in_a_year):
        # Apply response rate to new contacts added 7 days ago (if applicable)
        if day >= sequence_length_days:
            # Subtract responses from the total sequences initiated for the contacts from 7 days ago
            expected_responses += active_sequences[0] * response_rate

        # Calculate and subtract unsubscribes from all active days
        for i in range(sequence_length_days):
            active_sequences[i] -= active_sequences[i] * unsubscribe_rate

        # Calculate new contacts for the day, not exceeding the daily limit
        new_sequences_today = daily_email_limit - sum(active_sequences)

        # Update the total number of new sequences initiated
        new_sequences_initiated += new_sequences_today

        # Update active sequences for the next day
        active_sequences = active_sequences[1:] + [new_sequences_today]

    # Calculate the conversion funnel
    expected_meetings = expected_responses * meeting_rate
    opportunities_in_pipeline = expected_meetings * opportunity_rate
    opportunities_in_pipeline_value = opportunities_in_pipeline * average_deal_value
    expected_deals = opportunities_in_pipeline * deals_closed_rate
    revenue = expected_deals * average_deal_value
    
    # Format the results to remove unnecessary decimals
    new_sequences_initiated = round(new_sequences_initiated)
    expected_responses = round(expected_responses)
    expected_meetings = round(expected_meetings)
    opportunities_in_pipeline = round(opportunities_in_pipeline)
    opportunities_in_pipeline_value = round(opportunities_in_pipeline_value)
    expected_deals = round(expected_deals)
    revenue = round(revenue)
    
    return new_sequences_initiated, expected_responses, expected_meetings, opportunities_in_pipeline, opportunities_in_pipeline_value, expected_deals, revenue

# Using the provided parameters and an average deal amount of $75,000
average_deal_value = 15000

# Run the calculation
new_sequences_initiated, expected_responses, expected_meetings, opportunities_in_pipeline, opportunities_in_pipeline_value, expected_deals, revenue = email_campaign_calculator(
    daily_email_limit=1000,
    days_in_a_year=252,
    sequence_length_days=10,
    unsubscribe_rate=0.005,
    response_rate=0.10,
    meeting_rate=0.25,
    opportunity_rate=0.30,
    deals_closed_rate=0.40,
    average_deal_value=average_deal_value
)

# Print the results at each level of the conversion funnel
print(f"Total number of new sequences initiated in a year: {new_sequences_initiated}")
print(f"Expected responses from new sequences: {expected_responses}")
print(f"Expected meetings from responses: {expected_meetings}")
print(f"Opportunities in the pipeline from meetings: {opportunities_in_pipeline}")
print(f"Value of opportunities in the pipeline: ${opportunities_in_pipeline_value:,}")
print(f"Expected deals closed from opportunities: {expected_deals}")
print(f"Projected revenue from closed deals: ${revenue:,}")



# Step 2: Use the Output as Input for Revenue Calculator
def calculate_revenue(install_fee, monthly_service_fee, avg_months, expected_deals, managed_service_clients_factor, months):
    total_installs_year = expected_deals
    total_service_clients_year = expected_deals * managed_service_clients_factor

# Running the Python script with the new parameters to calculate monthly and annual revenues.

def calculate_revenue(install_fee, monthly_service_fee, avg_months, total_installs_year, total_service_clients_year, months):
    monthly_installs = [0] * months
    monthly_service_clients = [0] * months

    # Distribute the installations and clients more evenly over the months
    for i in range(total_installs_year):
        monthly_installs[i % months] += 1
    for i in range(total_service_clients_year):
        monthly_service_clients[i % months] += 1

    monthly_revenue = []
    total_service_clients = 0

    for month in range(months):
        # Add new service clients
        total_service_clients += monthly_service_clients[month]

        # Calculate install revenue for the month
        install_revenue = monthly_installs[month] * install_fee

        # Calculate managed service revenue for the month
        if month >= avg_months:
            total_service_clients -= monthly_service_clients[month - avg_months]

        service_revenue = total_service_clients * monthly_service_fee

        # Total revenue for the month
        total_revenue = install_revenue + service_revenue
        monthly_revenue.append(total_revenue)

    # Calculating total revenue by year
    annual_revenue = [sum(monthly_revenue[i:i + 12]) for i in range(0, len(monthly_revenue), 12)]

    return monthly_revenue, annual_revenue

# User-defined parameters
install_fee = 15000  # Installation fee
monthly_service_fee = 5000  # Managed services fee
avg_months = 18  # Average retention in months
total_installs_year = 12  # Total installations for the year
total_service_clients_year = 2  # Total new managed service clients for the year
months = 36  # Projection period in months

# Calculate revenue and total revenue by year
monthly_revenue, total_annual_revenue = calculate_revenue(install_fee, monthly_service_fee, avg_months, total_installs_year, total_service_clients_year, months)
monthly_revenue, total_annual_revenue


# Step 3: Define Parameters and Execute
# Parameters for email campaign
email_params = {
    "daily_email_limit": 1000,
    "days_in_a_year": 252,
    "sequence_length_days": 10,
    "unsubscribe_rate": 0.005,
    "response_rate": 0.10,
    "meeting_rate": 0.25,
    "opportunity_rate": 0.30,
    "deals_closed_rate": 0.40,
    "average_deal_value": 15000
}

# Run email campaign calculator
expected_deals = email_campaign_calculator(**email_params)

# Parameters for revenue calculation
install_fee = 15000
monthly_service_fee = 5000
avg_months = 18
managed_service_clients_factor = 0.5  # Example: 50% of the deals opt for managed services
months = 36

# Calculate revenue
monthly_revenue, total_annual_revenue = calculate_revenue(install_fee, monthly_service_fee, avg_months, expected_deals, managed_service_clients_factor, months)

# Print results
print("Monthly Revenue:", monthly_revenue)
print("Annual Revenue:", total_annual_revenue)
