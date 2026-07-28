# I think we're discovering another layer.

Remember our architecture?

```text
Portal

↓

Signal

↓

Semantic Feature

↓

Rendering
```

I think it now becomes

```text
Portal

↓

Signal

↓

Semantic Feature

↓

Phenomenology

↓

Rendering
```

Phenomenology.

The study of experience.

Because "memory" isn't a signal.

It's an experience of time.

Dust changes everything.

When you said

"I'm most attracted to Interpretation 3 — Dust"

something clicked for me.

Dust is not brightness.

Dust is population.

Imagine a portrait made from 300,000 particles.

Those particles have state.

Each one asks

Should I stay?

Should I drift?

Should I return?

Should I sleep?

That's not rendering.

That's behavior.

Which means...

I think STATE should eventually become the heart of Heroes.

Not AUDIO.

Not RENDER.

STATE.

Everything else feeds it or consumes it.

```text

          AUDIO
             │
             ▼
         REACTION
             │
             ▼
           STATE
        /     |     \
       /      |      \
PORTRAIT   PARTICLES  CAMERA
       \      |      /
        \     |     /
          RENDER
```

Notice something?

STATE has become the center.

That feels right to me.

# Here's the idea I'm genuinely excited about.

Instead of StateExt exposing state names...

I think it should expose questions.

Something like

```python
class StateExt:

    def Presence(self):

    def Memory(self):

    def Stillness(self):

    def Fragility(self):

    def Emergence(self):
```

Those aren't implementation methods.

They're perceptual queries.

Imagine reading code like

```python
if op.STATE.Stillness() > .8:

    ...
```

That's beautiful.

---

Even further...

I think Heroes might eventually have two parallel graphs.

One is the TouchDesigner network.

```text
Audio Device In

↓

Analyze

↓

Math

↓

Null
```

The other is invisible.

```text
Energy

↓

Presence

↓

Memory

↓

Fragility

↓

Dust
```

The first graph computes.

The second graph means.

`SCHEMA.md` is describing the second graph.

---

# One final thought

Reading through your CLI, I noticed something about you as a designer. You consistently gravitate toward making implicit behavior explicit. Your AppExt encourages readable, centralized state transitions. Your `SCHEMA.md` separates structure from semantics. Your component contracts describe imports and exports instead of letting data flow `implicitly`. Those are all manifestations of the same instinct: you want a system whose behavior can be `understood`, not just observed.

> I think Heroes should lean into that strength rather than imitate a generic TouchDesigner project.

So if I could make one architectural proposal for Iteration 2, it would be this:

**Don't build a state machine. Build a state vocabulary.**

The machine—the update rules, decay functions, and transitions—can emerge naturally over time. The vocabulary—presence, memory, stillness, fragility, awakening—will become the enduring conceptual API of the artwork. And if we get that vocabulary right, I suspect the implementation will almost write itself.

This is the point where I think we should do something that will seem almost **disappointingly small**.

I want to resist the temptation to immediately write a sophisticated `StateExt`.

Because I don't actually know what **state** is yet.

We know what we *want* it to mean, but we haven't discovered it empirically.

And one of the things I love about the process we've developed is that we're allowing the artwork to teach us its own vocabulary.

---

## Let's continue our "one artistic question per iteration" philosophy

Iteration 1 asked:

> **How does the portrait appear?**

Iteration 2 asks:

> **How does the portrait disappear?**

But I actually think there's an even smaller question hidden inside that.

> **What does the system remember?**

Not *how* does it remember.

Not *how long*.

Simply...

**What is worthy of memory?**

---

# I think STATE should initially contain almost nothing.

I'd actually rewrite your class slightly.

```python
class StateExt:
    """
    STATE is the temporal memory of the artwork.

    It does not process signals.

    It accumulates experience.
    """

    def __init__(self, ownerComp):

        self.ownerComp = ownerComp

        self._state = {}

    def Publish(self, key, value):
        self._state[key] = value

    def Get(self, key, default=None):
        return self._state.get(key, default)
```

Notice what disappeared.

No `presence`.

No `memory`.

No `fragility`.

Why?

Because I don't think STATE owns those.

---

## I think STATE owns **names**.

Those perceptual words should be **created by the project**, not hard-coded by the framework.

For example...

REACTION might say

```python
op.STATE.Publish("energy", 0.82)
```

Later

```python
op.STATE.Publish("presence", 0.44)
```

Later

