import re
with open("include/linux/sched.h") as fd:
    lines = fd.readlines()[632:1306]
lines = "".join(lines)
lines = re.sub(r"(?s)/\*.*?\*/", "", lines)
lines = re.sub(r"#.*", "", lines)
lines = re.sub(r"\t", "", lines)
lines = re.sub(r"\n+", "\n", lines)
lines = lines.split("\n")
print(f"{len(lines)} * 8 = {len(lines) * 8}")
