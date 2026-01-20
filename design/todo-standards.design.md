# TODO Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-01-20)

---

## 1) Goal (เป้าหมาย)

- สร้างมาตรฐานเดียวกันสำหรับ TODO.md ทั้งหมด
- ทำให้ TODO.md ดูเป็นมืออาชีพ สวยงาม และใช้งานได้จริง
- มีโครงสร้างที่ชัดเจน อ่านง่าย และหาข้อมูลได้รวดเร็ว
- รองรับการ track progress, priority, และ dependencies

---

## 2) Scope (ขอบเขต)

### 2.1 Documents Covered

- TODO.md หลักของ project
- TODO สำหรับ sub-projects หรือ modules

### 2.2 Standards Defined

- File structure and sections
- Visual hierarchy and formatting
- Task categorization
- Priority indicators
- Progress tracking
- Timeline representation
- Professional appearance

---

## 3) Standards (มาตรฐาน)

### 3.1 Document Structure (โครงสร้างเอกสาร)

```markdown
# [Project Name] - TODO

---

## 📊 Project Status Dashboard

[Quick summary: Progress, Active tasks, Blocked items, Upcoming]

---

## 🚀 High Priority (P0)

[Critical tasks that block progress]

---

## 🔥 Active Work (P1)

[Currently being worked on]

---

## 📋 Planned Tasks (P2)

[Backlog, organized by category]

---

## 📅 Timeline & Milestones

[Time-based view]

---

## 🔗 Quick Reference

[Links to related docs]

---

## 📜 History

[History of TODO.md updates and task progression]
```

### 3.2 Visual Hierarchy (ลำดับความสำคัญทางสายตา)

**Use Emojis for Categories:**

| Category | Emoji | Usage |
|----------|-------|-------|
| Dashboard | 📊 | Summary section |
| Critical | 🚨 | Blocking issues |
| High Priority | 🚀 | P0 tasks |
| Active Work | 🔥 | Currently doing |
| Planned | 📋 | Backlog |
| Timeline | 📅 | Time-based |
| Reference | 🔗 | Links |
| History | 📜 | Historical updates |

**Priority Indicators:**

```
P0 - 🚨 Critical (blocks everything)
P1 - 🔥 High (important, do soon)
P2 - 📋 Medium (planned, not urgent)
P3 - 💡 Low (nice to have)
```

**Status Badges:**

```markdown
[IN PROGRESS] - Currently working
[REVIEW] - Awaiting review
[BLOCKED] - Waiting for something
[DONE] - Completed
```

### 3.3 Task Format (รูปแบบ Task)

**⚠️ CRITICAL: All Tasks MUST Have Timestamps**

Every TODO item MUST include:
- **Created:** YYYY-MM-DD (when task was created/defined)
- **Started:** YYYY-MM-DD (optional, when work began)
- **Completed:** YYYY-MM-DD (optional, when finished)

**Standard Format:**

```markdown
### [PRIORITY] [Category] Task Name

**Status:** [STATUS] | **Assigned:** [Who]
**Created:** YYYY-MM-DD | **Started:** YYYY-MM-DD (optional) | **Due:** YYYY-MM-DD

**Description:**
[Brief description of what needs to be done]

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

**Dependencies:**
- Blocks: [task-name]
- Blocked by: [task-name]

**Notes:**
[Additional context, links, etc.]
```

**Examples:**

```markdown
### [P0] [Core] Fix Authentication Bug

**Status:** [IN PROGRESS] | **Assigned:** @darkwingtm
**Created:** 2026-01-20 | **Started:** 2026-01-20 | **Due:** 2026-01-21

**Description:**
Users cannot login with valid credentials due to token validation error.

**Acceptance Criteria:**
- [x] Identify root cause
- [ ] Fix token validation logic
- [ ] Add unit tests
- [ ] Deploy to staging

**Dependencies:**
- Blocks: [P1] User Profile Feature
- Related: [GitHub Issue #123](https://github.com/.../issues/123)

**Notes:**
Found in auth/token_validator.js:142
```

### 3.4 Task Organization (การจัดระเบียบ Task)

**MUST Separate Into Distinct Lists:**

```markdown
## ✅ Completed (เสร็จแล้ว)

Tasks that are 100% done with completion date.

### [P0] [Core] Task Name
**Status:** [DONE] | **Completed:** 2026-01-20
...

---

## 🔄 In Progress (กำลังทำ)

Tasks currently being worked on.

### [P1] [Feature] Task Name
**Status:** [IN PROGRESS] | **Started:** 2026-01-20
...

---

## 📋 Pending (รอดำเนินการ)

Tasks not yet started.

### [P2] [Enhancement] Task Name
**Status:** [PENDING] | **Created:** 2026-01-20
...
```

