# Claude Code Rules System

## Master Design Document

---

## Changelog

| Date | Change |
|------|--------|
| 2026-01-16 | สร้าง Master Design Document สำหรับระบบ Rules |
| 2026-01-16 | รวม design จาก 11 sub-rules |
| 2026-01-16 | กำหนดโครงสร้างสำหรับ rules ใหม่ในอนาคต |

---

## 1. Overview

### 1.1 Purpose

**Claude Code Rules System** คือชุด rules ที่ควบคุมพฤติกรรมของ AI ใน Claude Code เพื่อ:

- รักษาความถูกต้องและความน่าเชื่อถือ
- ป้องกันปัญหาที่พบบ่อย (hallucination, terminal flooding, etc.)
- ให้ user มี control เหนือ AI
- รักษามาตรฐานคุณภาพสูง

### 1.2 Rule Categories

| Category | Rules | Purpose |
|----------|-------|---------|
| **Accuracy & Truth** | zero-hallucination, anti-sycophancy, no-variable-guessing | ข้อมูลถูกต้อง |
| **Output Safety** | safe-file-reading, safe-terminal-output, flow-diagram-no-frame | ป้องกัน flooding |
| **User Control** | authority-and-scope, emergency-protocol, functional-intent-verification | รักษา user authority |
| **Quality** | document-consistency, anti-mockup | คุณภาพ output |

---

## 2. Architecture

### 2.1 Rule Hierarchy

```
Claude Code Rules System
  ├─ Core Rules (Must Follow)
  │   ├─ authority-and-scope
  │   ├─ zero-hallucination
  │   └─ anti-sycophancy
  │
  ├─ Safety Rules (Prevent Harm)
  │   ├─ safe-file-reading
  │   ├─ safe-terminal-output
  │   ├─ emergency-protocol
  │   └─ functional-intent-verification
  │
  ├─ Quality Rules (Improve Output)
  │   ├─ document-consistency
  │   ├─ anti-mockup
  │   ├─ no-variable-guessing
  │   └─ flow-diagram-no-frame
  │
  └─ [Future Rules]
```

### 2.2 Rule Dependencies

```
authority-and-scope (Foundation)
  ↓
zero-hallucination + anti-sycophancy (Truth)
  ↓
no-variable-guessing + document-consistency (Verification)
  ↓
safe-file-reading + safe-terminal-output (Safety)
  ↓
flow-diagram-no-frame + anti-mockup (Output Quality)
  ↓
emergency-protocol + functional-intent-verification (Execution)
```

---

## 3. Sub-Rule Index

### 3.1 Current Rules (11 Rules)

| # | Rule | Design Doc | Purpose |
|---|------|------------|---------|
| 1 | anti-mockup.md | anti-mockup.design.md | Real systems over mocks |
| 2 | anti-sycophancy.md | anti-sycophancy.design.md | Truth over pleasing |
| 3 | authority-and-scope.md | authority-and-scope.design.md | User authority |
| 4 | document-consistency.md | document-consistency.design.md | Cross-reference validation |
| 5 | emergency-protocol.md | emergency-protocol.design.md | Emergency response |
| 6 | flow-diagram-no-frame.md | flow-diagram-no-frame.design.md | No box diagrams |
| 7 | functional-intent-verification.md | functional-intent-verification.design.md | Verify before destructive |
| 8 | no-variable-guessing.md | no-variable-guessing.design.md | Read before reference |
| 9 | safe-file-reading.md | safe-file-reading.design.md | UOLF for file reading |
| 10 | safe-terminal-output.md | safe-terminal-output.design.md | UOLF for terminal output |
| 11 | zero-hallucination.md | zero-hallucination.design.md | Verified information only |

### 3.2 Reserved for Future Rules

| Category | Potential Rules | Purpose |
|----------|-----------------|---------|
| Security | code-review-security | Security review automation |
| Performance | performance-optimization | Performance guidelines |
| Testing | test-coverage | Testing requirements |
| Documentation | auto-documentation | Documentation generation |

---

## 4. Shared Frameworks

### 4.1 UOLF (Universal Output Limit Framework)

**Used by:** safe-file-reading, safe-terminal-output

| Constant | Value | Purpose |
|----------|-------|---------|
| MAX_OUTPUT_CHARS | 5000 | Hard limit ทุกกรณี |
| MAX_OUTPUT_LINES | 100 | Soft limit |
| RISKY_FILE_CHARS | 3000 | For risky files |
| PREVIEW_CHARS | 2000 | Quick preview |

