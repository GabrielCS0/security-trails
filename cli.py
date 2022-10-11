import argparse

parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    '-d', '--domain',
    help = 'The domain to be searched',
    required = True
)

parser.add_argument(
    '-k', '--api-key',
    help = 'Your Securitytrails API Key',
    dest = 'api_key',
    required = True
)

parser.add_argument(
    '-o', '--output',
    help = 'Save the results to text file',
    dest = 'output_file'
)