**Key Principles:**
1. ✅ **Completed** - Top section, finished tasks with **Completed:** date
2. 🔄 **In Progress** - Middle section, active tasks with **Started:** date
3. 📋 **Pending** - Bottom section, planned tasks with **Created:** date only

### 3.5 Progress Tracking (การติดตามความคืบหน้า)

**Section Level Progress:**

```markdown
## 🚀 High Priority (P0)

**Progress:** 2/5 tasks (40%)

### ✅ Completed
- [x] Task A
- [x] Task B

### 🔄 In Progress
- [ ] Task C [IN PROGRESS]

### ⏳ Pending
- [ ] Task D
- [ ] Task E
```

**Overall Dashboard:**

```markdown
## 📊 Project Status Dashboard

| Metric | Value | Target |
|--------|-------|--------|
| Overall Progress | 45% | 100% |
| Total Tasks | 20 | - |
| Completed | 9 | - |
| In Progress | 3 | - |
| Blocked | 1 | - |
| Pending | 7 | - |

**Active Sprint:** Week 3 (2026-01-20 to 2026-01-27)
**Sprint Progress:** 3/8 tasks (38%)
```

### 3.6 Timeline & Milestones (ไทม์ไลน์และเป้าหมาย)

**Timeline Format:**

```markdown
## 📅 Timeline & Milestones

### Q1 2026 (Jan - Mar)

**Week 3 (Jan 20-26)**
- [ ] [P0] Fix authentication bug
- [ ] [P1] Add user profile
- [ ] [P2] Update documentation

**Week 4 (Jan 27 - Feb 2)**
- [ ] [P1] Performance optimization
- [ ] [P2] Database migration

**Milestone: v1.0 Release (Feb 15)**
- [ ] All P0 tasks complete
- [ ] Testing complete
- [ ] Documentation ready
```

---

## 4) Best Practices (แนวปฏิบัติที่ดี)

### 4.1 Writing Style

**DO:**
- ✅ Use clear, concise task names
- ✅ Include acceptance criteria
- ✅ Link to related issues/docs
- ✅ Keep descriptions brief but informative
- ✅ Update status regularly

**DON'T:**
- ❌ Use vague descriptions like "fix stuff"
- ❌ Overload tasks with multiple goals
- ❌ Forget to update completion status
- ❌ Mix categories without clear separation

### 4.2 Maintenance

**Daily:**
- Update task statuses
- Mark completed items

**Weekly:**
- Review priorities
- Update timeline
- Check for blocked items

**Monthly:**
- Archive completed tasks to changelog
- Review overall progress
- Adjust milestones if needed

---

## 5) Examples (ตัวอย่าง)

### 5.1 Minimal TODO (Small Project)

```markdown
# My Project - TODO

## 📊 Status

**Progress:** 3/5 tasks (60%)

## 🔥 Active

- [ ] [P1] Add login feature [IN PROGRESS]
- [ ] [P1] Write tests

## 📋 Planned

- [ ] [P2] Update docs
- [ ] [P2] Add dark mode

## ✅ Done

- [x] [P0] Setup project

---

> Session: uuid | Updated: 2026-01-20
```

### 5.2 Full TODO (Large Project)

```markdown
# RULES System - TODO

---

## 📊 Project Status Dashboard

| Metric | Value | Target |
|--------|-------|--------|
| Overall Progress | 45% | 100% |
| Total Tasks | 20 | - |
| Completed | 9 | - |
| In Progress | 3 | - |
| Blocked | 1 | - |

**Active Sprint:** v4.0 Development (2026-01-20 to 2026-01-27)

---

## 🚨 Critical Issues (P0)

**Progress:** 1/2 tasks (50%)

### [P0] [Core] Fix History Format

**Status:** [IN PROGRESS] | **Assigned:** @ai-assistant | **Due:** 2026-01-20

**Description:**
History section needs to follow proper format with timestamps.

**Acceptance Criteria:**
- [x] Identify that History section is different from Changelog
- [ ] Update History section format in TODO.md
- [ ] Verify format follows standards

**Dependencies:**
- Blocks: [P1] README Update
- Related: [design/document-design-control.design.md](design/document-design-control.design.md)

---

## 🔥 Active Work (P1)

### [P1] [Docs] Update README with New Rules

**Status:** [BLOCKED] | **Blocked by:** History format update

### [P1] [Design] Create Image Generation Prompts

**Status:** [IN PROGRESS] | **Assigned:** @ai-assistant

---

## 📋 Planned Tasks (P2)

### [P2] [Enhancement] Design Templates

Create template files for new design documents.

### [P2] [Automation] Validation Script

Script to verify design document compliance.

---

## 📅 Timeline

**Week 3 (2026-01-20 to 2026-01-26)**
- [ ] [P0] Fix changelog format
- [ ] [P1] Update README
- [ ] [P1] Generate images

**Week 4 (2026-01-27 to 2026-02-02)**
- [ ] [P2] Create templates
- [ ] [P2] Write validation script

---

## 🔗 Quick Reference

- [Design Docs](./design/)
- [History Section](#️-history)
- [GitHub Issues](https://github.com/.../issues)

---

## 📜 History

| Date | Changes |
|------|---------|
| 2026-01-20 | Added P0 changelog fix task |
| 2026-01-20 | Restructured to professional format |

---

> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7
> **Last Updated:** 2026-01-20
```

