def detect_delimiter(file_content):
    delimiters = [',', ';', '\t']

    delimiter_counts = {}

    for delimiter in delimiters:
        delimiter_counts[delimiter] = file_content.count(delimiter)

    detected_delimiter = max(delimiter_counts, key=delimiter_counts.get)

    return detected_delimiter