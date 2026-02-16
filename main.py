import requests
import json
import os
username=os.getenv("GITHUB_USERNAME")
if not username:
    username=input("Enter username:")
url=f"https://api.github.com/users/{username}/repos"
r=requests.get(url)
if r.status_code==220:
    print("Error:")
    exit(0)
repos=r.json()

cache_file = f"cache/{username}_repos.json"
with open(cache_file, "w", encoding="utf-8") as f:
    json.dump(repos, f, indent=2)

summaries=[]
byt1=[]
totals=0
languagetot = {}

md= f"# GitHub Repository Report for {username}\n\n"
md+=f"Total repositories: {len(repos)}\n\n"

for repo in repos:

    name = repo["name"]

    stars = repo["stargazers_count"]
    totals=totals+stars
    forks = repo["forks_count"]

    lang = repo["language"]
    if lang==None:
        lang="Not specified"

    updated = repo["updated_at"]

    url = repo["html_url"]
    l2=repo["languages_url"]
    r2=requests.get(l2)
    dict1=r2.json()


    safe_name = repo["full_name"].replace("/", "_")
    langcache = f"cache/{safe_name}_languages.json"
    with open(langcache, "w", encoding="utf-8") as f:
        json.dump(dict1, f, indent=2)


    i=dict1.items()
    i2=sorted(i,key=lambda x:x[1],reverse=True)

    print(
        f"Name: {name}| Stars: {stars} | Forks: {forks} | Major Language: {lang} | Updated: {updated} | URL: {url}")
    print("Top 5 languages used in this repo:")
    for lan1,byt2 in i2[:5]:
        if lan1 in languagetot:
            languagetot[lan1] += byt2
        else:
            languagetot[lan1] = byt2
        print(f" | Language: {lan1}| Bytes: {byt2} | Total Bytes: {languagetot[lan1]} |")
    md += f"## {name}\n"
    md += f"- ⭐ Stars: {stars}\n"
    md += f"- 🍴 Forks: {forks}\n"
    md += f"- 🧠 Major Language: {lang}\n"
    md += f"- 🕒 Updated: {updated}\n"
    md += f"- 🔗 URL: {url}\n"
    md += f"- Top Languages:\n"
    for lan1, byt2 in i2[:5]:
        md += f"  - {lan1}: {byt2} bytes\n"
    md+="\n"

print("Total starts across all repos:", totals)
print("Total repositories:", len(repos))
md += f"\n# Summary\n"
md += f"- Total stars across all repos: {totals}\n"

with open("report.md","w",encoding="utf-8") as f:
    f.write(md)
cache_file = f"cache/{username}_repos.json"

with open(cache_file, "w", encoding="utf-8") as f:
    json.dump(repos, f, indent=2)













