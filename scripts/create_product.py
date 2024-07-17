import os
import shutil
import yaml

current_directory = os.getcwd()


class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


def opening_message():
    welcome_message = """
 ____              ____    _____                 _                       
/ ___|  __ _  __ _/ ___|  | ____|_   _____ _ __ | |_                     
\___ \ / _` |/ _` \___ \  |  _| \ \ / / _ \ '_ \| __|                    
 ___) | (_| | (_| |___) | | |___ \ V /  __/ | | | |_                     
|____/ \__,_|\__,_|____/  |_____| \_/ \___|_| |_|\__|                    
 __  __       _              _ _           __  __       _        _       
|  \/  | __ _| |_ _   _ _ __(_) |_ _   _  |  \/  | __ _| |_ _ __(_)_  __ 
| |\/| |/ _` | __| | | | '__| | __| | | | | |\/| |/ _` | __| '__| \ \/ / 
| |  | | (_| | |_| |_| | |  | | |_| |_| | | |  | | (_| | |_| |  | |>  <  
|_|  |_|\__,_|\__|\__,_|_|  |_|\__|\__, | |_|  |_|\__,_|\__|_|  |_/_/\_\ 
                                   |___/                                 

Welcome to the Event Maturity Matrix contribution script. This script will help you with the initial steps in
creating a new SaaS product and it's associated event sources (e.g. API endpoints or distinct event schemas). 

Please respond to the following prompts to create the necessary directories and files for your SaaS product.

Please note that the script will create a new directory in the 'products' folder for your product, as well as 
subdirectories for event examples and event sources.

Just press Enter to skip any prompts where the information is unknown. The information can be added manually at
a later time.
 
Thanks for contributing to the Event Maturity Matrix!
"""

    print(welcome_message)

    # Prompt to get started
    start = input("Would you like to get started? (Y/N): ")

    if start.lower() != 'y':
        print("Exiting the contribution script.")
        exit(0)


def user_prompts():
    # Prompt user for product information
    product_name = input("\nEnter the name of your SaaS product: ")
    product_description = input_with_default("Provide a brief description of your product: ")

    # Variables to collect event source information
    source_names = []
    source_descriptions = []
    source_references = []
    source_retention_durations = []
    source_retention_comments = []
    source_latency_durations = []
    source_latency_comments = []
    source_licensing_comments = []

    # Prompt user for event sources information
    sources_count = int(input("\nHow many event sources (API endpoints) are used to collect logs? "))

    # Loop through the number of sources to collect information
    for i in range(sources_count):
        source_name = (
            input_with_default(f"\nEnter the name of event source #{i + 1}: "))
        source_description = (
            input_with_default(f"Provide a brief description of event source #{i + 1} ({source_name}): "))

        source_retention_duration = (
            input_with_default(f"\nWhat is the retention period for event source #{i + 1} ({source_name}): "))
        source_retention_comment = (
            input_with_default(
                f"Provide any additional comments regarding the retention period for event source #{i + 1} ({source_name}): "))

        source_latency_duration = (
            input_with_default(f"\nWhat is the latency period for event source #{i + 1} ({source_name}): "))
        source_latency_comment = (
            input_with_default(
                f"Provide any additional comments regarding the latency period for event source #{i + 1} ({source_name}): "))

        source_licensing_comment = (
            input_with_default(
                f"\nProvide a brief description of any licensing requirements for event source #{i + 1} ({source_name}): "))

        source_reference_name = (
            input_with_default(f"\nEnter a name for a reference related to event source #{i + 1} ({source_name}): "))
        source_reference_description = (
            input_with_default(
                f"Provide a brief description of the reference for event source #{i + 1} ({source_name}): "))
        source_reference_url = (
            input_with_default(f"Provide a URL link for the reference of event source #{i + 1} ({source_name}): "))

        source_names.append(source_name)
        source_descriptions.append(source_description)
        source_references.append({
            "id": normalize_name("about_" + source_reference_name),
            "name": source_reference_name,
            "description": source_reference_description,
            "url": source_reference_url
        })
        source_retention_durations.append(source_retention_duration)
        source_retention_comments.append(source_retention_comment)
        source_latency_durations.append(source_latency_duration)
        source_latency_comments.append(source_latency_comment)
        source_licensing_comments.append(source_licensing_comment)

    # Remove spaces and dashes, replace with underscores
    normalized_product_name = normalize_name(product_name)

    # List with both the original and normalized product names
    product_names = [product_name, normalized_product_name]

    return (product_names, product_description, source_names, source_descriptions, source_references,
            source_retention_durations, source_retention_comments, source_latency_durations, source_latency_comments,
            source_licensing_comments)


