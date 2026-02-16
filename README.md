# Github Repo Analyzer
A Python tool that analyses a Github user's repositories and generates a Markdown report.
## Latest Report 
See the generated analysis here: [report.md](report.md)

## How it works (Control flow)
1. Fetch repos using Github API
2. For each repo, fetch languages_url
3. Aggregate language bytes
4. Generate report.md

## How to run
```bash
python tester.py
