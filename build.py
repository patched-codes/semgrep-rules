import os
import yaml

def combine_yaml_files(root_dir, output_file):
    # Delete the output file if it already exists
    if os.path.exists(output_file):
        os.remove(output_file)

    combined_rules = []
    rule_ids = set()
    duplicate_ids = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.yml') or file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as yaml_file:
                    try:
                        content = yaml.safe_load(yaml_file)
                        if 'rules' in content:
                            for rule in content['rules']:
                                rule_id = rule['id']
                                if rule_id in rule_ids:
                                    duplicate_ids.append(rule_id)
                                else:
                                    rule_ids.add(rule_id)
                                    combined_rules.append(rule)
                    except yaml.YAMLError as e:
                        print(f"Error reading {file_path}: {e}")

    if duplicate_ids:
        print(f"Duplicate rule IDs found: {duplicate_ids}")
        print("File not generated due to duplicate rule IDs.")
        return

    with open(output_file, 'w') as out_file:
        out_file.write("# Patched Semgrep Rules\n")
        out_file.write("# Source Repo: https://github.com/patched-codes/semgrep-rules\n")
        out_file.write("# License: MIT\n")
        out_file.write("# Version: 0.0.1\n")
        out_file.write("---\n")
        yaml.dump({'rules': combined_rules}, out_file, default_flow_style=False)

    print(f"Combined rules saved to {output_file}")

if __name__ == "__main__":
    root_directory = './'  # Update this to your root directory path
    output_yaml_file = 'patched-codes-semgrep-rules.yml'
    combine_yaml_files(root_directory, output_yaml_file)