def input_with_default(prompt, default_value="N/A"):
    user_input = input(prompt)
    return user_input if user_input else default_value


def normalize_name(name):
    return name.replace(' ', '_').replace('-', '_').lower()


# Create empty JSON files for each event source directory
def create_json_event_examples(directory, event_source_name):
    event_type_mapping = [
        "authentication_account_login_success.json",  # C0001_ET0001
        "authentication_account_login_failure.json",  # C0001_ET0001
        "authentication_account_logout.json",  # C0001_ET0002
        "authentication_mfa_verification.json",  # C0001_ET0003
        "authorization_create_user.json",  # C0002_ET0004
        "authorization_read_user.json",  # C0002_ET0005
        "authorization_update_user.json",  # C0002_ET0006
        "authorization_delete_user.json",  # C0002_ET0007
        "authorization_create_group.json",  # C0002_ET0008
        "authorization_read_group.json",  # C0002_ET0009
        "authorization_update_group.json",  # C0002_ET0010
        "authorization_delete_group.json",  # C0002_ET0011
        "authorization_add_to_group.json",  # C0002_ET0012
        "authorization_remove_from_group.json",  # C0002_ET0013
        "authorization_create_role.json",  # C0002_ET0014
        "authorization_read_role.json",  # C0002_ET0015
        "authorization_update_role.json",  # C0002_ET0016
        "authorization_delete_role.json",  # C0002_ET0017
        "authorization_add_permission.json",  # C0002_ET0018
        "authorization_remove_permission.json",  # C0002_ET0019
        "authorization_add_enrollment.json",  # C0002_ET0020
        "authorization_remove_enrollment.json",  # C0002_ET0021
        "system_audit_create_security_configuration.json",  # C0003_ET0022
        "system_audit_read_security_configuration.json",  # C0003_ET0023
        "system_audit_update_security_configuration.json",  # C0003_ET0024
        "system_audit_delete_security_configuration.json",  # C0003_ET0025
        "system_audit_create_integration.json",  # C0003_ET0026
        "system_audit_read_integration.json",  # C0003_ET0027
        "system_audit_update_integration.json",  # C0003_ET0028
        "system_audit_delete_integration.json",  # C0003_ET0029
        "activity_audit_create_resource.json",  # C0004_ET0030
        "activity_audit_read_resource.json",  # C0004_ET0031
        "activity_audit_update_resource.json",  # C0004_ET0032
        "activity_audit_delete_resource.json",  # C0004_ET0033
        "activity_audit_download_resource.json"  # C0004_ET0034
    ]

    for event_type_file in event_type_mapping:
        example_file = os.path.join(directory, event_type_file)
        with open(example_file, 'w'):
            pass


def create_directories(name):
    product_dir = os.path.join(current_directory, 'products', name)
    os.makedirs(product_dir, exist_ok=True)

    event_examples_dir = os.path.join(product_dir, 'event_examples')
    event_sources_dir = os.path.join(product_dir, 'event_sources')
    os.makedirs(event_examples_dir, exist_ok=True)
    os.makedirs(event_sources_dir, exist_ok=True)

    print(f"\nThe following product directories have been created:")
    print(f"-- {product_dir}")
    print(f"-- {event_sources_dir}")
    print(f"-- {event_examples_dir}")

    return product_dir, event_examples_dir, event_sources_dir


