#!/bin/bash

python generate-rss-csv.py
csv2md rss.csv > rss.md
rm rss.csv
