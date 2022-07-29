import urllib3

class FSNetConfiguration:
  def __init__(self, proxy_manager: urllib3.ProxyManager = None,
               http_pool: urllib3.HTTPConnectionPool = None,
               https_pool: urllib3.HTTPSConnectionPool = None,
               headers: dict = None) -> None:
    self.proxy_manager = proxy_manager
    self.http_pool = http_pool
    self.https_pool = https_pool
    self.headers = headers

  def should_use_http(self) -> bool:
    return self.http_pool is not None
  
  def should_use_https(self) -> bool:
    return self.https_pool is not None
  
  def should_use_proxy(self) -> bool:
    return self.proxy_manager is not None
  
  def use_custom_headers(self) -> bool:
    return self.headers is not None

  def delegate_request(self, method: str, url: str, headers: dict = None,
                       fields: dict = None,
                       **kwargs) -> urllib3.HTTPResponse:
    pool = (self.http_pool if self.should_use_http() else (
      self.https_pool if self.should_use_https() else (
        self.proxy_manager if self.should_use_proxy() else None
      )
    ))
    if self.should_use_https():
      if 'https' not in url: url = url.replace('http', 'https')

    if not pool: 
      raise Exception('Invalid pool option: missing pool object')

    if self.use_custom_headers():
      headers = self.headers
    
    return pool.request(method, url, headers=headers, fields=fields, **kwargs)