---

## 6) Quality Metrics (ตัวชี้วัด)

| Metric | Target | Notes |
|--------|--------|-------|
| Clear structure | 100% | All sections present |
| Priority indicators | 100% | All tasks have P0-P3 |
| **Timestamp compliance** | **100%** | **All tasks have Created/Started/Completed dates** |
| Status separation | 100% | Completed / In Progress / Pending clearly separated |
| Progress tracking | Active | Regularly updated |
| Dependencies tracked | Yes | When applicable |
| Professional appearance | High | Clean formatting |

---

## 7) Related Documents (เอกสารที่เกี่ยวข้อง)

- [document-design-control.md](../document-design-control.md) - Design standards
- [document-changelog-control.md](../document-changelog-control.md) - Version tracking

---

## 8) Research References & Industry Best Practices (ข้อมูลอ้างอิงและแนวปฏิบัติที่ดีจากอุตสาหกรรม)

> **Sources:** Web search on professional TODO list best practices (2026-01-20)

### 8.1 Task Format Best Practices (รูปแบบ Task ที่ดี)

**Verb + Noun Pattern:**
```
✅ Good: "Implement login feature"
✅ Good: "Fix authentication bug"
✅ Good: "Write unit tests"

❌ Avoid: "Login stuff"
❌ Avoid: "Fix things"
```

**Actionable Tasks:**
- Use specific, measurable verbs
- Include acceptance criteria
- Break down large tasks into smaller ones
- Each task should be completable in one session

