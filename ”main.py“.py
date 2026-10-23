import argparse
import re
from pathlib import Path

IMG_RE = re.compile(r"!\[(.*?)\]\((.*?)\)")
LINK_RE = re.compile(r"\[(.*?)\]\((.*?)\)")
HEADING_RE = re.compile(r"^(#{1,6}) (.*)$", re.MULTILINE)

def scan_md(root):
    p = Path(root)
    if not p.exists():
        raise FileNotFoundError("目录不存在")
    return list(p.rglob("*.md"))

def check_file(file: Path):
    txt = file.read_text(encoding="utf-8", errors="ignore")
    bad_img = []
    bad_link = []

    for alt, src in IMG_RE.findall(txt):
        if src.startswith("http"):
            continue
        if not (file.parent / src).exists():
            bad_img.append((alt, src))

    for name, href in LINK_RE.findall(txt):
        if href.startswith("http"):
            continue
        if not (file.parent / href).exists():
            bad_link.append((name, href))

    headings = []
    for mark, title in HEADING_RE.findall(txt):
        headings.append((len(mark), title))
    return bad_img, bad_link, headings

def gen_report(filepath, bad_img, bad_link, headings):
    lines = [f"# 检查报告：{filepath}", ""]
    lines.append("## 损坏图片")
    if bad_img:
        for a, s in bad_img:
            lines.append(f"- ![{a}]({s})")
    else:
        lines.append("- ✅ 无损坏图片")

    lines += ["", "## 失效本地链接"]
    if bad_link:
        for n, h in bad_link:
            lines.append(f"- [{n}]({h})")
    else:
        lines.append("- ✅ 无失效本地链接")

    lines += ["", "## 标题统计"]
    cnt = {}
    for lv, _ in headings:
        cnt[lv] = cnt.get(lv, 0) + 1
    for lv in sorted(cnt):
        lines.append(f"- H{lv}: {cnt[lv]} 个")

    lines += ["", "## 目录索引"]
    for lv, title in headings:
        lines.append("  "*(lv-1)+f"- {title}")
    lines.append("\n---")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Markdown本地文档检查工具")
    parser.add_argument("dir", help="待扫描目录")
    parser.add_argument("-o", "--output", help="输出报告md文件（可选）")
    args = parser.parse_args()

    md_list = scan_md(args.dir)
    print(f"找到 {len(md_list)} 个md文件")
    full = []
    for f in md_list:
        print(f"正在检查：{f}")
        bi, bl, hd = check_file(f)
        full.append(gen_report(str(f), bi, bl, hd))
    out_text = "\n\n".join(full)
    if args.output:
        Path(args.output).write_text(out_text, encoding="utf-8")
        print(f"✅ 报告保存到 {args.output}")
    else:
        print(out_text)

if __name__ == "__main__":
    main()