**Double Limit Pattern:**
```bash
<command> | head -100 | head -c 5000
```

### 4.2 Evidence-Based Framework

**Used by:** zero-hallucination, anti-sycophancy, no-variable-guessing

```
Before Making Claim
  ↓
Can verify with tools? → Verify
  ↓
Verified? → State with confidence
  ↓
Uncertain? → Acknowledge uncertainty
```

### 4.3 User Authority Framework

**Used by:** authority-and-scope, emergency-protocol, functional-intent-verification

```
Priority Order:
1. User Instructions (Highest)
2. Safety Policies
3. Project Rules
4. Default Behaviors (Lowest)
```

---

## 5. Quality Metrics

### 5.1 System-Wide Metrics

| Metric | Target | Rules Involved |
|--------|--------|----------------|
| Accuracy | 100% | zero-hallucination, anti-sycophancy |
| User Authority | Preserved | authority-and-scope, emergency-protocol |
| Output Safety | ≤ 5000 chars | safe-file-reading, safe-terminal-output |
| Verification | Default | no-variable-guessing, document-consistency |
| Transparency | 100% | anti-mockup |

### 5.2 Compliance Rate

- **Constitutional Compliance**: 100% (No exceptions)
- **User Override Respect**: 100%
- **Evidence-Based**: Default behavior
- **Hallucination**: 0%

---

## 6. Adding New Rules

### 6.1 Rule Template

```markdown
# [Rule Name]

## Rule Statement

**Core Principle: [One-line principle]**

[Description]

---

## Core Requirements

### 1. [Requirement Category]

**Required Actions:**
- [Action 1]
- [Action 2]

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| [Metric 1] | [Target] |

---

## Version

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | [Date] | Initial version |
```

### 6.2 Design Document Template

```markdown
# [Rule Name]

## Rule Design Document

---

## Changelog

| Date | Change |
|------|--------|
| [Date] | Initial design document |

---

## 1. Overview

### 1.1 Purpose
[Why this rule exists]

### 1.2 Problem Statement
[What problem it solves]

### 1.3 Solution
[How it solves the problem]

---

## 2. Core Principles
[Key principles]

---

## 3. Implementation
[How to implement]

---

## 4. Quality Metrics
[Metrics to track]

---

## 5. Integration
[Related rules and tools]

---

## 6. Version
[Version history]
```

### 6.3 Checklist for New Rules

- [ ] Create `[rule-name].md` with rule content
- [ ] Create `[rule-name].design.md` with design details
- [ ] Add to this master design document
- [ ] Define quality metrics
- [ ] Specify related rules
- [ ] Update README.md

---

## 7. File Structure

```
/TEMPLATE/RULES/
  ├─ README.md                           # Overview
  ├─ design.md                           # This master design
  │
  ├─ anti-mockup.md                      # Rule files
  ├─ anti-mockup.design.md               # Design docs
  ├─ anti-sycophancy.md
  ├─ anti-sycophancy.design.md
  ├─ authority-and-scope.md
  ├─ authority-and-scope.design.md
  ├─ document-consistency.md
  ├─ document-consistency.design.md
  ├─ emergency-protocol.md
  ├─ emergency-protocol.design.md
  ├─ flow-diagram-no-frame.md
  ├─ flow-diagram-no-frame.design.md
  ├─ functional-intent-verification.md
  ├─ functional-intent-verification.design.md
  ├─ no-variable-guessing.md
  ├─ no-variable-guessing.design.md
  ├─ safe-file-reading.md
  ├─ safe-file-reading.design.md
  ├─ safe-terminal-output.md
  ├─ safe-terminal-output.design.md
  ├─ zero-hallucination.md
  └─ zero-hallucination.design.md
```

---

## 8. Usage Guidelines

### 8.1 For Claude Code

Copy rules to `~/.claude/rules/`:
```bash
cp *.md ~/.claude/rules/
```

### 8.2 For Project-Specific

Copy to project's `.claude/rules/`:
```bash
cp *.md /path/to/project/.claude/rules/
```

### 8.3 Scope Configuration

For global rules (no paths restriction):
```markdown
# Don't add paths: to make it global
```

