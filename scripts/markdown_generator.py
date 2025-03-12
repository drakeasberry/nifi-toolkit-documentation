import os
import re

class NifiMarkdownGenerator:
    def __init__(self, help_dir, output_file, help_file):
        self.help_dir = help_dir
        self.output_file = output_file
        self.help_file=help_file

    def generate_table_of_contents(self, help_files):
        """
        Generate the Table of Contents section for the Markdown file.
        """
        links = []
        for help_file in help_files:
            if help_file != self.help_file:
                command_name = os.path.splitext(help_file)[0]
                command_name = command_name.replace('_help', '')
                header_link = NifiMarkdownPrep.to_header_link(command_name)
                links.append(f"- [{command_name}](#{header_link})")
        
        return "\n".join(links)

    def process_help_file(self, include_help):
        """
        Read and process the general 'help' file if needed.
        """
        if include_help:
            help_file_path = os.path.join(self.help_dir, self.help_file)
            if os.path.exists(help_file_path):
                with open(help_file_path, 'r') as f:
                    content = "## Help Commands\n\n"
                    content += "```text\n"
                    content += NifiMarkdownPrep.escape_markdown(f.read())
                    content += "\n```\n"
                    content += "\n[Back to Table of Contents](#table-of-contents)\n\n"
                    return content
            else:
                return "Help file not found.\n"
        return ""

    def process_command_files(self, help_files):
        """
        Process all command help files and generate corresponding Markdown sections.
        """
        content = ""
        for help_file in help_files:
            if help_file != self.help_file:  # Skip the general help file
                command_name = os.path.splitext(help_file)[0]
                command_name = command_name.replace('_help', '')
                
                with open(os.path.join(self.help_dir, help_file), 'r') as f:
                    content += f"## {command_name}\n\n"
                    content += "```text\n"
                    content += NifiMarkdownPrep.escape_markdown(f.read())
                    content += "\n```\n"
                    content += "\n[Back to Table of Contents](#table-of-contents)\n\n"
        return content

    def write_markdown(self, toc, help_content, command_content):
        """
        Write the final Markdown document.
        """
        with open(self.output_file, 'w') as md_file:
            md_file.write("# Nifi Toolkit Help Documentation\n\n")
            md_file.write("## Table of Contents\n\n")
            md_file.write(toc)
            md_file.write("\n\n")
            md_file.write(help_content)  # Add help file content (if included)
            md_file.write(command_content)  # Add all command documentation

class NifiMarkdownPrep:
    """
    Class to handle preparing markdown files to be generator with correct linking and formatting.
    """
    @staticmethod
    def escape_markdown(text):
        """
        Escape Markdown special characters, especially dashes at the start of lines.
        """
        text = re.sub(r'(^\s*)-(.*)', r'\1\- \2', text)
        return text
    
    @staticmethod
    def to_header_link(command_name):
        """
        Converts command names to a format suitable for Markdown header links.
        """
        return re.sub(r'[^a-z0-9]+', '-', command_name.lower()).strip('-')