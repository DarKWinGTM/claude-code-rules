# memory-context-intelligence

> **Status:** Usable in checked scope for `/memory-context-intelligence:analysis`; `review` and `packet` remain deferred
> **Current Version:** 0.1.72
> **Plugin Package Version:** 0.9.25
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-01)

---

## What this plugin does

`memory-context-intelligence` เป็น Claude Code plugin สำหรับอ่าน **bounded work evidence** จาก memory traces ที่ถูกเตรียมไว้ แล้วสรุปออกมาเป็น **topic cards** ที่ช่วยคุณเห็นว่า workflow, RULES, หรือ operating habits แบบไหนกำลังมี pattern ซ้ำ ๆ จนควรถูกยกขึ้นมาปรับปรุง

พูดง่าย ๆ: มันไม่ได้ช่วยเขียน feature ในโปรเจกต์โดยตรง แต่ช่วยตอบคำถามแบบนี้ได้ดี:
- `ช่วงนี้เราติด workflow แบบเดิมซ้ำ ๆ ไหม`
- `มี RULES gap อะไรที่ควรถูกเสนอขึ้นมาเป็น proposal`
- `ควรเริ่มคุยหรือวิจัยเรื่องไหนก่อน เพื่อให้การทำงานรอบต่อไปดีขึ้น`

Current checked public surface มีอันเดียว:
- `/memory-context-intelligence:analysis`

Current checked behavior ที่สำคัญ:
- default เป็น **historical-first analysis** ไม่ใช่สรุปเฉพาะ current session
- ใช้ `trace_evidence` เป็น live promotion anchor
- `recall_evidence`, `durable_memory_context`, และ `governance_context` ช่วยเสริมความชัดได้ แต่ไม่แทน trace proof
- ถ้าไม่มี config file ระบบจะโชว์ **guided config helper** แทนการบังคับให้ผู้ใช้จำ raw args

## When to use it

เหมาะเมื่อคุณอยากให้ Claude Code ช่วย review รูปแบบการทำงานย้อนหลังแบบ evidence-first เช่น:
- หลังทำงานมาสักพักแล้ว อยากดูว่า recurring blocker อะไรเริ่มโผล่ซ้ำ
- อยากหา candidate topic สำหรับปรับ RULES / workflow / governance
- อยากได้ historical review ที่กว้างกว่า current session เดียว
- อยากจำกัด source classes หรือ historical depth ด้วย config file โดยไม่เปลี่ยน evidence model หลัก

ไม่ใช่ทางเลือกที่เหมาะถ้าคุณต้องการ:
- แก้โค้ดทันทีโดยไม่สน trace history
- ใช้ bare `/analysis` เป็น public command
- ให้ plugin auto-run เองแบบ background hooks/monitors

## Install Claude Code

ใช้ Claude Code ให้พร้อมก่อน แล้วค่อยติดตั้ง plugin นี้

### Linux / WSL

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Windows PowerShell

```powershell
irm https://claude.ai/install.ps1 | iex
```

### Windows CMD

