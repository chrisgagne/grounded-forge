<!-- file: docs/bdd/index.md -->

# Behaviour-Driven Development

Behaviour-Driven Development (BDD) is the software development process that Cucumber was built to support.

There's much more to BDD than just using Cucumber.

## What is BDD?

BDD is a way for software teams to work that closes the gap between business people and technical people by:

* Encouraging collaboration across roles to build shared understanding of the problem to be solved
* Working in rapid, small iterations to increase feedback and the flow of value
* Producing system documentation that is automatically checked against the system's behaviour

We do this by focusing collaborative work around concrete, real-world examples that illustrate how we want the system to behave. We use those examples to guide us from concept through to implementation, in a process of continuous collaboration.

### BDD and agile

We assume that your team are using some kind of agile methodology already, planning work in small increments of value like [User Stories]. BDD does not replace your existing agile process, it enhances it.

Think of BDD as a set of plugins for your existing process that will make your team more able to deliver on the promises of agile: timely, reliable releases of working software that meets your organisation’s evolving needs, requiring some maintenance effort and discipline.

### Rapid iterations

We assume you would like to be able to respond quickly to feedback from your users, and do only the minimal work necessary to meet those needs.

BDD encourages working in rapid iterations, continuously breaking down your user's problems into small pieces that can flow through your development process as quickly as possible.

## Three practices

Essentially, day-to-day BDD activity is a three-step, iterative process:

1. First, take a small upcoming change to the system -- a [User Story] -- and talk about concrete examples of the new functionality to explore, discover and agree on the details of what's expected to be done.
1. Next, document those examples in a way that can be automated, and check for agreement.
1. Finally, implement the behaviour described by each documented example, starting with an automated test to guide the development of the code.

The idea is to make each change small and iterate rapidly, moving back up a level each time you need more information. Each time you automate and implement a new example, you've added something valuable to your system, and you're ready to respond to feedback.

We call these practices _Discovery_, _Formulation_, and _Automation_.

<figure>
  <img alt="Diagram of how the practices fit together" src="/img/docs/bdd-practices-diagram.png"/>
  <figcaption>Discovery, Formulation and Automation</figcaption>
</figure> 

Over time, the documented examples become an asset that enables your team to continue confidently and rapidly making changes to the system. The code reflects the documentation, and the documentation reflects the team's shared understanding of the problem domain. This shared understanding is constantly evolving.

There's lots to learn about each of these practices. We'll summarise each of them below.

### Discovery: What it _could_ do

> The hardest single part of building a software system is deciding precisely what to build.
>
> -- <cite>Fred Brooks, The mythical man-month</cite>

Although documentation and automated tests are produced by a BDD team, you can think of them as nice side-effects. The real goal is valuable, working software, and the fastest way to get there is through conversations between the people who are involved in imagining and delivering that software.

BDD helps teams to have the right conversations at the right time so you minimise the amount of time spent in meetings and maximising the amount of valuable code you produce.

We use structured conversations, called [discovery workshops], that focus around real-world examples of the system from the users' perspective. These conversations grow our team's shared understanding of the needs of our users, of the rules that govern how the system should function, and of the scope of what needs to be done.

It may also reveal gaps in our understanding, where we need more information before we know what to do.

The scrutiny of a discovery session often reveals low-priority functionality that can be deferred from the scope of a user story, helping the team to work in smaller increments, improving their flow.

If you're new to BDD, discovery is the right place to start. You won't get much joy from the other two practices until you've mastered discovery.

### Formulation: What it _should_ do

As soon as we have identified at least one valuable example from our discovery sessions, we can now formulate each example as structured documentation. This gives us a quick way to confirm that we really do have a shared understanding of what to build.

In contrast to traditional documentation, we use [a medium that can be read by both humans and computers](../gherkin), so that:

* We can get feedback from the whole team about our shared vision of what we're building.
* We'll be able to automate these examples to guide our development of the implementation.

By writing this executable specification collaboratively, we establish a shared language for talking about the system. This helps us to use problem-domain terminology all the way down into the code.

### Automation: What it _actually does_

Now that we have our executable specification, we can use it to guide our development of the implementation.