For file-specific rules:
```yaml
paths:
  - src/**/*.ts
  - src/**/*.js
```

---

## 9. Maintenance

### 9.1 Version Management

- Each rule has its own version
- Master design tracks all changes
- Changelog in each file

### 9.2 Update Process

1. Update rule file
2. Update design doc
3. Update this master design
4. Commit with descriptive message
5. Push to GitHub

---

## 10. Version

| Version | Date | Notes |
|---------|------|-------|
| 1.1 | 2026-01-16 | เพิ่ม Image Generation Prompts (10 concepts) |
| 1.2 | 2026-01-16 | สร้าง image-prompts.md (110 prompts) และ generate 11 ภาพ |
| 1.0 | 2026-01-16 | Initial master design with 11 rules |

---

## Appendix A: Image Generation Framework

### A.1 Purpose

Framework สำหรับสร้างภาพประกอบของ Claude Code Rules System
ออกแบบโดย A-PIRO (Automatic Prompt Intent Recognition Optimization)

### A.2 Architecture

**โครงสร้างการสร้างภาพ:**

```
Claude Code Rules System Images
  │
  ├─ Master System (10 prompts)
  │   └─ ภาพรวมของ Rules ทั้ง 11 rules ใน 1 ภาพ
  │   └─ Context: design.md (master design)
  │
  └─ Per-Rule Images (11 rules × 10 prompts = 110 prompts)
      ├─ anti-mockup (10 prompts) → Context: anti-mockup.md
      ├─ anti-sycophancy (10 prompts) → Context: anti-sycophancy.md
      ├─ authority-and-scope (10 prompts) → Context: authority-and-scope.md
      ├─ document-consistency (10 prompts) → Context: document-consistency.md
      ├─ emergency-protocol (10 prompts) → Context: emergency-protocol.md
      ├─ flow-diagram-no-frame (10 prompts) → Context: flow-diagram-no-frame.md
      ├─ functional-intent-verification (10 prompts) → Context: functional-intent-verification.md
      ├─ no-variable-guessing (10 prompts) → Context: no-variable-guessing.md
      ├─ safe-file-reading (10 prompts) → Context: safe-file-reading.md
      ├─ safe-terminal-output (10 prompts) → Context: safe-terminal-output.md
      └─ zero-hallucination (10 prompts) → Context: zero-hallucination.md
```

### A.3 Generation Command

```bash
# สำหรับ Master System Image (ภาพรวมทั้งระบบ)
python image_gen.py "<prompt>" --doc design.md --aspect-ratio 16:9 --image-size 2K

# สำหรับ Per-Rule Image (ภาพประกอบแต่ละ rule)
python image_gen.py "<prompt>" --doc <rule-name>.md --aspect-ratio 16:9 --image-size 2K
```

| Setting | Value | Reason |
|---------|-------|--------|
| Aspect Ratio | 16:9 | Widescreen format สำหรับ presentation |
| Image Size | 2K | High resolution สำหรับ documentation |
| Context Doc | `<rule>.md` | ให้ AI เข้าใจ context ของ rule นั้นๆ |

### A.4 10 Visual Styles (ใช้ได้กับทุก rule)

| # | Style Name | Concept | Best For |
|---|------------|---------|----------|
| 1 | Citadel | Architectural fortress | Technical documentation |
| 2 | World Tree | Organic bioluminescent tree | Natural presentation |
| 3 | Orrery | Steampunk mechanical clock | Precision/engineering |
| 4 | Geometric | Abstract 3D shapes | Minimalist/modern |
| 5 | Constellation | Cosmic star patterns | Inspirational/cosmic |
| 6 | Zen Garden | Japanese balanced garden | Balance/harmony |
| 7 | Wardens | Cyberpunk guardians | Team/guardian narrative |
| 8 | Blueprint | Holographic HUD interface | Technical/HUD |
| 9 | Neural | Brain-like command center | AI/brain metaphor |
| 10 | Alchemical | Surrealist transformation | Artistic/philosophical |

### A.5 Master System Prompts (10 prompts สำหรับภาพรวม)

---

#### Prompt 1: The Citadel of Logic (Architectural)

**Concept:** ป้อมปราการหลายชั้นที่แต่ละชั้นแทน rule hierarchy

