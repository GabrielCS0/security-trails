#!/usr/bin/env python3

import requests
import cli

def search_subdomains(domain: str, api_key: str) -> list:
    print(f'[*] Searching securitytrails.com for subdomains of {domain}')
    
    url = f'https://api.securitytrails.com/v1/domain/{domain}/subdomains?children_only=false&include_inactive=true'
    headers = {
        'APIKEY': api_key,
        'Accept': 'application/json'
    }
    request = requests.get(url, headers = headers)

    if request.status_code == 400:
        print('[Error] - The parameters provided contain invalid characters (e.g. domains)')
        quit()
    elif request.status_code == 401:
        print('[Error] - You did not provide a valid API key')
        quit()
    elif request.status_code == 403:
        print('[Error] - The requested information can not be accessed')
        quit()
    elif request.status_code == 429:
        print('[Error] - You reached your quota or rate limit')
        quit()

    subdomains = request.json()['subdomains']
    return subdomains

def print_result(subdomains: list, domain: str):
    if len(subdomains) == 0:
        print(f'[*] No subdomains were found for {domain}')
        return

    print(f'[*] Found {len(subdomains)} subdomains of {domain}\n')
    for subdomain in subdomains:
        print(f'{subdomain}.{domain}')

def save_subdomains_to_file(output_file: str, subdomains: list, domain: str):
    if output_file is None or len(subdomains) == 0:
        return

    with open(str(output_file), 'w') as file:
        for subdomain in subdomains:
            file.write(subdomain + '.' + domain + '\n')
    print(f'\n[*] Results saved in {output_file} file')

def main(domain: str, api_key: str, output_file: str):
    subdomains = search_subdomains(domain, api_key)
    print_result(subdomains, domain)
    save_subdomains_to_file(output_file, subdomains, domain)

if __name__ == '__main__':
    args = cli.parser.parse_args()
    main(args.domain, args.api_key, args.output_file)
