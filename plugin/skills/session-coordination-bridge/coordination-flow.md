# Coordination Flow

## Flow A — send work

Need to hand work to another session
  → inspect the current board state first
  → define the work as one request-layer slice
  → keep sender phase context in the description, not as the receiver's title
  → set clear done criteria / sync-back expectation
  → leave the board visible instead of clearing older useful coordination state

## Flow B — receive work

See a request-layer task
  → read the board entry
  → inspect phase / `phase/SUMMARY.md` / `TODO.md` / checked implementation state
  → use memory if continuity detail still helps
  → if extra recall is still needed, check memsearch availability first
  → remap the accepted request into the receiver's own execution structure
  → move into in-progress work

## Flow C — sync back

Execution slice changes state
  → update the board state
  → mark completed / blocked / returned clearly
  → update phase/TODO/docs when durable truth changed
  → keep enough visible history for another session to continue safely

## Request layer vs execution layer

Request layer
- cross-session ask
- visible board handoff
- receiving target made explicit

Execution layer
- receiver's actual task family
- receiver's phase/objective mapping
- checked implementation work

These two layers should connect, but they should not be collapsed into one label.
