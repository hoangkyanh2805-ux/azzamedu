# After reboot — start LearnHouse local

WSL was installed. **Reboot Windows once**, then:

## 1. Start Docker Desktop

- Open **Docker Desktop** from Start menu
- Wait until bottom-left shows **Engine running** (can take 1–2 min first time)

## 2. Run setup script

```powershell
cd "g:\Other computers\My Computer\Project\webkhoahoc\web\learnhouse"
.\scripts\local-setup.ps1
```

## 3. Open browser

| | |
|--|--|
| **URL** | http://localhost:8080 |
| **Email** | admin@hoa-homes.com |
| **Password** | AlphaElite-Local-2026! |

## 4. Build course in admin UI

Follow `admin-setup-checklist.md` — paste from `content/apprentice-operating-course/`.

## If script fails

```powershell
# Manual health check
docker info
cd "g:\Other computers\My Computer\Project\webkhoahoc\web\learnhouse\instance"
npx learnhouse@latest doctor
npx learnhouse@latest logs
```

Full guide: `local-test-guide.md`
