# Canadian Address to Postal Code Converter

This Python program is designed to take a list of Canadian addresses as input and output their corresponding postal codes. It utilizes the Nominatim API to perform the address lookup and retrieval of postal codes.

## Prerequisites

Before using this program, ensure you have the following installed:
- Python 3.x
- Necessary Python libraries (`pandas`, `requests`)

## Installation

1. Clone this repository to your local machine:

git clone

2. Navigate to the project directory:

3. Install the required Python libraries:
pip install -r requirements.txt

## Usage

1. Save your list of Canadian addresses in an Excel file with the following column headings:
   - `address`
   - `city`
   - `province`

   Save the file as `input_addresses.xlsx` in the root directory of the project.

2. Run the program

3. The program will process the addresses and generate an output file named `output_postal_codes.xlsx` containing the postal codes corresponding to the provided addresses.

## Example

Suppose `input_addresses.xlsx` contains the following data:

| address          | city       | province |
|------------------|------------|----------|
| 123 Main St      | Toronto    | ON       |
| 456 Elm St       | Vancouver  | BC       |
| 789 Oak Ave      | Montreal   | QC       |

After running the program, `output_postal_codes.xlsx` will contain:

| address          | city       | province | postal_code |
|------------------|------------|----------|-------------|
| 123 Main St      | Toronto    | ON       | M5V 2A1     |
| 456 Elm St       | Vancouver  | BC       | V6A 1A1     |
| 789 Oak Ave      | Montreal   | QC       | H3Z 2Y7     |

## Notes

- The accuracy of the postal codes retrieved depends on the accuracy of the provided addresses. 
      
