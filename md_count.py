import json
from pathlib import Path

def count_md(folder):
    out = []
    for f in Path(folder).rglob("*.md"):
        d = {"file":str(f),"lines":0,"chars":0,"status":"ok"}
        try:
            with open(f,"r",encoding="utf-8") as fp:
                lines = fp.readlines()
                d["lines"] = len(lines)
                d["chars"] = sum(len(l) for l in lines)
        except Exception as e:
            d["status"] = f"err:{e}"
        out.append(d)
    return out

if __name__ == "__main__":
    try:
        res = count_md("./test_md")
        with open("summary.json","w",encoding="utf-8") as f:
            json.dump(res,f,ensure_ascii=False,indent=2)
        print("完成")
    except Exception as e:
        print(e)