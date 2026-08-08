---
type: Reference
title: UML Class Diagram Notation
description: A glossary of common notation used to describe classes and their static relationships.
resource: https://open.oregonstate.education/setextbook/
tags:
  - uml
  - class-diagrams
  - notation
  - glossary
sources:
  - id: handbook-of-software-engineering-methods
    resource: https://open.oregonstate.education/setextbook/
    title: Handbook of Software Engineering Methods
generated:
  by: web-ingestion-instruction/gpt-5.6-sol
---
# Elements

- **Note** — a comment placed on the class diagram.
- **Class** — a box that can list the class name, attributes, and operations. Attributes are properties; operations are methods.
- **Visibility** — `+` marks public members, `-` marks private members, and `#` marks protected members.
- **Association** — a solid line indicating that a class contains a reference to an object or objects of another class.
- **Unidirectional association** — an association with an arrow showing which class has the other class.
- **Property name** — a label on an association naming the referencing property.
- **Multiplicity** — a label such as `0..1`, `1`, or `0..*` that states how many instances may participate at an end of an association.
- **Bidirectional association** — an association navigable in both directions; each class holds a reference to the other.
- **Inheritance** — a line with a hollow triangular arrowhead pointing to the superclass; the source is a subclass and "is a" target-class instance.