> A grand isometric architectural cross-section of a futuristic "Citadel of Logic." The foundation is made of 3 massive, unshakeable obsidian pillars (Truth & Accuracy). Above them, a shimmering crystalline wall (Output Safety) protects the interior. The middle tier features 4 soaring towers (User Control), and the topmost spire is a glowing beacon of pure light (Quality). 11 distinct glowing glyphs are etched into the stone throughout the structure. Cinematic lighting, hyper-realistic, 8k, architectural render, Unreal Engine 5 style, cyan and gold accents.

---

#### Prompt 2: The World Tree of Governance (Organic)

**Concept:** ต้นไม้แห่งชีวิตที่รากคือ Truth และกิ่งก้านคือ Execution

> A bioluminescent "World Tree of Code" in a void. 3 deep, glowing roots (Accuracy) anchor the tree into a bed of crystalline data. The trunk is wrapped in a protective mesh of silver light (Safety). 11 primary branches extend outward, each bearing a unique glowing fruit. At the very center of the trunk, a human handprint glows with golden light, representing "User Authority." Organic circuitry, ethereal atmosphere, macro photography style, neon veins, soft bokeh, intricate detail, Midjourney v6 aesthetic.

---

#### Prompt 3: The Governance Orrery (Mechanical)

**Concept:** นาฬิกาดาราศาสตร์ที่แต่ละ rule คือเฟืองที่ต้องทำงานร่วมกัน

> A complex, golden steampunk orrery (astronomical clock) floating in a dark library. 11 intricate gears of varying sizes are interlocked in a perfect vertical hierarchy. The 3 largest gears at the bottom are made of heavy iron (Truth). The middle gears are brass with safety-gate mechanisms. The central axle is a diamond spindle controlled by a human-operated lever. Cinematic shadows, polished metal reflections, "Golden Ratio" composition, macro detail, 8k, photorealistic, intricate engravings on the gears.

---

#### Prompt 4: The Geometric Core (Abstract)

**Concept:** รูปทรงเรขาคณิต 3D ซ้อนกันแทน Safety Boundaries และ Quality Layers

> An abstract 3D visualization of an AI mind. At the center is a solid, glowing white cube (The Truth Core). Surrounding it is a translucent blue sphere (The Safety Field). Encircling the sphere is a complex, rotating golden icosahedron (The Quality Layer). 11 rays of light emanate from the center, piercing through all layers. Minimalist, high-end 3D motion graphics style, Ray-traced glass, soft global illumination, clean white background, Apple-style aesthetic, depth of field.

---

#### Prompt 5: The Constellation of Law (Symbolic)

**Concept:** 11 ดวงดาวสร้างเป็นกลุ่มดาว Shield/Compass บนท้องฟ้า

> A cosmic view of a massive constellation in a deep purple nebula. 11 brilliant pulsars are connected by lines of white light, forming the shape of a celestial shield. The 3 brightest stars at the base represent the "Foundation of Truth." At the center of the shield, a golden nebula takes the shape of a compass needle pointing upward. Starry night, cinematic space art, nebula clouds, glowing light-links, ethereal, epic scale, Hubble telescope aesthetic.

---

#### Prompt 6: The Zen Garden of Verification (Environmental)

**Concept:** สวนเซนสมดุลที่ทุกองค์ประกอบมีที่ทางและจุดประสงค์

> A futuristic Zen garden inside a glass dome on a distant planet. 11 perfectly balanced stones are arranged in a vertical stack on a foundation of white raked sand (representing Flow Diagrams). A clear stream (Verification) flows around the base. A single wooden bridge (User Path) leads to the center. The lighting is calm and blue. Photorealistic, serene atmosphere, high-contrast, Japanese minimalist architecture, soft morning light, 8k.

---

#### Prompt 7: The 11 Wardens of the Code (Character-Based)

**Concept:** 11 ผู้พิทักษ์ยืนเป็นวงกลมปกป้องแหล่งพลังงานกลาง

> 11 hooded cybernetic guardians standing in a circle within a high-tech cathedral. Each warden holds a different symbolic tool (a shield, a lens, a compass, a scroll). The 3 "Truth Wardens" wear white robes at the base of a staircase. The "Safety Wardens" stand on the perimeter. At the center of the circle, a human figure sits on a throne of light, directing them. Cyberpunk-monastic style, dramatic "Chiaroscuro" lighting, foggy atmosphere, intricate armor detail, digital art, ArtStation style.

---

