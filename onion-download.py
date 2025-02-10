import os
import argparse
from requests_tor import RequestsTor
from tqdm import tqdm
from urllib.parse import unquote, urlparse

def download_file(rt, url, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with rt.get(url, stream=True) as r:
        r.raise_for_status()
        total_size_in_bytes = int(r.headers.get('content-length', 0))
        block_size = 1024 * 1024  # 1 MiB
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(output_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=block_size):
                progress_bar.update(len(chunk))
                f.write(chunk)
        progress_bar.close()
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Download a file through Tor.')
    parser.add_argument('url', type=str, help='The URL of the file to download')
    parser.add_argument('output', nargs='?', default=None, help='Optional output filename (with path)')
    args = parser.parse_args()
    
    url = unquote(args.url.strip())
    filename = args.output if args.output else os.path.join('tordownloads', os.path.basename(urlparse(url).path))
    
    rt = RequestsTor(tor_ports=(9050,), tor_cport=9051)
    
    try:
        filepath = download_file(rt, url, filename)
        print(f"Downloaded {filepath}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

if __name__ == '__main__':
    main()
