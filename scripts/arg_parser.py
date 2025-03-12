import argparse
import sys

class IndentedHelpFormatter(argparse.RawTextHelpFormatter):
    def format_description(self, description):
        # Indent all subsequent lines after the first one
        if description:
            return '\n'.join([line if i == 0 else '    ' + line for i, line in enumerate(description.splitlines())])
        return description
    
def nifi_parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Generate NiFi Toolkit Documentation.",
                                     formatter_class=IndentedHelpFormatter)

    parser.add_argument(
        '--help-dir',
        type=str,
        required=True,
        metavar='PATH',
        help="Use --help-dir </path/to/directory>\nThis directory should contain the help files to process into single document"
    )
    parser.add_argument(
        '--output',
        type=str,
        default='./export.md',
        metavar='FILENAME',
        help="Use --output </path/to/output_directory/filename.ext>\nThis stores output in user specified location with specified filename\nDefault location is ./export.md unless otherwise specified."
    )
    parser.add_argument(
        '--help-file',
        type=str,
        required=True,
        metavar='PREFIX',
        help="Use --help-file <filename prefix>\nEnter prefix to help filename ending in _help.txt found --help-dir." 
    )
    parser.add_argument(
        '--include-help',
        action='store_true',
        default=False,
        help="Use --include-help\nIncludes the help command documentation in the raw markdown escaped output\nDefault is set to False, no arguments are required with this flag."
    )

    try:
        # Parse arguments first
        args = parser.parse_args()

        # Ensure the main help file has correct suffix
        if not args.help_file.endswith('_help.txt'):
            args.help_file = f"{args.help_file}_help.txt"

        return parser.parse_args()
    
    except SystemExit as e:
        # Catch the missing required argument error and print the help message
        print(f"Error: {e}")
        print(f"Required argument {e} not provided. Please include the required argument {e}.")
        parser.print_help()  # This prints the help message
        sys.exit(1)  # Exit the script with a non-zero status