```batch
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Notes:
- บน native Windows, **Git for Windows เป็น recommended** เพื่อให้ Claude Code ใช้ Bash tool ได้
- ถ้าไม่ได้ติดตั้ง Git for Windows, Claude Code จะ fallback ไปใช้ PowerShell เป็น shell tool
- หลังติดตั้งแล้ว ให้เปิด Claude Code ด้วยคำสั่ง:

```bash
claude
```

ถ้ายังไม่เคย login ให้ทำใน session ด้วย:

```text
/login
```

## Install and load this plugin

Plugin นี้ใน checked scope ปัจจุบันถูกแจกผ่าน **local marketplace ชื่อ `darkwingtm`** ที่ root `TEMPLATE` และ marketplace entry ของมันชี้มาที่ source:
- `./RULES/plugin/memory-context-intelligence`

เพราะฉะนั้น end-user flow ที่ตรงกับ current truth คือ:

### 1) เตรียม local checkout ของ TEMPLATE

คุณต้องมีโฟลเดอร์ `TEMPLATE` อยู่บนเครื่องก่อน โดยใน root ต้องมี `.claude-plugin/marketplace.json`

Portable placeholder:
- `<template-root>` = path ไปยังโฟลเดอร์ `TEMPLATE` บนเครื่องคุณ

ตัวอย่างรูปแบบ path:
- Linux / WSL: `/home/<user>/work/TEMPLATE`
- Windows: `C:\Users\<user>\work\TEMPLATE`

### 2) Add the marketplace

ภายใน Claude Code session ให้เพิ่ม marketplace จาก local path:

```text
/plugin marketplace add <template-root>
```

ถ้าคุณอยากชี้ตรงไปที่ไฟล์ก็ได้:

```text
/plugin marketplace add <template-root>/.claude-plugin/marketplace.json
```

### 3) Install the plugin

```text
/plugin install memory-context-intelligence@darkwingtm
```

Official plugin docs ที่ checked ใน scope นี้บอกว่า direct install command แบบนี้จะลง **user scope by default**

ถ้าคุณต้องการเลือก scope เอง:
- เปิด `/plugin`
- ไปที่ Discover / plugin details
- เลือก `user`, `project`, หรือ `local`

### 4) Reload plugins

```text
/reload-plugins
```

### 5) Verify the install

วิธีเช็คแบบง่ายที่สุดคือ:
- เปิด `/plugin` แล้วดูว่า plugin ถูกติดตั้งและ enabled อยู่
- จากนั้นลองเรียก slash surface ด้านล่างได้เลย

## First use: start with `/memory-context-intelligence:analysis`

### Minimal first run

ใน Claude Code session ที่คุณต้องการวิเคราะห์ ให้พิมพ์:

```text
/memory-context-intelligence:analysis
```

นั่นคือ current checked public entrypoint ที่ควรเริ่มจากมันก่อน

### What you should expect

ถ้า evidence พร้อม คุณจะได้ผลลัพธ์แบบ topic cards เช่น:
- `Topic 1`, `Topic 2`, `Topic 3`
- แต่ละ card อธิบายว่า topic นี้คืออะไร
- ทำไมมันถูกยกขึ้นมาจาก evidence
- ก่อนปรับ / หลังปรับ จะต่างกันอย่างไร
- ตอนนี้เป็นเพียง `candidate only; advisory only; not approved yet`

ท้ายผลลัพธ์จะมี `Next action options` ให้คุณเลือกต่อ เช่น:
- เลือก topic number
- พิมพ์คำขอโดยตรง
- ขอ deep thinking / websearch / webfetch ก่อน

### If no config file is loaded

ถ้า run นี้ยังไม่มี `memory-context-intelligence.config.json` ที่ถูกโหลด คุณควรเห็น **Config helper** ซึ่งจะช่วยถามแนวคิดระดับ operator เช่น:
- จะให้ default scope เป็น historical-default หรือ narrow ลง
- จะเปิด source classes อะไรบ้าง
- จะยอมให้ same-day widening ได้ไหม
- จะ save config เป็น project default หรือใช้ครั้งเดียว

จุดสำคัญ:
- helper นี้เป็น **advisory only**
- plugin **ไม่ auto-write config ให้เอง**
- มันช่วยบอกว่าควรตั้ง policy ยังไง แล้วคุณค่อยเขียนไฟล์เองถ้าต้องการ

## Optional config file

ถ้าคุณอยากควบคุม source policy แบบชัดเจน ให้สร้างไฟล์ชื่อ:

```text
memory-context-intelligence.config.json
```

runtime จะหาไฟล์นี้แบบ **upward discovery** จาก working directory ปัจจุบัน

Example shape:

```json
{
  "analysis": {
    "source_policy": {
      "enabled_source_classes": [
        "trace_evidence",
        "recall_evidence",
        "durable_memory_context",
        "governance_context"
      ],
      "max_historical_shards": 5,
      "allow_same_day_widening": true
    }
  }
}
```

Current checked keys:
- `enabled_source_classes`
- `max_historical_shards`
- `allow_same_day_widening`

Important behavior:
- config file นี้เป็น **late-bound source policy** เท่านั้น
- มันไม่ได้สร้าง evidence class ใหม่
- มันไม่ได้ weaken `trace_evidence` ให้หายไปจาก role เดิมของมัน
- ถ้าคุณปิด `trace_evidence` หรือเหลือแต่ context-only sources ผลลัพธ์ต้องไม่ถูก overclaim ว่าเป็น promotable live candidate

## Boundaries you should know

Current checked boundaries ของ plugin นี้คือ:
- public surface ที่พิสูจน์แล้วมีแค่ `/memory-context-intelligence:analysis`
- bare `/analysis` **ยังไม่ใช่ current proved runtime behavior**
- `/memory-context-intelligence:review` และ `/memory-context-intelligence:packet` ยัง deferred
- `bin/memory-context-intelligence` เป็น internal implementation adapter ไม่ใช่ main user workflow
- plugin-managed auto-flow ยังไม่ถูก claim ว่าพร้อมใช้งาน
- README นี้ไม่ claim external marketplace publication หรือ broad production readiness

พูดง่าย ๆ: ติดตั้งแล้วคุณควรคาดหวัง **analysis command ที่เรียกเองเมื่ออยาก review pattern** ไม่ใช่ plugin ที่แอบรันเองตลอดเวลา

## Troubleshooting

### `/memory-context-intelligence:analysis` ไม่ขึ้นหรือเรียกไม่ได้

เช็กตามลำดับนี้:
1. รัน `/reload-plugins`
2. เปิด `/plugin` แล้วดูว่า plugin ยัง installed + enabled อยู่ไหม
3. เช็กว่า install มาจาก `memory-context-intelligence@darkwingtm`
4. ถ้ายังเพิ่งอัปเดต plugin ระหว่างที่ session เปิดค้างมานาน ให้ restart session แล้วลองใหม่

### `memory-context-intelligence@darkwingtm` ติดตั้งไม่ได้

มักเกิดจาก marketplace path ผิด

เช็กว่า:
- คุณ add marketplace จาก `<template-root>` ที่ถูกต้อง
- root ของ path นั้นมี `.claude-plugin/marketplace.json`
- marketplace entry ของ `memory-context-intelligence` ยังชี้ไปที่ `./RULES/plugin/memory-context-intelligence`

### ได้ผลลัพธ์ว่า blocked / dormant / no-topics

นั่นไม่ได้แปลว่าปลั๊กอินพังเสมอไป

ความหมายทั่วไปคือ:
- `blocked` = input หรือ dependency สำหรับ analysis ยังไม่พร้อม
- `dormant` = memory input ที่มีอยู่อาจ stale เกินไป
- `no-topics` = ยังไม่มี repeated pattern ที่แรงพอจะยกขึ้นมาเป็น proposal

สิ่งที่ควรทำต่อ:
- ทำงานจริงเพิ่มให้มี trace history มากขึ้น
- ลองปรับ source policy / historical depth
- ถ้าต้องการ narrow run ค่อยใช้ scope ที่แคบลงอย่างมีเจตนา

### Session เก่าแล้วพฤติกรรมดูไม่ตรงกับ source ล่าสุด

Current checked contract มี advisory warning ชื่อ `possible stale long-lived session`

ถ้า warning นี้โผล่:
- ให้ restart Claude Code session
- แล้วเรียก `/memory-context-intelligence:analysis` ใหม่

นี่เป็น diagnostic safeguard ชั่วคราว ไม่ใช่การบอกว่า long-lived session mismatch เป็นเรื่องปกติ

## Advanced notes

### Evidence model at a glance

Current implemented evidence model ใช้ 4 classes:
- `trace_evidence`
- `recall_evidence`
- `durable_memory_context`
- `governance_context`

หลักสำคัญคือ:
- `trace_evidence` ยังเป็น live anchor
- source mix ต้องมองเห็นได้ ถ้า durable memory หรือ governance context มีผลต่อ candidate
- historical-first เป็นค่า default แต่ explicit narrowing ยังทำได้เมื่อ operator ต้องการ

### Narrowing runs intentionally

ถ้าคุณต้องการ review slice ที่แคบลง current design ยังรองรับแนวคิดพวกนี้:
- `day=YYYY-MM-DD`
- `session=<id>`
- `lookback=<minutes|hours>`

แต่ current public UX ตั้งใจให้เริ่มจาก slash surface + guided config/helper ก่อน ไม่ใช่ให้ผู้ใช้ต้องจำ raw args เป็น main path

### What this plugin is not

Plugin นี้ไม่ใช่:
- automatic rule writer
- background monitor
- public proof ว่า bare `/analysis` ใช้ได้แล้ว
- shortcut สำหรับข้าม evidence gates
- replacement ของ real work traces

ถ้าคุณอยากใช้มันให้คุ้มที่สุด ให้คิดว่ามันคือ:
- `historical workflow reviewer`
- `RULES / governance topic suggester`
- `evidence-first reflection tool`

## Current truth summary

ถ้าคุณอยากจำสั้น ๆ ให้จำ 5 ข้อนี้:
1. ติดตั้ง Claude Code ก่อน
2. add local marketplace จาก `<template-root>`
3. install `memory-context-intelligence@darkwingtm`
4. run `/reload-plugins`
5. เริ่มใช้ด้วย `/memory-context-intelligence:analysis`

ถ้ารอบแรกยังไม่มี config file ก็ไม่เป็นไร — plugin ควรช่วยถามคุณต่อผ่าน guided config helper แทนการบังคับให้เริ่มจาก raw arguments