# On 'Python owns meaning'

TouchDesigner is incredible at moving numbers.

Python is incredible at assigning names.

That separation feels extremely healthy.

# Detail

for PORTRAIT.moviefileinCHOP you can use something like `f'{project.folder}/{root.fetch("CONFIG")["PORTRAIT"]["hero"]}'` for file as an `expression`

# TODO

- Write the artistic question first: "Which parts awaken first?"
- Create a new ANATOMY Base COMP that publishes semantic portrait regions.
- Keep those outputs semantic (eyes, face, background), not 
- implementation-specific (mask1, crop2).
- Extend STATE so memory can exist per region rather than only globally.
- Update RENDER to compose the portrait from independently driven regions.
- Observe the behavior before adding any polish or new effects.

#  Discoveries

## Discovery 1

Semantic regions are not measurements.

A region is a piece of the artwork.

A measurement is something computed about that region.

```text
head_region (TOP)

↓

Analyze

↓

head_luminosity (CHOP)
```

This was a major clarification.

## Discovery 2

REACTION is no longer a filter. It is a junction.

### Iteration 1

```text
energy

↓

luminosity
```

### Iteration 3

```text
head_region
        \
body_region ---- REACTION ---- head_luminosity
        /
audio_energy
```

> REACTION combines semantic streams.

## Discovery 3

STATE remembers semantic features, not implementations.

STATE doesn't know

`head`

It doesn't know

`Lag CHOP`

It knows

`head_memory`

## Discovery 4

Rendering has become compositional.

Instead of

```text
portrait

↓

brightness
```

you now have

```text
head

↓

brightness

+

body

↓

brightness

+

hands

↓

brightness

↓

portrait
```

The artwork is literally assembled from semantic regions.

## Discovery 5

Heroes is beginning to distinguish between space and time.

`ANATOMY` owns space.

`STATE`owns time.

`REACTION` connects them.

*This is one of the most profound discoveries in the project so far.*