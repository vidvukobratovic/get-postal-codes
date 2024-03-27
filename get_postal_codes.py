import pandas as pd
import requests
import re
input_file = "input_addresses.xlsx"
output_file = "output_addresses.xlsx"

df = pd.read_excel(input_file)


def get_postal_code(address, city, province):
    query = f"{address}, {city}, {province}"
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": query,
        "format": "json",
        "addressdetails": 1
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data:
        # Extract postal code from the first result
        address_details = data[0]['address']
        postal_code = address_details.get('postcode')
        return postal_code
    else:
        return None

# Function to clean addresses
def clean_address(address):
    # Remove leading and trailing whitespaces
    address = address.strip()

    # Remove all periods
    address = address.replace('.', '')

    # Replace 'route x' or 'rte x' with '# x'
    address = re.sub(r'(route|rte)\s+(\d+)', r'# \2', address, flags=re.IGNORECASE)

    return address

# Function to capitalize street names
def capitalize_street_name(street_name):
    return street_name.upper()

# Read the Excel file
input_file = "input_addresses.xlsx"
output_file = "output_addresses.xlsx"

df = pd.read_excel(input_file)

# Clean addresses
df['address'] = df['address'].apply(clean_address)

# Capitalize street names
df['address'] = df['address'].apply(capitalize_street_name)

# Process addresses and get postal codes
postal_codes = []
for index, row in df.iterrows():
    postal_code = get_postal_code(row['address'], row['city'], row['province'])
    postal_codes.append(postal_code)

# Add postal codes to the dataframe
df['postal_code'] = postal_codes

# Write the results to another Excel file
df.to_excel(output_file, index=False)

print("Postal codes extracted and saved to", output_file)
