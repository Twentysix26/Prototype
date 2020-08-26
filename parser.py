import yaml

with open("repositories.yaml") as f:
    data = yaml.safe_load(f.read())

sh = ""

repos = []
repos.expand(data["approved"])
repos.expand(data["unapproved"])

for r in repos:
    sh += f"git clone {r} && /"

with open("cloneme.sh", "w") as f:
    f.write(sh)
