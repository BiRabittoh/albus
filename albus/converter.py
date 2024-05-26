import os
from typing import Tuple
import pypandoc

# Map of file extensions to output formats
CONVERSION_MAP = {
    'docx': 'pdf',
    'odt': 'pdf',
    'epub': 'html'
}

def join_extension(filename: str, extension: str) -> str:
    return f"{filename}.{extension}"

def split_extension(filename: str) -> Tuple[str, str]:
    input_filename, input_extension = os.path.splitext(filename)
    input_extension = input_extension.lower()[1:]  # Remove leading dot and convert to lowercase
    return (input_filename, input_extension)

def convert_file(input_file: str) -> Tuple[str, str]:
    # Determine the input file extension
    filename, extension = split_extension(input_file)

    # Check if the input file extension is supported
    if extension in CONVERSION_MAP:
        output_format = CONVERSION_MAP[extension]

        # Perform the conversion using Pandoc
        pypandoc.convert_file(
            input_file,
            output_format,
            outputfile=join_extension(filename, output_format),
            extra_args=['--pdf-engine=tectonic']
        )
        return filename, output_format
    else:
        raise ValueError(f"Conversion from '{extension}' not supported.")