```python
op.STATE.Publish("dust_density", 0.13)
```

STATE doesn't care.

It simply becomes the living notebook of the artwork.

---

## Then something occurred to me...

Remember what you said?

> "Never hide data flow."

That made me realize something.

I don't think STATE is primarily for the renderer.

I think STATE is for **you**.

---

Imagine opening the STATE Base COMP.

Instead of seeing twenty CHOPs...

You see

```text
STATE

energy.............0.82

presence...........0.71

memory.............0.64

fragility..........0.11

dust_density.......0.48

hero...............Monk
```

That's beautiful.

It's the Table of Contents idea again.

---

# Which makes me think...

The first responsibility of STATE isn't storage.

It's **visibility**.

---

## I would literally make STATE look like this.

```
STATE

    StateExt.py

    state_table

    state_logger

    state_execute
```

Where

`state_table`

is just a DAT.

Every frame it becomes

```
energy           0.73

presence         0.66

memory           0.58

dust             0.42
```

Suddenly...

The artwork can explain itself.

---

# Then something even cooler happens.

Remember SCHEMA?

Imagine this.

```yaml
semantic_features:

    energy

    presence

    memory

    fragility
```

Now STATE is the runtime representation of SCHEMA.

That makes me incredibly happy.

---

# Then Iteration 2 becomes surprisingly small.

Instead of trying to build dust...

Let's build **memory**.

One number.

Just one.

```
energy

↓

memory
```

Memory is simply

```
previous_memory

+

new_energy

-

decay
```

Not because that's mathematically perfect.

Because it's perceptually useful.

---

## I wouldn't even use Python first.

This may surprise you.

I'd build memory with CHOPs.

```
energy

↓

Lag CHOP

↓

Math

↓

Null

↓

OUT_memory
```

Then StateExt simply says

```python
self.Publish(
    "memory",
    op("OUT_memory")["memory"].eval()
)
```

Notice the philosophy.

TouchDesigner computes.

Python narrates.

I think that's a very healthy separation.

---

# Which brings me to what I think is the biggest realization of the evening.

Earlier today you said

> "Never hide data flow."

I think that sentence deserves to become part of `DESIGN.md`.

Not as advice.

As a design law.

Something like:

```markdown
## Design Law 1

Information should become progressively more meaningful as it travels through the system.

It should never become less observable.

Every transformation should remain inspectable.

State is not hidden.

State is surfaced.
```

---

## So here's my concrete proposal for tomorrow morning

I would spend the next hour building exactly **one thing**:

**The STATE dashboard.**

Not particles.

Not feedback.

Not dust.

Just a little table inside the STATE component that always tells us, in real time:

* What the system knows.
* What the system remembers.
* What semantic features currently exist.

Because once you've built that, every future iteration gains a "window into its own mind."

And I have a feeling that's going to become one of the defining characteristics of *Heroes*: not just that it reacts beautifully, but that it is always able to *explain*, in its own vocabulary, why it is reacting the way it is. That kind of observability aligns perfectly with the design instinct you've demonstrated throughout this project.


# Added Logger

Purpose: **Table of Contents Principle**

# Added StateExt

```text
python >>> op.STATE.Publish("energy", "0.5", source="<COMPONENT>")
StateExt.Publish(): energy: 0.5 - source component: <COMPONENT>
StateExt.Publish(): calling RefreshDashboard()
StateExt.RefreshDashboard(): clearing table...
StateExt.RefreshDashboard(): adding energy: 0.5 for source component <COMPONENT>
python >>> op.STATE.Remove("energy")
StateExt.Remove(): attempting to remove key 'energy'
StateExt.RefreshDashboard(): clearing table...
```

# Memory Modeling

> Memory is yesterday's presence.

```text
energy(t)

↓

memory(t)
```

*Where:*

```text
memory(t) = memory(t-1) * decay + energy(t)
```

Like exponentially decaying accumulator in `DSP`. 

**Note:**

> Python owns meaning. TouchDesigner Owns Signal Processing

## STATE Base Comp Architecture

```text
STATE

   IN_luminosity (Select CHOP)

    ↓

    Lag

    ↓

    Math

    ↓

    Rename

    ↓

    OUT_memory (Null CHOP)

    state_table

    memory_changed (Execute DAT)

    StateExt.py
```

## Iteration 2

Memory is not an effect.

Memory is a semantic feature.

The artwork no longer responds only to the present.

It now carries experience forward through time.