import requests

def compare(base, pwd, label):
    s = requests.Session()
    t = s.post(f"{base}/auth/login", data={"username": "admin@hoa-homes.com", "password": pwd}).json()["tokens"]["access_token"]
    h = {"Authorization": f"Bearer {t}"}
    courses = s.get(f"{base}/courses/org_slug/alpha-elite/page/1/limit/50", headers=h).json()
    course = next(x for x in courses if "Smart Money" in x.get("name", ""))
    print(f"\n{label} course: {course['name']}")
    print(f"  thumbnail: {bool(course.get('thumbnail_image'))}")
    print(f"  about len: {len(course.get('about') or '')}")
    chapters = s.get(f"{base}/chapters/course/{course['id']}/page/1/limit/50", headers=h).json()
    act = chapters[0]["activities"][0]
    blocks = act.get("content", {}).get("content", [])
    text = []
    for b in blocks:
        for n in b.get("content") or []:
            if n.get("type") == "text":
                text.append(n.get("text", ""))
    joined = " ".join(text)
    print(f"  L1 blocks: {len(blocks)}")
    print(f"  L1 has youtube in text: {'youtube' in joined.lower()}")
    print(f"  block types: {sorted({b.get('type') for b in blocks})}")

compare("http://localhost:8080/api/v1", "AlphaElite-Local-2026!", "LOCAL :8080")
compare("http://learn.hoa-homes.com/api/v1", "AlphaElite-Prod-Learn-2026!", "PROD")

def count_videos(base, pwd, label):
    s = requests.Session()
    t = s.post(f"{base}/auth/login", data={"username": "admin@hoa-homes.com", "password": pwd}).json()["tokens"]["access_token"]
    h = {"Authorization": f"Bearer {t}"}
    courses = s.get(f"{base}/courses/org_slug/alpha-elite/page/1/limit/50", headers=h).json()
    course = next(x for x in courses if "Smart Money" in x.get("name", ""))
    chapters = s.get(f"{base}/chapters/course/{course['id']}/page/1/limit/50", headers=h).json()
    vid = total = 0
    for ch in chapters:
        for a in ch.get("activities", []):
            total += 1
            blocks = a.get("content", {}).get("content", [])
            if any(b.get("type") == "blockEmbed" for b in blocks):
                vid += 1
    print(f"{label}: {vid}/{total} lessons with video | thumbnail={bool(course.get('thumbnail_image'))}")

count_videos("http://localhost:8080/api/v1", "AlphaElite-Local-2026!", "LOCAL")
count_videos("http://learn.hoa-homes.com/api/v1", "AlphaElite-Prod-Learn-2026!", "PROD")
