import os
import csv
import urllib.request
import yaml


def build_sheet_url(doc_id, sheet_id):
    return f'https://docs.google.com/spreadsheets/d/{doc_id}/export?format=csv&gid={sheet_id}'


# Read in the Google sheet data and prepare the dataframe
def get_sheets_data(document_id, sheets_id):
    try:
        sheet_url = build_sheet_url(document_id, sheets_id)
        with urllib.request.urlopen(sheet_url) as response:
            reader = csv.reader(response.read().decode('utf-8').splitlines())
            header = next(reader)
            # Get column indices for columns to keep
            indices_to_keep = [header.index(col) for col in ['EMM Mapping Final', 'EMM Mapping for Event Source YAML']]
            data = []
            for row in reader:
                # Filter rows with NaN values in both columns
                if all(row[i] != '' for i in indices_to_keep):
                    data.append([row[i] for i in indices_to_keep])

        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Process the data and update the yaml file
def process_data(csv_data, yaml_file):
    # Load YAML file
    with open(yaml_file, 'r') as f:
        yaml_data = yaml.safe_load(f)

    # Iterate over data rows
    for row in csv_data:
        emm_mapping_final, emm_mapping_yaml = row

        category, event_type, attribute = emm_mapping_final.split('.')
        attribute_name, attribute_value = emm_mapping_yaml.split(':')

        # Find the mapping in YAML data
        for mapping in yaml_data['mappings']:
            if mapping['category'] == category and mapping['event_type'] == event_type:
                if attribute in mapping['attributes']:
                    mapping['attributes'][attribute] = attribute_value.strip()

    # Cleanup data before dumping
    mappings_to_remove = []
    for mapping in yaml_data['mappings']:
        attributes_to_remove = []
        for attribute, value in mapping['attributes'].items():
            # Remove attributes with value of null
            if value is None:
                attributes_to_remove.append(attribute)
        # Remove attributes with null values
        for attribute in attributes_to_remove:
            mapping['attributes'].pop(attribute)
        # Remove mappings with all attributes removed
        if not mapping['attributes']:
            mappings_to_remove.append(mapping)
    # Remove mappings with all attributes removed
    for mapping in mappings_to_remove:
        yaml_data['mappings'].remove(mapping)

    # Write updated YAML data back to file
    with open(yaml_file, 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, sort_keys=False)

    print(f"\nUpdated '{yaml_file.split('/')[-1]}' with data from Google Sheets")


def find_file_to_update(yaml_file_name):
    # Search the products directory for a matching filename and return the path
    current_directory = os.getcwd()
    # Check if in the root of the repository
    for root, dirs, files in os.walk(current_directory):
        # Check if the filename exists in the list of files
        if yaml_file_name in files:
            # If found, return the full path of the file
            return os.path.join(root, yaml_file_name)
    # If the filename is not found, return None
    return None


if __name__ == '__main__':
    doc_id = input("Enter the Google Sheets Document ID: ")
    sheet_id = input("Enter the Sheet ID (gid= in browser url) for 'Mapping Output': ")
    yaml_file = input("Enter the name of the YAML file to update: ")
    df_out = get_sheets_data(doc_id, sheet_id)
    yam_file = find_file_to_update(yaml_file)
    process_data(df_out, yam_file)
