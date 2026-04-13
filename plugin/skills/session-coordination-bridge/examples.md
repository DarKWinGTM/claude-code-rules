# Examples

## Example 1 — request-layer task

Title:
- `For 11c4bd2f owner: verify plugin skill packaging`

Description shape:
- source context: plugin rollout in RULES repo
- inspect first: `plugin/README.md`, `design/rules-plugin-extension.design.md`
- done when: packaging path is verified and sync notes are written back
- sync back: update the shared board and touched governance surfaces

## Example 2 — held-owner execution task

Title:
- `11c4bd2f owner: implement session coordination skill docs`

Meaning:
- the work is already accepted locally
- this is no longer only a request-layer prompt
- the receiver now owns the execution slice

## Example 3 — blocked-owner task

Title:
- `Blocked on 11c4bd2f: confirm plugin install migration`

Meaning:
- the blocked state is visible in the board
- another session can see why the work is waiting
- the task should not disappear just because the blocker is cross-session

## Example 4 — memsearch fallback

Situation:
- receiver wants extra recall detail
- memsearch is not available in the current environment

Correct behavior:
- continue with native memory plus checked execution surfaces
- do not turn the missing optional extension into a coordination stop

## Example 5 — peer signaling optional

Situation:
- `claude-peers-mcp` is available
- a direct signal would help notify another session quickly

Correct behavior:
- use peer signaling as an extra live channel
- still keep the board state updated
- do not let live messages replace visible coordination history
