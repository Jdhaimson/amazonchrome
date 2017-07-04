import argparse
import json

from amazon.api import AmazonAPI
from product_search.amazon_search import get_search_results

def main():
    parser = argparse.ArgumentParser(description='''
        This script queries Amazon to generates a list of products that can be shown in
        the chromeextension.
        ''')
    parser.add_argument('--tag', dest='tag', default='j2productions-20', required=True)
    parser.add_argument('--access_key', dest='access_key', default=None, required=True)
    parser.add_argument('--secret_key', dest='secret_key', default=None, required=True)

    args = parser.parse_args()
    
    search_results = get_search_results(args.access_key, args.secret_key, args.tag)
    print json.dumps(search_results, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    main()
