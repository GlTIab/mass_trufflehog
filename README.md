## Scan all the repositories of a specific profile on GitHub

1. Install https://github.com/trufflesecurity/trufflehog
   
2. Use https://github.com/GlTIab/github-repos-scraper/ to scrape all the repositories. It will save all the repositories to target-repos.txt.
   
3. Run the ```mass_trufflehog.py``` script with:
   
```curl -sSL https://raw.githubusercontent.com/GlTIab/mass_trufflehog/main/mass_trufflehog.py | python3 - -command "trufflehog github --repo={}" target-repos.txt```

OR

```git clone https://github.com/GlTIab/mass_trufflehog```

```cd mass_trufflehog```

```python3 mass_trufflehog.py -command "trufflehog github --repo={}" target-repos.txt```

Enjoy!