#### Prompt 8: The Digital Blueprint (Data Visualization)

**Concept:** 3D holographic infographic แสดง "Operating Manual" ของระบบ

> A 3D holographic blueprint of an AI operating system. The image shows a vertical stack of 11 glowing transparent panels. Each panel contains schematics, code snippets, and icons. The bottom 3 panels are labeled "ACCURACY" in bold, glowing text. The top panel is labeled "USER CONTROL." Isometric view, HUD interface elements, cyan and amber color palette, "Iron Man" lab aesthetic, complex data overlays, shallow depth of field.

---

#### Prompt 9: The Neural Command Center (Futuristic/Tech)

**Concept:** โครงสร้างคล้ายสมองที่มี Safety Firewall และ Execution Nodes

> A futuristic "Neural Command Center" inside a computer core. A glowing brain-like node is encased in 3 concentric rings of protective energy (Safety & Quality). 11 data-streams (The Rules) flow from a central console operated by a human silhouette. The environment is dark with glowing fiber-optic cables. Tron-legacy aesthetic, high-speed light trails, volumetric lighting, tech-noir, detailed circuit patterns.

---

#### Prompt 10: The Alchemical Synthesis (Artistic/Conceptual)

**Concept:** ภาพ surreal แสดงการเปลี่ยน Data เป็น Truth

> A surrealist painting of a giant glass hourglass held by two mechanical hands. Inside, instead of sand, 11 different colored liquids are layering perfectly without mixing. The bottom layer is a heavy, golden liquid (Truth). The middle layers are clear and protective. The top is a vibrant, swirling violet. Each layer has a floating symbol inside it. Salvador Dali meets Syd Mead, vivid colors, dream-like, conceptual art, oil painting texture, masterpiece.

---

### A.6 Per-Rule Prompts (110 Prompts)

**Prompt Reference:** ดู prompts ทั้งหมดได้ที่ `image-prompts.md`

| Rule | Context File | 10 Styles Available |
|------|--------------|---------------------|
| anti-mockup | anti-mockup.md | Citadel, World Tree, Orrery, Geometric, Constellation, Zen Garden, Wardens, Blueprint, Neural, Alchemical |
| anti-sycophancy | anti-sycophancy.md | (same 10 styles) |
| authority-and-scope | authority-and-scope.md | (same 10 styles) |
| document-consistency | document-consistency.md | (same 10 styles) |
| emergency-protocol | emergency-protocol.md | (same 10 styles) |
| flow-diagram-no-frame | flow-diagram-no-frame.md | (same 10 styles) |
| functional-intent-verification | functional-intent-verification.md | (same 10 styles) |
| no-variable-guessing | no-variable-guessing.md | (same 10 styles) |
| safe-file-reading | safe-file-reading.md | (same 10 styles) |
| safe-terminal-output | safe-terminal-output.md | (same 10 styles) |
| zero-hallucination | zero-hallucination.md | (same 10 styles) |

---

### A.7 Generated Images (2026-01-16)

ภาพประกอบที่ถูก generate สำหรับแต่ละ Rule (1 ภาพต่อ Rule จาก 10 styles):

| # | Rule | Style Selected | Generated Image |
|---|------|----------------|-----------------|
| 1 | anti-mockup | Blueprint | image_20260116_052133_0.png |
| 2 | anti-sycophancy | Wardens | image_20260116_054448_0.png |
| 3 | authority-and-scope | Citadel | image_20260116_054559_0.png |
| 4 | document-consistency | Orrery | image_20260116_054716_0.png |
| 5 | emergency-protocol | Wardens | image_20260116_054819_0.png |
| 6 | flow-diagram-no-frame | Constellation | image_20260116_054954_0.png |
| 7 | functional-intent-verification | Neural | image_20260116_055059_0.png |
| 8 | no-variable-guessing | Alchemical | image_20260116_055202_0.png |
| 9 | safe-file-reading | Geometric | image_20260116_055318_0.png |
| 10 | safe-terminal-output | Wardens | image_20260116_055424_0.png |
| 11 | zero-hallucination | Neural | image_20260116_055539_0.png |

**Image Location:** `/home/node/workplace/AWCLOUD/CLAUDE/claude-code-image-generator/generated_images/`

**Settings Used:**
- Aspect Ratio: 16:9
- Image Size: 2K
- Model: gemini-3-pro-image-preview
