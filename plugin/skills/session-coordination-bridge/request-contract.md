# Request Contract

A good shared-board request should answer these questions:

- who is the intended receiver?
- what concrete work is being requested?
- why now?
- what source context matters?
- what counts as done?
- what must be synced back?

## Title guidance

Request-layer form
- `For <session-short-id> owner: <work request>`

Held-owner execution form
- `<session-short-id> owner: <execution task>`

Blocked-owner form
- `Blocked on <session-short-id>: <task>`

## Description guidance

Keep the description compact but complete enough for safe continuation:
- source session or source context
- relevant upstream phase reference if it matters
- what the receiver should inspect first
- done criteria
- sync-back expectation

## Important boundary

Do not use the sender's phase label as the default visible title for the receiver.
If that phase matters, keep it in the description or handoff note.

พูดง่าย ๆ คือ title ใช้บอก request/owner state ส่วน phase ของฝั่งส่งเก็บเป็น context ไม่ใช่ชื่อหลักของงานฝั่งรับ.
