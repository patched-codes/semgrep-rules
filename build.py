import os
import ruamel.yaml
from collections import OrderedDict, defaultdict

yaml = ruamel.yaml.YAML()

def combine_yaml_files(root_dir, output_file):
    # Delete the output file if it already exists
    if os.path.exists(output_file):
        os.remove(output_file)

    combined_rules = OrderedDict()  # Use OrderedDict to preserve insertion order
    rule_ids = set()
    duplicate_ids = []
    language_counts = defaultdict(int)

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.yml') or file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as yaml_file:
                    try:
                        content = yaml.load(yaml_file)
                        if 'rules' in content:
                            for rule in content['rules']:
                                rule_id = rule['id']
                                if rule_id in rule_ids:
                                    duplicate_ids.append(rule_id)
                                else:
                                    rule_ids.add(rule_id)
                                    combined_rules[rule_id] = rule  # Store rule in OrderedDict
                                    for language in rule['languages']:
                                        language_counts[language] += 1
                    except Exception as e:
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
        yaml.dump({'rules': list(combined_rules.values())}, out_file)

    print(f"Combined rules saved to {output_file}")

    # Generate and print the summary table
    total_rules = sum(language_counts.values())
    print("\n### Summary")
    print("| Language | Number of Rules |")
    print("|----------|-----------------|")
    for language, count in language_counts.items():
        print(f"| {language} | {count} |")
    print("| **Total** | **{}** |".format(total_rules))

if __name__ == "__main__":
    root_directory = './'  # Update this to your root directory path
    output_yaml_file = 'patched-codes-semgrep-rules.yml'
    combine_yaml_files(root_directory, output_yaml_file)
