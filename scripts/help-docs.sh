while IFS= read -r command; do
    # Remove any carriage return characters (CR) or extra spaces
    command=$(echo "$command" | tr -d '\r')
    
    echo "${command}"

    # Create the output directory if it doesn't exist
    mkdir -p ./help_files

    # Write the command name as the first line (in markdown format)
    echo "## ${command}" > "./help_files/${command}_help.txt"
    
    # Get help for each command and output it to a new file
    ./bin/cli.sh $command help >> "./help_files/${command}_help.txt"
done < nifi-cli-command-list.txt
