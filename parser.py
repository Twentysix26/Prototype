import yaml

with open("repositories.yaml") as f:
    data = yaml.safe_load(f.read())

sh = ""

repos = []
repos.extend(data["approved"])
repos.extend(data["unapproved"])

for r in repos:
    sh += f"git clone {r} && / \n"

with open("cloneme.sh", "w") as f:
    f.write(sh)
