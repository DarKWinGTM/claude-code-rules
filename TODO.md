# TODO

## 1) ✅ อัปเกรด Design Rules (COMPLETED)
- ✅ ปรับโครงสร้าง design ให้เป็นมาตรฐานเดียวกันทั้งชุด
- ✅ เติมรายละเอียดที่ขาดใน design ที่ยังบาง
- ✅ ยืนยันการอ้างอิงระหว่าง rule ↔ design ให้ครบถ้วน
- ✅ อัปเดต README ให้สะท้อน rules ใหม่ (strict-file-hygiene, document-changelog-control)

## 2) ✅ แผนสร้าง Rules สำหรับ Document Design (COMPLETED)
- ✅ สร้าง `document-changelog-control.md` v4.0 - Version tracking system
- ✅ กำหนดมาตรฐาน **changelog แบบเป็นระบบ** (Version History + Detailed sections)
- ✅ **Single Source of Truth**: ชี้ตำแหน่งไฟล์ changelog หลัก
- ✅ **Design vs Product file distinction**:
  - Design files (`.design.md`): HAVE Version History sections
  - Rules files: NO Version History sections, only version number
- ✅ Session ID: Real UUID from environment (no placeholders)

## 3) 🔄 รออัปเดตขึ้น GitHub Repo
- ⏳ ตรวจรายการไฟล์เปลี่ยนแปลงก่อน push
- ⏳ เตรียม release note สั้นสำหรับ rules ใหม่
- ⏳ Push document-changelog-control.md v4.0

## 4) 📋 Image Gen (รอทำ)
- สร้างภาพสำหรับ `img/strict-file-hygiene.png`
- สร้างภาพสำหรับ `img/document-changelog-control.png`
- อัปเดต README เมื่อภาพพร้อมใช้งาน

## 5) 🔄 อัปเดต Rules เข้า Local Claude Code (IN PROGRESS)
- เป้าหมาย: `~/.claude/rules`
- ขั้นตอน: คัดลอกไฟล์ rules ทั้งหมดที่เปลี่ยนจาก TEMPLATE/RULES
- ไฟล์ที่ต้องอัพเดท:
  - ✅ document-changelog-control.md (v4.0)
  - ✅ README.md (v1.2.0)

## 6) 🆕 อัปเดต Main Design File (PENDING)
- อัพเดท `design/design.md` (main design ของ rules project นี้)
- เพิ่ม Version History สำหรับ project นี้
- บันทึกการเปลี่ยนแปลง v4.0

### ตัวอย่างอ้างอิง
- /home/node/workplace/AWCLOUD/CLAUDE/claude-code-media-generator/design/changelog/changelog.video.md
- /home/node/workplace/AWCLOUD/CLAUDE/claude-code-media-generator/design/changelog/changelog.master.md

---

> **Session**: a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7
> **Last Updated**: 2026-01-20
