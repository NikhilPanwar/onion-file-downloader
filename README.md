# Tor File Downloader

This script downloads files through the Tor network using `requests_tor`. It takes a URL as an argument and optionally allows specifying an output filename. If no filename is provided, it saves the file to the `tordownloads/` directory.

## Requirements

- Python 3.x
- `requests_tor`
- `tqdm`
- Tor service running on port `9050`

## Installation

1. Install dependencies:
   ```sh
   pip install requests_tor tqdm
   ```
2. Ensure Tor is running on port `9050` (and `9051` for control).

## Usage

Run the script with the following command:

```sh
python script.py <URL> [output_path]
```

### Examples

1. Download a file with an automatically generated filename:
   ```sh
   python script.py "http://exampleonion.onion/file.zip"
   ```
   - Saves to `tordownloads/file.zip`

2. Download a file with a specified output path:
   ```sh
   python script.py "http://exampleonion.onion/file.zip" "downloads/custom.zip"
   ```

## Notes

- The script ensures the `tordownloads/` folder exists before saving files.
- Make sure Tor is running to successfully download through the network.
- Use a valid `.onion` URL if downloading from the dark web.

