#!/usr/bin/env python
# encoding: utf-8

import proxy_fn

s = 'socks5://127.0.0.1:1080'

p = proxy_fn.random_python_telegram_bot_dict_from_file('proxy.txt')

print(p)