def prepare_templates(product_directory, examples_directory, sources_directory, product_names, production_description,
                      event_source_names, event_source_descriptions, event_source_references,
                      source_retention_duration, source_retention_comments, source_latency_duration,
                      source_latency_comments, source_licensing_comments):

    # Copy the template Product YAML file
    product_template_file = os.path.join(current_directory, 'templates', 'template.product.yml')
    product_file = os.path.join(product_directory, product_names[1] + '.product.yml')
    shutil.copy(product_template_file, product_file)

    print(f"\nThe following product files have been created:")
    print(f"-- {product_file}")

    # Copy the template Event Source YAML file & create directories for each event source
    event_source_template_file = os.path.join(current_directory, 'templates', 'template.event_source.yml')
    number_of_sources = len(event_source_names)
    source_files = []

    # Loop through each event source and create a YAML file
    for source_name in event_source_names:

        if source_name == "N/A":
            continue

        source_name = normalize_name(source_name)
        new_file = os.path.join(sources_directory, product_names[1] + '_' + source_name + '.yml')
        source_files.append(new_file)
        shutil.copy(event_source_template_file, new_file)

        print(f"-- {new_file}")

        # Create directories in event_examples for each event source
        source_dir = os.path.join(examples_directory, source_name)
        os.makedirs(source_dir, exist_ok=True)

        # Create empty JSON files for each event source directory
        create_json_event_examples(source_dir, source_name)

    # Update the Product YAML file based on user input
    with open(product_file, 'r') as file:
        product_data = yaml.safe_load(file)

    product_data['name'] = product_names[0]
    product_data['description'] = production_description

    # Add provided event sources to the product file
    # Add the first event source
    product_data['collection'][0]['id'] = normalize_name(event_source_names[0]) + '_collection'
    product_data['collection'][0]['name'] = event_source_names[0]
    product_data['collection'][0]['description'] = event_source_descriptions[0]
    product_data['collection'][0]['references'] = event_source_references[0]

    # Add additional event sources if provided
    if number_of_sources > 1:
        for i in range(1, number_of_sources):
            new_entry = {
                "id": normalize_name(event_source_names[i]) + '_collection',
                "name": event_source_names[i],
                "description": event_source_descriptions[i],
                "references": event_source_references[i]
            }
            product_data['collection'].append(new_entry)

    with open(product_file, 'w') as file:
        yaml.dump(product_data, file, default_flow_style=False, sort_keys=False, Dumper=MyDumper)

    # Update the Source YAML file(s) based on user input
    for i, source_file in enumerate(source_files):
        with open(source_file, 'r') as file:
            source_data = yaml.safe_load(file)

        source_data['product']['name'] = product_names[0]
        source_data['product']['collection_sources'][0] = normalize_name(event_source_names[i]) + '_collection'
        source_data['name'] = event_source_names[i]
        source_data['description'] = event_source_descriptions[i]
        source_data['references'] = event_source_references[i]
        source_data['retention']['duration'] = source_retention_duration[i]
        source_data['retention']['comments'] = source_retention_comments[i]
        source_data['latency']['duration'] = source_latency_duration[i]
        source_data['latency']['comments'] = source_latency_comments[i]
        source_data['licensing']['comments'] = source_licensing_comments[i]

        # iterate over each example location and replace "{event_source_name}" with the event source name
        for example in source_data['mappings']:
            for location in example['examples']:
                # find/replace string in location
                location['location'] = location['location'].replace('{event_source_name}',
                                                                    normalize_name(event_source_names[i]))

        with open(source_file, 'w') as file:
            yaml.dump(source_data, file, default_flow_style=False, sort_keys=False, Dumper=MyDumper)


def main():
    opening_message()

    (product_names, product_description, event_source_names, event_source_descriptions, event_source_references,
     source_retention_duration, source_retention_comments, source_latency_duration, source_latency_comments,
     source_licensing_comments) = user_prompts()

    product_directory, examples_directory, sources_directory = create_directories(product_names[1])

    prepare_templates(product_directory, examples_directory, sources_directory, product_names, product_description,
                      event_source_names, event_source_descriptions, event_source_references,
                      source_retention_duration, source_retention_comments, source_latency_duration,
                      source_latency_comments, source_licensing_comments)


if __name__ == "__main__":
    main()