**Sources:**
- [A Better To-Do List, According to a Scrum Master - Medium](https://forge.medium.com/how-to-stay-on-track-to-reach-your-goals-70d90cfc95c3)
- [How to Write a To-Do List That's Actionable AF - Work Brighter](https://workbrighter.co/actionable-to-do-list)

### 8.2 Prioritization Techniques (เทคนิคการจัดลำดับความสำคัญ)

**Eisenhower Matrix:**
```
┌─────────────────┬─────────────────┐
│  Urgent          │  Urgent          │
│  + Important     │  + Not Important │
│  (DO FIRST)      │  (DELEGATE)      │
├─────────────────┼─────────────────┤
│  Not Urgent      │  Not Urgent      │
│  + Important     │  + Not Important │
│  (SCHEDULE)      │  (ELIMINATE)     │
└─────────────────┴─────────────────┘
```

**80/20 Rule (Pareto Principle):**
- 20% of features deliver 80% of impact
- Identify high-value items and prioritize them

**Priority Levels (Industry Standard):**
- **P0** - Critical/Blocking: Must do now
- **P1** - High: Important, do soon
- **P2** - Medium: Planned, not urgent
- **P3** - Low: Nice to have

**Sources:**
- [Avoid the "Urgency Trap" with the Eisenhower Matrix - Todoist](https://www.todoist.com/productivity-methods/eisenhower-matrix)
- [Product Backlog Prioritization Techniques - Scrum.org](https://www.scrum.org/resources/blog/product-backlog-prioritization-techniques)
- [9 tips for an effective to-do list format - Zapier](https://zapier.com/blog/effective-to-do-list-format)

### 8.3 Agile & Scrum Best Practices (แนวปฏิบัติ Agile/Scrum)

**Sprint Backlog Essentials:**
- Clearly defined sprint goals
- Understanding of team capacity
- Prioritized set of backlog items

**20-30-50 Rule for Backlog:**
- **20%** - Ready for development immediately
- **30%** - No external inputs needed, can design
- **50%** - High-level ideas for discussion

**Backlog Refinement:**
- Should take 10% of total sprint length
- Regular review and prioritization

**Sources:**
- [What Is a Sprint Backlog? - Atlassian](https://www.atlassian.com/agile/project-management/sprint-backlog)
- [How to Prioritize Agile Backlog with 20-30-50 Rule - LinkedIn](https://www.linkedin.com/posts/jayita-dey_the-20-30-50-rule-in-agile-agile-projects-activity-7352999545569464320--_fX)
- [7 Best Practices for Sprint Backlog Management in Agile](https://vlajkoknezic.com/articles/sprint-backlog)

### 8.4 Progress Tracking Metrics (ตัวชี้วัดความคืบหน้า)

**Essential Metrics:**
| Metric | Purpose | Industry Standard |
|--------|---------|-------------------|
| Completion Rate | Track progress | % completed |
| Cycle Time | Speed of delivery | Days from start to done |
| Blockers | Identify issues | Count of blocked items |
| Velocity | Team capacity | Tasks completed per sprint |

**Status Tracking:**
- **Completed** - 100% done with completion date
- **In Progress** - Actively being worked on
- **Blocked** - Waiting for dependencies
- **Pending** - Not started yet

**Sources:**
- [Sprint Backlog Essentials - Parabol](https://www.parabol.co/blog/sprint-backlog-essentials)
- [The Ultimate Agile Sprint Planning Guide - EasyAgile](https://www.easyagile.com/blog/agile-sprint-planning)

### 8.5 GitHub-Specific Best Practices (แนวปฏิบัติเฉพาะสำหรับ GitHub)

**Markdown Task Lists:**
```markdown
- [ ] Unfinished task
- [x] Completed task
```

**GitHub Issues for Tracking:**
- Use Issues for bugs and features
- Include labels, milestones, and assignees
- Link commits to issues with keywords

**Project Boards:**
- Kanban-style columns (To Do, In Progress, Done)
- Automated workflows
- Template repositories for consistency

**Sources:**
- [About tasklists - GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists)
- [GitHub Issues · Project planning for developers](https://github.com/features/issues)
- [How to use GitHub for project management - Graphite](https://graphite.com/guides/github-project-management-guide)

### 8.6 Key Insights Summary (สรุปข้อควรค้นพบ)

**From Industry Research:**

1. **Actionable Tasks** - Use verb + noun format, be specific
2. **Time Constraints** - Include due dates and timestamps
3. **Regular Review** - Update status daily, review weekly
4. **Clear Priorities** - Use P0-P3 or Eisenhower Matrix
5. **Progress Visibility** - Dashboard with metrics
6. **Sprint Goals** - Clear objectives for each period
7. **Capacity Planning** - Understand team velocity
8. **Blocked Items** - Track and resolve quickly

**Common Pitfalls to Avoid:**
- ❌ Vague task descriptions ("do stuff")
- ❌ Missing due dates
- ❌ No priority levels
- ❌ Everything is P0 (lack of prioritization)
- ❌ Forgetting to update status
- ❌ Not tracking blockers

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-01-20 | **Fix: Rename Changelog to History** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Changed section name from Changelog to History | |
| | | - Updated emoji from 📝 to 📜 | |
| | | - Clarified purpose: History tracks TODO updates, not software changes | |
| | | - Updated all references throughout design document | |
| | | Summary: History section for TODO.md progression tracking | |
| 1.1 | 2026-01-20 | **Add: Research References & Industry Best Practices** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added Section 8: Research from web search | |
| | | - Task Format Best Practices (verb + noun pattern) | |
| | | - Prioritization Techniques (Eisenhower Matrix, 80/20 rule) | |
| | | - Agile & Scrum Best Practices (20-30-50 rule) | |
| | | - Progress Tracking Metrics (industry standards) | |
| | | - GitHub-Specific Best Practices (markdown, issues, projects) | |
| | | - Key Insights Summary & Common Pitfalls | |
| | | Summary: Added industry research to support design decisions | |
| 1.0 | 2026-01-20 | **Initial version** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Created comprehensive TODO standards | |
| | | - Defined document structure with sections | |
| | | - Added visual hierarchy (emojis, priorities, status) | |
| | | - Specified task format with metadata | |
| | | - Created progress tracking standards | |
| | | - Added timeline & milestones format | |
| | | - Provided minimal and full examples | |
| | | - Defined best practices and maintenance routines | |
| | | Summary: Professional TODO standards with clear structure | |

> Full history: [todo-standards.changelog.md](changelog/todo-standards.changelog.md)
