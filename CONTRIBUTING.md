# Contributing

Thanks for helping keep the catalog current. Pull requests are the preferred way to suggest additions or corrections.

## What belongs here

Add original, public technical research about a vulnerability in a Microsoft product or service, or a disclosure handled through MSRC. Conference slides and videos are welcome when they contain technical detail. Prefer the researcher's original publication over news coverage, vendor summaries, or pages that merely repeat a CVE description.

Please do not add generic security news, product announcements, exploit aggregators, or duplicate mirrors when the original source is still available.

## Add an entry

Add one row to `writeups.csv` using this schema:

```text
date,bounty,title,url,author,author-url,type,tweeted,archive-url
YYYY-MM-DD,amount-or-?,title,url,author,author-url-or-?,blog-or-video,false,?
```

- Use the public publication date, not the private report date.
- Record a bounty only when the source confirms the amount. Use `0` when the source explicitly says no bounty was paid, and `?` when it is unknown.
- Use the canonical HTTPS URL for the original research.
- Set `type` to `blog` for articles, advisories, papers, and slide decks; use `video` for video-only entries.
- Leave `tweeted` as `false` and `archive-url` as `?` for new entries.
- Quote any CSV field containing a comma.

You do not need to edit `README.md`; automation rebuilds it from the CSV after merge.

## Validate locally

Run:

```bash
python infra/builder/csv_to_readme.py writeups.csv README.md
```

The command validates dates, URLs, bounty values, row types, and duplicate URLs before generating the README.
