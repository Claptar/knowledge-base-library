---
title: below. Keep this information private.
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit2-dataTech.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# below. Keep this information private.

**Source:** [`units/unit2-dataTech.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

CONSUMER_KEY       = ""
CONSUMER_SECRET    = ""
OAUTH_TOKEN        = ""
OAUTH_TOKEN_SECRET = ""

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)
api = twitter.Twitter(auth=auth)

---

[← "Key and Access Tokens", you will find the information needed](15-key-and-access-tokens-you-will-find-the-information-needed.md) · [Up: contents](index.md) · [get the list of senators →](17-get-the-list-of-senators.md)
