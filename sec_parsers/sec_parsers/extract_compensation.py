import argparse
from sec_parsers import Filing, download_sec_filing


def main():
    parser = argparse.ArgumentParser(
        description="Extract Compensation Discussion and Analysis section from DEF14A HTML file.")
    parser.add_argument("url", type=str, help="URL of the DEF14A HTML file")
    args = parser.parse_args()

    html = download_sec_filing(args.url)
    filing = Filing(html)
    filing.parse()  # parses filing
    filing.visualizeXml()


if __name__ == "__main__":
    main()
