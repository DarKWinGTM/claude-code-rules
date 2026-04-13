# Capability Detection

Optional tooling must be detected before use.

## Detection order

1. shared task list
2. phase / `phase/SUMMARY.md` / `TODO.md`
3. checked implementation state
4. native memory
5. memsearch
6. `claude-peers-mcp`

## memsearch rule

Use memsearch only when:
- stronger coordination surfaces already identified the relevant continuation target
- extra recall detail is still materially useful
- availability has been checked in the current environment

If memsearch is unavailable or the probe step fails:
- fall back immediately to native memory plus checked execution surfaces
- do not turn optional-recall absence into a blocker

## peer-signaling rule

Use `claude-peers-mcp` only when:
- it is actually available now
- direct signaling materially improves the current send / accept / unblock step
- the shared board still remains the visible coordination history

If peer signaling is unavailable:
- keep working through the task list plus checked execution surfaces
- do not block coordination on missing live messaging

## Practical meaning

Availability-first means:
- no assumption from prior sessions
- no assumption from prior machines
- no assumption just because the package design mentions the tool

The current environment decides what can be used now.