Taking one example at a time, we automate it by connecting it to the system as a test. The test fails because we have not implemented the behaviour it describes yet. Now we develop the implementation code, using [lower-level examples of the behaviour of internal system components](https://www.geepawhill.org/2020/06/12/microtest-tdd-more-definition/) to guide us as required.

The automated examples work like guide-rails, helping us to keep our development work on track.

When we need to come back and maintain the system later, the automated examples will help us to understand what the system is currently doing, and to make changes safely without unintentionally breaking anything.

This rapid, repeatable feedback reduces the burden of manual regression testing, freeing people up to do more interesting work, like exploratory testing.

## Learn more

Read the topics below to dig deeper and learn more about BDD.

[discovery workshops]: /docs/bdd/discovery-workshop/
[User Story]: /docs/terms/user-story/
[User Stories]: /docs/terms/user-story/

<!-- file: docs/bdd/who-does-what.md -->

# Who does what?

Who should be writing [Gherkin](/docs/gherkin/) documents, and who should write
[step definitions](/docs/cucumber/step-definitions)?

Product owners, business analysts, programmers and testers are often confused
about who should take on what responsibilities.

The answer depends on several factors, such as team structure, skills, culture,
process and more.

## The Three Amigos

*The Three Amigos* is a meeting that takes user stories and turns them into clean, thorough Gherkin scenarios. It involves three voices (at least):

- **The product owner** - This person is most concerned with the scope of the application. This involves translating user stories into a series of features. As the tester comes up with edge cases, the product owner is responsible for deciding what is within scope.
- **The tester** - This person will be generating lots of Scenarios, and lots of edge cases. How will the application break? What user stories have we not accounted for within these Features?
- **The developer** - This person will add many of the Steps to the Scenarios, and think of the details that go into each requirement. How will this application execute? What are some of the roadblocks or requirements behind the scenes?

These conversations can produce great tests, because each amigo sees
the product from a different perspective. For this reason it is *essential* that all of these roles have conversations to discover examples *together*.
[Example Mapping](/docs/bdd/example-mapping) and Event Storming are great collaborative analysis techniques for discovering examples.

Finally, there is no reason to limit these meetings to three people—or to hold only one such meeting at the beginning of the project. Continually refine your features and collaborate with everyone to best understand how to talk about, develop, and test your application.

## Writing Gherkin

To start with, when the language and style used in the scenarios
is still being established, it is recommended that the entire team collaborate on writing the Gherkin.
Later, it can be efficiently done by a pair: a developer (or someone who is responsible for the
automation) and a tester (or someone who is responsible for quality) as long as their
output is actively reviewed by the product owner (or business representative).

## Writing features

Cucumber tests are written in terms of “Features”. Each feature consists of one or more “Scenarios”.

Let’s start with an example Feature file:

```Gherkin
Feature: Explaining Cucumber
  In order to gain an understanding of the Cucumber testing system
  As a non-programmer
  I want to have an overview of Cucumber that is understandable by non-geeks

  Scenario: A worker seeks an overview of Cucumber
    Given I have a coworker who knows a lot about Cucumber
    When I ask my coworker to give an overview of how Cucumber works
    And I listen to their explanation
    Then I should have a basic understanding of Cucumber
```

Note that the scenarios do not go into the details of what the software
(or, in this case, the coworker) will do. It stays focused on the perspective of
the person the Feature is intended to serve (in this case, “a non-programmer”).

Every feature file has a single feature description at the top, but can have any
number of scenarios.

The `Feature` line names the feature. This should be a short label.

`In order to` presents the reason/justification for having the feature. In
general, this should match to one of the project’s core purposes or “business
values” such as:

- Protect revenue
- Increase revenue
- Manage cost
- Increase brand value
- Make the product remarkable
- Provide more value to your customers

`As a` describes the role of the people/users being served by the feature.

`I want` is a one sentence explanation of what the Feature is expected to do.

So, those three lines cover Why, Who, and What. Then, the document gets into the “How” with scenarios.

## Scenarios

You can have any number of scenarios for a feature.

If you have lots and lots of scenarios in one feature, you might
actually be describing *more* than one feature. When that happens, we recommend
splitting up the document into separate Feature definitions (The definition of
“lots and lots” here is subjective, and it's up to you to determine when it's time to split up a feature).

The first line provides a short description of what the scenario is intended to
cover. If you can’t describe your scenario in a single sentence (and not a
run-on sentence), then it’s probably trying to cover too much, and should be
split into multiple scenarios.

That is followed by some combination of “Steps”—lines that begin with the
keywords `Given`, `When`, and `Then` (typically in that order).

You can have many lines that use the same keyword (e.g., `Given there is something` followed by `Given I have another thing`). To increase the readability, you can substitute the keywords `And` or `But` (e.g., `Given there is something` followed by `And I have another thing`).

In general, any `Given` step line should describe only one thing. If you have
words like “and” in the middle of a step, you are probably describing more than
one step, and should split it into multiple steps.

For example:

```gherkin
When I fill in the "Name" field and the "Address" field
```

Becomes:

```gherkin
When I fill in the "Name" field
And I fill in the "Address" field
```

Cucumber features are best served by consistency. Don't say the same thing in
different ways — say it the same way every time.

For example:

```gherkin
Given I am logged in
```

and

```Gherkin
Given I have logged in to the site
```

have identical meaning, so it’s better to pick one and use the same line in
every Scenario where you need to be logged in.

<!-- file: docs/bdd/discovery-workshop.md -->

# Discovery workshop

## What is a discovery workshop?

A discovery workshop is a conversation where technical and business people collaborate to explore, discover and agree as much as they can about the desired behaviour for a [User Story](/docs/terms/user-story/).

## How do you conduct a discovery workshop?

There are several discovery workshop models, these are just a few:

[**Example Mapping**](/docs/bdd/example-mapping/)

Uses a pack of index cards in four different colours to map rules (a summary of constraints/acceptance criteria the team has agreed upon) to examples (illustrations/cases of the acceptance criteria)

[**OOPSI Mapping (Outcomes, Outputs, Processes, Scenarios, Inputs)**](https://jennyjmar.com/2016/04/16/bdd-discovery-and-oopsi/)

Similar to Example Mapping, uses Post-it Notes of different colours to map shared processes/relationships between outputs and scenarios.

[**Feature Mapping**](https://johnfergusonsmart.com/feature-mapping-a-simpler-path-from-stories-to-executable-acceptance-criteria/)

Also uses Post-it Notes of different colours.  The team picks a story from the backlog, identifies the actors involved, breaks the story down into tasks, and maps those tasks to specific examples.

## When should you hold a discovery workshop?

As late as possible before development on a new User Story begins, in order to prevent details from being lost. Conducting a discovery workshop as late as possible also gives the team enough leg room to shift their plans should new details surface.

## Who should attend?

A good rule-of-thumb is 3-6 people, but at a bare minimum your [Three Amigos](/docs/bdd/who-does-what/#the-three-amigos/) should be present: a product owner, a developer, and a tester.  Your product owner will identify the problem the team should be trying to solve, your developer will address how to build a solution around said problem, and your tester will address any edge cases that could arise. 

## How long does a discovery workshop take?

A discovery workshop should ideally only last about 25-30 minutes per story.  If you need any more time than this, it's likely the story is far too large and should be broken down, or some of the specifics are missing.  In the latter case, you should set aside the story as the team needs to do more research.

## Why bother?

The purpose of a discovery workshop is to give all stakeholders, both technical and non-technical, a *shared understanding* of the work at hand.  Doing so encourages cross-functional collaboration, an increase in feedback, and covers any lost details or incorrect assumptions made.

## Conclusion

A discovery workshop is a very important piece of the BDD lifecycle, among other agile development approaches.  Without it, you are sure to run into miscommunications and your team won't discover any unknowns, which could really hamper your project's success.

<!-- file: docs/bdd/example-mapping.md -->

# Example Mapping

Before you pull a user story into development, it’s crucial to have a conversation to clarify and confirm the acceptance criteria.

Example Mapping is a method designed to make this conversation short and very productive.

## How it works

Concrete examples are a great way to help us explore and understand the problem domain. They are a great basis for our acceptance tests.

When discussing examples, other things might come up in the conversation that deserve to be captured too:

- **rules** that summarise a set of examples, or express other constraints.
- **questions** that cannot be answered during the conversation, or assumptions that are made.
- new **user stories** discovered or sliced and deferred out of scope.

We can capture these different types of information on index cards, and arrange them in a map:

- We write the story on a **yellow** card and place it on top.
- Each of the acceptance criteria, or rules, is written on a **blue** card and placed beneath the yellow story card.
- Examples to illustrate these rules are written on a **green** card and placed under the relevant rule.
- Questions that cannot be answered during the session are captured on a **red** card so we can move on with the conversation.

We keep going until the group is satisfied that the scope of the story is clear, or we run out of time.

## More information

For more details, see Matt Wynne's blog on [Example Mapping](/blog/bdd/example-mapping-introduction).

To get started yourself, see Steve Tooke's blog on [Your first Example Mapping session](/blog/bdd/your-first-example-mapping-session).

Or have a look at the [Example Mapping Webinar](/blog/bdd/example-mapping-webinar).

<!-- file: docs/bdd/better-gherkin.md -->

# Writing better Gherkin

There are several ways to make your Gherkin better.

## Describe behaviour

Your scenarios should describe the intended behaviour of the system, not the implementation.
In other words, it should describe *what*, not *how*.

For example, for an authentication Scenario, you should write:

```gherkin
When "Bob" logs in
```

instead of:

```gherkin
  Given I visit "/login"
  When I enter "Bob" in the "user name" field
    And I enter "tester" in the "password" field
    And I press the "login" button
  Then I should see the "welcome" page
```

The first example, **When "Bob" logs in**, is a *functional requirement*. The second, much longer, example is a *procedural reference*.
Functional requirements are features, but procedures belong in the implementation details.

That way, when the implementation of a feature changes, you'll only need to change the process steps behind the scenes.
The behaviour does not have to change just because the implementation does.
In fact, a good question to ask yourself when writing a feature clause is: “Will this wording need to change if the implementation does?”.

If the answer is “Yes”, then you should rework it avoiding implementation specific details.
As a side benefit, in consequence your scenarios will be a lot shorter and much easier to follow and understand.

## Consider a more declarative style

One way to make scenarios easier to maintain and less brittle is to use a declarative style. Declarative style describes the behaviour of the application, rather than the implementation details. Declarative scenarios read better as "living documentation". A declarative style helps you focus on the value that the customer is getting, rather than the keystrokes they will use.

Imperative tests communicate details, and in some contexts this style of test is appropriate. On the other hand, because they are so closely tied to the mechanics of the current UI, they often require more work to maintain. Any time the implementation changes, the tests need to be updated too.

Here's an example of a feature in an imperative style:

```gherkin
Feature: Subscribers see different articles based on their subscription level 

Scenario: Free subscribers see only the free articles
  Given users with a free subscription can access "FreeArticle1" but not "PaidArticle1" 
  When I type "freeFrieda@example.com" in the email field
  And I type "validPassword123" in the password field
  And I press the "Submit" button
  Then I see "FreeArticle1" on the home page
  And I do not see "PaidArticle1" on the home page

Scenario: Subscriber with a paid subscription can access "FreeArticle1" and "PaidArticle1"
  Given I am on the login page
  When I type "paidPattya@example.com" in the email field
  And I type "validPassword123" in the password field
  And I press the "Submit" button
  Then I see "FreeArticle1" and "PaidArticle1" on the home page  
```

Each step is a precise instruction. The inputs and expected results are specified exactly. But it's easy to imagine changes to the application which would require changing these tests. The available options for free versus paid subscriptions can change. Even the means of logging in could change. What if, in the future, users log in with a voice interface or a thumbprint? 

A more declarative style hides the details of how the application's capabilities are implemented.

```gherkin
Feature: Subscribers see different articles based on their subscription level
 
Scenario: Free subscribers see only the free articles
  Given Free Frieda has a free subscription
  When Free Frieda logs in with her valid credentials
  Then she sees a Free article

Scenario: Subscriber with a paid subscription can access both free and paid articles
  Given Paid Patty has a basic-level paid subscription
  When Paid Patty logs in with her valid credentials
  Then she sees a Free article and a Paid article
``` 

With a declarative style, each step communicates an idea, but the exact values aren't specified. The details of *how* the user interacts with the system, such as which specific articles are free or paid, and the subscription level of different test users, are specified in the step definitions (the automation code that interacts with the system). The subscription packages could change in the future. The business could change what content is available to subscribers on free and paid plans, without having to change this scenario and other scenarios that use the same step definitions. If another subscription level is added later, it's easy to add a scenario for that. By avoiding terms like “click a button” that suggest implementation, the scenario is more resilient to implementation details of the UI. The intent of the scenario remains the same, even if the implementation changes later. In addition, having too many implementation details in a scenario, makes it harder to understand the intended behaviour it illustrates.

<!-- file: docs/bdd/myths.md -->

# Myths about BDD

Let's bust some of the most common myths and misunderstandings about BDD.

## Myth: You can pick and choose the practices in any order

Here's [Liz Keogh's take](https://lizkeogh.com/2014/01/22/using-bdd-with-legacy-systems/) on this:

> having conversations is more important than capturing conversations is more important than automating conversations.

Unless you've already done effective discovery work, trying to formulate scenarios is a waste of time.

Similarly, you can't automate examples when you haven't done the work to figure out the most important examples to automate, or got your business stakeholder's feedback in how to word them.

## Myth: You can automate scenarios after the code is implemented

Many people use Cucumber to do test automation, to check for bugs after the code has already been implemented. That's a perfectly reasonable way to do test automation, but it's not BDD.

## Myth: Discovery doesn't need a conversation

We see plenty of teams who try to leave the work of identifying examples and turning them into formulated scenarios to a single individual on the team.

That's not BDD. Discovery work needs to be done _collaboratively_, bringing together representatives of the different specialists who all need to share understanding about what will be built.

## Myth: Using Cucumber means you're doing BDD

Just because you're using Cucumber, doesn't mean you're doing BDD. [There's much more to BDD than using Cucumber](/docs/bdd).

<!-- file: docs/bdd/history.md -->

# History of BDD

Behavior-driven development was pioneered by [Daniel Terhorst-North](https://dannorth.net) back in the early 00s, as he explained in a 2006 article called [Introducing BDD](http://dannorth.net/introducing-bdd/). It grew from a response to test-driven development (TDD), as a way to help programmers on new agile teams "get straight to the good stuff" of knowing how to approach testing and coding, and minimize misunderstandings. BDD has evolved into both analysis and automated testing at the acceptance level. [Liz Keogh](https://lizkeogh.com), another BDD pioneer, started writing and speaking about it extensively beginning in 2004.

## Early tools supporting BDD

In 2003, Daniel Terhorst-North started writing a replacement for JUnit called JBehave, using vocabulary based on "behaviour" rather than "test". Liz Keogh and Chris Matts also started contributing early on. Influenced by the idea of ubiquitous language introduced in Eric Evans' [Domain-Driven Design](https://domainlanguage.com/ddd/), and also focusing on business value, the "Given/When/Then" template was developed to capture a story's acceptance criteria in an executable form. It grew partly from the "As a..., I ..., So that..." template for writing user stories, created by [Rachel Davies](http://rachelcdavies.github.io/) at Connextra that had become a recognized standard.  

In 2005, the [RSpec](https://rspec.info/) project, which supported BDD in the Ruby language, was founded by [Dave Astels](http://daveastels.com/), [Steven Baker](https://stevenrbaker.com/), [Aslak Hellesøy](https://twitter.com/aslak_hellesoy) and [David Chelimsky](https://twitter.com/dchelimsky). 

## Origins of Cucumber

As he helped improve RSpec, Aslak had a lot of ideas for improvements in areas like error messages, step definition snippets, and result reporting. RSpec was designed for programmers, whereas the RSpec Story Runner was for the whole team, including non-coding stakeholders. 

He started a new project, intending to make a better version of Story Runner. He initially called it _Stories_, but asked his then-fiancée for a catchier name. She thought of _Cucumber_, and it stuck.

<!-- file: docs/bdd/examples.md -->

# Examples

Good BDD examples are *concrete* rather than *abstract*. They mention names of 
people and places, exact dates and amounts, and anything that is relevant to the
problem domain of the software.

Good examples don't mention technical details.

:::info[Imagine it's 1922]
Most software does something people could do manually (just not as efficiently).

Try hard to come up with examples that don't make any assumptions about
technology. Imagine it's 1922, when there were no computers.
:::

<!-- file: docs/gherkin/index.mdx -->

# Gherkin

<DocCardList />

<!-- file: docs/gherkin/reference.md -->

# Reference

Gherkin uses a set of special [keywords](#keywords) to give structure and meaning to
executable specifications. Each keyword is translated to many spoken languages;
in this reference we'll use English.

Most lines in a Gherkin document start with one of the [keywords](#keywords).

Comments are only permitted at the start of a new line, anywhere in the feature file. They begin with zero or more spaces,
followed by a hash sign (`#`) and some text.

Block comments are currently not supported by Gherkin.

Either spaces or tabs may be used for indentation. The recommended indentation
level is two spaces. Here is an example:

```gherkin
Feature: Guess the word

  # The first example has two steps
  Scenario: Maker starts a game
    When the Maker starts a game
    Then the Maker waits for a Breaker to join

  # The second example has three steps
  Scenario: Breaker joins a game
    Given the Maker has started a game with the word "silky"
    When the Breaker joins the Maker's game
    Then the Breaker must guess a word with 5 characters
```

The trailing portion (after the keyword) of each step is matched to
a code block, called a [step definition](/docs/cucumber/step-definitions).

Please note that some keywords *are* followed by a colon (`:`) and some *are not*. If you add a colon after a keyword
that should not be followed by one, your test(s) will be ignored.

## Keywords

Each line that isn't a blank line has to start with a Gherkin *keyword*, followed by any text you like. The only exceptions are the free-form descriptions placed underneath `Example`/`Scenario`, `Background`, `Scenario Outline` and `Rule` lines.

The primary keywords are:

- [`Feature`](#feature)
- [`Rule`](#rule) (as of Gherkin 6)
- [`Example`](#example) (or `Scenario`)
- [`Given`](#given), [`When`](#when), [`Then`](#then), [`And`](#and-but), [`But`](#and-but) for steps (or [`*`](#*))
- [`Background`](#background)
- [`Scenario Outline`](#scenario-outline) (or [`Scenario Template`](#scenario-outline))
- [`Examples`](#examples) (or [`Scenarios`](#examples))

There are a few secondary keywords as well:

- `"""` (Doc Strings)
- `|` (Data Tables)
- `@` (Tags)
- `#` (Comments)

:::info[Localisation]
Gherkin is localised for many [spoken languages](#spoken-languages); each has their own localised equivalent of these keywords.
:::

### Feature

The purpose of the `Feature` keyword is to provide a high-level description
of a software feature, and to group related scenarios.

The first primary keyword in a Gherkin document must always be `Feature`, followed
by a `:` and a short text that describes the feature.

You can add free-form text underneath `Feature` to add more description.

These description lines are ignored by Cucumber at runtime, but are available for reporting (they are included by reporting tools like the official HTML formatter).

```gherkin
Feature: Guess the word

  The word guess game is a turn-based game for two players.
  The Maker makes a word for the Breaker to guess. The game
  is over when the Breaker guesses the Maker's word.

  Example: Maker starts a game
```

The name and the optional description have no special meaning to Cucumber. Their purpose is to provide
a place for you to document important aspects of the feature, such as a brief explanation
and a list of business rules (general acceptance criteria).

The free format description for `Feature` ends when you start a line with the keyword `Background`, `Rule`, `Example` or `Scenario Outline` (or their alias keywords).

You can place [tags](/docs/cucumber/api/#tags) above `Feature` to group related features,
independent of your file and directory structure.

You can only have a single `Feature` in a `.feature` file.

### Descriptions

Free-form descriptions (as described above for `Feature`) can also be placed underneath
`Example`/`Scenario`, `Background`, `Scenario Outline` and `Rule`.

You can write anything you like, as long as no line starts with a keyword.

Descriptions can be in the form of Markdown - formatters including the official HTML formatter support this.

### Rule

The (optional) `Rule` keyword has been part of Gherkin since v6.

The purpose of the `Rule` keyword is to represent one *business rule* that should be implemented.
It provides additional information for a feature.
A `Rule` is used to group together several scenarios
that belong to this *business rule*. A `Rule` should contain one or more scenarios that illustrate the particular rule.

For example:

```gherkin
# -- FILE: features/gherkin.rule_example.feature
Feature: Highlander

  Rule: There can be only One

    Example: Only One -- More than one alive
      Given there are 3 ninjas
      And there are more than one ninja alive
      When 2 ninjas meet, they will fight
      Then one ninja dies (but not me)
      And there is one ninja less alive

    Example: Only One -- One alive
      Given there is only 1 ninja alive
      Then they will live forever ;-)

  Rule: There can be Two (in some cases)

    Example: Two -- Dead and Reborn as Phoenix
      ...
```

### Example

This is a *concrete example* that *illustrates* a business rule. It consists of
a list of [steps](#steps).

The keyword `Scenario` is a synonym of the keyword `Example`.

You can have as many steps as you like, but we recommend 3-5 steps per example. Having too many steps will cause the example to lose its expressive power as a specification and documentation.

In addition to being a specification and documentation, an example is also a *test*. As a whole, your examples are an
*executable specification* of the system.

Examples follow this same pattern:

- Describe an initial context (`Given` steps)
- Describe an event (`When` steps)
- Describe an expected outcome (`Then` steps)

### Steps

Each step starts with `Given`, `When`, `Then`, `And`, or `But`.

Cucumber executes each step in a scenario one at a time, in the sequence you’ve written them in.
When Cucumber tries to execute a step, it looks for a matching step definition to execute.

Keywords are not taken into account when looking for a step definition. This means you cannot have a
`Given`, `When`, `Then`, `And` or `But` step with the same text as another step.

Cucumber considers the following steps duplicates:

```gherkin
Given there is money in my account
Then there is money in my account
```

This might seem like a limitation, but it forces you to come up with a less ambiguous, more clear
domain language:

```gherkin
Given my account has a balance of £430
Then my account should have a balance of £430
```

#### Given

`Given` steps are used to describe the initial context of the system - the *scene* of the scenario.
It is typically something that happened in the *past*.

When Cucumber executes a `Given` step, it will configure the system to be in a well-defined state,
such as creating and configuring objects or adding data to a test database.

The purpose of `Given` steps is to **put the system in a known state** before the user (or external system) starts interacting with the system (in the `When` steps).
Avoid talking about user interaction in `Given`'s. If you were creating use cases, `Given`'s would be your preconditions.

It's okay to have several `Given` steps (use `And` or `But` for number 2 and upwards to make it more readable).

Examples:

- Mickey and Minnie have started a game
- I am logged in
- Joe has a balance of £42

#### When

`When` steps are used to describe an event, or an *action*. This can be a person interacting with the system, or it can be an event triggered by another system.

Examples:

- Guess a word
- Invite a friend
- Withdraw money

:::info[Imagine it's 1922]
Most software does something people could do manually (just not as efficiently).

Try hard to come up with examples that don't make any assumptions about
technology or user interface. Imagine it's 1922, when there were no computers.

Implementation details should be hidden in the [step definitions](/docs/cucumber/step-definitions).
:::

#### Then

`Then` steps are used to describe an *expected* outcome, or result.

The [step definition](/docs/cucumber/step-definitions) of a `Then` step should use an *assertion* to
compare the *actual* outcome (what the system actually does) to the *expected* outcome
(what the step says the system is supposed to do).

An outcome *should* be on an **observable** output. That is, something that comes *out* of the system (report, user interface, message), and not a behaviour deeply buried inside the system (like a record in a database).

Examples:

- See that the guessed word was wrong
- Receive an invitation
- Card should be swallowed

While it might be tempting to implement `Then` steps to look in the database - resist that temptation!

You should only verify an outcome that is observable for the user (or external system), and changes to a database are usually not.

#### And, But

If you have successive `Given`'s or `Then`'s, you *could* write:

```gherkin
Example: Multiple Givens
  Given one thing
  Given another thing
  Given yet another thing
  When I open my eyes
  Then I should see something
  Then I shouldn't see something else
```

Or, you could make the example more fluidly structured by replacing the successive `Given`'s or `Then`'s with `And`'s and `But`'s:

```gherkin
Example: Multiple Givens
  Given one thing
  And another thing
  And yet another thing
  When I open my eyes
  Then I should see something
  But I shouldn't see something else
```

#### \*

Gherkin also supports using an asterisk (`*`) in place of any of the normal step keywords. This can be helpful when you have some steps that are effectively a _list of things_, so you can express it more like bullet points where otherwise the natural language of `And` etc might not read so elegantly.

For example:

```gherkin
Scenario: All done
  Given I am out shopping
  And I have eggs
  And I have milk
  And I have butter
  When I check my list
  Then I don't need anything
```

Could be expressed as:

```gherkin
Scenario: All done
  Given I am out shopping
  * I have eggs
  * I have milk
  * I have butter
  When I check my list
  Then I don't need anything
```

### Background

Occasionally you'll find yourself repeating the same `Given` steps in all of the scenarios in a `Feature`.

Since it is repeated in every scenario, this is an indication that those steps
are not *essential* to describe the scenarios; they are *incidental details*. You can literally move such `Given` steps to the background, by grouping them under a `Background` section.

A `Background` allows you to add some context to the scenarios that follow it. It can contain one or more `Given` steps, which are run before *each* scenario, but after any [Before hooks](/docs/cucumber/api/#hooks).

A `Background` is placed before the first `Scenario`/`Example`, at the same level of indentation.

For example:

```gherkin
Feature: Multiple site support
  Only blog owners can post to a blog, except administrators,
  who can post to all blogs.

  Background:
    Given a global administrator named "Greg"
    And a blog named "Greg's anti-tax rants"
    And a customer named "Dr. Bill"
    And a blog named "Expensive Therapy" owned by "Dr. Bill"

  Scenario: Dr. Bill posts to his own blog
    Given I am logged in as Dr. Bill
    When I try to post to "Expensive Therapy"
    Then I should see "Your article was published."

  Scenario: Dr. Bill tries to post to somebody else's blog, and fails
    Given I am logged in as Dr. Bill
    When I try to post to "Greg's anti-tax rants"
    Then I should see "Hey! That's not your blog!"

  Scenario: Greg posts to a client's blog
    Given I am logged in as Greg
    When I try to post to "Expensive Therapy"
    Then I should see "Your article was published."
```

`Background` is also supported at the `Rule` level, for example:

```gherkin
Feature: Overdue tasks
  Let users know when tasks are overdue, even when using other
  features of the app

  Rule: Users are notified about overdue tasks on first use of the day
    Background:
      Given I have overdue tasks

    Example: First use of the day
      Given I last used the app yesterday
      When I use the app
      Then I am notified about overdue tasks

    Example: Already used today
      Given I last used the app earlier today
      When I use the app
      Then I am not notified about overdue tasks
  ...
```

You can only have one set of `Background` steps per `Feature` or `Rule`. If you need different `Background` steps for different scenarios, consider breaking up your set of scenarios into more `Rule`s or more `Feature`s.

For a less explicit alternative to `Background`, check out [conditional hooks](/docs/cucumber/api/#conditional-hooks).

#### Tips for using Background

* Don't use `Background` to set up **complicated states**, unless that state is actually something the client needs to know.
    * For example, if the user and site names don't matter to the client, use a higher-level step such as
      `Given I am logged in as a site owner`.
* Keep your `Background` section **short**.
    * The client needs to actually remember this stuff when reading the scenarios. If the `Background` is more than 4 lines long, consider moving some of the irrelevant details into higher-level steps.
* Make your `Background` section **vivid**.
    * Use colourful names, and try to tell a story. The human brain keeps track of stories much better than it keeps track of names like `"User A"`, `"User B"`, `"Site 1"`, and so on.
* Keep your scenarios **short**, and don't have too many.
    * If the `Background` section has scrolled off the screen, the reader no longer has a full overview of what's happening.
      Think about using higher-level steps, or splitting the `*.feature` file.

### Scenario Outline

The `Scenario Outline` keyword can be used to run the same `Scenario` multiple times,
with different combinations of values.

The keyword `Scenario Template` is a synonym of the keyword `Scenario Outline`.

Copying and pasting scenarios to use different values quickly becomes tedious and repetitive:

```gherkin
Scenario: eat 5 out of 12
  Given there are 12 cucumbers
  When I eat 5 cucumbers
  Then I should have 7 cucumbers

Scenario: eat 5 out of 20
  Given there are 20 cucumbers
  When I eat 5 cucumbers
  Then I should have 15 cucumbers
```

We can collapse these two similar scenarios into a `Scenario Outline`.

Scenario outlines allow us to more concisely express these scenarios through the use
of a template with `< >`-delimited parameters:

```gherkin
Scenario Outline: eating
  Given there are <start> cucumbers
  When I eat <eat> cucumbers
  Then I should have <left> cucumbers

  Examples:
    | start | eat | left |
    |    12 |   5 |    7 |
    |    20 |   5 |   15 |
```

### Examples

A `Scenario Outline` must contain one or more `Examples` (or `Scenarios`) section(s). Its steps are interpreted as a
template
which is never directly run. Instead, the `Scenario Outline` is run *once for each row* in
the `Examples` section beneath it (not counting the first header row).

The steps can use `<>` delimited *parameters* that reference headers in the examples table.
Cucumber will replace these parameters with values from the table *before* it tries
to match the step against a step definition.

You can use parameters in `Scenario Outline` descriptions as well.

You can also use parameters in [multiline step arguments](#step-arguments).

## Step Arguments

In some cases you might want to pass more data to a step than fits on a single line.
For this purpose Gherkin has `Doc Strings` and `Data Tables`.

### Doc Strings

`Doc Strings` are handy for passing a larger piece of text to a step definition.

The text should be offset by delimiters consisting of three double-quote marks on lines of their own:
```gherkin
Given a blog post named "Random" with Markdown body
  """
  Some Title, Eh?
  ===============
  Here is the first paragraph of my blog post. Lorem ipsum dolor sit amet,
  consectetur adipiscing elit.
  """
```
In your step definition, there’s no need to find this text and match it in your pattern.
It will automatically be passed as the last argument in the step definition.

Indentation of the opening `"""` is unimportant, although common practice is two spaces in from the enclosing step.
The indentation inside the triple quotes, however, is significant. Each line of the Doc String will be dedented according to the opening `"""`. Indentation beyond the column of the opening `"""` will therefore be preserved.

Doc strings also support using three backticks as the delimiter:

~~~gherkin
Given a blog post named "Random" with Markdown body
  ```
  Some Title, Eh?
  ===============
  Here is the first paragraph of my blog post. Lorem ipsum dolor sit amet,
  consectetur adipiscing elit.
  ```
~~~

This might be familiar for those used to writing with Markdown.

:::warning[Tool support for backticks]
Whilst all current versions of Cucumber support backticks as the delimiter, many tools like text editors don't (yet).
:::

It's possible to annotate the DocString with the type of content it contains. You specify the content type after the
triple quote, as follows:

```gherkin
Given a blog post named "Random" with Markdown body
  """markdown
  Some Title, Eh?
  ===============
  Here is the first paragraph of my blog post. Lorem ipsum dolor sit amet,
  consectetur adipiscing elit.
  """
```

:::warning[Tool support for content types]
Whilst all current versions of Cucumber support content types as the
delimiter, many tools like text editors don't (yet).
:::

### Data Tables

`Data Tables` are handy for passing a list of values to a step definition:

```gherkin
Given the following users exist:
  | name   | email              | twitter         |
  | Aslak  | aslak@cucumber.io  | @aslak_hellesoy |
  | Julien | julien@cucumber.io | @jbpros         |
  | Matt   | matt@cucumber.io   | @mattwynne      |
```
Just like `Doc Strings`, `Data Tables` will be passed to the step definition as the last argument.

#### Table Cell Escaping

If you want to use a newline character in a table cell, you can write this
as `\n`. If you need a `|` as part of the cell, you can escape it as `\|`. And
finally, if you need a `\`, you can escape that with `\\`.

#### Data Table API

Cucumber provides a rich API for manipulating tables from within step definitions.
See the [Data Table API reference](https://github.com/cucumber/cucumber-jvm/tree/main/datatable) reference for
more details.

## Spoken Languages

The language you choose for Gherkin should be the same language your users and
domain experts use when they talk about the domain. Translating between
two languages should be avoided.

This is why Gherkin has been translated to [over 70 languages](/docs/gherkin/languages) .

Here is a Gherkin scenario written in Norwegian:

```gherkin
# language: no
Funksjonalitet: Gjett et ord

  Eksempel: Ordmaker starter et spill
    Når Ordmaker starter et spill
    Så må Ordmaker vente på at Gjetter blir med

  Eksempel: Gjetter blir med
    Gitt at Ordmaker har startet et spill med ordet "bløtt"
    Når Gjetter blir med på Ordmakers spill
    Så må Gjetter gjette et ord på 5 bokstaver
```

A `# language:` header on the first line of a feature file tells Cucumber what
spoken language to use - for example `# language: fr` for French.
If you omit this header, Cucumber will default to English (`en`).

Some Cucumber implementations also let you set the default language in the
configuration, so you don't need to place the `# language` header in every file.

<!-- file: docs/gherkin/step-organization.mdx -->

# Step organization

You can have all of your step definitions in one file, or in multiple files. When you start with your project, all your step definitions will probably be in one file.
As your project grows, you should split your step definitions into meaningful groups in different files.
This will make your project more logical and easier to maintain.

## How Cucumber finds your features and step definitions

Be aware that, regardless of the directory structure employed, Cucumber effectively flattens the `features/` directory tree when running tests.
This means that anything ending in <Term>file-extension</Term> inside the directory in which Cucumber is run is treated as a step definition. In the same directory, Cucumber will search for a `Feature` corresponding to that step definition.
This is either the default case or the location specified with the relevant option.

## Grouping step definitions

Technically it doesn't matter how you name your step definition files, or which step definitions you put in a file.
You *could* have one giant file containing all your step definitions. However, as the project grows, the file can become messy and hard to maintain.
Instead, we recommend creating a separate <Term>steps-file-pattern</Term> file for each domain concept.

A good rule of thumb is to have one file for each major <Term>domain-object</Term>.

For example, in a Curriculum Vitae application, we might have:

<Tabs>
    <Tab lang="java">
        <ul>
            <li>`EmployeeStepDefinitions.java`</li>
            <li>`EducationStepDefinitions.java`</li>
            <li>`ExperienceStepDefinitions.java`</li>
            <li>`AuthenticationStepDefinitions.java`</li>
        </ul>
    </Tab>
    <Tab lang="kotlin">
        <ul>
            <li>`EmployeeStepDefinitions.kt`</li>
            <li>`EducationStepDefinitions.kt`</li>
            <li>`ExperienceStepDefinitions.kt`</li>
            <li>`AuthenticationStepDefinitions.kt`</li>
        </ul>
    </Tab>
    <Tab lang="ruby">
        <ul>
            <li>`employee_steps.rb`</li>
            <li>`education_steps.rb`</li>
            <li>`experience_steps.rb`</li>
            <li>`authentication_steps.rb`</li>
        </ul>
    </Tab>
    <Tab lang="javascript">
        <ul>
            <li>`employee_steps.js`</li>
            <li>`education_steps.js`</li>
            <li>`experience_steps.js`</li>
            <li>`authentication_steps.js`</li>
        </ul>
    </Tab>
    <Tab lang="golang">
        <ul>
            <li>`employee_steps.go`</li>
            <li>`education_steps.go`</li>
            <li>`experience_steps.go`</li>
            <li>`authentication_steps.go`</li>
        </ul>
    </Tab>
</Tabs>

The first three files would define all the `Given`, `When`, and `Then` step definitions related to creating, reading, updating, and deleting the various <Term>types-of-objects</Term>
The last file would define step definitions related to logging in and out, and the different things a certain user is allowed to do in the system.

If you follow this pattern, you also avoid the
[Feature-coupled step definitions](/docs/guides/anti-patterns#feature-coupled-step-definitions) anti-pattern.

Of course, how you group your step definitions is really up to you and your team. They should be grouped in a way that
is meaningful to *your* project.

## Writing step definitions

Don't write step definitions for steps that are not present in one of your scenarios. These might end up as unused
[cruft](https://en.wikipedia.org/wiki/Cruft) that will need to be cleaned up later. Only implement step definitions that
you actually need. You can always refactor your code as your project grows.

## Avoid duplication

Avoid writing similar step definitions, as they can lead to clutter. While documenting your steps helps, making use of
[helper methods](#helper-methods) to abstract them can do wonders.

For example, take the following steps:

```gherkin
Given I go to the home page
Given I check the about page of the website
Given I get the contact details
```

If all of these steps open their respective web pages, you might be writing *redundant steps*. While the underlying code
for these steps could be different, their **behaviour** is essentially the same, i.e. *to open the Home, About or
Contact page*.

As such, you can use abstract helper methods to reduce them into a single step:

```gherkin
Given I go to the {} page
```

And the following step definition:

<Tabs>
    <Tab lang="java">

```java
@Given("I go to the {string} page")
public void i_want_to_open_page(String webpage) {
    webpageFactory.openPage(webpage);
}
```

    </Tab>
    <Tab lang="kotlin">

```kotlin
@Given("I go to the {string} page")
fun `I want to open page`(webpage: String) {
    webpageFactory.openPage(webpage)
}
```

    </Tab>
    <Tab lang="javascript">

```javascript
Given("I go to the {string} page", function (webpage) {
    webpageFactory.openPage(webpage)
}
```

    </Tab>
    <Tab lang="ruby">

```ruby
Given 'I go to the {string} page' do |page|
    open_web_page page
end
```

    </Tab>
    <Tab lang="golang">

```go
s.Step(`^I go to the "([^"]*)" page$`, goToPage)

func goToPage(webpage string) error {
    return webpageFactory.Open(webpage)
}
```

    </Tab>
</Tabs>

Your step definitions are the glue to the actual code (in this example, a factory method to decide which page to open).
They can also be used to hide implementation details by calling several reusable helper methods from one step
definition.

This helps in a number of ways:

* Increased maintainability.
* Increased scalability with reusable steps.
* More understandable tests.

You can handle other behaviours, like *validating a web page, clicking a button, etc.*, the same way.

Also, using [Data Tables](/docs/cucumber/api/#data-tables) for providing inputs to steps helps increase maintainability and understandability.

## Helper methods

Always keep in mind that Cucumber is a DSL wrapper around the programming language whose full expressiveness
remains available to you in the step definition files (*but not in feature files*).
On the other hand, do not lose sight that every step called as such in a step definition file is first parsed by
[Gherkin](/docs/gherkin/) and therefore must conform to the same syntax as used in feature files.

In fact, it is recommended to refactor step definitions into helper methods for greater modularity and reuse.
The method can reside in the same <Term>file-extension</Term> file as the step definition.

This makes your project more understandable for people who join your project at a later date; which also makes your project easier to maintain.

<!-- file: docs/gherkin/languages.mdx -->

# Localisation

In order to allow Gherkin to be written in a number of languages, the keywords have been translated into multiple languages. To improve readability and flow, some languages may have more than one translation for any given keyword.

You can find all translation of Gherkin [on GitHub](https://github.com/cucumber/gherkin).
This is also the place to add or update translations.

A list of the currently supported languages and their keywords can be found below.

<GherkinLanguages/>
