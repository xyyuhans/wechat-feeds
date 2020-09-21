import csv
import pandas as pd

df = pd.read_csv("list.csv")
df["bizid"] = "[inoreader](" + "https://www.inoreader.com/?add_feed=" + "https://github.com/hellodword/wechat-feeds/raw/feeds/" + df["bizid"] + ".xml)"
df.to_csv("rss.csv", index=False)
