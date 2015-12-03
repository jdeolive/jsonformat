# JSON Formatter

A simple Python script for parsing and formatting a JSON string.

    # format from stdin
    % echo '{"foo":"bar", "baz": 2}' | python jsonformat.py 

    # format from file
    % python jsonformat.py /path/to/file.json

    # format file inplace
    % python jsonformat.py -i /path/to/file.json

    # unformat
    % python jsonformat.py -u /path/to/file.json
