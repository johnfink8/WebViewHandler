# WebViewHandler
Python logging handler that outputs real-time to a simple web-based viewing portal

## Usage
    import logging
    from WebViewHandler import WebViewHandler
    logger = logging.getLogger('MyLoggerName')
    wh = WebViewHandler()
    logger.addHandler(wh)

    logger.info('Yay it works!')

Navigate to http://<my_ip>:8080 to see your logs.
