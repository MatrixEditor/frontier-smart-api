# MIT License

# Copyright (c) 2022 MatrixEditor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import argparse
import os
import re

from fsapi import all as fsapi
from json import dump
from time import sleep, time

RE_IPV4 = r"^\d{1,3}(.\d{1,3}){3}$"

__BANNER__ = """\
             __ __ _  _ ___
            |_ (_ |_||_) | 
            |  __)| ||  _|_
───────────────────────────────────────
"""

def delegate_explore(args: dict, radio: fsapi.RadioHttp):
  verbose = args['verbose']
  exclude = args['exclude'].split(',')

  if verbose: print('\n[+] Starting to explore target host...')
  sleep(1)
  
  sid = fsapi.netremote_request(fsapi.CREATE_SESSION, fsapi.nodes.BaseCreateSession, radio).content.value

  results = {}
  node_types = fsapi.get_all_node_types()
  for name in node_types:
    node_type = node_types[name]
    if fsapi.is_list_class(node_type):
      result = fsapi.netremote_request('LIST_GET_NEXT', node_type, radio, 
                                       parameters={'maxItems': 100, 'sid': sid})
    else: 
      result = fsapi.netremote_request('GET', node_type, radio, parameters={'sid': sid})

    if result.status not in exclude:
      if args['json']:
        results[node_type.get_name()] = {
          'status': result.status,
          'result': result.to_json()
        }
      if verbose: print('  - %s --> %s' % (node_type.get_name(), result.status))

  if args['json']:
    name = 'fsapi_exploration-%s.json' % time()
    with open(name, 'w') as _res:
      dump(results, _res)
    if verbose: print('\n[+] Saved exlporation result to:', name)

def delegate_isu(args: dict, radio: fsapi.RadioHttp):
  verbose = args['verbose']
  
  if args['find']:
    # REVISIT: add not null checks
    mac = fsapi.netremote_request('GET', fsapi.nodes.BaseSysInfoRadioId, radio).content.value
    version = fsapi.netremote_request('GET', fsapi.nodes.BaseSysInfoVersion, radio).content.value
    
    values = version.split('_V')
    result = fsapi.isu_find_update(mac, values[0], values[1], verbose)
    if not result or not result['update_present']:
      print('\n[+] Generating current URL...')
      sleep(1)
      url = 'https://%s/Update.aspx?f=/updates/%s.isu.bin' % (
        fsapi.ISU_FILE_PROVIDER_HOST, version.replace('_V', '.')
      )
      print("     - url:", url)
    else:
      sleep(1)
      print('[+] Found at least one Update:')
      for update in result['updates']:
        print("    -", update)
        url = update.download_url

    path = args['collect']
    if path:
      if path == '_': path = version
      if verbose: print('\n[+] Downloading update file to: %s.isu.bin' % path)
      fsapi.isu_get_update(args['collect'] + 'isu.bin', url, verbose=verbose)
      if verbose: print('[+] Download complete')
  elif args['file']:
    path = args['target']
    if verbose: print('\n[+] Downloading updates located in file: %s' % path)
    
    try: os.mkdir('isu-download')
    except: pass
    
    for _firmware in open(path, 'r').read().split('\n'):
      if not _firmware: continue
      
      url = fsapi.isu_new_url(_firmware)
      if not url:
        if verbose: print('[-] Could not create download URL')
        continue
      
      if verbose: 
        print(' > Donwload of: isu-download/%s.isu.bin' % _firmware)
        print('     ::url "%s"' % url)
      fsapi.isu_get_update('isu-download/%s.isu.bin' % _firmware, url, verbose=verbose)
      print()
    if verbose: print('[+] Download complete')

def delegate_get(args: dict, radio: fsapi.RadioHttp):
  node_types = fsapi.get_all_node_types()
  node = args['node']
  
  if node not in node_types:
    print('[-] Undefined node:', node)
    exit(0)

  result = fsapi.netremote_request(fsapi.GET, node_types[node], radio)
  if result:
    print("[+] fsapiResponse of %s:" % node)
    print('     - status: %s' % (result.status))
    if result.status == 'FS_OK':
      print('     - value: %s' % (result.content.value))
      print('     - readonly: %s' % result.content.is_readonly())
      print('     - notifying: %s' % result.content.is_notifying())

