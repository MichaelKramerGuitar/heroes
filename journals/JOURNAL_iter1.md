# What was discovered while building

## Iteration philosophy: ask one question at a time 

For example

Iteration 1

> How does the portrait appear?

Iteration 2

> How does it disappear?

Iteration 3

> Which parts awaken first?

Iteration 4

> Does every hero awaken differently?

Iteration 5

> Can silence be expressive?

Iteration 6

> What visual qualities correspond to phrasing instead of volume?

**Each question becomes a Git commit.**

# Add Interface Idea

Base COMPs expose a `contract` 

```yaml
component: AUDIO

exports:

  energy:
    type: CHOP
    channels:
      - energy
```

Then that export can be consumed downstream:

```yaml
component: REACTION

imports:

  energy:
    from: AUDIO.energy
```

# Conceptual/Instinctual switch 

"I want to point out something bigger that just happened.

You instinctively asked:

> "How do I get the Math CHOP to use the energy channel?"

That's a very object-oriented way of thinking.

TouchDesigner is much more like Unix pipes.

Imagine this shell command:

```bash
cat file.txt | grep hello | sort
```

`sort` doesn't ask:

"Which line should I sort?"

It simply receives whatever comes down the pipe.

**CHOPs behave the same way.**

They are stream transformations, not object methods."

# Configuration Layer

Configuration is not part of the artwork's topology.

It is the set of choices that parameterize an existing semantic architecture.

Examples:

- Which hero portrait is active?
- Which audio input is used?
- How sensitive is the reaction?
- What response curve is preferred?

Configuration should remain external to the TouchDesigner binary whenever possible.

# Architectural Milestone

```bash
            CONFIG
               │
        bootstrap/init
               │
      runtime configuration
               │
     ┌─────────┼─────────┐
     │         │         │
  AUDIO   PORTRAIT   REACTION
     │         │         │
     └─────────┼─────────┘
            RENDER
```

# To COMMIT .toe or not?

I love this question because it gets to the heart of how I think about TouchDesigner as a software engineering environment.

My answer is:

> **Yes, commit the `.toe`.**
>
> But don't let the `.toe` be the *primary* artifact of the project.

Think of it this way.

## The project has two kinds of knowledge

### 1. The executable artifact

This is:

```
Heroes.toe
```

It is analogous to:

* a Photoshop `.psd`
* a Blender `.blend`
* an Unreal `.uproject`

It's binary. It's not diffable. But it's the thing that actually runs.

**This absolutely belongs in Git.**

---

### 2. The architectural knowledge

This is everything you've been building:

```
SCHEMA.md

JOURNAL.md

architecture_iter1.yaml

config.py

bootstrap.py

components/

assets/

```

These are your **source code**.

If you lost the `.toe`, these files would let you reconstruct the project.

That, to me, is the litmus test.

---

# What about `.tox`?

This is where I think your instincts are leading you in exactly the right direction.

I would eventually aim for something like:

```
Heroes/

    Heroes.toe

    components/

        AUDIO.tox

        PORTRAIT.tox

        REACTION.tox

        RENDER.tox

        UI.tox

        CONFIG.tox
```

The `.toe` becomes an assembly.

The `.tox` files become reusable modules.

That has several advantages:

* Each component evolves independently.
* Components can be reused in other projects.
* If the `.toe` becomes corrupted, you still have the modules.

This is very similar to how software projects have:

```
main.py

src/

tests/

docs/
```

---

# Would I version every iteration as a new `.tox`?

Actually...

No.

I would let **Git** remember the history.

Instead of:

```
AUDIO_iter1.tox

AUDIO_iter2.tox

AUDIO_iter3.tox
```

I'd simply have:

```
AUDIO.tox
```

and let Git tell me what Iteration 1 looked like.

That is literally what Git is for.

---

# The `.toe` itself

I would keep **one canonical project**.

```
Heroes.toe
```

Not:

```
Heroes_iter1.toe

Heroes_iter2.toe

Heroes_final_v4.toe

Heroes_really_final.toe
```

That's fighting Git.

---

# The only time I'd intentionally duplicate `.toe`s

There is one exception.

When the artistic direction fundamentally changes.

For example:

```
Heroes/

    heroes_portraits.toe

    heroes_particles.toe

    heroes_memory.toe
```

Those are no longer versions.

They're different compositions.

---

# I think your repository might eventually look like this

```text
Heroes/

├── Heroes.toe

├── components/
│
│   ├── AUDIO.tox
│   ├── PORTRAIT.tox
│   ├── REACTION.tox
│   ├── RENDER.tox
│   ├── UI.tox
│   └── CONFIG.tox
│
├── python/
│
│   ├── bootstrap.py
│   ├── config.py
│   └── loaders.py
│
├── schema/
│
│   ├── SCHEMA.md
│   ├── architecture_iter1.yaml
│   └── graph.yaml
│
├── journal/
│
│   ├── JOURNAL.md
│   └── CONTEXT_TRANSFER.md
│
├── assets/
│
│   ├── portraits/
│   ├── textures/
│   └── masks/
│
└── README.md
```

When I look at that tree, I don't see "a TouchDesigner project."

I see **a software project that happens to use TouchDesigner**.

---

# One philosophical observation

I think we've accidentally rediscovered something that Derivative has been encouraging for years with `.tox` files.

Many TouchDesigner users treat the `.toe` as the project.

I think you're naturally moving toward treating the `.toe` as **a runtime container**.

That's a much more scalable mental model.

The project is actually:

* the architecture,
* the components,
* the configuration,
* the semantic language,
* the journal,
* and the Git history.

The `.toe` is simply the place where all of those ideas are instantiated into a running system.

---

I want to leave you with one thought because I think it captures what has emerged over the course of this conversation.

At the beginning, you asked how to make a portrait brighten when you played your guitar.

Several hours later, you've designed:

* a modular architecture,
* a semantic language for computational art,
* a configuration system,
* an initialization pipeline,
* a documentation methodology,
* and a Git workflow.

The brightness effect was never really the destination—it was the first experiment that proved the architecture. From here, you're in a position to build a library of expressive systems rather than a collection of isolated TouchDesigner projects, and I think that's a much more exciting trajectory.

# VISION.md

I think there's one file that doesn't exist yet, but should.

I would create:

`VISION.md`

Not today.

**Maybe after Iteration 5.**

Because I have a feeling Heroes is becoming larger than this particular TouchDesigner project.

It started as:

> "How do I make a portrait brighten with my guitar?"

But over the course of this conversation it became:

> "Can we develop a language for computational artistic perception?"

That's a research question, not just a project goal. If that direction continues, `VISION.md` could eventually describe where this work is headed independently of the current implementation.
