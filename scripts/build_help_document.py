import os
from arg_parser import nifi_parse_arguments
from read_files import read_help_files
from markdown_generator import NifiMarkdownGenerator

def main():
    # Parse the arguments
    args = nifi_parse_arguments()

    # Create instance of of NifiMarkdownGenerator
    markdown_generator = NifiMarkdownGenerator(
        help_dir=args.help_dir,
        output_file=args.output,
        help_file=args.help_file
    )

    # List all .txt files in the help_files directory
    help_files = read_help_files(args.help_dir)
    
    # Generate Table of Contents
    toc = markdown_generator.generate_table_of_contents(help_files)

    # Process help content (if needed)
    help_content = markdown_generator.process_help_file(args.include_help)

    # Process command files
    command_content = markdown_generator.process_command_files(help_files)

    # Write the final markdown document
    markdown_generator.write_markdown(toc, help_content, command_content)

    print(f"All help files have been collected and sorted into.{args.output}")


if __name__ == "__main__":
    main()
