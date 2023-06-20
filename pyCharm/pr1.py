#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import collections

# Подсчет файлов 1
if __name__ == "__main__":
    print(collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir()))
