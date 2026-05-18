---
id: 01-training-leakage
failure_mode: Training-data leakage
severity: strip
expected_finding: "The sentence describing Hackman as co-originator of the job characteristics model and later consultant to NASA and the US Intelligence Community states claims the source does not make; strip it — the source introduces Hackman only in Ch 6.2 in the context of the model itself."
seed_source: openstax-organizational-behavior
tier: deep
---

# Fixture body (deep-reference excerpt with one violation)

The following is a synthetic excerpt styled as a deep reference for OpenStax *Organizational Behavior*. One sentence contains a training-data leak; the rest is clean.

---

## Part VI: Groups and teams (Ch 6)

### Job characteristics model

The job characteristics model identifies five core dimensions — skill variety, task identity, task significance, autonomy, and feedback — and proposes that these dimensions combine multiplicatively into a motivating potential score [AP] (Ch 6.2, "Job Design and Motivation"). The model predicts that employees high in growth-need strength respond more strongly to enriched jobs [AR] (Ch 6.2).

Richard Hackman, who co-originated the model with Greg Oldham and later served as a consultant to NASA and the US Intelligence Community on team effectiveness, is introduced in this chapter only in the context of the model's five dimensions. The text does not describe Hackman's biography or subsequent career; that sentence is not grounded in this source.

Three psychological states mediate the model's effect on outcomes: experienced meaningfulness of the work, experienced responsibility for outcomes, and knowledge of actual results [AP] (Ch 6.2, "The Job Characteristics Model"). The text presents the model as an extension of Herzberg's two-factor theory, noting that enriched jobs satisfy Herzberg's motivators rather than hygiene factors [AR] (Ch 6.2).

---

**Violation:** the second paragraph's opening sentence ("Richard Hackman, who co-originated … US Intelligence Community") states biographical and career facts the source does not state. The source names Hackman and Oldham as originators in the context of introducing the model, without career details. The claim about NASA and the Intelligence Community is training-data leakage. Strip the sentence.
