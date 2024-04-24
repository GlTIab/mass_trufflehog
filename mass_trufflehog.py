import subprocess
import argparse

def run_trufflehog(command, filename):
    # Read URLs from the file
    with open(filename, 'r') as file:
        urls = file.readlines()

    # Remove whitespace characters like `\n` at the end of each line
    urls = [url.strip() for url in urls]

    # Run trufflehog for each URL
    for url in urls:
        full_command = command.format(url)
        subprocess.run(full_command, shell=True)

def main():
    parser = argparse.ArgumentParser(description='Run trufflehog for multiple GitHub repositories listed in a file.')
    parser.add_argument('-command', required=True, help='The trufflehog command with placeholder {}')
    parser.add_argument('filename', help='The name of the file containing GitHub repository URLs')
    args = parser.parse_args()

    run_trufflehog(args.command, args.filename)

if __name__ == "__main__":
    main()
