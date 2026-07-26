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