import os
import shutil


def main():
    # Prompt user for product name
    product_name = input("Enter the name of the product: ")
    event_sources_count = int(input("Enter the number of event sources(API Endpoints) used to collect logs: "))
    event_source_names = []
    for i in range(event_sources_count):
        source_name = input(f"Enter the name of event source {i + 1}: ")
        event_source_names.append(source_name)

    # Remove spaces and dashes, replace with underscores
    product_name = product_name.replace(' ', '_').replace('-', '_')

    # Create product directory
    current_directory = os.getcwd()
    product_dir = os.path.join(current_directory, 'products', product_name)
    os.makedirs(product_dir, exist_ok=True)

    # Create event_examples and event_sources directories
    event_examples_dir = os.path.join(product_dir, 'event_examples')
    event_sources_dir = os.path.join(product_dir, 'event_sources')
    os.makedirs(event_examples_dir, exist_ok=True)
    os.makedirs(event_sources_dir, exist_ok=True)

    # Copy template YAML file
    product_template_file = os.path.join(current_directory, 'templates', 'template.product.yml')
    new_file = os.path.join(product_dir, product_name + '.product.yml')
    shutil.copy(product_template_file, new_file)
    event_source_template_file = os.path.join(current_directory, 'templates', 'template.event_source.yml')
    for source_name in event_source_names:
        new_file = os.path.join(event_sources_dir, product_name + '_' + source_name + '.event_source.yml')
        shutil.copy(event_source_template_file, new_file)
        # Create directories in event_examples for each event source
        source_dir = os.path.join(event_examples_dir, source_name)
        os.makedirs(source_dir, exist_ok=True)
    print(f"Product directory '{product_name}' created.")


if __name__ == "__main__":
    main()