def delegate_set(args: dict, radio: fsapi.RadioHttp):
  node_types = fsapi.get_all_node_types()
  node = args['node']

  if node not in node_types:
    print('[-] Unknown node class')
  elif node_types[node].is_readonly():
    print('[-] Node is set to be read only. A SET-request is not possible.')
  else:
    params = {}
    for key in args['args']:
      name, value = key.split(':')
      params[name] = value
    
    result = fsapi.netremote_request(fsapi.SET, node_types[node], radio, parameters=params)
    if result:
      print("[+] fsapiResponse of %s:" % node)
      print('     - status: %s' % (result.status))
    else:
      print('[-] Failed to read response or to fetch url.')

def delegate_list(args: dict, radio: fsapi.RadioHttp):
  node_types = fsapi.get_all_node_types()
  node = args['node']

  if node not in node_types:
    print('[-] Unknown node class')
  else:
    params = {}
    for key in args['args']:
      name, value = key.split(':')
      params[name] = value
    
    result = fsapi.netremote_request(fsapi.LIST_GET_NEXT, node_types[node], radio, parameters=params)
    if result:
      print("[+] fsapiResponse of %s:" % node)
      print('     - status: %s' % (result.status))
      if result.status == 'FS_OK':
        result_list: fsapi.NodeList = result.content
        print('     - list: size=%d' % (result_list.size()))
        for item in result_list.get_items():
          print('         | %s' % (item.attr))
    else:
      print('[-] Failed to read response or to fetch url.')


if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="""
    A python implementation of the FSAPI with all possible nodes.

    You can execute the fsapi.isu or fsapi.ecmascript module
    by typing the same command but with their module name."""
  )
  subparsers = parser.add_subparsers(help="sub-commands:")

  explore_parser = subparsers.add_parser('explore', help="Node Exploration")
  explore_parser.add_argument('--json', action='store_true', default=False,
    help="Saves information in JSON-format"
  )
  explore_parser.add_argument('-E', '--exclude', type=str, default='', required=False,
    help="Exclude the following arguments from being analysed (if more that one, separate them with a comma)"
  )
  explore_parser.set_defaults(func=delegate_explore)

  isu_parser = subparsers.add_parser('isu', help="ISU Firmware Context")
  isu_parser.add_argument('--find', action='store_true', required=False, default=False,
    help="Find an update for the specified host. If none was found a download URL for the current version will be generated."
  )
  isu_parser.add_argument('--collect', type=str, default=None, metavar='PATH',
    help="Collect the firmware to the specified path. (only together with --find)"
  )
  isu_parser.add_argument('-F', '--file', action='store_true', default=False, 
    help="Collect the firmware from the specified path."
  )
  isu_parser.set_defaults(func=delegate_isu)

  get_parser = subparsers.add_parser('get', help="Request a simple property")
  get_parser.add_argument('-n', '--node', required=True, 
    help='The netremote package name. (format: netremote.xxx.xxx.xxx)'
  )
  get_parser.set_defaults(func=delegate_get)

  set_parser = subparsers.add_parser('set', help='Apply a value to a stored property.')
  set_parser.add_argument('-n', '--node', required=True, 
    help='The netremote package name. (format: netremote.xxx.xxx.xxx)'
  )
  set_parser.add_argument('--args', nargs='*', 
    help='The arguments passed to the request. (format: --args arg:value [arg:value [...]]))'
  )
  set_parser.set_defaults(func=delegate_set)

  list_parser = subparsers.add_parser('list', help='Query property lists')
  list_parser.add_argument('-n', '--node', required=True, 
    help='The netremote package name. (format: netremote.xxx.xxx.xxx)'
  )
  list_parser.add_argument('--args', nargs='*', 
    help='The arguments passed to the request. (format: --args arg:value [arg:value [...]]))'
  )
  
  list_parser.set_defaults(func=delegate_list)

  gb_group = parser.add_argument_group('Global options')
  gb_group.add_argument('target', type=str, 
    help="The host address in IPv4 format."
  )
  gb_group.add_argument('-W', '--pin', type=str, required=False,
    help="A PIN used by the device (default 1234).", default='1234'  
  )
  gb_group.add_argument('-v', '--verbose', action='store_true', default=False,
    help="Prints useful information during the specified process."
  )

  nspace = parser.parse_args().__dict__
  target = nspace['target']
  verbose = nspace['verbose']

  if verbose: print(__BANNER__)
  if not target or not re.match(RE_IPV4, target):
    if 'file' not in nspace and not nspace['file']:
      print("[-] Error: Invalid IPv4 or target host == null!")
      exit(0)
  
  radio = fsapi.RadioHttp(target, nspace['pin'])
  if verbose: print('[+] Setting up netremote with:', radio)
  nspace['func'](nspace, radio)

