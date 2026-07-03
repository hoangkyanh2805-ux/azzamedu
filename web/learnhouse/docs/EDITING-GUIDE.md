# Hướng dẫn chỉnh sửa khóa học LearnHouse

**Course:** Apprentice Operating Course  
**Cấu trúc hiện tại:** 21 section · 114 lessons (clone Udemy SMC gốc, compliance rewrite)  
**Local:** http://localhost:8080 · `admin@hoa-homes.com` / `AlphaElite-Local-2026!`

---

## Sửa nhanh trong LearnHouse UI (khuyến nghị cho 1 bài)

1. Mở http://localhost:8080 → đăng nhập admin
2. Vào **Courses** → **Apprentice Operating Course**
3. Sidebar phải: chọn section (vd. `S02: Definitions — Market Structure Foundations`)
4. Click vào tên lesson cần sửa
5. Nút **Edit** / biểu tượng bút (góc phải)
6. Sửa nội dung trong rich-text editor
7. **Save** → refresh trang

Dùng khi: sửa chữ, thêm video embed, upload PDF worksheet.

### Sửa trang tổng quan course (About / What you will learn)

1. Vào course → **Settings** / **Edit course**
2. Sửa **About**, **Description**, **What you'll learn**
3. Save

Phần video hero (ô số 1 trên screenshot) → upload thumbnail / intro video trong course settings.

---

## Sửa cấu trúc section & tên bài (clone Udemy)

File nguồn: `content/udemy-clone-curriculum.json`

```json
{
  "number": 2,
  "title": "Definitions — Market Structure Foundations",
  "lessons": [
    {"title": "Liquidity — participation zones (education)", "type": "video"},
    {"title": "Quiz — How to document liquidity participation", "type": "quiz"}
  ]
}
```

- `type`: `"video"` hoặc `"quiz"`
- Đổi tên section/lesson → sửa JSON → chạy lại seed (xóa course cũ cùng tên, tạo mới):

```powershell
cd "g:\Other computers\My Computer\Project\webkhoahoc\web\learnhouse"
.\scripts\seed-udemy-clone.ps1
```

**Lưu ý:** Seed **tạo lại toàn bộ** course — mọi chỉnh sửa làm tay trong UI sẽ mất. Chỉ chạy seed khi đổi cấu trúc; sửa nội dung từng bài thì dùng UI.

---

## Sửa nội dung mẫu auto-generate (tất cả 114 bài)

Mỗi lesson được sinh từ `scripts/seed-udemy-clone.py` → hàm `generate_lesson_body()`.

Muốn đổi template chung (Objective, Lesson body, Key points) → sửa hàm đó → chạy lại `seed-udemy-clone.ps1`.

Muốn nội dung riêng cho 1 bài → thêm field `"body"` trong JSON:

```json
{"title": "BOS and CHoCH", "type": "video", "body": "### Objective\n...\n\n#### What it is\n..."}
```

---

## Thêm video YouTube

Trong lesson (UI hoặc body markdown), thay:

```markdown
### Video
`[PENDING: YouTube unlisted]`
```

bằng:

```markdown
### Video
https://www.youtube.com/watch?v=XXXXXXXX
```

Hoặc trong LearnHouse UI: đổi activity type sang **External video** để embed player.

---

## Bản 8 module cũ (35 lessons) — nếu cần

File markdown: `content/apprentice-operating-course/m01`–`m08`  
Sync (không xóa course, chỉ update lesson khớp M1L1…M8Lx):

```powershell
.\scripts\sync-course.ps1
```

**Không dùng** sync sau khi đã seed Udemy clone — tên lesson khác (`S01:...` vs `M1L1`).

---

## Lệnh thường dùng

```powershell
.\scripts\local-start.ps1       # bật Docker + LearnHouse
.\scripts\seed-udemy-clone.ps1  # tạo lại 21 section / 114 lessons
.\scripts\sync-course.ps1       # chỉ cho bản 8 module markdown
```

---

## Map 21 section ↔ Udemy gốc

| # | Section |
|---|---------|
| S01 | Introduction |
| S02 | Definitions (liquidity, IMB, BOS, POI…) |
| S03 | Double OB + POI |
| S04 | Trend follow vs break |
| S05 | Double OB + BOS bounce |
| S06 | Extra knowledge |
| S07 | Case walkthroughs (XAUUSD, US30…) |
| S08 | POI quality & confirmation |
| S09–S12 | Session reviews + scalping |
| S13 | Trading journal |
| S14 | Bonus |
| S15–S16 | Quiz banks (15+15) |
| S17 | Tips & psychology |
| S18 | Final exam |
| S19 | 2026 update |
| S20 | Tools & lot size |
| S21 | Close & next steps |

Tiêu đề đã rewrite compliance (không signal group, không % profit). Nội dung lesson hiện là **template ~500 từ/bài** — cần quay video + mở rộng body cho bài core (S02–S08) để đạt độ dài Udemy.

Mẫu bài dài: `content/LESSON-TEMPLATE-FULL.md`
