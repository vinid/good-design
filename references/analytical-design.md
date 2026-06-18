# Analytical Design, Sparklines, and Layering

Extends `tufte-principles.md` with material from *Envisioning Information*, *Visual Explanations*, and *Beautiful Evidence*.

---

## 1. The Six Principles of Analytical Design

From *Beautiful Evidence*. These apply to any analytical presentation, not just charts.

1. **Show comparisons, contrasts, differences**
   Every display should answer "compared to what?"

2. **Show causality, mechanism, structure, explanation**
   Move beyond description. Show why the pattern occurs when the evidence supports it.

3. **Show multivariate data**
   Real problems are multivariate. Reducing to one variable often hides interactions.

4. **Integrate words, numbers, images, diagrams**
   Do not segregate by mode. Put labels next to the data they describe.

5. **Thoroughly describe the evidence**
   Provenance, authorship, scales, sources, and measurements enable trust.

6. **Content quality is paramount**
   No amount of design fixes weak evidence.

**Use in critique:** walk through all six. The lowest-scoring principle is usually the biggest improvement opportunity.

---

## 2. Sparklines

Word-sized, data-intense graphics.

**Defining properties:**
- Typographic resolution: sized like text and embedded inline with prose or tables
- No axes, no labels, no decoration
- Endpoints often marked
- Reveals shape, trend, variability at a glance

**Design rules:**
- Height around x-height of surrounding text
- Length around a word or short phrase
- Use one colored dot to flag a key point
- Pair with the most recent numeric value
- Stack in tables so eyes can scan vertically

**When to use:**
- Dashboards with many metrics
- Inline prose
- Anywhere a full chart would dominate but trend matters

**When not to use:**
- When precise readings matter
- For categorical or part-to-whole data

---

## 3. Layering and Separation

Dense displays work when elements are separated by value, weight, hue, or transparency rather than by wasting space.

**Techniques:**
- Lighten adjacent lines to suppress the 1+1=3 effect.
- Put primary data in dark or saturated values.
- Put secondary context in light gray.
- Use color for separation, not decoration.
- Grids, axes, and reference lines should whisper.

**Test:** Squint at the graphic. The most important data should remain visible; chartjunk should disappear first.

---

## 4. Micro/Macro Design

A micro/macro graphic reveals different stories at different viewing distances.

- **Macro view:** overall pattern, shape, trend
- **Micro view:** individual data points, labels, exceptions

**Design implication:** do not choose between overview and detail. Show both by layering.

---

## 5. Escaping Flatland

The screen is flat; good information design adds dimensions without 3D gimmicks.

**Dimensions available on flat media:**
- Color
- Size
- Shape
- Position
- Time
- Layering

**Anti-pattern:** 3D bars, pie charts with depth, and isometric projections that distort proportions.

---

## 6. Range-Frame and Dot-Dash Plot

Every standard chart element can be redesigned to carry data.

**Range-frame:**
- Replace the full axis with a line spanning only the actual data range.
- Axis ends at min/max values, not arbitrary round numbers.
- Tells the viewer the data extent without extra annotation.

**Dot-dash plot:**
- Scatter plot where axes are replaced by marginal rug plots.
- Each axis becomes a 1D distribution.
- Same ink, more information.

---

## 7. Confections, Parallelism, Narrative

**Confections:** assemblages of visual elements into one explanatory composition. They work when each element serves the argument.

**Parallelism:** repetition of visual structure to enable comparison. Small multiples are one form.

**Narrative graphics of space and time:** combine spatial and temporal dimensions in one frame.

---

## 8. Cause and Effect

Causality is hard to visualize because it requires both variables and mechanism.

**Techniques:**
- Show the intervention and response in the same frame.
- Annotate the causal mechanism directly on the data.
- Use sequence or small multiples through time to imply mechanism.
- Pair the data display with a process diagram.

---

## Quick Reference: Extended Tufte Test

After applying the standard test in `tufte-principles.md`, add:

8. **Comparison:** Does the graphic answer "compared to what?"
9. **Causality:** Is the mechanism visible, not just the pattern?
10. **Multivariate:** Are interactions shown, or has the problem been over-reduced?
11. **Integration:** Are words, numbers, and images interleaved?
12. **Documentation:** Can a stranger evaluate the evidence?
13. **Layering:** Do important elements dominate and secondary elements recede?
14. **Micro/macro:** Does the display reward both a glance and a close read?
