import os
import re
import argparse

# Constants
HELP_FILES_DIR = './help_files/'
OUTPUT_FILE = 'nifi_toolkit_documentation.md'
OVERALL_HELP = 'help_help.txt'


def escape_markdown(text):
    """
    Escape Markdown special characters, especially dashes at the start of lines.
    """
    text = re.sub(r'(^\s*)-(.*)', r'\1\- \2', text)
    return text


def to_header_link(command_name):
    """
    Converts command names to a format suitable for Markdown header links.
    """
    return re.sub(r'[^a-z0-9]+', '-', command_name.lower()).strip('-')


def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Generate NiFi Toolkit Documentation.")
    parser.add_argument(
        '--include_help',
        action='store_true',
        default=False,
        help="Include the help command documentation in the output (default: False)"
    )
    return parser.parse_args()


def generate_table_of_contents(help_files):
    """
    Generate the Table of Contents section for the Markdown file.
    """
    links = []
    for help_file in help_files:
        if help_file != OVERALL_HELP:
            command_name = os.path.splitext(help_file)[0]
            command_name = command_name.replace('_help', '')
            header_link = to_header_link(command_name)
            links.append(f"- [{command_name}](#{header_link})")
    
    return "\n".join(links)


def process_help_file(include_help):
    """
    Read and process the general 'help' file if needed.
    """
    if include_help:
        help_file_path = os.path.join(HELP_FILES_DIR, OVERALL_HELP)
        if os.path.exists(help_file_path):
            with open(help_file_path, 'r') as f:
                content = "## Help Commands\n\n"
                content += "```text\n"
                content += escape_markdown(f.read())
                content += "\n```\n"
                content += "\n[Back to Table of Contents](#table-of-contents)\n\n"
                return content
        else:
            return "Help file not found.\n"
    return ""


def process_command_files(help_files):
    """
    Process all command help files and generate corresponding Markdown sections.
    """
    content = ""
    for help_file in help_files:
        if help_file != OVERALL_HELP:  # Skip the general help file
            command_name = os.path.splitext(help_file)[0]
            command_name = command_name.replace('_help', '')
            
            with open(os.path.join(HELP_FILES_DIR, help_file), 'r') as f:
                content += f"## {command_name}\n\n"
                content += "```text\n"
                content += escape_markdown(f.read())
                content += "\n```\n"
                content += "\n[Back to Table of Contents](#table-of-contents)\n\n"
    return content


def write_markdown(content, toc, help_content, command_content):
    """
    Write the final Markdown document.
    """
    with open(OUTPUT_FILE, 'w') as md_file:
        md_file.write("# Nifi Toolkit Help Documentation\n\n")
        md_file.write("## Table of Contents\n\n")
        md_file.write(toc)
        md_file.write("\n\n")
        md_file.write(help_content)  # Add help file content (if included)
        md_file.write(command_content)  # Add all command documentation


def main():
    # Parse the arguments
    args = parse_arguments()

    # List all .txt files in the help_files directory
    help_files = [f for f in os.listdir(HELP_FILES_DIR) if f.endswith('.txt')]
    help_files.sort()

    # Generate Table of Contents
    toc = generate_table_of_contents(help_files)

    # Process help content (if needed)
    help_content = process_help_file(args.include_help)

    # Process command files
    command_content = process_command_files(help_files)

    # Write the final markdown document
    write_markdown(command_content, toc, help_content, command_content)

    print(f"All help files have been collected and sorted into {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
