from amazon.api import AmazonAPI

def get_search_results(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, Keywords = 'dress'):
    """
    Function which queries the Amazon Product API to get relevant products
    """
    amazon_api = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
    products = amazon_api.search_n(20, Keywords=Keywords, SearchIndex='FashionWomen', Sort="relevancerank")
    hipbuy_products = map(_amazon_product_to_hipbuy, products)
    return hipbuy_products

def _amazon_product_to_hipbuy(product):
    """
    Helper function to convert Amazon API return to chromeextension format 

    :param product: An AmazonProduct instance
    """
    (price, currency) = product.price_and_currency
    # Make sure we always have two decimal places in the price
    
    if currency == 'USD':
        price_str = "$" + '{:0.2f}'.format(price)
    else:
        raise Exception("Non USD Cost")
        
    return {
        "url": product.offer_url
        , "imgurl": product.large_image_url
        , "name": product.title
        , "price": price_str
    }
