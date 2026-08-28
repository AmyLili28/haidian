import base64, re, sys

def embed_font(html_path, font_b64):
    with open(html_path, encoding="utf-8") as f:
        t = f.read()
    if "@font-face" in t and "WeavingCJK" in t:
        return False  # 已嵌入
    fontface_css = """@font-face {
  font-family: 'WeavingCJK';
  src: url(data:font/woff2;base64,__FONT_B64__) format('woff2');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}
""".replace("__FONT_B64__", font_b64)
    m = re.search(r"<style[^>]*>", t)
    if not m:
        return False
    t = t[:m.end()] + fontface_css + t[m.end():]
    # 各种 font-family 写法统一在前面插入 WeavingCJK
    t = re.sub(
        r'font-family\s*:\s*(-apple-system[^;}]+)',
        lambda mm: 'font-family: "WeavingCJK",' + mm.group(1),
        t, count=1
    )
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(t)
    return True

if __name__ == "__main__":
    font_b64 = base64.b64encode(open("/tmp/weaving-font-subset.woff2","rb").read()).decode()
    for p in sys.argv[1:]:
        r = embed_font(p, font_b64)
        print(p, "->", "embedded" if r else "already/skip")
