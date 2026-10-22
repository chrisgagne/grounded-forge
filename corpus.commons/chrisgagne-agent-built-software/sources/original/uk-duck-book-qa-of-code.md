<!-- file: book/intro.md -->

# Quality assurance of code for analysis and research

This Government Analysis Function (AF) guidance, also known as the Duck Book,
is produced by the Analysis Standards and Pipelines hub of the [Office for National Statistics](https://www.ons.gov.uk).

The guidance is a living document, which is continually updated.
We are extremely grateful for any feedback that you can provide on existing and future content.


## How to get the most out of the book

This guidance describes software engineering good practices that are tailored to those working with data using code.
It is designed to support you to quality assure your code and increase the reproducibility of your analyses.
Software that apply these practices are referred to as reproducible analytical pipelines (RAP).

This guidance is relevant if you are:

- writing code to automate part of your work and would like to assure that it is working as expected
- developing statistical or data engineering pipelines and would like to assure that they are sustainable and reproducible
- developing models and would like to assure that they are transparent and reproducible
- developing data science techniques and would like your code to be useful to others
- looking for a high level introduction to software engineering practices in the context of analysis and research

The good practices outlined in the book are general to many applications of programming, so may also be relevant for those outside of government.

The [RAP learning pathway](https://learninghub.ons.gov.uk/course/view.php?id=1273) provides training for many of these good practices.
This book can be used to guide your learning and as a reference when applying these practices in your work.
Each chapter describes the risks that each practice may help to address.
As recommended by [the Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government),
you should strive to apply the most appropriate and proportionate quality assurance practices given the risks associated with your work.

The principles in this book are computer language agnostic.
The book does not aim to form a comprehensive learning resource and you may often need to study further resources to implement these practices.
That said, we have provided examples and useful references for **Python** and **R**, as these open source languages are commonly applied across government.


## About us

The Analysis Standards and Pipelines hub supports government analysis by providing guidance, consultancy and training.

You can find us on:

- Our websites: [Government Analysis Function](https://www.gov.uk/government/organisations/government-analysis-function)
- Email: [Analysis Standards and Pipelines hub](mailto:ASAP@ons.gov.uk)
- Slack: [Government Data Science](https://govdatascience.slack.com)
- Twitter: [Government Analysis Function](https://twitter.com/gov_analysis) and [UK GSS](https://twitter.com/ukgss)


## Citing the book

The book uses an Open Government Licence which can be read on the National Archives website:
[National Archives](https://nationalarchives.gov.uk/doc/open-government-licence/version/3/)

In summary, you are free to use, adapt and distribute the information in this book with citation but not imply endorsement,
and the information here is provided 'as is' without warranty.

The following structure can be used to reference the current version of the book:

> UK Government Analytical Community. (2020). Quality assurance of code for analysis and research (version 2026.1).
> Office for National Statistics, Analytical Standards and Pipelines hub:
> [https://best-practice-and-impact.github.io/qa-of-code-guidance/](https://best-practice-and-impact.github.io/qa-of-code-guidance/)


## Accessibility statement

This accessibility statement applies to the Quality assurance of code for analysis and research guidance.
Please note that this does not include third-party content that is referenced from this guidance.

The website is managed by the Quality and Improvement division of the Office for National Statistics.
We would like this guidance to be accessible for as many people as possible.
This means that you should be able to:

- change colours, contrast levels and fonts
- zoom in up to 300% without the text spilling off the screen
- navigate most of the website using just a keyboard
- navigate most of the website using speech recognition software
- listen to most of the website using a screen reader (including the most recent versions of JAWS, NVDA and VoiceOver)

For keyboard navigation, {kbd}`Up Arrow` and {kbd}`Down Arrow`keys can be used to scroll up and down on the current page.
{kbd}`Left Arrow` and {kbd}`Right Arrow` keys can be used to move forwards and backwards through the pages of the book.
Tabbed content (including code example) can be focused using the {kbd}`Tab` key.
{kbd}`Left Arrow` and {kbd}`Right Arrow` keys are then used to focus the required tab option,
where {kbd}`Enter` can be used to select that option and display the associated content.


### Help us improve this book

We’re always looking to improve the accessibility of our guidance.
If you find any problems not listed on this page or think that we’re not meeting accessibility requirements, please contact us by emailing [ASAP@ons.gov.uk](mailto:ASAP@ons.gov.uk).
Please also get in touch if you are unable to access any part of this guidance, or require the content in a different format.

We will consider your request and aim to get back to you within five working days.


### Enforcement procedure

The Equality and Human Rights Commission (EHRC) is responsible for enforcing the
[Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018 (the ‘accessibility regulations’)](https://www.legislation.gov.uk/uksi/2018/952/made).
If you’re not happy with how we respond to your complaint, you should [contact the Equality Advisory and Support Service (EASS)](https://www.equalityadvisoryservice.com/).

<!-- file: book/glossary.md -->

# Glossary of terms

```{note}
This section is a draft, while we make sure that it meets user needs.

Please get in touch with feedback [by creating a GitHub Issue](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues) or [emailing us](mailto:ASAP@ons.gov.uk).
```

## Terms
### Abstraction

Treating a problem as an idea or concept, rather than a detailed individual example.

Abstraction is used to manage the complexity of software, by describing our logic in a more generic way or by hiding complexity.
When we use similar logic in multiple parts of our code, we can abstract this logic into a generic function or method to be reused.
When part of our process is very complex, but is self-contained, we can hide this complexity it by putting it inside a function and referring to the function.


### Application Programming Interface (API)

An interface that defines how you can interact with software through code.
For example, the functions or methods from a package that a typical user will interact with.


### Attribute

A variable associated with a class object.


### Automated testing

Tests that are written in code, to check that other code works as expected.
Test are like a controlled experience, to check that our code produces the expected outcome.
Tests can check code multiple levels, for example, checking that an individual function works or checking that a pipeline runs from end to end.


### Code interpreter

A computer program that runs code in a particular programming language.
For example, the program that reads your Python or R analysis code and runs it.
A non-interactive interpreter runs code in order, which is important for reproducibility.

Interactive interpreters allow you to run individual lines of code, which means that you can run code  out of order.
Notebooks use interactive interpreters.
These are not suitable for running analysis pipelines, because they do not ensure that the code is run reproducibly.


### Class

Contains code to create instances of objects and methods to edit these instances of classes and their attributes. Methods may also produce output other than the class instance.

Examples of built in python classes are float, string, and bool.

Examples of built in R classes are double, character, and logical.


### Cloud computing

Cloud computing allows us to access scalable computing power and data storage on-demand.
This means that we can access high-specification hardware or store large amounts of data, usually only paying for what we have used.

The most common cloud platforms are Google Cloud Platform (GCP), Amazon Web Service (AWS) and Microsoft Azure.


### Code

The part of software that contains program instructions.
In analysis, code is a set of human-readable instructions that tell a computer how to carry out our analysis.


### Code repository

A folder for storing the code and associated documents for a piece of software.
These are often associated with Git, as the folder that is being version controlled.
Also known as a 'repo'.


### Configuration file

Files that are used to configure the parameters or settings of a program.
In analysis, these often include paths to input data files and other information that may change between each run of the pipeline.


### Continuous integration and continuous delivery (CI/CD)

CI/CD tools help to automate parts of your code development workflow.
This can include running automated tests against your code and deploying the latest version of your code into production.
GitHub Actions is an example tool for running CI/CD workflows.

Continuous integration describes regularly combining code changes from multiple contributors on a single software project.
Integrating these changes regularly helps to check that independent changes work correctly together.
Continous delivery describes automation of the software release process.
Automating both of these using a CI/CD tool increases the efficiency of building software and getting it into production.


### Debugger

A computer program that is used to test software and to identify the root cause of errors or "bugs".
Debuggers allow you to pause the code at specific points and to walk through code step by step, in order to understand how it is working.


### Dependencies

Something that is required for your code to run correctly - your code depends upon it.
This includes your operating system, environment, software and packages (and their versions), if these are needed to reproducibly run your analysis code.
Dependencies are usually documented alongside code, so that others can prepare an environment to run the code.


### Documentation

Human readable text that describes your analysis and code.
There are many ways to document code.
Low level documentation might describe a single function, a code comment might describe a decision you made when writing the code,
and high level documentation might describe your overall approach to a piece of analysis.


### Dual Running

In a RAP context, where a pipeline or process is run in different ways, on different systems, or by different people to verify reproducibility.


### Functions and methods

Functions and methods are named units of logic that can be used multiple times in our code.
Methods are similar to functions, but are associated with a class.
Functions and methods are crucial for creating modular code.

Functions are written to generalise a piece of logic, so that it can be used consistently in multiple places in our code.
You might define a function for a particular statistical method, validation check or to manipulate data in a certain way.


### Git

By far the most popular version control tool.
Used to version changes to code for any programming language.


### Instance

When an object is created by a constructor of a class, the resulting object is called an instance of the class. The variables specific to an object are called instance variables.


### Integrated development environment (IDE)

An IDE is a tool that facilitates software development for a given programming language.
An IDE will usually consist of a code editor, debugger and development automation tools like a text auto-complete.


### Interative Running

Where a script is run as expressions with immediate feedback given, such as in a terminal or command line.


### Logging

Automatically recording information when your analysis runs.
This might include what options were used when configuring the pipeline and any decisions that the code made when running.
Recording this information can help you to reproduce previous runs of the analysis and to identify the source of errors.


### Maintainability

Ability to easily understand, modify and repair the code.


### Modularity

Modular code is written in discrete, re-usable chunks.
Similar code is kept close together, while pieces of code with different uses are stored separately.
Breaking code down in this way makes code easier to work with, understand and review.


### Module

A module is a script grouping related functions and/or classes that are reused across larger programs. It may also include statements used to initialise the module when it is imported in another script. 


### Notebooks

Notebooks are documents that contain text, executable code, and the output of that code.
Notebooks are used to share the results of exploratory analysis.
However, because parts of a notebook can be run out of order they are not suitable for production of published outputs.


### Object-oriented programming (OOP)

Writing code that defines and uses classes.
Classes are objects that contain both data (attributes) and logic (methods).
Classes are often used to represent a real life entity - for example a bank account, which stores a balance and has method for withdrawing money.


### Open source

A type of software license that allows users to view the software's code.
Open-source code is openly available to anyone.
Using open-source software and publishing our code with open-source licenses ensures that our users can easily understand and reproduce our analysis.

Open-source programming languages are free to use.
We recommend using Python and R, which support the good practices outlined in this guidance.

Proprietary software, including SPSS, SAS, and Stata are closed source.
These are expensive to use and do not support many of the good analysis practices outlined in this guidance.
Not using open source analysis tools means that your users need to purchase software to reproduce your results.


### Packages

Packages are file structures that contain code and documentation.
These collections of code are designed for you to install and re-use them with ease.
Packages in Python and R act as extensions, to allow us to reuse code that has already been written.

"Library" is similarly used to describe a software collection, however, packages are more specifically for distribution of code.


### Parameters and arguments

Parameters are the variables that a piece of code expects to be provided when it is used.
They act as placeholders, to allow us to make code more generic.
A function might have parameters to allow it to be run on different inputs.
For example, there may be a parameter to allow the user to select which column of data a piece of logic should use.

An argument is the value that is being passed to a given parameter.


### Peer review

Having another developer review changes that you have made to code.
This helps to assure that your code is readable and follows a sensible approach.
It also helps to transfer understanding of the code between members of the team.


### Pipeline

A orchestrated chain of programs that will execute the next program(s) in the chain when a program completes successfully. Outputs will be stored on completion of a program and will feed in as inputs to the next program(s) in the chain.


### Procedural Running

Where a script is executed as statements that run one after the other.


### Program

A main script that can contain statements, functions, and methods. The main script may import functions and methods from other scripts. This is the script that would be run by the user/orchestration tool.


### Python and R

Python and R are high-level programming languages that are commonly used in government analysis.
They are both free to use and open source.


### Readability

Ability to gain an understanding of code within a reasonable amount of time.


### Reproducible Analytical Pipelines (RAP)

Reproducible Analytical Pipelines (RAP) are analyses that are carried out following good software engineering practices that are described by this guidance.
They focus on the use of open-source analytical tools and a variety of techniques to deliver reproducible, auditable, and assured data analyses.
RAP is more generally a culture of wanting to improve the quality of our analysis, by improving the quality assurance of our analysis code.


### Scripts

A script is a single file containing code. Code in scripts can be run interactively or procedurally.


### Variables

A variable is a named code object for storing data within a programming language.


### Version control

Saving versions of documents to keep an audit trails of changes.
Version control tools typically allow you to backtrack to previous versions and to merge multiple concurrent changes from different users.


### Version control platforms

For example, GitHub, GitLab and BitBucket.

These services use Git to manage remote repositories.
Having a remote version of your repository allows multiple users to collaborate using Git.
Each platform has free and paid options and allow users to open-source their work.

Some platforms (e.g. GitLab) are open source and can be hosted internally by your organisation.


### Virtual environment

Virtual environments are tools for managing dependencies and isolating projects.
A virtual environment is effectively a folder tree containing the programming language version and a list of dependencies.
This helps keep track of dependencies and avoid conflicts between different projects.

<!-- file: book/managers_guide.md -->

# Managing analytical code development

```{note}
This section is a draft, while we make sure that it meets user needs.

It would benefit from case studies that demonstrate how to decide what level of quality assurance a piece of analysis requires.

Please get in touch with feedback or case studies to support the guidance
[by creating a GitHub Issue](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues)
or emailing us at [emailing us](mailto:ASAP@ons.gov.uk).
```

This section of the guidance targets those who manage data analysis, science and engineering work in government
or those acting as product owners for analytical products.

It aims to help you support your team to apply the good quality assurance practices described in the wider
[Quality assurance of code for analysis and research guidance](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html).
We refer to processes that apply these good practices as a reproducible analytical pipelines (RAP).

Before applying this guidance, you should have a basic awareness of the tools and
techniques used to do quality analysis as code - the [introduction to RAP course](https://learninghub.ons.gov.uk/course/view.php?id=1236) outlines these.
You should also be aware of any specific tools and platforms that are used in your department.

[The Government Service Standard](https://www.gov.uk/service-manual/service-standard) outlines best practices for creating public services, which include analysis.
You should use this when designing and managing the development of analysis as code.


## Apply quality assurance proportional to risk

As the [the Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) notes,
the quality assurance we apply to our analysis should be proportionate to the complexity and risk that the analysis carries.

When managing analytical work, you should not need an in-depth understanding of the analysis code to trust that it is working correctly.
However, you should be confident that the team who built the analysis process has taken an appropriate approach given the user need,
and that proportionate quality assurance is being applied to the development and running of the analysis.

You should work with your team to decide which quality assurance practices are necessary given each piece of analysis.
You might find our [](checklists.md) useful templates for defining the target level of assurance.
When possible, you should define the target assurance level before starting the analysis.


```{important}

While quality assurance must be applied relative to the risk and complexity of the analysis, you must consider the skills of your team.
It will take time to learn to apply the necessary good practices, so you should support their gradual development of these skills.

[The RAP learning pathway](https://learninghub.ons.gov.uk/mod/page/view.php?id=8699) provides training in good practices.
You can use the wider [Quality assurance of code for analysis and research guidance](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html)
as a reference to apply these practices to analysis.
You should identify where each analyst is along the pathway - they should look to develop the next skill in the pathway and apply this,
rather than attempting to adopt them all at once.

Note that it is important to maintain technical skills in the analysis team for sustainability, to ensure that the analysis can be understood, updated, and maintained.
```

Despite the initial cost of developing technical skills,
[evidence shows that applying good practices increases the efficiency of code development and maintainability of the code](https://www.devops-research.com/research.html).
There are number of case studies that describe how
[good quality assurance practices have improved government analysis](https://analysisfunction.civilservice.gov.uk/support/reproducible-analytical-pipelines/rap-case-studies/).

Not following good practices creates [technical debt](https://en.wikipedia.org/wiki/Technical_debt), which slows down further development of the analysis.
This can be necessary for delivering to short deadlines, but you should set aside time to address this for continued development of the analysis.

Where quality assurance of the code doesn't meet your target level of assurance,
for example where there is limited time or skill,
then you should supplement this with more in-depth assurance of outputs.
This might include dual running the analysis with an independent system and consistency checks across the output data.

The remaining parts of this section provide questions that aim to help you assess the quality assurance practices that your team are applying in their analysis.


## Design quality analysis

These questions aim to help you assess the design decisions at the beginning of the analysis.


### Why have you chosen to do the analysis this way?

Understanding user needs ensures that the analysis is valuable.

* You should have a plan to consult users at the beginning and throughout the development process, to ensure that you meet their needs.
* The methodology and data should be suitable for the question being asked.
* More than one person should develop the analysis to allow pair programming, peer review, and mentoring. This increases the sustainability of analysis.
* You should use open-source analysis tools to carry out the analysis, wherever possible.
Your team should be able to explain why they have chosen the analysis tools and why they are confident that they are fit for purpose.


### How are you storing input data?

Versioning input data ensures that we can reproduce our analysis.

* You should version input data so that you can reproduce analysis outputs.
* You should store data in an open format (e.g. CSV or ODS), not formats that are restricted to proprietary software like SAS and Stata.
* You should store large or complex datasets in a database.
* You should monitor the quality of data, following [the government data quality framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework).


### How will you keep track of changes to the code and why they were made?

[Version control](version_control.md) of changes provides an audit trail.

* You should version control the code, documentation, and peer reviews. Git software is most commonly used for this.
* You should develop the code on an open source code platform, like GitHub. This transparency increases your users trust in the analysis and promotes collaboration and re-use.
* You should have a clear record of every change and who made it.
* Each change should be linked to a reason, for example, a new requirement or an issue in the existing code.
* You should store reviews of changes with the version of the analysis that was reviewed.


## Quality assure throughout development

These questions can be used throughout the development of the analysis,
to assess how the team are progressing towards the target quality assurance practices that you have agreed.


### How is your code structured?

[Modular code](modular_code.md) makes it easier to understand, update and reuse the code.

* You should write logic as functions, so that it can be reused consistently and tested.
* You should group related functions together in the same file, so that it is easy to find them.
* You should clearly separate logic with different responsibilities (e.g., reading data versus transforming data).
* When code can be reused for other analyses, you should store and share this as a package.


### How easy is it to adjust the way that the analysis runs?

[Configuration files](configuration.md) allow you to change the way the code runs without editing the code itself.

* You should store parameters for the code that often change between runs in separate configuration files.
* Things that often change in analysis code include input and output file paths, reference dates and model parameters.


### How is the analysis documented?

[Code documentation](code_documentation.md) is essential for business continuity and sustainability.

* You should document every function in the code, so it is clear what each function is supposed to do.
* Function documentation should include what goes in and what comes out of each function.
* Where others will run or re-used the code, documentation should include usage examples and test data.


### What are the dependencies?

[Project documentation](project_documentation.md) ensures that others can reproduce our analysis.

* You should provide user instructions for running the analysis.
* You should document software and package versions with the code.
Typically, you record package versions using `setup.py` and `requirements.txt` files (Python) or a `DESCRIPTION` file (R).
* Code should not be dependent on a specific computer to run. Running it on a colleague's system can help to check this.
* When you run the same analysis multiple times or on different systems, it should give reproducible outcomes.
* Container systems, like Docker, help to create reproducible environments to run code.


### What assumptions does the analysis make?

Transparency of our analysis increases trust.

* You should record assumptions and caveats of the analysis close to the code.
* You must communicate these to users when releasing results from the analysis.


### How has peer review been done?

[Peer review](peer_review.md) increases the quality of our analysis and transfers skills and knowledge.

* Technical colleagues should conduct internal peer reviews of each change to the code.
This will identify issues early on and makes the review process more manageable than reviewing only the final analysis.
* Peer review should follow a standard procedure, so that reviews are consistent. Reviewers should check that each change follows the agreed good practices.
* You should evidence that peer reviews are acted on and how. When issues or concerns are raised, they should be addressed before the analysis is used.
* If the product is high risk,  you should arrange and conduct external peer review.


### How have you tested the code?

[Testing](testing_code.md) assures us that the code is working correctly.

* Testing means making sure that the code produces the right outputs for realistic example input data.
* You should apply automated 'unit' testing to each function to ensure that code continues to work after future changes.
* You should test each function and the end-to-end analysis using minimal, realistic data.
* Your testing should be more extensive on the most important or complex parts of the code. However, ideally you would test every single function.
* Tests should account for realistic cases, which might include missing data, zeroes, infinities, negative numbers, wrong data types, and invalid inputs.
* Reviewers should sign-off that there is enough testing to assure that the code is working as expected.
* Each time you identify an error in the code,you should add a test to assure that the error does not reoccur.


### What happens when the analysis fails to run?

Recording and reporting errors provides an audit trail and makes it easier for users to correctly use the code.

* When code fails to run, it should provide informative error messages to describe the problem.
* If another team will operate the code, error messages should help users to correct the problem.
* Errors or warnings might also be raised when data validation is not met.
* When code is run in production, errors should be recorded or logged.


### How does the analysis result differ from the previous analysis?

Comparing analysis to previous results can help to ensure reproducibility and identify errors.

* When repeating analysis over time, you should compare results between analyses.
Large differences in the outcome of the results may indicate an issue with the analysis process.
* When developing code to replace legacy analysis, you may wish to parallel this with the new method. This will allow you to identify differences and improvements.


### How can we further improve the quality of the analysis?

Code quality improves over time, as your team learn more about good practices.

* The team should be aiming to meet the agreed assurance level, but should also consider which practices could be applied next to improve the code beyond this.
* You should review training needs in your team and allow time for continuous personal development of these practices.

<!-- file: book/checklists.md -->

# Code quality assurance checklists

The code checklists have been removed whilst we work to update them.

If you need the checklists for your work or have any questions about the updates, please email the [Analysis Standards and Pipelines hub](mailto:ASAP@ons.gov.uk).

<!-- file: book/principles.md -->

# Principles

When we do analysis, it must be fit for purpose.
If it isn't, we risk misinforming decisions.
Bad analysis can result in harm or misallocation of public funds.
So we must take the right steps to ensure high quality analysis.

This book recognises three founding principles of good analysis, each supported by the one before it.
Programming in analysis makes each of these principles easier to fulfil in most cases.

```{figure} ./_static/repro_stack.png
---
width: 50%
name: repro_stack
alt: Founding principles of good analysis.
---
Founding principles of good analysis
```

Reproducibility guarantees that we have done what we are claiming to have done, and that others can easily replicate our work.
Auditability means that we know why we chose our analysis, and who is responsible for each part of it - including assurance.
Assurance improves the average quality and includes the communication of that quality to users.

```{admonition} Key strategies
:class: admonition-strategies

Government guidance is available to help you when develop analysis.
We recommend:

1. The [Analysis Function reproducible analytical pipelines (RAP) strategy](https://analysisfunction.civilservice.gov.uk/policy-store/reproducible-analytical-pipelines-strategy/),
when considering how your department should adopt good practices.
2. The [Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government)
to understand guidance around assurance.
3. The [Analysis Function Quality Strategy](https://analysisfunction.civilservice.gov.uk/policy-store/government-statistical-service-gss-quality-strategy/)
when thinking about the quality of statistics.
4. The [DCMS Data Ethics Framework](https://www.gov.uk/government/publications/data-ethics-framework/data-ethics-framework)
when approaching any analysis.
5. The [Communicating quality, uncertainty and change guidance](https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/)
whenever you must develop user-facing products.

Each of these pieces of guidance advocate reproducibility as a core tenet of quality analysis.
```


## Reproducible

Reproducibility is the only thing that you can guarantee in your analysis.
It is the first pillar of good analysis.
If you can't prove that you can run the same analysis, with the same data, and obtain the same results, then you are not adding a valuable analysis.
The additional assurances of peer review, rigorous testing,
and validity are secondary to being able to reproduce any analysis that you carry out in a proportionate amount of time.

A reproducible and transparent production process ensures that anyone can follow your steps and understand your results.
This transparency eases reuse of your methods and results.
Easy reproducibility helps your colleagues test and validate what you have done.
Guaranteeing reproducibility means that users and colleagues can focus on verifying that the implementation is correct and that the research is useful for its intended purpose.

Reproducibility relies on effective documentation.
Good documentation should show how your methodology and your implementation map to each other.
Good documentation should allow users and other researchers to reuse and adapt your analysis.

Reproducible analysis supports the requirements of the [Code of Practice for Statistics](https://www.statisticsauthority.gov.uk/code-of-practice/)
around quality assurance and transparency (auditability).
We share the code we used to produce our outputs wherever possible, along with enough data to allow for proper testing.


## Auditable

If decisions are made, based on your analysis, then you must make sure that your analysis and the evidence that you provide are available for scrutiny and audit.
Auditable analysis is about being able to, at any point, answer:

* Who made each decision?
* When was this decision made?
* What evidence was this decision based on?

Answering these questions gives decision makers and users greater trust in your work.
They know the story of your analysis and why you made certain analytical choices.
They know who is responsible for each part of the analysis, including the assurance.
They know exactly what changes have been made at any point.

In a reproducible workflow, you must bring together the code and the data that you used to generate your results.
Ideally, you would publish these alongside your reports, with a record of analytical choices made and the responsible owners of those choices.
This increases the trustworthiness of your work.
More eyes examining your work can point out challenges or flaws that can help you to improve.
You can be fully open about the decisions you made when you generated your outputs, so that other analysts can follow what you did and re-create them.
By making your analysis reproducible, you make it easier for others to quality assure, assess and critique.


## Assured

Quality Assurance (QA) is vital for good quality analysis.
If decisions are being made based on analysis then this analysis must be held to high standards.
This is true for analysis carried out using any medium, including code.

However, some of the analysis that we do in government doesn't bear on decisions at that level.
We don't want to overburden analysts with QA procedures when they are not required.
In government we advocate **proportionality** - the right quality assurance procedures for the right analysis.
You can proportionately assure analysis through peer review and defensive design.

We suggest following your department's guidance on what proportionate quality assurance looks like.
Most departments derive their guidance from the [Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government).
Assurance is best demonstrated through peer review.
Peer reviewers must be able to understand your analytical choices and be able to reproduce your conclusions.
Consider dual running, particularly for high risk analysis.

Publish guarantees of quality assurance alongside any report, to be taken into consideration by decision makers.


## Reproducible analytical pipelines

Producing analysis, such as official statistics, can be time-consuming and painstaking.
We need to make sure that our outputs are both accurate and timely.
We aim to develop effective and efficient analytical workflows that are repeatable and sustainable over time.
These workflows should follow the principles of reproducible analysis.
We call these [Reproducible Analytical Pipelines (RAP)](https://analysisfunction.civilservice.gov.uk/support/reproducible-analytical-pipelines/).

Reproducible analysis is still not widely practised across government.
Many analysts use proprietary (paid-for) analytical tools like SAS or SPSS in combination with programs like Excel, Word, or Acrobat to create statistical products.
The processes for creating statistics in this way are usually manual or semi-manual.
Colleagues then typically repeat parts of the process manually to quality assure the outputs.

This way of working is time consuming and can be frustrating, especially where the manual steps are difficult to replicate quickly.
Processes like this are also prone to error, because the input data and the outputs are not connected directly, only through the analyst’s manual intervention.

More recently, the tools and techniques available to analysts have evolved.
Open-source tools like [Python](https://www.python.org/) and [R](https://www.r-project.org/) have become available.
Coupled with version control and software management platforms like [Git](https://git-scm.com/) and Git-services,
these tools have made it possible to develop automatic, streamlined processes, accompanied by a full audit trail.

RAP was [first piloted in the Government Statistical Service in 2017](https://dataingovernment.blog.gov.uk/2017/03/27/reproducible-analytical-pipeline/)
by analysts in the Department for Digital, Culture, Media and Sport (DCMS) and the Department for Education (DfE).
They collaborated with data scientists from the Government Digital Service (GDS) to automate the production of statistical bulletins.

To support the adoption of RAP across government, there is a network of [RAP champions](https://analysisfunction.civilservice.gov.uk/support/reproducible-analytical-pipelines/reproducible-analytical-pipeline-rap-champions/).
RAP champions are responsible for promoting reproducible analysis through the use of reproducible analytical pipelines,
and supporting others who want to develop RAP in their own departments.

<!-- file: book/modular_code.md -->

# Modular code

This chapter outlines principles that represent good practices for general programming and software development.
We have tailored these to support analytical workflows.

```{admonition} Pre-requisites
:class: admonition-learning

You will get the most benefit from this section, if you understand and are comfortable with core programming concepts such as:

* storing information in variables
* using control flow, such as if-statements and for-loops.
* writing code as functions or classes.
* using functions or classes in your code.

There are links in the [](learning.md) section of the book to relevant training.
```


## Motivation

Even experienced programmers can find it difficult to understand code that is repetitive, disorganised, or overly complex.
This makes assuring, testing or changing the code more burdensome.
You may also find it harder to spot and fix mistakes.

Code that isn't modular can cause a range of issues:

- walls of repetitive code that are hard to absorb.
- long, complex scripts that are hard to follow.
- over-complicated code where a simpler solution could be used.
- a code base that makes it difficult to find what you're looking for.

This chapter highlights ways to write modular code that is easy to read, review, and maintain.
These practices will also help you implement the other good coding practices you will come across in this book, such as version control, review, testing and documentation.
Because of this, modular code is fundamental to making analysis more reproducible, auditable and assured.


(modular)=
## Modular code

Improving readability often involves breaking your code down into smaller, more manageable chunks.
Regardless of the language, you can containerise your code into self-contained parts such as modules, classes, or functions.


(functions)=
### Write re-usable code as functions

In the early stages of analysis, we often copy and paste code to 'make it work'. As the code matures, it is worth taking repetitive code and turning it into functions.
Functions allow us to make a piece of logic reusable in a consistent and readable way, and also makes it easier for us to [test our logic](testing_code.md).

When starting to write functions, you should consider what is the right level of complexity for a single function.
A helpful starting point is to consider if the code containing the logic can be turned into a concise and readable function. Signs that the code is too complex to work as a single function are that the function is very long or you have to pass it lots of arguments to get it to work.
If this is what you find, it is usually best to break the code into multiple smaller functions. You can 
then use these smaller functions to build up a larger high-level function that performs the group of actions that you need.
Smaller functions also have the advantage that you might also be able to re-use them in other places in your code. For example, in other high-level functions that perform similar tasks.

This approach helps you break complex logic down into small, understandable chunks that can be documented and tested more easily.

When writing functions, it is also important to consider how they interact with other parts of your code.
As a general rule of thumb, your code should run in the same way if a call to your function was replaced by the value that it would have returned.
This is called 'referential transparency'.

In practice, this means that your functions should not depend on or affect variables that have not been explicitly fed into them as arguments.
For instance, a function should not add columns to a data table that has not been passed as an input to the function. It should not assume that data or other functionality exists if they have not been supplied as arguments or explicitly referenced from other libraries.
Nor should the action of a function be affected by anything other than arguments that are passed to it.
For example, running your function twice with the same inputs should always produce the same results.

Avoiding such behaviours makes your code more transparent;
it is easier for users and developers to understand which functions affect which data without being concerned about hidden behaviours.
In turn, this makes it easier to locate bugs in the code and assure its function by peer review.

When it is not possible or practical to follow these practices, you should ensure that any 'side-effects' are adequately documented for both users and developers.
This may be the case where your code interacts with a file, database or an external service.
Ultimately, signalling where these kind of things might happen, helps someone trying to debug issues know where to look.

To summarise:

- Make sure that functions are not overcomplicated;
break down your code into smaller functions and build up your functionality with larger functions from these small building blocks.
- Minimise the 'side-effects' of functions in order to make sure that your code is easy to debug and is transparent in its functionality.
- Strive to make sure that running your function with the same inputs will produce the same results every time.


### Group data and methods as classes

Classes are fundamental parts of [object-orientated programming (OOP)](https://en.wikipedia.org/wiki/Object-oriented_programming).
They create an association between data (attributes of the class) and logic (methods of the class).
Classes can be useful when representing real objects in our code, as the examples below demonstrate.

Although classes exist in R, [writing custom classes](https://adv-r.hadley.nz/oo.html) is less common than it is in Python (and other OOP enabling languages).
Because of this, the following sub-section will focus primarily on Python classes.

With a more complex system, OOP can help to reduce complexity by hiding low-level details from users, such as an internal state.

```{note}
An object's 'state' is usually a set of variables that are particular to a given instance of a class.
To illustrate, imagine a bank account that is represented by an `Account` class.
You can have many instances of this class (many unique bank accounts), each defined by the following internal state:

- owner name
- account number
- balance
```

When writing classes consider marking such state as 'private', since the end user does not need to know all of the state associated with an object.
This prevents users from accessing attributes directly, instead accessing them through class methods (functions defined with the class).

````{admonition} Method vs Function
When talking about methods, we mean functions that are strictly 'attached' to a given class.
The following example illustrates the difference between the two:

```python
# Defining a class with a diagnose method
class Car:
    """A car class"""
    wheels = 4
    def __init__(self, brand):
        self.brand = brand

    def diagnose(self):
        ...

# versus defining a standalone diagnosis function
def diagnose(car, ...):
    """A car diagnosis function"""
    ...


# Calling a method on a class instance that holds it's own state
cadillac = Car(brand="Cadillac")
cadillac.diagnose()

# Calling a function by passing all relevant information explicitly
# Note: for the sake of variety the information about the car is represented in a dictionary
diagnose({"brand":"Cadillac", "wheels":4})
```

````

In some languages 'private' state can be used to prevent access to parts of your class.
In Python [truly private instance variables do not exist](https://docs.python.org/3/tutorial/classes.html#private-variables),
so it is not possible to prevent access to any part of your class.
The standard convention in Python is to prefix attribute names with a single underscore (`_my_class_attribute`)
to indicate that users shouldn't be concerned with these attributes.

In addition to private attributes, you can use the same naming convention to indicate that a method is 'private' and should not be used by users.
This can be useful when writing reusable low-level methods within an object, analogous to breaking a large function down into multiple smaller functions.
These private methods can then be called by high-level methods that are exposed to users.

```{caution}
In Python, the notion of 'private' does not mean secure.
The main goal of private attributes and methods is to expose less unnecessary information to the anyone using your class in their code.
```

```python
class BankAccount:
    def __init__(self, balance, credentials):
        self._balance = balance
        self._credentials = credentials

    def _private_withdraw(self, amount):
        """Private withdrawal helper method."""
        self._balance -= amount

    def _check_credentials(self, credentials):
        """Private check helper method."""
        if credentials == self._credentials:
            return True
        else:
            return False

    def withdraw(self, credentials, amount):
        """Public withdrawal method."""
        if _check_credentials(credentials):
            self._private_withdraw(amount)
```

When using classes in our code, we care more about what methods a class provides than what `type` it is defined as.
This is known as 'duck typing'; if a class has the same methods as another class, then you can use either class in your code.

> If it walks like a duck, and it quacks like a duck, then it must be a duck.

Given the example above, if we created a class `LoyaltyAccount` with the same `withdraw` method for withdrawing points,
we could feasible switch between using the `BankAccount` and `LoyaltyAccount` classes without affecting how our code runs.

Object-Orientated Programming introduces the concept of inheritance - where a class can 'inherit' methods from another class in order to extend it.
In this situation, a new class 'subclasses' the 'superclass' or 'parent' that it is inheriting from.
When defining multiple classes with similar functionality, inheritance can be used to store the shared logic in a separate class type,
which we can then extend by subclassing.
For example, we might create an `Account` class to store a `balance` and the logic behind our `withdraw` method.
Our `BankAccount` and `LoyaltyAccount` could then subclass `Account` to extend it with any additional logic that is specific to their account types.

```{note}
[Liskov substitution](https://en.wikipedia.org/wiki/Liskov_substitution_principle) states that
subclasses should not damage the functionality of their parent class in their implementation.
They should extend their usefulness, but retain their original functionality.
If our `BankAccount` class inherits from `Account` we should consider that 'a `BankAccount` is an `Account`'.
Liskov substitution strengthens this statement to '`BankAccount` is interchangeable with an `Account`';
we can replace any `Account` with `BankAccount` without changing how our code runs.
This is because `BankAccount` provides all of the same methods that an `Account` does.

You can apply this similarly to functions.
If you were to increase the domain and range of a function, to account for new cases, then this function should observe the same interface as the previous function.

In short:

- You should be able to replace objects with instances of their subclasses, without altering the correctness of that program.
- You should be able to replace functions with similar functions that share the same interface.
```

However, we should be wary that inheritance locks our class in to the object that it inherits from.
If the superclass changes, our class is forced to change with it.
When using inheritance to reuse code from an unrelated class, 'encapsulation' may be more appropriate.
For example, a `Car` class might want to use a method from an `Engine` class, but a car could not be substituted for an engine.
It would not be suitable for `Car` to inherit from `Engine`.
Therefore, you might keep a private instance of the `Engine` class you wish to re-use, and delegate the work down to it in the `Car` methods.
Then, if you change your mind about using this `Engine` class in your `Car` class, you aren't tied to it and can easily replace it.

(interfaces)=
In OOP, an 'interface' can be defined to act as a blueprint or specification for writing classes.
An interface outlines the attributes and methods that a class must provide to be considered equivalent to a group of classes.
Perhaps we want to use classes to read and write data - this might require several different classes, with `read` and `write` methods for different file formats.
For example, one class could deal with storing data in a database, and another could store data in local `.csv` files instead.
In our code, we could switch which class is provided to downstream functions.
Our functions don't need to know if they are reading or writing from databases or `.csv` files,
however, they do require the `read` and `write` methods of the class to work in a standard way.
An `interface` would help to define the standard for interacting with this group of classes.

In Python, the `abc` module allows us to define ['abstract' base classes and methods](https://docs.python.org/3/library/abc.html)
to enforce that our classes provide the required methods.
When a subclass does not implement the required abstract methods, instances of the class cannot be created.
These abstract base classes achieve the same as interfaces in other object-based languages.
We can illustrate this concept in the following example:

```python
from abc import ABC, abstractmethod

class FileHandler(ABC):
    """An abstract class for reading and writing"""
    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def read(self, query):
        pass

class CsvHandler(FileHandler):
    ...
    def write(self, data):
       return write_to_file(data, self.filename)

    def read(self, query):
       data = read_csv(self.filename)
       data = parse(data)
       data = process(query, data)
       return data

class SqlHandler(FileHandler):
    ...
    def write(self, data):
       connect_to_database(self.connection_url)
       return write_to_database(data)

    def read(self, query):
       data = read_from_database(self.connection_url)
       data = process(query, data)
       return data
```

When multiple classes have a similar application programming interface (API, i.e. the methods they supply for users), we can easily switch between them.
A good real-world example of this can be seen in the `scikit-learn` package, where the different linear model types are represented by different classes.
Each linear model class supports a common set of methods, e.g. `fit()` and `predict()`.
As such, you can use any model in a pipeline and swap them out with minimal effort.
Therefore, when thinking about how to break you code up into classes, consider the use of standardised methods across similar objects to make them interchangeable.


(class-responsibilities)=

```{note}
A word of caution, when creating your own classes.
It is easy to start to mapping nouns in system descriptions to classes, and any adjectives applied to the nouns as methods.
For example: 'the model loads the data', which implies that `Model` is a class that should have a `load_data` method.
This works well for small systems, but as the complexity of your code grows you might find that one of your classes gains the majority of the underlying logic.
This often leads to one class with many methods, while other classes just store data with very few methods.
We describe this as 'Data Driven Design'.

When most of your code resides in a single class, this can indicate that this class is responsible for too much of your code's logic.
This class might become overly complex and hence difficult to maintain.
Consequently, changes to requirements will cause this one class to change, which may affect other unrelated functionality in the class.

For more complex analytical work, a better approach might be [Responsibility Driven Design](https://en.wikipedia.org/wiki/Responsibility-driven_design).
Here, we write small classes with a focussed responsibility.
This reduces complexity and helps classes to avoid being affected by changes to other, unrelated parts of our code.
However, be aware of the trade-off between the complexity of one large class versus many smaller classes.
```

[Responsibility Driven Design](https://en.wikipedia.org/wiki/Responsibility-driven_design) makes objects that are usually 'passive' become 'active'.
For example, with a banking system, an  object representing a bank account, and handling all money movements, might become overly complex.
Instead, objects representing `Cheques` and `Cash` might be designed with payment methods.
In this situation, a `Cheque` knows how much money it contains and how to pay itself into an account.
A `Cheque`'s responsibility is to retrieve money from its associated account and pay itself in to another bank account.
If we later needed to add new payment methods, the existing payment type classes (`Cheque` and `Cash`) will unlikely to be affected.
The bank account's responsibility is holding money, receiving it and paying it out.

```{tip}
Many [Design Patterns](https://en.wikipedia.org/wiki/Software_design_pattern) are available with OOP.
These are reusable solutions to common problems.
```

Finally, be wary when using classes to 'chain' methods together.
For instance, if a 'book' has a 'publisher' and the publisher has an 'address', you could write `book.publisher().address().postcode()`.
However, chains like this are fragile as they depend on multiple parts of the system not changing.
The 'Demeter' research project found that this style of code produce a high proportion of bugs,
resulting in the [Law of Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter): 'Only talk to your immediate friends'.
Namely, only access the objects you know about directly within a class.
This reduces the opportunity for your code to be damaged by a change in your dependencies.
There is a penalty for this - you replace with `book.publisherPostcode()` which internally would call `publisher.postcode()`,
so we've added a method to `publisher` as well as `book`; we're trading maintainability for complexity, so consider if it is worthwhile.

To summarise:

- Classes hide implementation detail from users, enabling implementation to be changed without affecting users.
- You should look to use consistent methods in a group of related classes, so that you can switch between them without affecting the code using it.
You should consider Python 'duck typing' or abstract classes and methods.
- You should avoid storing all logic in a single class. Instead, distribute logic based on responsibilities.
- Be aware of trading maintainability for complexity - one large class or too many classes can be hard to understand.
- You will find Design Patterns a useful toolbox as they have solutions to many common problems.
- You should opt for encapsulation over inheritance, especially with code reuse.


### Split complex code into multiple scripts

Scripts are simply files containing code that you would like to execute.
In Python you commonly have a `main.py` script that orchestrates part of your codebase to achieve an outcome.
In machine-learning projects, you sometimes have `train.py` and `test.py`, which are scripts that train the model and produce performance metrics.

Scripts, if written well, are reproducible.
In languages like R and Python, when executed from the command line using commands like `python main.py` or `Rscript main.R`
they are read top to bottom and executed line by line.
This is in contrast to running code in an interactive interpreter or notebook, where the human has control of the order of execution.
Manually executing individual lines of code risks creating errors when things are run in the wrong order. Rather, we recommend using end-to-end scripts.

Ultimately for code pipelines you will need to have some way of running your code - the script is
the primary way of orchestrating your functions and classes in a pipeline fashion.

```{note}
Using a script does not guarantee that your code will run reproducibly, but it does ensure that code is run in the same way across multiple runs.
```

To summarise:

- Scripts are a good way to orchestrate your functions and classes in order to build a simple, yet effective pipeline.
- They are text documents containing source code, which makes them easily human readable and auditable.
- They can be broken down into sections using [comments](code_documentation.md) for readability.


(modules)=
### Organise related classes and functions into modules

Simply put, modules are scripts that contain functions that you want to use in other scripts.
As you write your code and find opportunities to create classes or functions that reduce repetition and promote easier code comprehension,
you might decide that you want these functions to sit outside of your main pipeline script.
This is where modules come in, to separate reusable code into logical groups.

Consider a project where an analyst has created one large data analysis script.
Upon reflection, they decide to split the logic from their pipeline into groups of functions relating to 'data processing', 'data modelling', and 'result presentation'.
They then create a file to contain each of these groups of functions: `processing.py`, `modelling.py`, and `reporting.py`.
They decide that they want to have a pipeline script called `main`, but they want to keep this script readable and simple.
In R, it's best to also use an R project file.
Working within a project allows you to use relative file paths and avoid the need to refer to specific script locations.
Their directory now looks something similar to:

`````{tabs}

```` {tab} Python
```
project
├── main.py 
├── modelling.py 
├── processing.py 
├── reporting.py 
├── README.md 
```
````

```` {tab} R
```
project 
├── main.R 
├── modelling.R 
├── processing.R 
├── reporting.R 
├── README.md
└── project.Rproj 
```
````
`````

````{warning}
R projects are a really useful and simple way to organise your projects better.
However, be sure to check your settings.
R projects save history and data by default.
This is not a good idea if you're using git, as it means data can easily make its way into the version history.
To disable these options in RStudio, open the project options menu in the tools tab.
In the menu, set the options "save workspace to .RDATA on exit" and "Always save history" to "No".
Alternatively, you can edit the .Rproj file in an editor of your choice by adding these settings:

```
SaveWorkspace: No
AlwaysSaveHistory: No
```
````

They then import the relevant functions into the main script from their modules as follows:

````{tabs}
```{code-tab} py
import pandas as pd

from modelling import predict_results
from processing import clean, preprocess
from reporting import generate_report, export

data = pd.read_csv("data/path.csv")
data = preprocess(clean(data))
results = predict_results(data)
report = generate_report(results)
export(report)
```

```{code-tab} r R
# These relative file paths only work while working within an R project
source("modelling.R")
source("processing.R")
source("reporting.R")

data <- utils::read.csv("data/path.csv")
data <- preprocess(clean(data))
results <- predict_results(data)
report <- generate_report(results)
export(report)
```
````

```{note}
This is a minimal example of a pipeline script, illustrating how you might import reusable functions from other modules.
These main scripts lack the ability to configure things like the path to the input data.
This requires users to manually alter file paths in the code, which is highly discouraged.
```

``````{admonition} A step further
Another step that you can take to improve clarity is to further wrap these modules into their own folder like so:

`````{tabs}
````{tab} Python
```
project
├── library
│   ├── __init__.py
│   ├── modelling.py
│   ├── processing.py
│   └── reporting.py
├── LICENSE
├── main.py
└── README.md
```
````

```` {tab} R
```
project
├──R
│   ├── modelling.R
│   ├── processing.R
│   └── reporting.R
├── LICENSE
├── main.R
├── README.md
└── project.Rproj
```
````
`````
``````


(packages)=
### Organise and document your modules as packages

Programming languages often come with quite a few in-built functions and classes that are available to the end-users.
However, when it comes to solving specialised problems, these in-built functions are often not enough.
In these cases, you may need to build functionality to address a given problem from scratch.
If the solutions you build are useful and reusable, you can then wrap them up in a package to allow other users to install it.
They can then reuse the work you have put in within their own code to solve similar problems.

Packages are self-contained collections of code written by someone else to solve a particular problem.
For example, packages like `dplyr` and `pandas` are essential when performing data wrangling in R and Python, respectively.
They contain a toolbox of predefined functions that allows us to avoid rewriting this functionality from scratch every time.
Inside these packages is a set of [modules](modules) containing relevant functions, classes and other code that someone has written.
These are wrapped up into a package structure so that the programming language you use can understand, install and make available the code for you to import.

```{note}
This section will not cover the practices required to package and distribute your code as a package.
However if you would like to know more please look to the [code documentation section](code_documentation.md)
and seek out the packaging guides for your programming language.
```

It is useful to keep in mind the question:
is my code solving a problem that someone else has not already solved in my programming language?
If the answer is 'Yes' then perhaps it is worth considering wrapping up your code and distributing it wider.

```{note}
Packaging code properly will involve applying many of the recommendations from this book.

You will have to consider how to test, document and lay out your code for it to be usable and packagable.
In the end, high quality packages are the cornerstone of open-source package ecosystems.
However, it is not trivial to maintain and develop well-regarded open-source packages.

If you feel like you are writing code that you might consider turning into a package,
consult this book and strive to apply as many of the recommendations as you go.
This will make the final polishing and packaging much simpler, and will produce packages that are easier for third-parties to trust and use.
```


### Think carefully about whether notebooks are a suitable way to organise your code

Jupyter and other code Notebooks allow you to include live code alongside text and visualisation.
Although individual notebooks can seem like a good way to modularise your analysis for distribution, for larger projects this is not usually the best idea.

Notebooks are inherently difficult to review and audit through version control software like `git`.
Simple text files like scripts can be version controlled easily as you can see which lines of text change from one version to another.
Notebooks store their internal workings in a much more complicated format,
so seeing the changes as differences line by line is not possible in common version control tools.

Furthermore, defining and keeping functions within notebooks makes testing them more difficult.
It is not simple to test individual cells of a notebook with standard external tooling.

Lastly, one of the key issues with notebooks when they are used as methods for running a pipeline is the ability to run cells out of order.
In practice this means that a user can accidentally execute the steps of the analysis in the wrong order causing issues and different results.
As such, notebook results may not always be reproducible.

That said, great strengths of notebooks include their flexibility in displaying results while you are exploring data,
and their ability to present final research code alongside a narrative.
Therefore two good places to use notebooks in the project lifecycle is to:

- Explore and 'play' with the data while developing your methods.
- Turn notebooks into HTML reports to present results to end users.

In short, notebooks are not suitable for modularising analysis pipelines. However, they are a great way to do research analytics and to present results.
Therefore, as the exploratory part of your analysis draws to a close, or there is a need to produce similar analysis more regularly, it is wise to refactor notebooks.
Reusable functions and classes can be moved to modules and the main analysis pipeline might instead be reproducibly run from a script.
Here are a few suggestions to consider when refactoring code from notebooks:

- Review the repetitive cells and assess which of them can be turned into reusable functions.
- Extract existing functions into related groups, as modules.
- Document, test and improve these functions and modules following the guidance laid out in this book.
- Import the required functionality from these new modules into the notebook or pipeline script.
- For new analysis, reuse functionality from these modules in new notebooks and continue to document your analytical thinking alongside your code in these notebooks.

After this, you might turn existing notebooks into HTML to send them stakeholders, or save them as is so that analytical peers can re-run and review your notebooks.
The steps that you've taken to simplify your notebook code will make your code much easier to understand by readers.

Bear in mind that other analysts can still run notebook files out of order, so they should not be used as the main method of actually generating outputs.
Output generation should instead be trusted to scripts, where human decisions do not alter the order that code is run.

<!-- file: book/readable_code.md -->

# Readable code

The principles outlined in this chapter represent good practices for general programming and software development.
These have been tailored to analytical workflows.

```{admonition} Pre-requisites
:class: admonition-learning

To get the most benefit from this section, you should have an understanding of modular code, which was covered in the [previous chapter](modular_code.md).
You should also be familiar with core programming concepts such as:

* storing information in variables.
* using control flow, such as if-statements and for-loops.

You can find links to relevant training in the [](learning.md) section of the book.
```


## Motivation

```{epigraph}
Code is read more often than it is written.

-- Guido van Rossum (creator of Python)
```

When writing code, we should expect that at some point someone else will need to understand, use, and adapt it.
That someone might be you in six months time!
As such, it is important to empathise with these potential users and write code that is tidy, understandable, and does not add unnecessary complexity.
Doing this will make for a 'self-documenting' codebase that does not need as much additional documentation.

This chapter highlights good coding practices that will improve the readability and maintainability of your code.
Here, readability refers to how easily another analyst can gain a decent understand of how your code works, within a reasonable amount of time.
Maintainability refers to how easily other analysts can understand your code well enough to modify and repair it.


## Clean code

```{epigraph}
Programs are meant to be read by humans and only incidentally for computers to execute.

-- Donald Knuth, The Art of Computer Programming
```

Code with high readability is often referred to as 'clean code'.
Clean code helps us understand a program faster, as it avoids points of confusion and ambiguity.

The following sections set out some key aspects of writing clean code that are fairly widely applicable.
That said, each individual programming language has idiomatic ways of writing code that are specific to its features.
Additionally, each language usually has some form of accepted style guide.

Make sure to consult the style guides for your language as first point of call.
It is important to stress this point, as these guides will capture the most up to date guidance for your language of choice,
which may not be available in this document.


(naming)=
### Use informative names

The most important aspect of clean code is the naming of identifiers within your code.
This includes variables, functions, classes, constants and any other objects that can be assigned a name.

Someone reading your code will benefit greatly if you use names that are:

- informative and not misleading.
- concise but not cryptic.


(naming-variables)=
#### Give variables clear and concise names

You may have previously come across code that contains variable names that are meaningless, or that imply an incorrect purpose:

````{tabs}
```{code-tab} py
import pandas as pd

x = "Sioban"

y = 42

z = pd.DataFrame()

my_favourite_number = "ssh, I'm a string"
```

```{code-tab} r R
x <- "Sioban"

y <- 42

z <- data.frame()

my_favourite_number <- "ssh, I'm a string"
```
````

Another developer, or even 'future you', would be unable to correctly interpret what these variable names to represent.
Therefore, you should try very hard to avoid cryptic or single-letter identifiers.

That said, there are situations where some seemingly cryptic identifiers make sense.
Using single letters to name variables is suitable when implementing methodologies from mathematical notation.
However, even in these cases you must make sure that the formulas being implemented are clear,
readily available to the reader and are consistent throughout your code.
Be sure to cite the source of the mathematical formula in these cases.

In other cases, using variable names that contain a few (3 or so) informative words can drastically improve the readability of your code.
Your language of choice will impact how you separate words (be it `CamelCase` or `snake_case`).

````{tabs}
```{code-tab} py
import pandas as pd

# Defining variables
first_name = "Sioban"

number_of_attendees = 42

empty_dataframe = pd.DataFrame()


# Using variables
print("Hi " + first_name)

number_of_attendees += 1

empty_dataframe.empty
```

```{code-tab} r R
# Defining variables
first_name <- "Sioban"

number_of_attendees <- 42

empty_dataframe <- data.frame()


# Using variables
paste("Hi", first_name)

number_of_attendees <- number_of_attendees + 1

plyr::empty(empty_dataframe)
```
````

Ideally, the purpose of variables should be clear from reading their names.
In addition, the variable names should make logical sense in the context that they are used later on in the code.
This removes the need for explanatory comments, as your intentions can be interpreted from the code itself ('self-documenting' code).

Naming is important for distinguishing between similar variables.
A first instinct might be to assign numerical suffixes or other similar tags to differentiate variables.
However, unless the suffix itself is meaningful within the context of the rest of the code, it will not make the code more understandable:

````{tabs}
```{code-tab} py
letters_1 = ["a", "b", "c"]
letters_2 = ["x", "y", "z"]
```

```{code-tab} r R
letters_1 <- c("a", "b", "c")
letters_2 <- c("x", "y", "z")
```
````

Here we can infer what these lists and vectors contain, but it is not apparent what makes `letters_1` different to `letters_2`.

Variable names can be used to document differences between variables, or to incrementally describe changes made to a variable.

````{tabs}
```{code-tab} py
letters_first_three = ["a", "b", "c"]
letters_last_three = ["x", "y", "z"]

letters_first_three_reversed = reversed(letters_first_three)
```

```{code-tab} r R
letters_first_three <- c("a", "b", "c")
letters_last_three <- c("x", "y", "z")

letters_first_three_reversed <- rev(letters_first_three)
```
````

Here the naming convention indicates that both lists are similar, but also describes the differences between them.
It is also clear how the third, new list relates to the first list that was used to create it.

With more informative names, we obviously lose the brevity of variable names:

```none
letters_first_three_reversed_plus_t_minus_a_converted_to_greek
```

There is a clear trade-off between the usability and informativeness of variable names.
You'll need to use your best judgement to adapt variable names in order to keep them informative but reasonably concise.

```{note}
You will be more aware of this trade-off in languages like Python, where indentation is part of the syntax to denote code blocks.

The PEP8 style guide for Python recommends line widths of 79 characters. Having overly descriptive names might impact your compliance with a style guide.
```


(naming-functions)=
#### Name functions after the task that they perform

You should respect the best practices already covered in the [Naming variables](naming-variables) when naming functions.
However, there are a few other points worth raising that are exclusive to function and method names.

Firstly, your user should be able to infer the purpose or action of a function from its name.
A warning sign that your function may be overly complex or require further detail in its documentation is when you find that you can't describe the overall task performed by the function in a few words.

It can be effective to describe the specific task a function performs in its name, starting with a verb:

````{tabs}
```{code-tab} py
def process_text(data):
    ...

processed_text = process_text("The following document was handled using...")
```

```{code-tab} r R
process_text <- function(data) {
    ...
}

processed_text <- process_text("The following document was handled using...")
```
````

This is often a tidy way to structure high-level functions in your pipeline.
Well defined, verb-based names often lead to clear pipelines such as:

```` {tabs}
``` {code-tab} py
data_path = "path/to/data"

# in short
report_data = generate_report( model( clean( load( data_path ))))

# or, more explicitly
data = load(data_path)
clean_data = clean(data)
model_results = model(clean_data)
report_data = generate_report(model_results)
```

``` {code-tab} r R
data_path <- "path/to/data"

# in short
report_data <- generate_report(model(clean(load(data_path))))

# or, more explicitly
data <- load(data_path)
clean_data <- clean(data)
model_results <- model(clean_data)
report_data <- generate_report(model_results)
```
````

Naming a function in the form of a question is useful when in cases where a function responds with a Boolean (True or False) value.

````{tabs}
```{code-tab} py
def are_missing_values_present(data):
    if None in data:
        return True
    else:
        return False
```

```{code-tab} r R
are_missing_values_present <- function(data) {
  if (NA %in% data) {
      TRUE
  } else {
      FALSE
  }
}
```
````

This improves the readability of code that applies these functions.

````{tabs}
```{code-tab} py
if is_clean(data):
   model(data)
```

```{code-tab} r R
if (is_clean(data)) {
    model(data)
}
```
````


#### Make classes easy to identify

Class names are usually started with a capital letter, and in `CamelCase`, as this differentiates them from `variableNames` and `variable_names`.
Class names follow the same advice as for [](naming-functions) - namely, is it obvious from the class name what it does?
If it is too complex to name concisely, it is an indication of too many [responsibilities](class-responsibilities)
and you should refactor your code into more, smaller classes.

Method names in a class closely follow the requirements for [](naming-functions), as methods are just functions that are tied to a class.
They should ideally read clearly when called from a class instance - such as `bookParser = TextParser(book_data)` followed with `bookParser.getNextWord()`.
Compare this against `bp = Reader(book_data)` then `bp.fetch()`, where there is not enough context.

(code-style)=

``` {note}
Writing custom classes is more common in Python than in R, as discussed in the [](modular_code.md) chapter. As such, the examples above only apply to Python. 
```


### Make code easier to read by following a consistent style

Programming languages can differ in lots of ways.
One way R and Python differ, for example, is their use of indentation.
Indentation is part of the well defined syntax of Python but is not for R.
This does not mean that you shouldn't use indentation in R to make your code more readable.
If in doubt, you should consider consulting how to use formatting to write more readable code by finding the style guidelines for your language.

Generally, code style guides provide a standard or convention for formatting and laying out your code.
The purpose of these style guides is to increase consistency across the programming community for a given language.

They might include how to appropriately:

- comment or document your code.
- name your functions, variables or classes.
- separate elements of your code with whitespace.
- use indentation to make sure your code is readable.
- provide other useful guidance regarding formatting.

The existence of such style guides does not necessarily mean that each individual or team will apply these conventions to the letter.
Organisations and developer teams often have needs that might not be addressed in a general style guidance document.
After all, these documents aim to capture the needs of a diverse group of developers.
Therefore, these guides are more useful as starting points in a discussion on 'how should our team be consistent internally in the way we write code?'.

```{figure} ./_static/code_quality.png
---
width: 80%
name: code_quality
alt: Comic strip describing a brutal code review.
---
Code Quality, from [xkcd](https://xkcd.com/1513/)
```

The core idea around these guides is that individual teams have to either adopt them or adapt them for use while writing code.
The goals are readability and consistency.
This consistency between developers will most likely aid speed of development and review,
as well as the ability of one developer to comprehend code written by their colleagues.

```{admonition} Common Style Guides
[PEP8](https://www.python.org/dev/peps/pep-0008/) is an official Python style guide, which is widely used.
The [Google](https://google.github.io/styleguide/Rguide.html) and [tidyverse](https://style.tidyverse.org/) style guides are commonly used for R.
```


#### Write code that other programmers will find easy to read

There is perhaps a misconception that following style guidelines and formatting your code accordingly is the fundamental goal of writing good code in a given language.

In reality, guidelines may encourage code-reviews to focus on style over more fundamental problems with the code.
They have the potential to detract from assessment of whether the code is making the best use of a given language.

The notion of style goes beyond simple spacing or capitalisation.
In the same way that knowing and using common idioms such as 'over the moon' or 'cold feet' make you seem like a more fluent speaker of English,
a part of being fluent in a programming language is being able to write 'idiomatic' code.
Idiomatic stands for 'using, containing, or denoting expressions that are natural to a native speaker'.
In Python, idiomatic approaches to writing code are commonly referred to as 'pythonic'.

This might mean simplifying complex and perhaps hard to read patterns into a simpler, but well established alternative.
For example, the pieces of code below are equivalent:

````{tabs}
```{code-tab} python
# Example 1 - very unpythonic
i = 0
my_data = []
while i < 100:
  my_data += [i * i / 356]
  i += 1

# Example 2 - more use of Python features, such as `range` and `append`
my_data = []
for i in range(100):
  my_data.append(i**2 / 356)

# Example 3 - making full use pythonic idioms, `range` with list comprehension
my_data = [i**2 / 356 for i in range(100)]
```

```{code-tab} r R
# Example 1 - not idiomatic
i = 0
my_data = c()
while (i < 100) {
  my_data = c(my_data, i * i / 356)
  i = i + 1
}

# Example 2 - more use of R features, e.g. `append` and idiomatic assignment (' <- ')
my_data = c()
for (i in 0:100) {
  my_data <- append(my_data, i^2 / 365)
}

# Example 3 - making  use of R's built-in vectors
my_data <- (0:100) ^ 2 / 365
```
````

The ability to write idiomatic code in a given language comes with time.
However, it is important to think about it while looking at a given piece of code: is it using everything that language 'X' has to offer?

That said, we should still prefer readability over idioms that might make our code more complex.
For example, attempting to fit too much logic into a single line of code can make it considerably harder to understand.


(automate-style-checks)=
#### Automate style checks

Following a style guide from the beginning of a project is good practice.
However, checking that code continues to follow a particular style, or to fix code formatting when it doesn't can be tedious.
Hence, automated support can be sought to speed up this work,
either by providing suggestions as the code is written or by reformatting your code to comply with some style.

See [](linters-formatters) for further information on automating these checks.


(software-ideas-for-analysts)=
## Software ideas for analysts

It's important to remember that when we write code for analysis, we are developing software.
Over many years, software engineering teams have developed good practices for creating robust software.
These practices help to make our code simple, readable, and easier to maintain.
Analysts using code as a means to perform analysis can benefit from at least partially applying such practices in their own codebases.

This chapter will try to condense key messages and guidelines from these practices, for use by analysts who write code.
Reading and learning more about these practices will likely to benefit the quality of your code and is highly encouraged.


### Keep it simple

The ability to convey information in a simple and clear way matters.

This is particularly true when explaining concepts that are already complex.
You are often trying to solve problems that are complex in nature when writing code.
You should avoid introducing extra complexity to these problems, wherever possible.

Here are a few tips to make sure you keep your project nice and simple:

- Solve the problem - do not get distracted and make sure you have a clear outcome in mind.
- Try not to 'reinvent the wheel' - use existing packages when they already have functionality that solves the problem.
They will most likely be better documented and won't need extra maintenance.
- Split your code into understandable parts - consider how to [make your code modular](modular).
- Don't over-engineer your solution - if it is understandable and works, refrain from over-complicating for the sake of small increases in efficiency.
- When you have a choice of alternative packages to do the same thing, use one and stick to it. For example, the R packages dplyr and sqldf both enable the use of selection and filtering operations. Stick to one unless there is a very good reason to use both. When choosing between alternatives, think about their familiarity for other coders, ease of use and efficiency.

```{note}
It's important to capture the requirements of your code before writing it.
This includes when your code needs to be adapted to meet changing needs.
You should then aim to meet these requirements in the functionality that your code provides.

It can be tempting to try to account for every eventuality in your program, but developing anything more than these requirements may not be beneficial.
There's a good chance that many cases that you account for will never occur, so you should try to prioritise based on what you're certain is needed from your code.

> You ain't gonna need it

Remember that additional features will require more documentation and testing to ensure that they are working correctly.
Really consider if adding these extras will make your code more or less maintainable, user-friendly and correct. 
```

Lastly, it is worth stressing that complex problems might require complex solutions.
In those cases make sure that you only introduce complexity where it is needed.
You should address necessary complexity with proportionate quality assurance - through documentation, testing and review.
For instance, if the execution time of your code is critical, then making the code more complex to achieve a faster runtime may be an acceptable trade-off.


### Don't repeat yourself

In the section on [modular code](modular), you were encouraged to refactor your code into more self-contained components for ease of testing,
reproducibility and reusability.
However, it is worth stressing that 'quick and dirty' solutions often involve copy-pasted code that is functionally identical.
This is expected and is natural in the initial stages of a project.
Nonetheless, repetition not only wastes your time, but it also makes your code more difficult to read.
Consider a script that contains three copies of a similar piece of code.
If the code that is used to perform the repetitive task is found to be incorrect, or if a developer wishes to modify the task being performed by this code,
they must implement a similar change in each of the three copies.
If only two copies were spotted and amended, there is now a bug sleeping in the code waiting to be triggered...
Moreover, anyone reviewing the code would need to check that the right logic is being used three times over.

To put this in context, let us use an example where the developer wants to get the odd numbers from three different lists of numbers:

````{tabs}
```{code-tab} py
# Note: this is an example of bad practice
first_ten_numbers = list(range(1, 11))
second_ten_numbers = list(range(10, 21))
third_ten_numbers = list(range(20, 31))

odd_first = []
for number in first_ten_numbers:
    if number % 2 == 1:
        odd_first.append(number)

odd_second = []
for number in second_ten_numbers:
    if number % 2 == 1:
        odd_second.append(number)

odd_third = []
for number in third_ten_numbers:
    if number % 2 == 0:
        odd_third.append(number)
```

```{code-tab} r R
# Note: this is an example of bad practice
first_ten_numbers <- 1:10
second_ten_numbers <- 11:20
third_ten_numbers <- 21:30

odd_first <- c()
for (number in first_ten_numbers) {
  if (number %% 2 == 1) {
    odd_first <- c(odd_first, number)
  }
}

odd_second = c()
for (number in second_ten_numbers) {
  if (number %% 2 == 1) {
    odd_second <- c(odd_second, number)
  }
}

odd_third = c()
for (number in third_ten_numbers) {
  if (number %% 2 == 0) {
    odd_third <- c(odd_third, number)
  }
}
```
````

In this example, the third repeated snippet of code actually collects even numbers, but incorrectly assigns them to the `odd_third` variable.
Because each copy looks very similar, you might assume that all copies of the code are performing the same task.
Even when you are aware of the difference between the copies, you might be unable to tell if the difference is intentional or a mistake.
The example demonstrates how repetition can add confusion when trying to maintain or review code.

Modifying multiple copies of a code snippet is laborious and presents a risk - some copies of the repeated code may be modified,
while others erroneously remain the same.
This is analogous to modifying the formula in individual cells of a spreadsheet.
If you refactor repetitive code into functions or classes, then bug fixes or modifications need only be carried out once to change all uses of that code.
New, intended behaviour is then consistently given by each call of the function or method.

The following presents how one could change the previous example for the better:

````{tabs}
```{code-tab} py
def get_odd(numbers):
    """Get only the odd numbers"""
    return [number for number in numbers if number % 2 == 1]

first_ten_numbers = list(range(1, 11))
second_ten_numbers = list(range(20, 21))
third_ten_numbers = list(range(20, 21))

odd_first = get_odd(first_ten_numbers)
odd_second = get_odd(second_ten_numbers)
odd_third = get_odd(third_ten_numbers)
```

```{code-tab} r R
get_odd <- function(numbers) {
# Get only the odd numbers
  numbers[numbers %% 2 == 1]
}

first_ten_numbers = 1:10
second_ten_numbers = 11:20
third_ten_numbers = 21:30

odd_first = get_odd(first_ten_numbers)
odd_second = get_odd(second_ten_numbers)
odd_third = get_odd(third_ten_numbers)
```
````

If the functionality of `get_odd` needs to be modified, it now need only be done once.
Additionally, this code is more concise and its purpose is easier to interpret.

`````{note}
If two slightly different tasks must be carried out, for example you need both the odd and the even numbers, you might approach this in one of two ways:

- Develop two functions containing the different elements of code, with names that express the difference in their purpose.
- Add a parameter to your function that will allow a user to differentiate between the two tasks.

````{tabs}
```{code-tab} py
# Simple and modular
def is_odd(number):
    """Check if a number is odd."""
    if number % 2 == 1:
        return True
    else:
        return False

def get_odd(numbers):
    """Get only the odd numbers."""
    return [number for number in numbers if is_odd(number)]

def get_even(numbers):
    """Get only the even numbers."""
    return [number for number in numbers if is_odd(number) == False]


# More concise, but also more complex - not always best
def get_numbers_with_parity(numbers, parity):
    """Get numbers with a given parity ('odd' or 'even')."""
    if parity not in ["odd", "even"]:
        raise ValueError("parity must be 'odd' or 'even'")
    remainder = 1 if parity == "odd" else 0:
    return [number for number in numbers if number % 2 == remainder]

odd_numbers = get_numbers_with_parity(list(range(1, 11), "odd"))
```

```{code-tab} r R
# Simple and modular
is_odd <- function(numbers) {
  ifelse(numbers %% 2 == 1, TRUE, FALSE) 
}

get_odd <- function(numbers) {
  numbers[is_odd(numbers)]
}

get_even <- function(numbers) {
  numbers[!is_odd(numbers)]
}

# More concise, but also more complex - not always best
get_numbers_with_parity <- function(numbers, parity) {
  numbers_with_parity <- c()
  if (parity == "odd") {
    remainder <- 1
  } else if (parity == "even") {
    remainder <- 0
  } else {
    stop("parity must be 'odd' or 'even'")
  }
  
  numbers[numbers %% 2 == remainder]
}

odd_numbers <- get_numbers_with_parity(1:10, "odd")
```
````

You should use your best judgement to decide which is most appropriate in a given situation.
`````

It can be difficult to decide when repetition warrants refactoring of code into reusable functions or classes.
The 'Rule of Three' suggests that if similar code has been written more than two times,
then it is worth extracting its logic to a reproducible procedure like a function or class.
However, as you write code you should try to anticipate whether it is likely to be reused in future.
If the answer is yes, you might opt to write it straight into something more modular and reusable.


### Be explicit

In the literary sense of the word!

```{epigraph}
Explicit is better than implicit

-- The Zen of Python (`import this`)
```

In some programming languages, it is possible to perform a task or decision by relying on an implied interpretation of your code.
For example, in Python `1`, `100`, `["A list of text"]` and many other objects evaluate to `True`, while `0`, `[]` and `None` evaluate to `False`.

To make your intentions clear, you should explicitly state your intended comparison in the code.

````{tabs}
```{code-tab} py
student_count = None

# Relying on falseness of None
if student_count:
    print("There are " + student_count + " students!")
```

```{code-tab} r R
student_count <- FALSE

# Relying on falseness of FALSE
if (student_count) {
  paste("There are", student_count, "students!")
}
```
````

In the example above, the student count is not printed because `None` and `FALSE` evaluate to `False`.
In Python and R, `0` will also evaluate to `False`.
Therefore, it is unclear whether the programmer intended that the statement is printed when the count is 0.
If a count of 0 should be printed, then this lack of specificity has created a bug.

To perform the same decision explicitly, we should specify the exact condition under which the student count should be printed.

````{tabs}
```{code-tab} py
student_count = 0

# Explicitly print only if more than 0
if student_count >= 0:
    print("There are " + student_count + " students!")
```

```{code-tab} r R
student_count <- 0

# Explicitly only print if more than 0
if (student_count >= 0) {
  paste("There are", student_count, "students!")
}
```
````

Now the count is printed if it is more than or equal to 0.
It's clear that we intend for this to be the case.


### Separate responsibilities

> An object should have a single responsibility.
> Only changes to one part of the software's specification should be able to affect the specification of the class.

The 'single responsibility' principle suggests that a single element of your code (a function or class)
should be responsible for a single part of your software's functionality.
It should take on one task and perform it well.
This is because each piece of code is more robust if there are fewer reasons to change it in the future.

When you work with code that is designed to multitask,
it is often difficult to modify this code without having an unintentional effect on other aspects of the software.

Imagine trying to create a model of the economy, which is a complex web of interconnected interactions.
Creating 'abstractions' in the form of classes or functions that try to model multiple aspects of the economy at once might seem helpful,
but when used incorrectly might instead add to the complexity.

For example, consider a class that represents a whole country (`Country`).
This would represent a model that is trying to predict economic statistics for a country such as unemployment or inflation.
One can imagine that this class will quickly grow into something unmanageable, as its responsibilities grow in the form of additional methods and attributes.

Based on the other chapters in this guidance, you might eventually realise that you need to break this class down further.
If you had applied the idea of single responsibility,
you might have broken the `Country` class down into smaller components such as `UnemploymentModel`, `InflationModel`.
These classes would be responsible for doing specific modelling, while the `Country` class might only responsible for presenting the results to,
let's say, a higher level economy model that tries to model cross-country trade.

This simplicity also increases usability, by minimising the number of parameters that each function or class might require.

```{note}
If you remember the [section on interfaces](interfaces),
the different model classes here are a prime example where defining an interface would help you make sure each `*Model` object is interchangeable.
```

The 'separation of concerns' principle captures a similar concept to single responsibility, but on a higher level.
This principle suggests that your software should be separated into distinct sections that each address a single concern.

In the previous economic modelling example, you might establish your concerns to be:

- Model economy at low level: `UnemploymentModel` and `InflationModel`.

  These are concerned with the 'low-level' details of giving estimates of economic output.
  They are independent of each other and concerned only by what they are trying to estimate.

- Model country level interactions and trade blocks: `Country` and `TradeBlock`.

  These parts of your code relate to higher level concepts.
  They will be using the lower level `Model` classes, but are primarily concerned with interactions between countries.

- Run simulations given a description of the desired economy.

  Once the model is ready, there might be a `SimulationRunner` that takes in your model of the world economy and runs simulations.
  In this case, this part of your codebase will only revolve around running the actual simulations.

In each of these distinct sections of your codebase there will be multiple classes and functions,
which should follow the single responsibility concepts outlined earlier.

For example, within the section of your code concerned with modelling data, you might have a set of functions to download data from an external data store.
These functions should only be responsible for receiving the required data safely and providing it to the `Model` object.
If you had the need to download data from different sources online (i.e., Database, CSV or other), you might create several download functions.
To pick the right function for each model you might create a ['LoaderFactory'](<https://en.wikipedia.org/wiki/Factory_(object-oriented_programming)>)
who's only responsibility is to provide the `Model` with the right loading function for the right data source.

```{figure} ./_static/separation_of_concerns.png
---
width: 80%
name: separation_of_concerns
alt: Representation of concerns and responsibilities within a piece of software.
---
Representation of concerns and responsibilities within a piece of software
```

As such, separate sections of your software should be responsible for each of the concerns.
Within each section of your software, distinct functions or classes should be responsible for each task that is required for that section's overall functionality.

```{admonition} In the context of functions
The previous example was heavily focused on classes and Object-Oriented Programming. The same principles apply in the world of functions.
You define each concern that is addressed by a module containing functions who follow the single responsibility principle.

So the previous example could equally include:

- An `unemployment_model` - function running the unemployment modelling.
- An `inflation_model` - function running the inflation modelling.

These functions would produce data about a given country, to be stored in an object.
Another function might then take these data for multiple countries and start modelling it across country boundaries.

The same core concepts still fully apply.
```


### Make functions open to extension, but closed for modification

This means that it should be possible to extend the functionality of classes or functions, without modifying their source code or how they work.

````{tabs}
```{code-tab} python
# some function that we want to keep closed for modification
def core_method(data):
    ...
    return result

# if we want to extend a function without modifying it, we can always do the following
def extended_functionality(results):
     ...
     return extended_result

def extended_methodology(data):
     core_results = core_method(data)
     return extended_functionality(core_results)
```

```{code-tab} r R
# some function that we want to keep closed for modification
core_method <- function(data) {
  ...
  return(result)
}

# if we want to extend a function without modifying it, we can always do the following
extended_functionality <- function(result) {
  ...
  return(extended_result)
}

extended_methodology <- function(data) {
  core_results = core_method(data)
  return(
    extended_functionality(core_results)
  )
}
```
````

The same applies to classes through ideas like inheritance.

When you think about the consequences of this, the open-closed principle gives you:

1. Confidence that essential behaviour of parts of your code should not be expected to change.
2. The ability to easily add more functionality, as your code evolves.

````{note}
In functional programming we use higher-order functions and functional composition to enact these principles.
'Functional composition' deserves a brief explanation, as a concept that might be keenly used in a data analytics pipeline.

In simple terms, functional composition is a mathematical idea that takes two functions $f$ and $g$ and produces function $h$, such that $h(x) = g(f(x))$.
Analysts familiar with R's `%>%` operator will find this idea familiar.

Imagine you have a task to perform modelling and report generation from data.
You can lay out your code to be easily composable with the following functions, with single responsibilities:

- `load` - loads data.
- `model` - runs the model on data.
- `report` - runs report generation.

So when it comes to creating a pipeline you end up with something like:

````{tabs}
```{code-tab} python
report = report(model(load(filepath)))

```

```{code-tab} r R
report <- report(model(load(filepath)))
```
````

We will now assume that these individual functions are closed for modification.
However, we can extend the functionality of `load` by adding a `clean` function that cleans the data. In which case, we end up with:

````{tabs}
```{code-tab} python
# We can extend this without modifying the source code of `load`
report = report(model(clean(load(filepath))))

# or we can first define a new load as follows
def new_load(filepath):
    return clean(load(filepath))

report = report(model(new_load(filepath)))

# or with the help of anonymous (lambda)
new_load = lambda data: clean(load(data))
report = report(model(new_load(filepath)))

# We can even use this to create a single function to run our defined pipeline
pipeline = lambda data: report(model(clean(load(filepath))))
report = pipeline(filepath)
```

```{code-tab} r R
# We can extend this without modifying the source code of `load`
report <- report(model(clean(load(filepath))))

# or we can first define a new load as follows
new_load <- function(filepath) clean(load(filepath))

report <- report(model(new_load(filepath)))

# We can even use this to create a single function to run our defined pipeline
pipeline <- function(data) report(model(clean(load(filepath))))
report = pipeline(filepath)
```
````

<!-- file: book/project_structure.md -->

# Structuring your project

When you are designing your analysis it can be difficult to keep your thoughts tidy.
Analysis is often exploratory and subject to change.
This means that scripts and programs can become messy.
The messier the programs, the harder they are to maintain and change in future.

Good directory structure and file hygiene can go a long way to mitigate this.
It will help others to read your code more easily, and you will write better code into the bargain.
Some structures have been found to be generally quite effective through trial and error.
Others are more specific, and - as with all guidelines - should not be taken as mandatory.


## Run scripts from end to end to ensure your code is executed reproducibly

As you begin developing your project, it's a good idea to save your working code in a script file.
In R these are saved as `.R` files, and in Python as `.py`.
You can use scripts within an Integrated Development Environment (IDE) like
[Visual Studio Code](https://code.visualstudio.com/), [RStudio](https://rstudio.com/), or [PyCharm](https://www.jetbrains.com/pycharm/).
Inside an IDE you can usually run through your script line-by-line, or run the whole file at once.
This can be an easier workflow than running code in the Python or the R console and then rewriting the same code in a script later.

Scripts serve as the basic units of saved code.
Often, we like to define functions or reusable bits of code in one file and then use these in another file.
For example we may write a few functions that help us to calculate `mean`, `mode`, and `median` of our dataset in the `functions.R` file.
Then we can use those functions in our main script, saved in `main.R`.

Outside of an IDE you can also run your scripts using the Python or R interpreters from the command line.
Other programs can then use your scripts because of this.
For example you can use the `Rcmd <script-path>` command to run your R scripts or the `python <script-path>` command to run your Python scripts.

Running your analysis files from end to end ensures that your code is executed in the same order each time.
It also runs the code with a clean environment, without variables or other objects from previous runs that can be a common source of errors.


## Keep your project structure clean

As your analysis project grows it becomes more important to keep your project structure clean.
Every project is different and the right way to organise your project might differ from another project.
However, there are some principles that are useful to consider.


### Use good filename conventions

Much like the names of elements in your code, good filenames inform you of the purpose of a file.
Within a project, you should follow a standard file naming convention.
Good naming practices improve your ability to locate and identify the contents of files.

Good naming conventions include:

* Consistency, above all else.
* Short but descriptive and human readable names.
* No spaces, for machine readability - underscores (`_`) or dashes (`-`) are preferred.
* Use of consistent date formatting (e.g. [YYYY-MM-DD](https://en.wikipedia.org/wiki/ISO_8601)).
* Padding the left side of numbers with zeros to maintain order -  e.g. `001` instead of `1`. The number of zeros should reflect the expected number of files.

When using dates or times to name files, start with the largest unit of time and work towards the smallest.
So we would use `2020-10-15_data_input`, and not `15-10-2020_data_input`.
This will ensure that the default ordering of these files is in chronological order.
This makes it much easier to find the earliest or latest files.

You should start filenames with numbers to order files, if ordering is logical and informative.
For example, where the `001_introduction` should come before `002_methodology` and `003_results`.


### Organise analysis as a Directed Acyclic Graph

Analysis can best be thought of as a Directed Acyclic Graph (DAG).
Don't let the name scare you off!
All we mean by this is that you start off with the input data, you finish with the output(s), and in between there are no lines that link backwards.

```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Tred-G.svg/800px-Tred-G.svg.png
---
width: 50%
name: dag
alt: Analysis is a directed, acyclic graph that links the input data through a series of steps to the outputs.
---
Defining analysis as a DAG - linking the input data at (a) to the output at (e).
```

When thinking about how to structure your project it is useful to think in terms of what your project's DAG looks like.
Each project should be kept in its own folder, with a descriptive name.
Most analysis will have an ingest or input stage, a processing stage, and a reporting stage.
You should use folders within each project to separate raw data, documentation, source code (or `src`) and results.

A typical analytical project folder in Python might look like:

```` {tabs}
``` {code-tab} py
|-- README.md
|-- requirements.txt
|-- data/
|   -- incident_counts.csv
|-- docs/
|   -- notebook.md
|   -- manuscript.md
|   -- changelog.md
|-- results/
|   -- incident_counts_by_age.csv
|   -- incidents_over_time.svg
|-- src/
|   -- data_cleaning.py
|   -- main_analysis.py
|   -- generate_plots.py
```

``` {code-tab} r R
|-- README.md
|-- project.Rproj
|-- data/
|   -- incident_counts.csv
|-- docs/
|   -- notebook.md
|   -- manuscript.md
|   -- changelog.md
|-- results/
|   -- incident_counts_by_age.csv
|   -- incidents_over_time.svg
|-- R/
|   -- data_cleaning.R
|   -- main_analysis.R
|   -- generate_plots.R
```
```` 

Where you have written code that is used by multiple projects, this code should reside in its own separate folder.
This will allow you to record changes to your code independent of other dependencies of each project.


### Preserve raw data

You should not alter raw data - treat it as read-only.
You should conduct data cleaning on a copy of the raw data, so that you can document which cleaning decisions have been made.

Your project structure should include an immutable store for raw data. This does not have to be inside the code repository and it is usually best to separate operational folders for inputs and outputs from the code base.


### Check that outputs are disposable

You should be able to dispose of your outputs, deleting them, without worrying, because you should be able to regenerate them easily by re-running your pipeline.
If you are worried about deleting your outputs (i.e., results) then it is likely you lack confidence in reproducing your results.

Frequently deleting and regenerating your outputs when developing analysis is good practice.


## Structure code as modules and packages

Code that is complex, high risk or reusable between projects can benefit from being structured into a package.
Modules are single files that contain one or more reusable units of code.
A package typically contains multiple related modules.

It's likely that you've already used a package written by somebody else as part of your analysis.
For example, installing additional functionality for Python using `pip install <package>` on the command line or
running `install.packages("<package>")` in an R interpreter.

```{admonition} Key Learning
:class: admonition-learning

[The Python Packaging User Guide](https://python-packaging-user-guide.readthedocs.io/) describes good packaging practices using the most up-to-date Python tools.
While [the R Packages book](https://r-pkgs.org/) provides a comprehensive summary of packaging in R.
[The rOpenSci packaging guide](https://devguide.ropensci.org/building.html) also contains useful tips for packaging in R.
```

See [](project_documentation.md) for a summary of common package and project documentation types.


## Use project templates

Many analysts choose to use similar structures for multiple projects even though project structure can be flexible.
Consistency in structure makes it easier to navigate unfamiliar projects, especially if they use the same coding style.
It means that members of the team can quickly orient themselves when joining an existing project or starting a new one.

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) is a command-line tool that creates projects from templates (cookiecutters).
Using an existing cookiecutter, or creating one to meet your needs, can be a useful way to increase consistency in structure between your projects.
Increase consistency and good practice by creating common folder structures, laying out essential documentation or even starting off your code with a basic boilerplate.
This can also save you time. Laying out a structure to include documentation and code testing also encourages  good practices.

Useful cookiecutters include:

* The government data science [govcookiecutter](https://github.com/ukgovdatascience/govcookiecutter), including data security features.
* The comprehensive Python data science project template [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/).
* The Python package template [cookiecutter-pypackage](https://cookiecutter-pypackage.readthedocs.io/en/latest/).

Rstudio provides a standard template for R packages via `File > New Project... > New Directory > R Package`.
We have created some basic templates for an [R package](https://github.com/best-practice-and-impact/example-package-r)
and a [Python package](https://github.com/best-practice-and-impact/example-package-python) that may be helpful.
R project structures can also be set up or extended, one component at a time, using the [`usethis` workflow package](https://usethis.r-lib.org/). usethis() sets up packages that follow the structure in the R packages book.
For example, `use_test()` will add the directories necessary for testing using `testthat` and generate basic test file templates for a given function name.


## Use version controlled repositories

Repositories or 'repos' are typically project folders that are version controlled using Git or a similar version control system.
One repository usually contains a single project.
Developing your project using a version controlled repository has significant benefits for reproducibility.

See [](version_control.md) for more information.

<!-- file: book/code_documentation.md -->

# Code documentation

```{epigraph}
Documentation is a love letter that you write to your future self.

-- Damian Conway
```


## Comments

> Use comments sparingly and with purpose

Comments are lines of text in source code files that typically are not executed as part of the program.
They are small notes or annotations written by those working on the code.
Often, they provide context or explain the reasoning behind implementation decisions.

Comments are essential for explaining non-obvious details around around how and why the code has been written in a particular way to help those working on the code in the future.
As such, when it comes to providing relevant and perhaps higher-level documentation to the end consumer on the functionality of your code,
there are much more appropriate solutions such as [docstrings](docstrings).

Although extremely useful, you should use code comments sparingly.
Excessive use of code comments often leads to redundancy and can, ironically, make your code harder to read.
It is easy to fail to update comments as you change code. However, outdated and irrelevant comments are likely to confuse or mislead.

```{note}
**Remember**: the only point of 'truth' is the code that is executed - if the comments are out of date compared to the actual code, this may not be immediately obvious.
```

````{tabs}

```{code-tab} py
# Set number_1 to 5
number_1 = 5

# Set number_2 to 9
number_2 = 9

# Set total to the sum of number_1 and number_2
total = number_1 + number_2
```

```{code-tab} r R
# Set number_1 to 5
number_1 <- 5

# Set number_2 to 9
number_2 <- 9

# Set total to the sum of number_1 and number_2
total <- number_1 + number_2
```

````

Comments that describe exactly **what** is occurring in the code, like the examples above, are usually unnecessary.
They are usually redundant if you follow [good naming practices](naming) to self-document the steps that occur in your code.
For a more detailed description of **what** the code does, the developer can also read more appropriate forms of documentation (see [docstrings](docstrings) below).

If it is difficult to understand your code without comments,
this can indicate that your code is too complex and might benefit from being broken down, or 'refactored', into smaller units.
That said, sometimes you will be faced with functions and classes that are complex for a reason.
Stopping to reflect on why your documentation is so large is a good prompt to consider whether refactoring is in order.

````{note}
```{epigraph}
Simple is better than complex.
Complex is better than complicated.

-- Zen of Python
```
For complex methodologies, it is hard to completely eliminate complexity and it will eventually have to 'sit' somewhere.
This is natural, as real-world problems can be complex.
The key is to manage that complexity without adding to it.
````

Comments can be used more effectively to explain **why** you have written code in a certain way.
For example, you might explain to other analysts and developers why a section of your code doesn't follow standard practices,
perhaps because the typical method didn't work.
This type of comment helps to clarify your decision-making process, without needing to describe the individual steps taken.

In short, comments that explain **why** you made programming choices will help your future self and other developers to understand your intentions.

```{code-block}
# Tried solution X, but Y worked better because of Z

# Don't use function X here, because of Y

# Temporary work around for bug in function X
# TODO: fix function X, so that Y

# This section of code is commented out because of X
```

Comments are sometimes used to divide long sections of code into sub-sections that relate to their overall functionality.
The merit of doing this will depend on the value added.
For example, the code below is already fairly self-documenting and therefore adding the section headings does not add much value.

````{tabs}

```{code-tab} py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


## Get data
penguins = sns.load_dataset("penguins")

## Analyse
species_means = penguins.groupby("species").mean()

## Report
plt.plot(penguins.bill_length_mm)
species_means.to_csv("penguin_species_mean_measurements.csv")
```

```{code-tab} r R
library(palmerpenguins)
library(dplyr)


## Get data
penguins_data <- penguins

## Analyse
species_means <- penguins_data |>
  dplyr::group_by(species) |>
  dplyr::summarize(across(where(is.numeric), mean, na.rm = TRUE))

## Report
plot(penguins_data$bill_length_mm)
utils::write.csv(species_means, "penguin_species_mean_measurements.csv")
```

````

Leaving unused code in your scripts makes them much more difficult to read and understand. Blocks of commented out code add visual noise to anyone trying to understand your code at pace.
Furthermore, relying on someone to comment and uncomment things to alter the functionality of the code is **highly discouraged**.
Doing so reduces the reproducibility of your analysis, increases the risk that incorrect functionality is deployed and adds to the time and effort needed to get the code to run as intended.

````{tabs}

```{code-tab} py
print("Run me!")
# print("Don't run me...")
```

```{code-tab} r R
print("Run me!")
# print("Don't run me...")
```

````

It is very easy to forget which parts of code have been commented out and why they have been commented.
A human factor is then introduced, which might not be accounted for if someone in the future is not aware of the commented-out code. This can introduce significant risk.    
It is likely to produce inconsistent runs of the same piece of code.
The code might quickly become out of sync with the rest of the changes in the codebase,
as developers may not consider updating code that is commented out if they assume it is obsolete.

You should instead use appropriate control flow (such as `if/else` statements) to determine when sections of code should be run.
Consider [defining these options in a dedicated configuration file](configuration.md) when changes are required between individual runs of your analysis. Using configuration files means that developers do not need to edit the code base to change the behaviour of your pipeline. Instead, they can just update the configuration.

In summary, use comments sparingly but purposefully.    
Make sure comments:

- explain **why** certain things are done, in order to provide context around the decisions that you have made.
- do not repeat what your code is already telling the reader.
- are accurate and still relevant after code changes.


(docstrings)=
## Docstrings

When your code is structured as functions or classes, these functional units can be efficiently documented using docstrings.
Docstrings are specialised multi-line descriptions that appear at the start of a function definition and are the de facto way of documenting these individual components.    

In practice they can be either strings (as in Python docstrings) or comments (as in R comments).
Note that module or script level docstrings are also commonly used (usually at the top of the module file in the case of Python).
Use of docstrings keeps the documentation of your code closely associated with the relevant sections of code.
This close association means it is easier to keep documentation up to date as changes are introduced to the code.

An end-user can access these docstrings by typing `help(function_name)` after they have imported your library,
so they are handily available without needing to have the source code files open in another window.
Other tools, like Jupyter for Python, allow users to easily access these docstrings for quick reference.
Hence the focus on detail and comprehensiveness is key - this is the first point of call for an end-user trying to understand what a given function does.

Docstrings commonly describe:

- what the function or class does
- what parameters the function or class takes as arguments and their types
- what the code returns
- what common errors can occur and the exceptions they'll raise
- links to or descriptions of the methodology the function implements
- example usage of the function
- references to other functions or classes that are related to this function

But in general, there is scope to add any information that you consider relevant to an end-user of this particular function.

````{tabs}

```{code-tab} py
def add_to_each(numbers, to_add):
    """
    Adds a number to each number in a list.

    Parameters
    ----------
    numbers : list
        Numbers to add `to_add` to.
    to_add : int or float
        Number to be added to each element of `numbers`.

    Raises
    ------
    TypeError
        if `numbers` is not a list.

    Returns
    -------
    list
        `numbers` with `to_add` added to each element.

    Examples
    --------
    >>> my_numbers = [2, 4, 6, 8]
    >>> add_to_each_in_list(my_numbers, 3)
    [5, 7, 9, 11]

    See Also
    --------
    add : Adds two numbers
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    new_numbers = [number + to_add for number in numbers]
    return new_numbers
```

```{code-tab} r R
#' @title Add to a vector
#' 
#' @description Add a number to elements of a vector.
#' 
#' @details Cycles through a vector of numbers and adds a user-specified number to each element.
#' 
#' @param numbers A vector of numbers.
#' @param add A float or integer to be added to each element of \code{numbers}.
#' 
#' @return \code{numbers} with \code{add} added to each element.
#' 
#' @seealso \code{\link{add}}
#' @examples
#'  add_to_each(list(1, 2, 3), 5)
#' 
#' @export
add_to_each <- function(numbers, add) {
  if (!(is.vector(numbers) & is.numeric(numbers)) {
    stop("'numbers' must be a numeric vector.")
  }
  numbers + add
}
```

````

In this example, the function docstring starts with a brief description.
It then lists the parameters that our function takes, along with the suggested type for each parameter and a brief description of what they control.
It also tells us that the function will raise an error if the wrong type is provided for the first parameter.
Note that the listed errors are the errors that are expected by the writer of the documentation,
other unexpected issues can still occur if the function is not properly tested and will not be signposted in the docstring.
Then there is a description of the object that is returned from the function, followed by an example of the functions use.
Finally, it references a similar related function that might be of interest to the end-user.

The R example uses a format called [roxygen](https://roxygen2.r-lib.org/).
You should use roxygen formatting to write function documentation as part of R packages.
If you are documenting functions that are not part of a package, you can use regular code comments.
However, documenting functions using roxygen syntax is very helpful if you are planning on packaging the code in future and gives a clear and standard structure to your documentation.

You might find that writing function, class, or package descriptions before writing their code helps you to focus on the task at hand.
The documentation should be a specification of what the code is expected to do.
As documentation tends to be user-focused, this approach helps you to keep the user's needs in mind when developing code and
provides a quick reference when more information on its capabilities are required.

Lastly, one of the key things to remember when writing docstrings is to **keep them up to date**.
If these crucial bits of information no longer represent what the code actually does, the end-user will be misled.
This might lead to problems ranging from wasted time to serious methodological implications or even outputs that are plain wrong.

Therefore, write your docstrings early, preferably as you go along or even beforehand when you have a clear idea of what you want to implement.
Make sure to update them as you change the functionality of the code.
Good function or class level documentation is an essential habit to develop when writing professional working code.

```{note}
**Docstrings conventions and styles**

The Python example above follows the [numpydocs style](https://numpydoc.readthedocs.io/en/latest/format.html)
and is a common sight when using the `numpy` python package.
However, there are various other standards such as [the Google style guides for docstrings](https://google.github.io/styleguide/)
as well as official [docstring specification for Python](https://www.python.org/dev/peps/pep-0257/).
The R example uses the [roxygen2 package](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html) and follows the [tidyverse style guide](https://style.tidyverse.org/documentation.html).

In general, the core idea behind style is **consistency**.
Whatever alterations to these conventions you use for your particular area,
it is much more important to keep them up to date and consistent between your collaborators than the exact choice of a style guide.
However, as you will see in the section on [generating documentation](generating_docs),
having a well-known standard in place helps you to find tools that can generate clear, simple and hostable documentation automatically.

Other useful resources include:

- [Python docstring convention](https://www.python.org/dev/peps/pep-0257/)
- Guidance for [documenting objects and functions in R](http://r-pkgs.had.co.nz/man.html)
```


### Document scripts or modules using docstrings

Docstrings are not just for function documentation.
You will often want to include explanatory notes alongside modules containing multiple functions or standalone scripts.

In those cases, the structure is a lot looser and will depend on what the script is intended to do.
The docstrings should be brief and avoid repeating details found in function documentation or other code comments later in the script.
You may want to include:

- A title.
- A brief description.
- Any important usage notes not covered elsewhere.
- Any copyright information if the script reproduces open source code from elsewhere.
- Academic citations, if applicable.

````{tabs}

```{code-tab} py
"""
Data cleaning 

Functions to tidy and clean ingested csv and SQL data
"""
```

```{code-tab} r R
# Data import functions
#
# Functions to tidy and clean ingested csv and SQL data
```

````

The examples above document a simple module as part of an analysis package. The notes are brief and explain the main purpose of the module.
Please note: in R, it is acceptable to include either multiple functions per file or have separate files for each function.
You do not need to include module documentation if a file only contains one function.

````{tabs}

```{code-tab} py
"""
Duck census main analysis 

Produces the duck census bulletin outputs for the annual publication.

Check the configuration file before running and run from the command line. 
Detailed setup and desk instructions can be found in README.md.

"""
```

```{code-tab} r R
# Duck census main analysis 
#
# Produces the duck census bulletin outputs for the annual publication.
#
# Check the configuration file before running and run from the command line. 
# Detailed setup and desk instructions can be found in README.md.
```

````

These examples document a main analysis script.
They include enough information that a user can get started, without repeating too much that should be documented elsewhere.


(generating_docs)=
## Generate documentation automatically

This section describes tools that automate generation of searchable, user-friendly HTML documentation that can really provide a great experience for end-users.
Accurate, up to date and accessible documentation is one of the cornerstones of well-adopted, open-source packages.

Perhaps it is worth reflecting on truly how much we use well-rendered documentation for our favourite programming packages.
It would be much harder it to adopt these packages to solve hard programming problems if they were not well-documented and their documentation was not easily accessible.

The information presented in this section seeks to inform you of how you can take your well-crafted [docstrings](docstrings)
and turn them into more widely accessible hosted documentation.


### Generate HTML documentation


#### Python

For Python, we recommend the Python package [`sphinx`](https://www.sphinx-doc.org/en/master/) for generating HTML documentation.
Sphinx primarily uses the [`reStructuredText`](https://docutils.sourceforge.io/docs/user/rst/quickstart.html) markup language, which is similar to `markdown`.
That said, for those more familiar with `markdown` and in teams/environments where learning a new markup language is not a top priority,
[`sphinx` can be extended to also support `markdown`](https://www.sphinx-doc.org/en/master/usage/markdown.html).

Sphinx supports code highlighting for multiple programming languages within a project. However, you may require other tools to automatically collate documentation from code in languages other than Python. These are not addressed here.

Sphinx also supports theming, with a [myriad of themes](https://www.writethedocs.org/guide/tools/sphinx-themes/) available out of the box.
You can even develop and adapt the existing themes into a custom theme suitable for your work with a little bit of extra time.

`Sphinx` allows users to develop extensions that extend its functionality, as well as theming support.
This GitHub repository provides a list of [useful ways to extend the functionality of `sphinx`](https://github.com/yoloseem/awesome-sphinxdoc) to suit your needs.

To illustrate how this can be extremely useful, we will introduce the [doctest extension](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html).
It searches your existing docstrings for the `Examples` section and runs all of the included snippets of code, warning you if they do not run successfully.
This means that you can ensure that your examples written in the documentation run to completion.
Although this can't replace thorough code testing, it may help you to spot a whole slew of issues stemming from potentially out of date documentation
and examples that no longer apply when the code has been fundamentally altered.


#### R

For R projects, you might want to consider [`pkgdown`](https://pkgdown.r-lib.org/).
This package will create a HTML references section, containing your code documentation.
It uses your project's README file as a home page for the site and you can add additional content to the site in the form of [vignettes](https://r-pkgs.org/vignettes.html).

The [package's website](https://pkgdown.r-lib.org/) and [its source code](https://github.com/r-lib/pkgdown/)
provide a good demonstration of how you would apply it in practice.


### Make human readable documentation easily available to users

Once built, the HTML files containing your documentation can be opened in any browser.
Usually this means looking for an `index.html` file in the output directory and opening it with your browser.
This is sufficient for local usage. However, it is wise to host this documentation somewhere where it will be publicly available to improve the end-user experience and remove the need to browse the files looking for `index.html`.

Your version control platform might support hosting web pages already.
GitHub provides this hosting via [GitHub Pages](https://pages.github.com/) and is able to host not only documentation,
but any web page virtually for free. The book that you're reading right now is hosted in this way.
In many cases, you may also be able to automatically update your hosted documentation using [Continuous Integration](continuous-integration) practices.

[Read the docs](https://readthedocs.org/) is a community-funded project that provides hosting for open source projects and
is a great place to host any rendered documentation.

### AI coding assistants

You may have access to an AI coding assistant that you can ask to generate module and function documentation for you. AI assistants can be very effective and can save you a lot of time. If you use one, always check that the documentation it produces is correct, clear and concise and manage your expectation by providing well-defined, bounded requirements. Do not expect a coding assistant to document your entire application correctly with minimal intervention.

<!-- file: book/project_documentation.md -->

# Project documentation

Documenting your project will makes it much easier for others to understand your goal and ways of working, whether you're developing a package or collaborating on a piece of analysis.


## README

When working on a collaborative or open coding project, it's good practice to describe an overview of your project in a README file.
This allows users or developers to grasp the overall goal of your project.
As well as a description of the project, it might include examples using your code or references to other associated projects.
This file can be any text type, including `.txt`, `.md`, and `.rst`, and can be associated with your automated documentation.

We suggest the following for a good README:

- Short statement of intent.
- Longer description describing the problem that your project solves and how it solves it.
- Basic installation instructions or link to installation guide.
- Example usage.
- Screenshot if your project has a graphical user interface.
- Links to other project guidance, for example methodological papers or document repositories.
- Links to related projects.


## Contributing guidance

When collaborating, it is also useful to set out the standards used within your project.
This might include particular packages required for certain tasks and guidance on the [code style](code-style) used in the project.
Consider including a code of conduct if you plan to have contributors from outside your organisation.
Please [see GitHub](https://docs.github.com/en/github/building-a-strong-community/adding-a-code-of-conduct-to-your-project) for advice on creating a code of conduct.

See the CONTRIBUTING file from our [gptables package](https://github.com/best-practice-and-impact/gptables/blob/master/CONTRIBUTING.md) for an example:

`````{tabs}

````{tab} Markdown
```{code-block}
# Contributing

When contributing to this repository, please first discuss the change you wish
to make via issue, email, or any other method with the owners before making a change.

## Pull/merge request process

1. Branch from the `dev` branch. If you are implementing a feature name it
`feature/name_of_feature`, if you are implementing a bugfix name it
`bug/issue_name`.
2. Update the README.md and other documentation with details of major changes
to the interface, this includes new environment variables, useful file
locations and container parameters.
3. Once you are ready for review please open a pull/merge request to the
`dev` branch.
4. You may merge the Pull/Merge Request in once you have the sign-off of two
maintainers.
5. If you are merging `dev` to `master`, you must increment the version number
in the VERSION file to the new version that this Pull/Merge Request would
represent. The versioning scheme we use is [SemVer](http://semver.org/).

## Code style

- We name variables using few nouns in lowercase, e.g. `mapping_names`
or `increment`.
- We name functions using verbs in lowercase, e.g. `map_variables_to_names` or
`change_values`.
- We use the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html)
format for documenting features using docstrings.

## Review process

1. When we want to release the package we will request a formal review for any
non-minor changes.
2. The review process follows a similar process to ROpenSci.
3. Reviewers will be requested from associated communities.
4. The `dev` branch will only be released once reviewers are satisfied.
```
````

````{tab} HTML
<h1>Contributing</h1>

When contributing to this repository, please first discuss the change you wish
to make via issue, email, or any other method with the owners of this
repository before making a change.

<h2>Pull/merge request process</h2>

1. Branch from the `dev` branch. If you are implementing a feature name it
`feature/name_of_feature`, if you are implementing a bugfix name it
`bug/issue_name`.
2. Update the README.md and other documentation with details of major changes
to the interface, this includes new environment variables, useful file
locations and container parameters.
3. Once you are ready for review please open a pull/merge request to the
`dev` branch.
4. You may merge the Pull/Merge Request in once you have the sign-off of two
maintainers.
5. If you are merging `dev` to `master`, you must increment the version number
in the VERSION file to the new version that this Pull/Merge Request would
represent. The versioning scheme we use is [SemVer](http://semver.org/).

<h2>Code style</h2>

- We name variables using few nouns in lowercase, e.g. `mapping_names`
or `increment`.
- We name functions using verbs in lowercase, e.g. `map_variables_to_names` or
`change_values`.
- We use the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html)
format for documenting features using docstrings.

<h2>Review process</h2>

1. When we want to release the package we will request a formal review for any
non-minor changes.
2. The review process follows a similar process to ROpenSci.
3. Reviewers will be requested from associated communities.
4. Only once reviewers are satisfied, will the `dev` branch be released.
````
`````

In this case we have outlined our standard practices for using version control on GitHub,
the code style that we are using in the project and the review process that we follow.
We have used the [Markdown](https://daringfireball.net/projects/markdown/syntax) (`.md`) markup language for this document,
which is formatted into HTML when viewed on our repository.


## User desk instructions

If your project is very user focused for one particular task,
for example, developing a statistic production pipeline for other analysts to execute,
it is very important that the code users understand how to appropriately run your code.

These instructions should include:

- How to set up an environment to run your code (including how to install dependencies).
- How to configure the project, for example how to set folders and environment variables if you use them.
- How to run your code.
- What outputs (if any) your code or system produces and how these should be interpreted.
- What quality assurance has been carried out and what further quality assurance of outputs is required.
- How to maintain your project (including how to update data sources).


## Dependencies

The environment that your code runs in includes the machine, the operating system (Windows, Mac, Linux...), the programming language, and any external packages.
It is important to record this information to ensure reproducibility.

The simplest way to document which packages your code is dependent on is to record them in a text file.
We typically call this text file `requirements.txt`.

Python packages record their dependencies within their `setup.py` file, via `setup(install_requires=...)`.
You can get a list of your installed python packages using `pip freeze` in the command line.

[R packages](https://r-pkgs.org/) and projects record their dependencies in a [DESCRIPTION](https://r-pkgs.org/description.html) file.
Packages are listed under the `Imports` key.
You can get a list of your installed R packages using the `installed.packages()` function.

You will find environment management tools, such as
[`renv`](https://rstudio.github.io/renv/articles/renv.html) for R or
[`pyenv`](https://github.com/pyenv/pyenv) for python useful for keeping track of software and package versions used in a project.


## Citation

It can be helpful to provide a citation template for research or analytical code that is likely to be referenced by others.
You can include this in your code repository as a `CITATION` file or part of your `README`.
For example, the R package `ggplot2` provides the following:

```none
 To cite ggplot2 in publications, please use:

 H. Wickham. ggplot2: elegant graphics for data analysis. Springer New York,
 2009.

A BibTeX entry for LaTeX users is

@Book{,
   author = {Hadley Wickham},
   title = {ggplot2: elegant graphics for data analysis},
   publisher = {Springer New York},
   year = {2009},
   isbn = {978-0-387-98140-6},
   url = {http://had.co.nz/ggplot2/book},
 }
```

If your project includes multiple datasets, pieces of code or outputs with their own
[DOIs](https://en.wikipedia.org/wiki/Digital_object_identifier), this might include multiple citations.

See this [GitHub guide for more information on making your public code citable](https://guides.github.com/activities/citable-code/).


## Vignettes

Vignettes are a form of supplementary documentation, containing applied examples that demonstrate the intended use of the code in your project or package.
Docstrings may contain examples applying individual functional units, while vignettes may show multiple units being used together.
We use the term vignette with reference to R packages, for example this introduction to the
[`dplyr` package](https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html) for data manipulation.
However, the same long-form documentation is beneficial for projects in any programming language - for instance the
[`pandas` basics guide](https://pandas.pydata.org/docs/user_guide/basics.html).

We've seen that [docstrings](docstrings) can be used to describe individual functional code elements.
Vignettes demonstrate the intended use for these classes and functions in a realistic context.
This shows users how different code elements interact and how they might use your code in their own program.

Another good example is this vignette describing [how to design vignettes](http://r-pkgs.had.co.nz/vignettes.html) in Rmarkdown.
You can produce this type of documentation in any format, though Rmarkdown is particularly effectively at combining sections of code,
code outputs, and descriptive text.

You might also consider providing examples in an interactive notebook that users can run for themselves.


## Versioning

Documenting the version of your code provides distinct points of reference in the code's development.
Recording the version of code used for analysis is important for reproducing your work.
Combining versioning with [](version_control.md) allows you to recover the exact code used to run your analysis, and thus reproduce the same results.

[Semantic versioning](https://semver.org/) provides useful rules for versioning releases of your code.
Follow these rules to help other users of your code  understand how changes in your code may affect their software.
Each level of version number indicates the extent of changes to the application programming interface (API) of your code,
i.e., the part of the code that a user interacts with directly.
Changes to the major version number indicate changes to the API that are not compatible with use of previous versions of the code.
While changes to the minor and patch numbers indicate changes that are either compatible or have no effect on the use of the code, respectively.

```{figure} ./_static/semantic_versioning.png
---
width: 70%
name: semantic_versioning
---
[Semantic versioning](https://semver.org/)
```

You'll see this, or a similar version numbering, on packages that you install for Python and R.

Changes to this book don't cause backwards-compatibility issues in the same sense as code.
We've chosen to use a form of calender versioning ([CalVer](https://calver.org/)).
You'll see the current version below the site's table of contents, where the first four digits represent the year that latest changes were made.
The incremental number following the full stop indicates how many versions of the guidance have been published in that year.
As this guidance will change over time, this version number provides users with a reference for citing a specific state of the guidance.


## Changelog

A changelog records the major changes that have occurred to a project or package between versioned releases of the code.

```{code-block}
# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2020-01-21
### Added
- `add_to_each_in_list()`
- online sphinx-generated documentation
- contribution guide

### Removed
- `subtract_to_each_in_list()`

### Changed
- Improved function documentation

### Fixed
- bug in `multiple_each_in_list()`, where output was not returned
```

Like versioning, users find a changelog is useful to determine whether an update to your code is compatible with their work, which may depend on your code.
It can also document which parts of your code will no longer be supported in future version and which bugs in your code you have addressed.
Your changelog can be in any format and should be associated with your code documentation, so that it is easy for users and other contributors to find.

[keep a changelog](https://keepachangelog.com/en/1.0.0/) provides a simple but effective template for recording changes to your code.


## Copyright and Licenses

Copyright indicates ownership of work.
All material created by civil servants, ministers, government departments and their agencies are covered by
[Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/).
It is not essential to include a copyright notice on your work, but doing so can help to avoid confusion around ownership. We recommend including one in government projects.

Licenses outline the conditions under which others may use, modify and/or redistribute your work.
As such, including a license with code is important for users and other developers alike.
This [online tool](https://choosealicense.com/) might help you to choose an appropriate license for your project.
The Government Digital Service generally recommends using the
[MIT license](https://opensource.org/licenses/MIT) for code and the
[Open Government License (OGL)](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) for documentation.

Both copyright and license are usually placed in a LICENSE file in your project.
For example, an MIT LICENSE file might look like:

> Copyright 2020, Crown copyright
>
> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
> to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
>and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
> INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
> IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
> WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Open source your code

In government, we [support and promote open source](https://www.gov.uk/service-manual/service-standard/point-12-make-new-source-code-open) whenever possible.
[Open source](https://opensource.com/resources/what-open-source) software is software with source code that anyone can freely inspect, modify and enhance.
As a government analyst, you should aim to make all new source code open, unless you can justify witholding part of your source code.

Open sourcing code benefits you, other government analysts, and the public.

Personal benefits from open sourcing include:

- Attribution - coding in the open creates a public record of your contributions to analysis and software.
- Collaboration - you can gain experience working with analysts in other departments.
- Review - peers and experts in the field can provide advice on improving your analysis and coding.
- Feels good - we regularly benefit from open source software, so it's nice to give something back.

While the public benefit from:

- Transparency - stakeholders can understand and reproduce our analysis, which is a core element of the [Statistics Code of Practice](https://code.statisticsauthority.gov.uk/).
- Sharing value - others can benefit from our work, either through reuse or demonstration of good practices.
- Sharing opportunity - others can gain insight and experience from reading and possibly contributing to  your code.

Please see the [Government Data Service (GDS) guidance](https://www.gov.uk/government/publications/open-source-guidance/when-code-should-be-open-or-closed)
for help deciding when code should be open or closed.
Further
[GDS guidance](https://www.gov.uk/government/publications/open-source-guidance/security-considerations-when-coding-in-the-open) addresses security concerns for coding in the open. Additional guidance on deciding when and how to open source, the benefits, and good practice is available from the [Analysis Function](https://analysisfunction.civilservice.gov.uk/policy-store/open-sourcing-analytical-code/).

<!-- file: book/version_control.md -->

# Version control

Version control is managing changes to your analysis over time.
In this chapter, we primarily discuss the benefits of using [the Git version control system](https://git-scm.com/).

```{admonition} Pre-requisites
:class: admonition-learning

To get the most benefit from this section, you should have a basic understanding of how to use Git.
Many of the examples used in this section refer to the command-line interface for Git, so general command-line knowledge may also help. 

```

You can find links to relevant training in the [](learning.md) section of the book.

## Keep an audit trail of changes

As we discussed in [](principles.md), an audit trail is essential for assuring quality analysis.
It's important for us to be able to answer the following questions about our analysis:

* What changes have been made to our project?
* When were those changes made?
* Why were those changes made?
* Who made those changes?

Version control software, like Git, records the answers to these questions throughout the development of a project.
We can detail our development decisions alongside changes, using commit messages and Pull or Merge Requests.
In turn, this keeps our analysis workspace clean of commented-out old code and numerous files containing previous versions.

```{figure} https://imgs.xkcd.com/comics/documents.png
---
width: 30%
name: file_names
alt: Comic demonstrating poor file naming, like "Untitled 138 Copy.docx".
---
Documents, from [xkcd](https://xkcd.com/1459/).
This work is licensed under a [Creative Commons Attribution-NonCommercial 2.5 License](https://creativecommons.org/licenses/by-nc/2.5/).
```

Effective use of version control helps us to identify which changes have negatively impacted our work and remove them.
Furthermore, a detailed audit trail allows us to refer to specific versions of our code that have been used to produce outputs,
which is important for reproducing our analysis.

Git is invaluable when recording and combining changes from multiple developers, as merging allows us to resolve conflicts between overlapping changes.
A remote Git repository maintains a single source of truth, even when multiple individuals are working on a project.
Additionally, version control platforms, like GitHub and GitLab, can make it easier to track and review ongoing work.
This avoids duplication of effort and keeps review embedded in the development workflow.


## Include code and documentation in version control

Ideally, you should include all code and documentation that is required to understand and run your analysis.

This may include:

* Project documentation including readme and contribution guidance.
* Packaged functions and code documentation.
* Unit tests.
* Dummy data and example configuration files.
* User documentation such as desk notes and installation guidance.

## Exclude sensitive information from version control

In a public repository, you may need to omit confidential or sensitive aspects of the project.

```{caution}

You should **never** include the following in your code repository:

* Passwords, credentials or keys.
* Real configuration files.
* Code that contains sensitive information.
  * for example, code that describes a method for fraud detection.
  * or code that contains references to personally identifiable data.
  * or code that might compromise security protocols.
* Data, except for small example datasets.
```

See [](excluding-from-git) for details on how to mitigate the risk of including sensitive information in a Git repository.

It is again worth stressing the importance of not committing sensitive, unpublished, or disclosive data to your Git history.
If you would like to include an example for end-users, a minimal dummy dataset can be committed to the repository.
When creating realistic dummy data, care should be taken not to disclose sensitive features of the true data such as distributions and trends.
Dummy data should always be carefully peer reviewed before being added to a repository.


## Using Git for version control

Git is a distributed version control system.
This means that all users have access to a complete and self-contained history of changes to a given project.
The software can be used to record local changes, with the option of then synchronising these changes with a central, remote repository.
Remote repositories are typically hosted on a platform like GitHub or GitLab.

The following sections describe useful concepts for using Git to version control your analysis.
We use examples of Git commands throughout, but do not provide detailed descriptions of Git usage.
If you are not familiar with using command line tools, or Git specifically, you should first look into [introductory training](git-learning).


### Write short and informative commits

Commits are collections of changes to one or more files in a repository.
Every commit is attributed to the author of the changes, providing an audit trail.
Each commit has a unique hash - or identifier - associated with it, which has a long (e.g., `121b5b4f18231e4ee32c9c61f6754429f9572743`) and short version (e.g., `121b5b4`).
These hashes allow us to refer to specific changes, but each commit also has an associated message that is used to describe the changes.

```{note}
When adding changes to be included in a commit, you should preferentially add individual files or directories.
For example, using `git add src/my_file.txt` rather than a catch-all like `git add .`.
This specificity ensures that only intended changes are included, reducing the likelihood of including unrelated changes or files that should not be versioned
(when they are not included in `.gitignore`).
Using `git status` after adding changes can help to confirm that only the desired changes are included.
```

Most commit messages are short and informative, but in some cases you may want to provide more detail.
Common standards follow this model commit message from ["A note about Git commit messages"](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html):

```{code-block} text
Capitalized, short (50 chars or less) summary

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of an email and the rest of the text as the body. The blank
line separating the summary from the body is critical (unless you omit
the body entirely); tools like rebase can get confused if you run the
two together.

Write your commit message in the imperative: "Fix bug" and not "Fixed bug"
or "Fixes bug". This convention matches up with commit messages generated
by commands like git merge and git revert.

Further paragraphs come after blank lines.

- Bullet points are okay, too

- Typically a hyphen or asterisk is used for the bullet, followed by a
  single space, with blank lines in between, but conventions vary here

- Use a hanging indent
```

A concise summary of your change is usually sufficient,
but remember that it is these commit messages that will be used in the future to understand what changes have been made to your project.
You might rely on these to identify where an error has been introduced, so it is important that you write these messages clearly and informatively.

How often you commit when working on a project should depend on what benefit you would like to get from versioning your work.
When reviewing code that has been version controlled, the commit history provides a chronological summary of the changes that have been made to a project.
To make this audit trail useful, commits should be made whenever a discrete unit of work has been completed.
When useful commit messages have been used to describe these units of work,
it is easier for others to understand steps taken to develop the analysis to its current state.

You should also make commits whenever you have made changes that you might wish to revisit or undo.
As Git allows us to easily `revert` changes by referring to a commit's hash,
you should try to ensure that each commit only contains changes to single aspect of your analysis.
Consider a commit that includes changes to several files.
We discover that one change in this commit has created a bug in our analysis code.
We can revert the commit to remove the bug, but this also removes the other changes that were made in the same commit.
As such, we'll need to invest more effort to work out which change causes the bug and selectively undo that change.


### Use branching appropriately

Branches are independent copies of a project's history, copied from a parent branch at a specific point in its history.
You typically create a new branch to make a change to your code, which might be building a new feature or fixing a bug in your analysis.
You can create multiple branches from a single parent branch when multiple changes are being worked on independently.
This is especially useful when multiple analysts are working collaboratively and are making changes in parallel.

Once changes have been implemented and sufficiently quality assured (think documentation and testing),
the branch containing the changes can be merged onto another branch.
The target branch for this merging is typically the parent branch, which the branch was branched from.
You should eventually merge complete changes onto the `main` branch, which is the public-facing branch that is ready for use.
You must resolve any overlapping or 'conflicting' changes between the current and target branches during merging.

It is important to note that your approach to branching within a project
should be proportional to number of collaborators and the complexity of the development work.
For example, if working alone on a project you might only be working a single development branch at any moment in time,
or might choose to track all changes on a single `main` branch.
The `main` or `master` branch is the default highest level branch in a Git repository.

```{figure} ./_static/git_main.png
---
width: 70%
name: git_master
alt: Commits along a single "main" Git branch.
---
Commits along a single "main" Git branch.
```

More complex projects may warrant using branching.
When using branches, the `main` branch should be considered as the most 'stable' branch in the repository -
meaning that the code on this branch builds successfully and executes as expected.
When you make changes to code, they may initially be less stable or reliable.
Therefore, you should make these changes on a new branch so that the working code on the `main` branch is unaffected.
As the changes to the code are refined, it becomes safer to merge these changes onto a higher level branch such as `main`.
For example, when the code has been reviewed and suitably tested.
You should aim to only merge onto a more stable branch when you don't expect it to break the working code on the target branch.

```{figure} ./_static/git_feature.png
---
width: 70%
name: git_feature
alt: Creating a feature branch from a main branch.
---
Working on changes on a single `feature` branch.
```

Here we show a single `feature` branch being created from the `main` branch.
Changes are initially quite experimental, but are refined over a few commits.
Finally, we merge the complete, working feature back onto the `main` branch.

Many small scale projects iteratively work on individual feature or development branches in this way.
The [GitHub flow branching strategy](https://guides.github.com/introduction/flow/) uses this approach in combination with [Pull Requests](pull-requests),
to incorporate peer review into the development workflow.

```{figure} ./_static/git_develop.png
---
width: 90%
name: git_develop
alt: Iteratively creating and merging a develop branch from a main branch.
---
Iteratively working on a `develop` branch.
```

We can create multiple branches from our `main` branch at any point.
We might do this when multiple features are being developed in parallel, or perhaps when multiple analysts wish to make changes to the same piece of code independently.

```{figure} ./_static/git_multiple_features.png
---
width: 90%
name: git_multiple_features
alt: Two features branches created from a single main branch.
---
Working on multiple parallel branches.
```

Here we create two feature branches from `main`.
Work on each feature is carried out independently of the other feature and can be merged onto `main` once it is complete.
If changes from separate branches affect the same files, merging these branches to `main` may lead to merge conflicts.
In these cases you should resolve the conflicts to keep your desired overall change.

```{note}
If you are able to break up your work into independent features that are not expected to affect the same files, you should do this.
This helps to avoid conflicts in the merging process that need to be resolved manually.
```

In addition to having multiple branches from our `main` branch, we can also create deeper branches from our other branches.
You might create additional sub-branches when the development of a feature involves multiple sub-tasks,
or when a problem needs to be fixed during development of a feature.
Deeper branching usually reflects work that is less stable and more exploratory or experimental.

```{figure} ./_static/git_deeper_branching.png
---
width: 90%
name: git_deeper_branching
alt: A sub branch being created from a feature branch.
---
Using deeper branching to manage sub-tasks.
```

In this example, we have created a `feature` branch.
Early in development of the feature we want to fix a bug that has been created,
but this work can be carried out independently to the remaining development of the feature.
As such, we create another, deeper branch to carry out the bug fix.
Once we fixed the bug, we merge the `bug-fix` onto our `feature` branch. And finally, the finished `feature` can be merged back onto `main`.

The [Git flow branching strategy](https://nvie.com/posts/a-successful-git-branching-model/) describes an alternative to progressively merging our changes onto `main`.
Instead, development work is branched from a `develop` branch.
You only use merges from `develop` onto the `main` branch to release a new version of the code.
This approach can be useful when deploying code directly into production from the `main` branch.
However, analysts should use the most simple and beneficial approach to branching depending on their project.

```{note}
Although we have used very simple branch names in the examples above, it's important that you use informative names for your branches in practice.
If using an [issue tracker](issues) (e.g. GitHub Issues or Jira), it can be useful to include the issue number in branch names (e.g., `#155-fix-index-aggregation`).
This makes it easy to trace the branch back to the associated issue or task.
Otherwise, aim to use meaningful names that describe the feature or bug that the changes will be ed on. 
```


### Resolve merge conflicts

Git is effective at merging different branches.
However, when the same file is edited in two different branches at the same time, this can lead to a merge conflict when you try to merge those branches.
When this happens, you will see a message telling you there is a merge conflict and which files are affected.
The file name will appear as `branch-name|MERGING`.
You can fix this by manually selecting which changes to keep.
If using the command line, you can also run `git status` to output the names of the affected files.

When merge conflicts happen, git will mark the clashes using this syntax:

```none
Changes on the branch being merged
=======
```

The row of equals signs divides the old from the new.
The contents in the first division are the changes in the current branch.
Changes in the second division are from the new branch.
You can choose to keep one, both, or neither.
To resolve the merge conflict, you will need to make the necessary changes and delete the relevant symbols that git added to the text.
Once you have resolved all conflicting text manually (there may be more than one), then you can add and commit the changes to resolve the merge conflicts.

Avoid merge conflicts whenever possible.
Do this by avoiding editing the same files across different branches.
If this is difficult to do, it may be that your scripts are too monolithic and should be modularised or split into multiple scripts.


### Versioning large files

Git stores compressed copies of all previous versions of each file when versioning your repository.
Despite the file compression, this means that versioning very large or binary files quickly increase the size of your repository's history,
especially if there are multiple versions of them.
The size of your Git history determines how long it takes to `clone` or `pull` and `push` changes to and from your remote repository.
This includes when a continuous integration platform downloads your repo to run tests and other checks.
Therefore, storing large files in Git typically slows down your development workflow.

[Git Large Files Storage (LFS)](https://git-lfs.github.com/) is a Git extension that allows you to version large files,
but without storing the files in your repository history.
Large files in your repository's history are instead replaced with a small text-based pointer.
This pointer references versions of the actual files, which are stored in a separate part of your remote repository (e.g., GitHub or GitLab).
When you `pull` a repository including large files, only the current version of the file is retrieved from the remote server, rather than its whole history.
This reduces the size of your local repository and the time taken to `push` and `pull` changes.
[Git-LFS integrates well with a normal Git workflow](https://www.youtube.com/watch?v=uLR1RNqJ1Mw) and can be used for specific files,
or even all files of a particular type within your repository.

Other tools, including [git-annex](https://git-annex.branchable.com/) can be used for a similar purpose.

Despite this support for large files, we recommend that remote Git repositories are not used to store data.
Versioning of your data could instead be handled independently to your code;
the version of your code should not be influenced directly by changes in the data and vice versa.
You can achieve this separation using a tool like [DVC](https://dvc.org/), which allows you to specify where data versions are store (locally or on the cloud).
Alternative, third party storage (e.g., cloud-based 'buckets' or databases) can provide easy data storage with varying levels of version control capability.


### Tag new releases

Regularly `commit`ing changes using Git helps us to create a thorough audit trail of changes to our project.
However, there may be discrete points in the history of the project that we want to mark for easier future reference.
This is incredibly useful, as commit hashes like `121b5b4` serve as really poor identifiers for human users.

Git allows us to create "tags" to reference specific points in project's history.
These tags essentially act as an alias for a particular commit hash, so we can refer to it by an informative label.
We might use tags to mark a particular model version in an analytical project or an important stage of our analysis.
For example, we might tag code that has been used to generate a particular output so that it can easily be accessed to reproduce that output in future.
If developing a package as part of your analysis, these tags are also commonly used to indicate new package versions.

By default, tags will reference the current position in history (i.e., the latest commit or `HEAD`).
An annotated tag might be created for a new model version like so:

```{code-block}
git tag -a v0.2.7 -m "Model version 0.2.7"
git push origin v0.2.7
```

You can also retrospectively tag an older commit by providing that `commit`'s hash:

```{code-block}
git tag -a v0.1.0 -m "Model version 0.1.0" 9fceb02
git push origin v0.1.0
```

Once tags have been created, these locations in the projects history can be easily recovered by either checking out:

```{code-block}
git fetch --all
git checkout tags/v0.1.0 -b new_branch_name
```

or cloning the tag:

```{code-block}
git clone https://github.com/<user>/<repo>.git --branch=v0.1.0
```


(excluding-from-git)=
## Avoid committing sensitive information to Git repositories

Code itself is very rarely sensitive, so we should be open to sharing it.
However, analysts may be required to use sensitive information in their analysis.
This might be in the form of credentials, used to access a service, or data that contains personally identifiable information.

In these cases, we need to minimise the risk of inadvertently sharing this information with our code.
This subsection suggests how you might mitigate this risk in your analysis.

You should ensure that passwords or credentials that are used in your code are stored in [environment variables](environment-variables)
and are not written directly into code.
This includes in the early stages of development, as your version control history will retain copies of these.


### Automatically avoid committing unwanted files using .gitignore

As mentioned above, you may not want to include all of the files associated with your project in a Git repository.
A `.gitignore` file allows you to exclude folders or files from being tracked by Git. Within this file, you provide a list of text patterns.
If a folder matches one of your `.gitignore` file patterns, none of the files or folders below that folder will be tracked.
If an individual file matches one of the patterns, this file will not be tracked.

Given this example `.gitignore` file:

```none
secrets.yaml
sandpit/
*.csv
```

The first pattern tells Git to ignore any file with the exact name `secrets.yaml`.
The second will ignore all files within a folder named `sandpit/`.
Note that if there are multiple folders in the project named `sandpit/`, they will all be excluded.
You should make the pattern more specific if you want to exclude particular directories.
The third pattern will exclude all `.csv` files, regardless of which folder or sub-folder they are in.

```{caution}
Files that are already being tracked by Git will not be excluded when you add new patterns to your `.gitignore` file.
Ensure that you set up your `.gitignore` before adding files to be tracked in your repository.
```

Please see the [Git documentation for `.gitignore`](https://git-scm.com/docs/gitignore) for more details.

While we may not want to share files containing credentials, configuration and data, it can be useful to provide dummy examples of these files.
Demonstrating the format of these files can help others to reuse your code, without sharing sensitive information.


### Exclude `.Rdata` and `.Rhistory` files

R saves objects from your workspace (working environment) into an `.RData` file at the end of your session.
This can save time when reloading large objects into R, when returning to a project.
Depending on your settings, it may prompt you to ask if you would like to save them or it may do this automatically.
If you have read sensitive information into R during the session, this information may be saved to the `.RData` file.
As such, we must be careful not to include this information in commits to remote repositories.

Similarly, R stores a record of all commands executed in your session in a `.Rhistory` file.
If you have referenced sensitive information directly in your R commands, then this information will be written to the `.Rhistory` file.

We can exclude these files (via `.gitignore`) or prevent R from generating them to handle this.
If you do not use these files, it is safest not to generate them in the first place.

In Rstudio, you can disable writing of these files via `Tools > Global options`:

* Under Workspace, select `Never` for `Save workspace to .RData on exit:`.
* Under History, deselect `Always save history`.

Or to set these for a particular project you can include the following in your `.Rproj` file:

```none
RestoreWorkspace: No
SaveWorkspace: No
AlwaysSaveHistory: No
```


### Avoid saving data from Jupyter Notebooks

Jupyter Notebooks save a copy of the data that is used to create cell outputs by default.
For example, the data used to generate a chart, table or print a section of a dataframe.
This can be useful for sharing your code outputs without others needing to re-execute the code cells.

If you work with sensitive datasets in notebooks, this means that your notebooks may store sensitive data to display cell outputs.
You may be making sensitive data available to unauthorised individuals if these notebooks are subsequently shared in code repositories, .

It is [not currently possible to prevent the notebooks from retaining cell outputs](https://github.com/ipython/ipython/issues/1280).

The best way to handle this situation is to clear the outputs from your notebooks before committing them to Git repositories.
You can do this from the notebook itself, by going to the menu `Cell > All > Output > Clear` and then saving your notebook.
Alternatively, you can do this from the command line by running this command with your notebook file path:

```none
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace <notebook_file_path>
```

This approach is quite laborious and could easily be forgotten.
As such, we advise you to automate the cell clearing using [Git filter](https://git-scm.com/docs/gitattributes/#_filter) as follows.
First, we tell Git to set an attribute on our notebook files by creating a `.gitattributes` file in the root of our repo:

```none
*.ipynb filter=jupyternotebook
```

We can then define our cleaning instructions in a `.gitconfig` configuration file:

```none
[filter "jupyternotebook"]
    clean = jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace %f
    required
```

You can add this to your global `.gitconfig` or create a local `.gitconfig` file in the root of your repo.
If you create a new config in your repo, you must run the following in that repo:

```none
git config --local include.path ../.gitconfig
```

This configuration will now run the notebook output cleaning command every time a change to an `.ipynb` file is added to your local repo.
You will need to then `git add` the file a second time to add the changes from the cleaning.
This should prevent notebook outputs from being included in commits to this repository.

If you adjust the filter at any point, you should run this command to apply the changes to existing files:

```none
git add --renormalize .
```

This approach has been borrowed from this [blog post by Yury Zhauniarovich](https://zhauniarovich.com/post/2020/2020-10-clearing-jupyter-output-p3/).


### Control access to code only when essential

Remote version control platforms, like GitHub,
have a [visibility setting](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/setting-repository-visibility)
that represents whether the repo can be viewed publicly or only by owners of the project
 We find that some analytical teams choose to develop code in the open, as per guidance from the
 [Government Service Manual](https://www.gov.uk/service-manual/service-standard/point-12-make-new-source-code-open).
 Others work in a private repositories, and then might either change to public or migrate to a fresh public repository to make the code open.

```{caution}
Access control should not be used instead of the good practices outlined above.
Restricting access can help to limit the risk of releasing sensitive information, but correct use of version control tools avoids these issues.
```

On GitHub, Organizations provide an area for collating multiple repos that are associated with a particular team or department.
Within Organizations, Teams can be also created to manage view and contribution permissions for specific projects within the Organization.
External collaborators can also be added to projects to allow direct contribution from those outside of the Organization.
Detailed setup and management of Organizations and Teams are described in the
[relevant section of the GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-organizations-and-teams).

Only Organization members and collaborators may make direct contributions to the code in the repo regardless of the visibility status of a repo,.
Others can contribute by Forking and using Pull Requests.


### Handle data breaches via Git

If unauthorised individuals may access sensitive information through their accidental inclusion in a remote repository, this is a data breach.
For example, pushing credentials or sensitive data to a remote public GitHub repository.

To handle a data breach, you should:

* Firstly, prevent further access to the information.
  * Restrict access of the repository to only those who should have access to the information. For example, make a public repository private.
  * Remove the offending files from the **commit history** of the repository.
  * If credentials (passwords or keys) have been revealed, you should change these credentials.
  * Ask anyone that you know has access to the repository to delete their local copy and re-clone the cleaned remote repository.
* Secondly, report the incident.
  * Record roughly how long the information was available for and the potential impact of releasing this information.
  * Inform the data owner of the breach.
  * Discuss the breach with the Data Protection Officer in your department.
 They should be able to advise you on the steps you should take as well, according to your departments data security policy.
  * If the breach includes pre-publication statistics, you must also report the breach to the [Office for Statistics Regulation](https://osr.statisticsauthority.gov.uk/).

```{warning}
Deleting a sensitive file and committing this change is not sufficient.
All previous versions of files are retained in a repository's history, so sensitive parts of the file must be entirely removed from the history.

The [Pro Git book section on rewriting history](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)
details methods for editing and deleting files from your repository's commit history.
Git has a built-in way to do this.
If you are able to install them in your department, you may use one of the simpler alternatives, such as
[git-filter-repo](https://github.com/newren/git-filter-repo) (python) or
[BFG repo-cleaner tool](https://rtyley.github.io/bfg-repo-cleaner/) (Java).
```


## Using GitHub

A number of version control platforms extend the functionality of Git to further improve collaborative working.

Here we describe some of the beneficial features supported by [GitHub](https://github.com/), the world's leading software development platform.
GitHub provides additional tools for better management of collaborative work. Many of these tools are also discussed in detail on the
[GitHub features page](https://github.com/features/project-management/),
but we will describe how they may be applied in analytical workflows here.


(issues)=
### Use Git issues to plan and discuss development of your project

Issues offer a method for requesting or recording tasks, including enhancements and bug fixes in a project.
They act as a collaborative todo list which users and developers can easily contribute to.
When combined with [Project boards](https://docs.github.com/en/free-pro-team@latest/github/managing-your-work-on-github/about-project-boards),
the issues system works very similarly to other tools like Trello and Jira.

The basic elements of an issue are the:

* Title and description, provided by the person that submitted the issue.
* Labels that categorise the issue (e.g., enhancement or bug).
* Comments section where the issue can be discussed.
* Assigned developers that are working on resolving the issue.

Within an issue's description and comments, you can reference other issues both within (e.g., `#12`) and between repos,
and tag individuals to notify them of your comments (`@whatstheirface`).
Similarly, you can link issues to specific [changes that will be merged to resolve or help to solve the issue](pull-requests).
This makes them useful for discussing bugs and new features within a team.

When a GitHub repo is publicly visible, the issues are also open and can be contributed to by others, including users.
Open source projects benefit from this transparency by providing users with a platform to highlight which changes to the project will be most beneficial for them.
In turn, developers in the community can then address these issues to improve the project.

Analytical projects might use issues to plan and discuss the steps involved in developing the project.
Collaborators might be tagged or assigned to the task where additional help is required.
If your analysis code is widely useful, others that use your code may also suggest improvement and offer to contribute to the project via these issues.

[Setting issue templates](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/configuring-issue-templates-for-your-repository)
for your project can be an effective way of encouraging users and collaborators to use informative descriptions when creating issues.
For example, a bug issue should include simple instructions to help maintainers reproduce the problem.
Feature requests might include information on how the user expects the new feature to work and details what problem it will help them to overcome.


(pull-requests)=
### Use pull requests for reviewing changes

Once changes have been implemented, perhaps to meet the requirements of an issue,
Pull Requests (PRs) provide a useful interface for incorporating changes into the main project.
We typically use PRs to merge a development branch (the source branch) onto a more stable branch in the main project (the target branch).
The development branch here may be within the same repo, a [Fork](forking) of this project, or even a completely separate project.

You should include the high level changes that have been made in the initial description of the PR, and you might point to any relevant issues that it resolves.
You can link PRs to other issues and PRs, and should provide a coherent narrative of development work much like issues.
[You can use Keywords when linking an issue (e.g., 'fixes #42')](https://docs.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)
to trigger the issue to close the PR is merged.
You can assign contributors or tag them in discussion, which can be useful for requesting help or review of a group of changes.

Put checklists into your pull request comments.
These come with check boxes that can be ticked.
This is useful when breaking down tasks into smaller chunks.
Use checklists to help the reviewer review all the relevant parts of the pull request when requesting a review.
As a reviewer, use checklists to list changes needed before the pull request can be approved.
[The Government Digital Service have good examples of what this can look like.](https://github.com/alphagov/github-organisation-administration/pull/1)

Alongside the main "Conversation" view of a PR, the GitHub web interface also provides a useful overview of changes that are included in the PR.
You're able to view the list of individual commits that are included in the PR and, better still, you can view changes to each file in detail.

```{figure} ./_static/github_pr_changes.png
---
width: 90%
name: github_pr_changes
alt: The GitHub Pull Request web interface.
---
Changes from [an example Pull Request on the `fingertipsR` package](https://github.com/ropensci/fingertipsR/pull/91/files).
```

In the "Files changed" section of a PR (shown above), altered sections of files are shown before and after the changes were made, on the left and right respectively.
Where changes have deleted lines of code, these lines are highlighted in red on the left panel. And changes that add lines of code to the file are shown on the right.

This highlighted summary of changes provides a useful interface for [peer review](peer_review.md).
When carrying out a review using this view, you can add comments to specific lines of code and these comments can include suggested changes.
All comments made using this view are also shown in the main Conversation view.
When completing a review, a reviewer can indicate whether the PR should be merged or if additional changes are required.

Once a PR has been reviewed and the reviewer is happy with the changes,
internal developers can use the Conversation view to merge the PR changes onto the target branch.

```{note}
The repository settings can be adjust to project branches against specific actions.
You should consider preventing merging onto the `main` branch without an approved Pull Request to enforce peer review.
You can combine this with a [Pull Request template](https://docs.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository)
to ensure that a standard peer review process is followed for all changes. 
```


(forking)=
### Fork a repository to maintain an independent copy

Forking a repository takes a complete copy of a third-party project's current state, including its history and all existing branches and tags.
Any changes made to a fork do not affect the code on the original repo, and *vice versa*.

You might fork a repository when you want to:

* Contribute to a project as an external collaborator
* Make changes to a project for your own use, or to maintain a copy that is independent to the original

In the first case, lets consider an example where an issue describes a bug in a project's code.
Looking at the code, you think that you know where the source of the bug is.
You create a fork of the project and clone your copy of the project locally.
Here you make commits that include changes to fix the bug and test that these changes work.
Once the bug is fixed, you create a Pull Request on the original project and describe how your changes fix the bug.
The source branch of this PR will be the branch that you committed to on your fork of the project,
while the target will be the development or main branch of the original repo.

In the second case, perhaps you want to reuse or adapt code from an existing project.
If the changes that you wish to make to the code are not in line with the aim of the original project or the project is no longer actively maintained,
then you might create a fork to contain these changes.

You should note that forks do not automatically synchronise with the original repo.
This means that after you create a fork, changes to the original repo need to be manually synchronised if you want to include them in your repo.
You should ensure that you synchronise your branch with any new changes before offering to contribute your changes to the original project (see [Pull Requests](pull-requests)).

See the GitHub documentation for
[instructions on forking a repo and keeping your fork up to date](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo)
with a project and also
[working with forks](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/working-with-forks).


### Use GitHub Actions for continous integration

Continuous Integration is discussed in more detail in [](continuous_integration.md).


### Other GitHub features

[Project boards](https://docs.github.com/en/free-pro-team@latest/github/managing-your-work-on-github/about-project-boards)
offer project management features through a
[Kanban-style board](https://en.wikipedia.org/wiki/Kanban_board).
These boards can be used to track assignment and progress of specific tasks.
Linking tasks to specific issues and pull requests aids the use of boards.

[GitHub Pages](https://pages.github.com/) offers hosting of static web content, which can be useful for code documentation.
You can use GitHub Actions to generate this documentation from the code and deploy directly to the Pages site.
Alternatively, [project Wikis](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/about-wikis)
can be used to manually document your project using [Markdown](https://www.markdownguide.org/basic-syntax/).

<!-- file: book/configuration.md -->

# Configuration

Configuration describes how your code runs when you execute it.

In analysis, we often want to run our analysis code using different inputs or parameters.
And we likely want other analysts to be able to run our code on different machines, for example, to reproduce our results.
This section describes how we can define analysis configuration that is easy to update and can remain separate from the logic in our analysis.


## Basic configuration

Configuration for your analysis code should include high level parameters (settings) that can be used to easily adjust how your analysis runs.
This might include paths to input and output files, database connection settings, and model parameters that are likely to be adjusted between runs.

In early development of our analysis, lets imagine that we have a script that looks something like this:

````{tabs}

```{code-tab} python
# Note: this is not an example of good practice
# This is intended as example of what early pipeline code might look like
data = read_csv("C:/a/very/specific/path/to/input_data.csv") 

variables_test, variables_train, outcome_test, outcome_train = train_test_split(data["a", "b", "c"], data["outcome"], test_size=0.3, random_seed=42)

model = Model()
model.fit(variables_train, outcome_train)

# prediction = model.predict(variables_test, constant_a=4.5, max_v=100)
prediction = model.predict(variables_test, constant_a=7, max_v=1000)

prediction.to_csv("outputs/predictions.csv")

```

```{code-tab} r R
# Note: this is not an example of good practice
# This is intended as example of what early pipeline code might look like
data <- utils::read.csv("C:/a/very/specific/path/to/input_data.csv") 

set.seed(42)
split <- caTools::sample.split(data, SplitRatio = .3)

train_data <- data[split, ]
test_data <- data[!split, ]

model <- glm(formula = outcome ~ a + b + c, family = binomial(link = "logit"), data = train_data, method = "model.frame")
# model <- glm(formula = outcome ~ a + b + c, family = binomial(link = "logit"), data = train_data, method = "glm.fit")

prediction <- predict(model, test_data, type = "response")

utils::write.csv(prediction, "outputs/predictions.csv")

```

````

Here we're reading in some data and splitting it into subsets for training and testing a model.
We use one subset of variables and outcomes to train our model and then use the subset to test the model.
Finally, we write the model's predictions to a `.csv` file.

The file paths we use to read and write data in our script are particular to our working environment.
These files and paths may not exist on another analyst's machine.
As such, to run our code, other analysts need to read through the script and replace these paths.
As we'll demonstrate below, collecting flexible parts of our code together makes it easier for others to update them.

When splitting our data and using our model to make predictions, we've provided some parameters to the functions that we have used to perform these tasks.
Eventually, we might reuse some of these parameters elsewhere in our script (e.g., the random seed)
and we are likely to adjust these parameters between runs of our analysis.
We should store them in variables to make it easier to adjust these consistently throughout our script.
We should also store these variables with any other parameters and options, so that it's easy to identify where they should be adjusted.

Note that in this example we've tried our model prediction twice, with different parameters.
We've used comments to switch between which of these lines of code runs.
This practice is common, especially when we want to make a number of changes when developing how our analysis should run.
However, commenting sections of code in this way makes it difficult for others to understand our code and reproduce our results.
We should avoid this form of ambiguity because another analyst would not be sure which set of parameters was used to produce a given set of predictions.
Below, we'll look at some better alternatives for storing and switching analysis parameters.

````{tabs}

```{code-tab} python
# Note: this is not an example of good practice
# This is intended as an example of basic in-code configuration. 

# Configuration
input_path = "C:/a/very/specific/path/to/input_data.csv"
output_path = "outputs/predictions.csv"

test_split_proportion = 0.3
random_seed = 42

prediction_parameters = {
    "constant_a": 7,
    "max_v": 1000
}

# Analysis
data = read_csv(input_path)

variables_test, variables_train, outcome_test, outcome_train = train_test_split(data["a", "b", "c"], data["outcome"], test_size=test_split_proportion, random_seed=random_seed)

model = Model()
model.fit(variables_train, outcome_train)

prediction = model.predict(variables_test, constant_a=prediction_parameters["constant_a"], max_v=prediction_parameters["max_v"])

prediction.to_csv(output_path)
```

```{code-tab} r R
# Note: this is not an example of good practice
# This is intended as an example of basic in-code configuration. 

# Configuration
input_path <- "C:/a/very/specific/path/to/input_data.csv"
output_path <- "outputs/predictions.csv"

random_seed = 42
test_split_proportion = .3
model_method = "glm.fit"

#analysis
data <- utils::read.csv(input_path) 

set.seed(random_seed)
split <- caTools::sample.split(data, SplitRatio = test_split_proportion)

train_data <- data[split, ]
test_data <- data[!split, ]

model <- glm(formula = outcome ~ a + b + c, family = binomial(link = "logit"), data = train_data, method = model_method)

prediction <- predict(model, test_data, type = "response")

utils::write.csv(prediction, output_path)
```

````

Separating configuration from the rest of our code makes it easy to adjust these parameters and apply them consistently throughout the analysis script.
We're able to use basic objects (like lists and dictionaries) to group related parameters.
We then reference these objects in the analysis section of our script.

Our configuration could be extended to include other parameters, including which variables we're selecting to train our model.
However, we must keep the configuration simple and easy to maintain.
Before moving aspects of code to the configuration, consider whether it improves your workflow.
You should include things that are dependent on the computer that you are using (e.g., file paths) or are likely to change between runs of your analysis, in your configuration.


## Use separate configuration files

We can take our previous example one step further using independent configuration files.
We simply take our collection of variables, containing parameters and options for our analysis, and move them to a separate file.
These files can be written in the same language as your code or other simple languages, as we'll describe in the following subsections.

Storing our analysis configuration in a separate file to the analysis code is a useful separation.
It means that we can version control our code based solely on changes to the overall logic - when we fix bugs or add new features.
We can then keep a separate record of which configuration files were used with our code to generate specific results.
We can easily switch between multiple configurations by providing our analysis code with different configuration files.

You may not want to version control your configuration file if it includes file paths that are specific to your machine or references to sensitive data.
In this case, include a sample or example configuration file, so others can use this as a template to configure the analysis for their own environment.
It is key to keep this template up to date, so that it is compatible with your code.


### Use code files for configuration

We can copy our parameter variables directly from our scripts to use another code script as our configuration file.
Because these variables are defined in the programming language that our analysis uses, it's easy to access them in our analysis script.
In Python, variables from these config files can be imported into your analysis script.
In R, your script might `source()` the config file to read the variables into the R environment.


### Use dedicated configuration files

Many other file formats can be used to store configuration parameters.
You may have come across data-serialisation languages (including YAML, TOML, JSON and XML), which can be used independently of your programming language.

If we represent our example configuration from above in YAML, it would look like this:

```yaml
input_path: "C:/a/very/specific/path/to/input_data.csv"
output_path: "outputs/predictions.csv"

test_split_proportion: 0.3
random_seed: 42

prediction_parameters:
    constant_a: 7
    max_v: 1000
```

You can use relevant libraries to read configuration files that are written in other languages.
For example, we could read the YAML example into our analysis like this:

````{tabs}

```{code-tab} python
import yaml

with open("./my_config.yaml") as file:
    config = yaml.safe_load(file)

data = read_csv(config["input_path"])
...
```

```{code-tab} r R
config <- yaml::yaml.load_file(config_path)

data <- read.csv(config$input_path)
...
```

````

Configuration file formats like YAML and TOML are compact and human-readable.
This makes them easy to interpret and update, even without knowledge of the underlying code used in the analysis.
Reading these files in produces a single object containing all of the `key:value` pairs defined in our configuration file.
We can then select our configuration parameters using their keys in our analysis.


## Use configuration files as arguments

In the previous example, we have stored our configuration options in a separate file and referenced this in our analysis script.
Although this allows us to separate our configuration from the main codebase, we have used a hard-coded path to the configuration file.
This is not ideal, as for the code to be run on another machine the configuration file must be saved on the same path.
Furthermore, if we want to switch the configuration file that the analysis uses we must change this path or replace the configuration file at the specified path.

We can adjust our analysis script to take the configuration file path as an argument when the analysis script is run to overcome this.
We can achieve this in a number of ways, but we'll discuss a minimal example here:

````{tabs}

```{code-tab} python
import sys
import yaml

if len(sys.argv) < 2:
    # The Python script name is counted as the first argument
    raise ValueError("Configuration file must be passed as an argument.")

config_path = sys.argv[1]
with open(config_path) as file:
    config = yaml.safe_load(file)
...
```

```{code-tab} r R
args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 1) {
  stop("Configuration file must be passed as an argument.")
}

config_path <- args[1]
config <- yaml::yaml.load_file(config_path)
...
```

````

When executing the analysis file above, we pass the path to our configuration file after calling the script.
If our script was named 'analysis_script', it would be called from the command line as:

````{tabs}

```{code-tab} sh Python
python analysis_script.py /path/to/my_configuration.yaml
```

```{code-tab} sh R
Rscript analysis_script.R /path/to/my_configuration.yaml
```

````

If we now want to run our analysis with a different configuration we can simple pass another configuration file to the script.
This means that we don't need to change our code to account for changes to the configuration.

```{note}
It is possible to pass configuration options directly as arguments in this way, instead of referencing a configuration file.
However, you should use configuration files as they allow us to document which configuration
has been used to produce our analysis outputs, for reproducibility.
```


(environment-variables)=
## Configure secrets as environment variables

Environment variables are variables that are available in a particular environment.
In most analysis contexts, our environment is the user environment that we are running our code from.
This might be your local machine or an analysis platform.

If your code depends on credentials of some kind, do not write these in your code.
You can store passwords and keys in configuration files, but there is a risk that these files may be included in [version control](version_control.md).
To avoid this risk, store this information in local environment variables.

Environment variables can also be useful for storing other environment-dependent variables.
For example, the location of a database or a software dependency.
We might prefer this over a configuration file the code requires very few other options.

In Unix systems (e.g., Linux and Mac), you can set environment variables in the terminal using `export` and delete them using `unset`:

```none
export SECRET_KEY="mysupersecretpassword"
unset SECRET_KEY
```

In Windows, the equivalent commands to these are:

```none
setx SECRET_KEY "mysupersecretpassword"
reg delete HKCU\Environment /F /V SECRET_KEY
```

You can alternatively define them using a graphical interface under `Edit environment variables for your account` in your Windows settings.

Once stored in environment variables, these variables will remain available in your environment until you delete them.

You can access this variable in your code like so:

````{tabs}

```{code-tab} python
import os

my_key = os.environ.get("SECRET_KEY")
```

```{code-tab} r R
my_key <- Sys.getenv("SECRET_KEY")
```

````

It is then safer for this code to be shared with others, as they can't acquire your credentials without access to your environment.

<!-- file: book/data.md -->

# Data management

Data management covers a broad range of disciplines, including organising, storing and maintaining data.
Dedicated data architects and engineers typically handle data management. However, analysts are often expected to manage their own data or will work alongside other data professionals.
This section aims to highlight good data management practices, so that you can either appreciate how your organisation handles its data
or implement your own data management solutions.

We need to be able to identify and access the same data that our analysis used if we are to reproduce a piece of analysis .
This requires suitable storage of data, with documentation and versioning of the data where it may change over time.

```{admonition} Key strategies
:class: admonition-strategies

[The Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework)
focuses primarily on assessing and improving the quality of input data.
It should be a primary resource for all analysts working with data in the public sector.

The Office for Statistics Regulation provides a standard for
[quality assurance of administrative data](https://osr.statisticsauthority.gov.uk/guidance/administrative-data-and-official-statistics/).
```


## Data storage

We assume that most data are now stored digitally.

Digital data risk becoming inaccessible as technology develops and commonly used software changes.
Use open or standard file formats, not proprietary ones, for long term data storage.
There are [recommended formats](https://www.ukdataservice.ac.uk/manage-data/format/recommended-formats.aspx) for storing different data types,
though we suggest avoiding formats that depend on proprietary software like SPSS, STATA, and SAS.

Short term storage, for use in analysis, might use any format that is suitable for the analysis task.
However, most analysis tools should support reading data directly from safe long term storage, including databases.


### Spreadsheets

Spreadsheets (e.g., Microsoft Excel formats and open equivalents) are a very general data analysis tool.
The cost of their easy to use interface and flexibility is increased difficulty of quality assurance.

```{figure} https://imgs.xkcd.com/comics/norm_normal_file_format.png
---
width: 50%
name: data-file-comic
alt: A comic strip describing someone sending "data" in the form of a screenshot of a spreadsheet document.
---
.NORM Normal File Format, from [xkcd](https://xkcd.com/2116/)
```

Do not use spreadsheets for storage of data (or statistics production and modelling processes).
Using spreadsheets to store data introduces problems like these:

* Lack of audibility - changes to data are not recorded.
* Multiple users can't work with a single spreadsheet file at once, or risk complex versioning clashes which can be hard to resolve.
* They are error prone and have no built in quality assurance.
* Large files become cumbersome.
* There is a risk of automatic "correction" of grammar and data type, which silently corrupts your data.
  * Converting dates to a different datetime format.
  * Converting numbers or text that resemble dates to dates.

See the European Spreadsheet Risks Interest Group document
[spreadsheet related errors and their consequences](https://eusprig.org/research-info/horror-stories/) for more information.


### Databases

Databases are collections of related data, which can be easily accessed and managed.
Each database contains one or more tables, which hold data.
Database creation and management is carried out using a database management system (DBMS).
DBMSs usually support authorisation of access to the database and support multiple users to concurrently access the database.
Popular open source DBMS include:

* SQLite
* MySQL
* PostgreSQL
* Redis

Relational databases are the most common form of database.
Common keys (e.g., unique identifiers) link data in the tables of a relational database.
This allows you to store data with minimal duplication within a table, but quickly collect related data when required.
Relational DBMS are called RDBMS.

Most DBMS communicate with databases using structured query language (SQL).

```{admonition} Key Learning
:class: admonition-learning

You might find this [foundations of SQL (government analysts only course)](https://learninghub.ons.gov.uk/enrol/index.php?id=1162)
or [w3schools SQL tutorials](https://www.w3schools.com/sql/default.asp) useful for learning the basics of SQL.
```

Common analysis tools can interface with databases using SQL packages, or those which provide an object-relational mapping (ORM).
An ORM is non-SQL-based interface to connect to a database.
They are often user-friendly, but may not support all of the functionality that SQL offers.

```{admonition} Key Learning
:class: admonition-learning

This guide covers [Python SQL libraries](https://realpython.com/python-sql-libraries/) in detail.
While this Software Carpentry course covers [SQL databases and R](http://datacarpentry.org/R-ecology-lesson/05-r-and-databases.html).
```

Other database concepts:

* Schema - a blueprint that describes the field names and types for a table, including any other rules (constraints).
* Query - a SQL command that creates, reads, updates or deletes data from a database.
* View - a virtual table that provides a quick way to look at part of your database, defined by a stored query.
* Indexes - data structures that can increase the speed of particular queries.

Good practices when working with databases include:

* Use auto-generated primary keys, rather than composites of multiple fields.
* Break your data into logical chunks (tables), to reduce redundancy in each table.
* Lock tables that should not be modified.

Other resources:

* This [SQL lecture from Harvard's computer science course](https://www.youtube.com/watch?v=u5pDdEKnbKA)
may be a useful introduction to working with databases from Python.
* A guide to [using the `sqldf` R package](https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/sql.html).

## Documenting data

It is difficult to understand and work with a new dataset without documentation.

For our analysis, we should be able to quickly grasp:

* What data are available to us?
* How were these data collected or generated?
* How are these data represented?
* Have these data been validated or manipulated?
* How am I ethically and legally permitted to use the data?

Data providers and analysts should create this information in the form of documentation.


### Data dictionary

A data dictionary describes the contents and format of a dataset.

For variables in tabular datasets, you might document:

* A short description of what each variable represents.
* The frame of reference of the data.
* Variable labels, if categorical.
* Valid values or ranges, if numerical.
* Representation of missing data.
* Reference to the question, if survey data.
* Reference to any related variables in the dataset.
* If derived, detail how variables were obtained or calculated.
* Any rules for use or processing of the data, set by the data owner.

See this detailed example -
the [National Workforce Data Set](https://www.datadictionary.nhs.uk/data_sets/administrative_data_sets/national_workforce_data_set.html#dataset_national_workforce_data_set),
from the NHS Data Model and Dictionary.

Please see [UK Data Service guidance on documenting other data](https://www.ukdataservice.ac.uk/manage-data/document/data-level/tabular.aspx),
including qualitative data.


### Information Asset Register (IAR)

An information asset register (IAR) documents the information assets within your organisation.
Your department should have an IAR in place, to document its information assets.
As an analyst, you might use the register to identify contacts for data required for your analyses.

Although this form of documentation may not contain detailed information on how to use each data source (provided by data dictionaries), an IAR does increase visibility of data flows.
An IAR may include:

* The owner of each dataset.
* A high level description of the dataset.
* The reason that your organisation holds the dataset.
* How the information is stored and secured.
* The risk of information being lost or compromised.

GOV.UK provides [IAR templates](https://www.gov.uk/government/publications/information-asset-register) that your department might use to structure their IAR.


## Version control data

To reproduce your analysis, you need to be able to identify the data that you used.
Data change over time;
Open data and other secondary data may be revised over time or cease to be available with no notice.
You can't rely on owners of data to provide historical versions of their data.

As an analyst, it is your responsibility to ensure you identify the exact data that you have used.

You should version and document all changes to the data that you use whether using a primary or secondary data source,.
You should include the reason why the version has changed in documentation for data versions.
For example, if an open data source has been recollected, revisions have been made to existing data, or part of the data has been removed.

You should be able to generate your analytical outputs reproducibly and, as such, treat them as disposable.
If this is not the case, version outputs so that you can easily link them to the versioned input data and analysis code.

To automate the versioning of data, you might use the Python package [DVC, which provides Git-like version control of data](https://dvc.org/).
This tool can also relate the data version to the version of analysis code, further facilitating reproducibility.
You can use Git to version data, but you should be mindful of where your remote repository stores this data.
The [`daff` package summarises changes in tabular data files](https://github.com/paulfitz/daff), which can be integrated with Git to investigate changes to data.

You might alternatively version your data manually e.g., by creating new database tables or files for each new version of the data.
It must be possible to recreated previous versions of the data, for reproducibility.
As such, it is important that you name data file versions uniquely, for example, using incrementing numbers and/or date of collection.
Additionally, do not modify file versions after they have been used for analysis - they should be treated as read-only.
All modifications to the data should result in new versions.

```{todo}
Diagram of good manual data versioning workflow.

[#22](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/22)
```

Finally, for this to be effective, your analysis should record the version of data you used to generate a specified set of outputs.
You might document this in analysis reports or automatically logged by your code.


## Use these standards and guidance when publishing data

You should use the [5-star open data standards](https://5stardata.info/en/) to understand and improve the current utility of your published data.
We recommend the [CSV on the Web (CSVW) standard](https://csvw.org/) for achieving the highest ratings of open data.

When publishing statistics you should follow government guidance for [releasing statistics in spreadsheets](https://analysisfunction.civilservice.gov.uk/policy-store/releasing-statistics-in-spreadsheets/).

When publishing or sharing tabular data, you should follow the [GOV.UK Tabular data standard](https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard).

Analysts producing published statistics may also be interested in [Connected Open Government Statistics (COGS)](https://analysisfunction.civilservice.gov.uk/the-gss-data-project/)
and [the review of government data linking methods](https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods).

The UK Data Service provides guidance on [data security considerations](https://www.ukdataservice.ac.uk/manage-data/store/security).

<!-- file: book/peer_review.md -->

# Peer review

Peer review of code is a quality assurance activity where a developer, other than the code's author, views and tests the usage of a piece of code.

Peer review allows for a fresh pair of eyes to take a look at your work.
It helps to assure that you have taken an appropriate approach to your analysis and may highlight errors in the analysis process.
Constructive review feedback helps you to improve your code quality and provides confidence in your work.
It acts to assure that your analysis is fit for purpose.

```{epigraph}
For analysis to be used to inform a decision it must be possible to assess its utility, reliability,
and the degree of validation and verification to which it has been subjected.

-- [The Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government)
```

[The Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government)
tells us that we should proportionately quality assurance our analysis depending on the complexity and business risk of the analysis.
This means that you may require both internal and external peer review to adequately assure your analysis.
We recommend External review if your analysis uses novel or complex techniques,
if comparison with other analyses cannot be used to challenge your results, or if the analysis is business critical.

```{epigraph}
Continuous challenge and improvement is essential to ensure that the people we serve – ministers and, of course, the public – have trust in our analysis. 

-- Nick Macphereson, former Permanent Secretary to the Treasury
```


## Focus reviews on code quality

Our [](checklists.md) provide an extensive list of good practices that reviewers can look for.
Many of these criteria consider the whole project.
You should tailor your review to the quality assurance criteria that the project is trying to meet and the scale of the review.

Reviewing is centered around conversations - asking yourself and the reviewer questions.
While reviewing changes to analytical code, example questions might be:


### Can I easily understand what the code does?

In more depth:

* Is the code sufficiently documented for me to understand it?
* Is there duplication in the code that could be simplified by refactoring into functions and classes?
* Are functions and class methods simple, using few parameters?

As we discussed in [](readable_code.md), good quality, modular code is easier to read, understand, and maintain.
Peer review improves the quality of our code through the reviewer's constructive challenges.
You might do this as a reviewer by suggesting alternative ways to represent the analysis or
by asking about decisions that have been made in the approach to the analysis.

Another benefit, particularly of internal review, is knowledge transfer.
Both the reviewer and reviewee are exposed to new ideas.
The reviewer must understand what the code is doing to validate that it works as expected.
This may provide your team members with the understanding required to use and maintain your code in the future.


### Is the required functionality tested sufficiently?

If we do not test each part of the code, then we can't be sure that it works as expected.
As a reviewer, you should ask whether the amount of testing is proportionate given the risk to the analysis if the code does not work.


### How easy will it be to alter this code when requirements change?

In more depth:

* Are high level parameters kept in dedicated configuration files?
* Or would somebody need to work their way through the code with lots of manual edits to reconfigure for a new run? This is much more risky.

Most analysis stems from some form of customer engagement.
Throughout design, implementation and review of analysis we must continue to assess whether our analysis is fit for purpose:
Does it meet the needs of the customer?
Document the scope of your analysis and any requirements to make this assessment as easy as possible.
Support the auditability of your analysis with additional documentation, including assumption logs,
technical reports describing the analysis and documentation on any verification or validation that has already been carried out.


### Can I generate the same outputs that the analysis claims to produce?

In more depth:

* Have dependencies been sufficiently documented?
* Is the code version, input data version and configuration recorded?

A key aspect of review is checking that you get the same results when running your code with the same input data.
Assurance that analysis can be reproduced increases the trust in the results.

Note that each of these example questions focuses on important quality assurance practices in the code, rather than minor issues like code layout and style.


## Give practical feedback

Provide practical and constructive feedback.
For example, you should suggest an improvement or alternative that the developer may consider and learn from.
You should avoid making feedback personal, although it may be necessary to highlight specific examples.

The CEDAR feedback model can be a useful framework for structuring review comments.
This model breaks review down into five sections:

1. Context - describe the issue and the potential impact.
2. Examples - give specific examples of when and where the issue has been present.
3. Diagnosis - use the example to discuss why this approach was taken, what could have been done differently and why the alternatives could be an improvement.
4. Actions - ask the person receiving feedback to suggest actions that they could follow to avoid this issue in future.
5. Review - revisit the discussion to look for progress following on the feedback.

This approach has been designed from a coaching or mentoring perspective, and can work well in verbal discussion or when giving written feedback.


## Document review feedback and outcomes

When you identify issues with code functionality or quality you should suggest improvements to solve these issues.
The code developer may respond to your comments to justify why they have taken a certain approach, otherwise they should act on your feedback before using the analysis.

You may need to re-review changes that have resulted from your initial review, to confirm that your feedback has been actioned appropriately.

```{important}
Document what you have considered in your review and how the developer has responded to your feedback.
You should keep this documentation close to the relevant version of the code, so that others can see what has been reviewed.
The easiest way to manage this is by using the Merge Request or Pull Request feature on your version control platform to conduct the review.
See [](version_control.md) for more information.
```


## Give consistent feedback

You might formalise your review using a template, to ensure that review is consistent within a project.
Templates are useful for setting criteria to review against.
You should tailor any template to reflect the scope of your review.
For example, small regular reviews may focus on smaller aspects of the analysis compared to a large project-wide review.
The general example below is written in Markdown, so that it can be used in version control platform Merge or Pull requests:


```{code-block} md
##  Code review

#### Documentation

Any new code includes all the following forms of documentation:

- [ ] **Function Documentation** as docstrings within the function definition.
- [ ] **Examples** demonstrating major functionality, which runs successfully locally.

#### Functionality

- [ ] **Installation**: Installation or build of the code succeeds.
- [ ] **Functionality**: Any functional claims of new code have been confirmed.
- [ ] **Automated tests**: Unit tests cover essential functions for a reasonable range
  of inputs and conditions. All tests pass on your local machine.
- [ ] **Packaging guidelines**: New code conforms to the project contribution
  guidelines.
---

### Review comments

*Insert detailed comments here!*

These might include, but not exclusively:

- bugs that need fixing (does it work as expected? and does it work with other code that it is likely to interact with?)
- alternative methods (could it be written more efficiently or with more clarity?)
- documentation improvements (does the documentation reflect how the code actually works?)
- additional tests that should be implemented (do the tests effectively assure that it  works correctly?)
- code style improvements (could the code be written more clearly?)

Tailor your suggestions to the code that you are reviewing.
Be critical and clear, but not mean. Ask questions and set actions.

```

Carry out internal review regularly within the development team.
Reviewing code written by those with more and less experience than you is beneficial for both reviewer and developer.
You can ask similar questions from both perspectives, for the reviewer to get a good understanding of the approach and decisions behind the analysis.


## Give timely feedback

Provide feedback in good time so the review process does not hold up development of the code
and that issues can be addressed before more code is written using the same practices.

We strongly recommend applying pair programming for code review, as the most timely and practical method.
However, you may find a separate review process necessary when multiple developers are not available to work at the same time.


### Review through pair programming

> Two heads are better than one.

Review doesn't have to be an arduous standalone task.
Pair programming combines the code writing and the review process into a single step.
Here, two or three developers work together to write a single piece of code.
Each developer takes turns to actively author parts of the code, while others provide real-time feedback on the code being written.

This practice encourages developers to consider why they are writing code in a particular way and to vocalise this ("programming out loud").
Additionally, it gives reviewers a chance to suggest improvements and question the author's approach as they write the code.
Working in this way can be more efficient than reviewing code separately - you identify issues sooner, so they are easier to fix.
Despite the upfront cost of two individuals writing the code, the resulting code is often higher quality and contains fewer bugs.

The rotational aspect of pair programming ensures that all team members gain experience from both the author and review perspective.
From both angles, you'll learn new programming and communication techniques.
Additionally, sharing knowledge of how the code works across the team prevents putting too much risk on individuals.

Developers working in pairs can approve changes to code as it is written. However, you should still document
key discussions from pair programming sessions to demonstrate which aspects of the code have been reviewed and discussed.

This blog post from the Government Digital Service provides
[more detailed steps to apply pair programming](https://gds.blog.gov.uk/2018/02/06/how-to-pair-program-effectively-in-6-steps/).


### Review separately when necessary

A separate review involves sharing your code with a reviewer, and receiving written feedback.
We describe this as separate, because code development and review are separate and the code author does not need to be present for the review.
This type of review is an iterative process, where the reviewer may make additional suggestions until they are satisfied with the code changes.

This form of review works best when changes to the code are small and frequent.
Requesting review of small but regular changes reduces the burden on reviewers, relative to large review of a complete project.
Similarly to pair programming, reviewing small changes to code allows you to catch issues sooner.

```{important}
If a project is only reviewed when all of the code has been written, this significantly reduces the benefit of review.

This creates a much larger burden on the reviewer.
Additionally, fixing any issues that are identified may take a lot of time to fix.
A reviewer might highlight that certain quality assurance practices have not been used -
for example, there has not been enough documentation or automated testing in the project.
Adding documentation and testing for the whole project would take substantial effort.
If this was identified earlier, the improved practices could be applied as the remaining code is developed.
```

When you must carry out a review of larger or complete pieces of work, consider reviewing different aspects of the code in separate sessions.
For example, reviewing documentation in one session and functionality in the next.

The thought of someone else reviewing your code in this way encourages good practices from the outset:

* Clear code and documentation - so others with no experience can use and test your code.
* Usable dependency management - so others can run your code in their own environment.

Separate review is aided by version control platforms' features. See [](version_control.md) for more information.


#### Case study - rOpenSci review

Here we discuss a [review example from rOpenSci](https://ropensci.org/);
a community led initiative that curates open source, statistical R packages.
rOpenSci apply a rigorous peer review process to assure the quality of packages before including them in their collection.
This peer review process is entirely remote and is performed in the open, via GitHub pull requests.

In this example, from colleagues at Public Health England, [the `fingertipsR` package is reviewed](https://github.com/ropensci/software-review/issues/168).
The initial comment describes the package that is being submitted and includes a check against a list of minimum requirements.
The [`goodpractice` R package](http://mangothecat.github.io/goodpractice/) is used to check that good R packaging practices have been followed.
[Continuous integration](https://www.atlassian.com/continuous-delivery/continuous-integration#:~:text=Continuous%20integration%20(CI)%20is%20the,builds%20and%20tests%20then%20run.)
is commonly used to carry out automated checks on code repositories.
The reports from these checks can save reviewers time, by providing indicators of things like code complexity and test coverage.

Two external reviews conduct reviews before the package is accepted - these reviews include checking common aspects of code packages,
like documentation, examples, and automated testing.
Perhaps the most informative part of these reviews is the detailed bespoke comments.
Here the reviewers highlight problems, ask questions to clarify aspects of the package design, and suggest improvements to the implementation of the code
(with examples).

Following the reviews, the authors wrote comments describing how the reviewers requested changes were addressed.
And finally, a sign off confirmed that the reviewers are satisfied with the package.

Although this review looked at an entire, mature package, you can apply parts of this review process to smaller pieces of code as required.

<!-- file: book/testing_code.md -->

# Testing code

Code documentation helps others to understand what you expect your code to do and how to use it. Code tests verify that your analytical code is working as expected.  

You cannot confirm your code works correctly if you don’t carry out tests, so you cannot be confident that your analysis is fit for purpose without them.  
Good tests tell a story - given this data, having run this code, we expect this output.  

Testing brings strong benefits. It helps you assure your code quality and makes developing your code more efficient.
Code that has not been tested is more likely to contain errors and need more maintenance in the future.

## What should I test?

The question you need to answer here is a simple one:    

How can I demonstrate that my code does what it is supposed to do?    

As the developer of the code, you are best placed to decide what tests you need to put in place to answer that question confidently.

Take a risk-based approach to testing. You should use tests proportionately based on your analysis.  This usually means writing more tests for parts of your code that are very new, more complex, or carry more risk.  

When you are developing your tests, here are some points to think about:    

1.  You don't need to test everything. It is realistic to assume that third party functions and tools which are adequately quality assured (and you can verify this) work as intended.  For example, if you use R you would not expect to write tests to verify that simple arithmetic, base R, or packages published on [CRAN](https://cran.r-project.org/) operate correctly, because there is already sufficient assurance. You may be less confident about very new functionality from third parties, or experimental tools. Here, you might decide you do need to do some extra validation.    
2. Think carefully about whether third party tools really do what you need for your particular context.  For example, the base R `round()` function intentionally behaves differently to the rounding function in Excel. While we can be confident that `round()` works as specified, does it produce what you need?
3. Testing is a great way to verify that your approach is the right one. By thinking about what to test, you challenge your own assumptions and the way you have done things. This can reveal issues or scenarios that you had not considered. It means the code you write should be more resilient.
4. Be guided by the risks you need to mitigate. For example, if inputs are invalid or unusual, do you want the code to stop with an error message or do something else? Use tests to check that the code does the right thing at the right time. 

## How are tests structured?

Tests come in many shapes and sizes, but usually follow the pattern:

1. Arrange - set up any objects needed for your test, for example sample input data and expected output data.
2. Act - run the code that you are testing (one or more functions or methods).
3. Assert - verify that the code performed the expected action, for example, that the output matched the expected output.

```{admonition} Key Learning
:class: admonition-learning

Follow the [Introduction to Unit Testing course](https://learninghub.ons.gov.uk/course/view.php?id=1171) for applied examples in Python and R.
This course also covers writing and documenting functions, and error handling.

Other useful learning resources include:
* [`pytest` getting started](https://docs.pytest.org/en/stable/getting-started.html)
* Real Python [Getting Started With Testing in Python](https://realpython.com/python-testing/)
* Hadley Wickham's [testthat: getting started with testing](https://vita.had.co.nz/papers/testthat.pdf) and [testing design in R](https://r-pkgs.org/testing-design.html)
```

In this section, we assume that you are using a testing framework to run your tests (for example, `pytest` for Python or `testthat` for R) and have your code in a package.
It is more difficult to test code that is not in a package and therefore follow the testing good practices described here.

## Write reproducible tests

As an analyst, you routinely check that your analysis is carried out correctly.
You might do this informally by running all or part of your analysis with example data or subsets of real data.

These tests give you confidence that your analysis is correct.
However, it's important you are able to produce the same checks against your code reproducibly.
Code changes over time, so you need to be able to repeat these checks against the updated code.
Additionally, other analysts should be able to carry out the same checks and get the same results.

You can consistently repeat the same steps when you represent your tests as code.
This lets you or another analyst carry out the same verification again to get the same results.
When you have carried out a test manually, you should ensure that you add a code test to reproduce this.

Code that you write for testing should also follow the good practices described earlier on in this book, in particular [](readable_code).

## Write repeatable tests

You need your tests to be repeatable for you to be able to trust their results.
This means they should give the same outcome if you run them more than once against the same version of your analysis code.

For tests to run repeatably, each test must be independent.
There should not be a shared state between tests, for example a test should not depend on another test having already run.
You could intentionally randomise the order that tests are executed to encourage this.

Where possible, tests should be deterministic.
As such, the only reason for a test to fail should be that the code being tested is incorrect.
Where your code relies on randomness tests should reuse the same random seed each time they are run.

Where this is not possible/logical for the scenario that you are testing, you may want to run the test
case multiple times and make an assertion about the distribution of the outcomes instead.
For example, if you are testing a function that simulates a coin flip you might run it 100 times and
check the proportion of heads versus tails is close to half (within a reasonable range).

## Run all tests against each change to your code

Run **all** tests whenever you make changes to your analysis.
This ensures that changes do not break the existing, intended functionality of your code.
Running the entire collection of tests has the added benefit of detecting unexpected side-effects of your changes.
For example, you might detect an unexpected failure in part of your code that you didn't change.

If you run tests regularly, you will be more able to fix any issues before changes are added to a stable or production version of your code (e.g. the `main` Git branch).

If you have altered the functionality of your code, this will likely break existing tests.
Failing tests here act as a good reminder that you should update your tests and documentation to reflect the new functionality.
Many testing frameworks support writing tests as examples in the function documentation, which ties these together nicely.

It's not easy to remember to run your tests manually at regular intervals.
And you're right to think "surely this could be automated too?".
Use [continuous integration](continuous-integration) to automate
the running of tests. This way, you can trigger tests to run when any changes are made to your
remote version control repository.

## Record the outcomes of your tests

For auditability, it is important you record the outcome from running tests.
Record the test outcomes with the code, so that
it is clear which tests have been run successfully for a given version of the code.

As mentioned above, automating the running of tests on a version control platform is the simplest and
most effective way to achieve this association between the code version and test outcomes.
See [](continuous_integration) for further guidance on using these tools.

## Minimise your test data

Tests for analytical code will usually require data. To ensure that tests are clear in their meaning, you should use the smallest possible dataset for a test.

Good test data are:
* only just detailed enough data to carry out the test
* fake, static (hardcoded), and readable
* stored closely to the test

```{warning}
You must not copy the output from running your code to create your expected test outcomes.
If you do this the test will check that the function is running in the same way that it ran when you generated the data.
This assumes that your function is working correctly.

You must create your test data independently, ensuring that it reflects how you want your code to work, rather than how it currently works.
```

It's tempting to create a test dataset that closely mimics your real data, like the example below:

```{code-block} python
from my_package import add_columns
from pandas.testing import assert_frame_equal
import pandas as pd

def test_sum_columns():
    expected_output = pd.DataFrame(
        'region_1_sales':            [1000,  50000, 500 , 30000, 10000,   50000 ],
        'region_2_sales':            [4000,  45000, 1000, 13000, 60000,   80000 ],
        ...
        'region_30_sales':           [1500,  32000, 2000, 41000, 40000,   10000 ],
        'total_sales':               [85000, 92000, 7000, 110000, 600000, 400000]
    )

    input_data = expected_output.drop('total_sales')

    actual_output = sum_columns(
        df=input_data,
        column_to_assign="total_sales",
        columns_to_sum=["region_1_sales", "region_2_sales"]
        )
    assert_frame_equal(expected_output, actual_output)
```

However, you can still conduct the same test with much less data like so:

```{code-block} python
...

def test_sum_columns():
    expected_output pd.DataFrame(
        'input_1': [1, -1, -1, 0],
        'input_2': [1, -1,  1, 0]
        'outcome': [2, -2,  0, 0]
    )
    input_data = expected_output.drop('outcome')

    actual_output = sum_columns(
        df=input_data,
        column_to_assign="outcome",
        columns_to_sum=["input_1", "input_2"]
        )
    assert_frame_equal(expected_output, actual_output)
```

Using minimal and general data in the test has made it clearer what is being tested, and also avoids any unnecessary disclosure.
In this case, the function is very generic, so the test doesn't need to know the names of real columns in our data or even have similar values in the data.
The test data are focussed on testing specific, realistic cases.
This makes it easy to see that this function works correctly with positive, negative and zero values.

Note that the way you write your test affects how the function is implemented.
Using minimal, generalised data encourages you to follow good practices when designing your function.
This function doesn't know the name of the columns that it will use in advance, so they are passed as parameters.
This makes the function reusable.
You might have named the original function `sum_sales_columns`, but the more general name used here makes it clear
that you could use this to sum columns in any other context.

The example above is a single test function, but could have created separate tests for each scenario and included tests for more than two input columns, for example.

## Structure test files to match code structure

In [](modular_code) we describe how complexity can be managed by separating code into related groups.
Modular, well-structured code is easier to write tests for.
But we also want to make it easy to identify which tests relate to which parts of our code.

You should mirror the structure of your code in the structure of your test files.
You might use one test file per function/class or one test file per module.
Overall, the aim is to make it easy to find the tests for a given function or class and vice versa.

`````{tabs}
````{tab} Python
```
project/
│
├── src/
│   ├── __init__.py
│   ├── math.py
│   ├── strings.py
│   └── api.py
│
└── tests/
    ├── unit/
    │   ├── test_math.py
    │   └── test_strings.py
    │
    ├── integration/
    │   └── test_api.py
    │
    └── end_to_end/
        └── test_end_to_end_pipeline.py
```
````

````{tab} R
```
project/  
│  
├── .Rproj  
│  
├── R/  
│   ├── math.R  
│   ├── strings.R  
│   └── api.R  
│  
└── tests/  
    │  
    ├── testthat/  
    │   ├── test-maths_abs.R  
    │   ├── test-maths_sum.R  
    │   └── test-strings_option.R  
    │  
    └── testthat.R  
```
````

`````

The Python example above has one file containing unit tests for each module (group of related functions and classes).
When using this structure, you may want to also group multiple test functions into test classes.
Having one test class per function/class that you are testing will make it clear that the group of tests relates to that function or class in your source code.

```{code-block} python
# An example for tests/unit/test_math.py

class TestAbs:
    def test_abs_all_positive_values(self):
        ...

    def test_abs_all_negative_values(self):
        ...
    
    ...


class TestSum:
    def test_sum_all_positive_values(self):
        ...

    def test_sum_all_negative_values(self):
        ...
    
    ...
```

Using classes for unit tests has many additional benefits, allowing reuse of the same logic either by class inheritance, or through fixtures.
Similar to fixtures,
you can use the same pieces of logic through class inheritance in Python.
Note that it is easier to mix up and link unit tests when using class inheritance.
The following code block demonstrates an example of class inheritance which will inherit both the
variable and the `test_var_positive` unit test, meaning three unit tests are run.
You can overwrite the variable within the subclass at any time, but will still inherit defined functions/tests from the parent class.

```{code-block} python
class TestBase:
    var = 3

    def test_var_positive(self):
        assert self.var >= 0

class TestSub(TestBase):
    var = 8
    def test_var_even(self):
        assert self.var % 2 == 0
```


The R  project structure above has one test file per function in the modules.
There are multiple test files for the `math.R` module because it contains more than one function.
Tests in these test files do not need grouping into classes, as the file name is used to indicate exactly which function or class is being tested.
Tests in R are now linked together based on the file, previously named [contexts](https://testthat.r-lib.org/reference/context.html).
Context is now tied to test file name to ensure they are always synced.
The `context()` function is now depreciated and should be removed from your R script.

These are the common conventions for each of Python and R, but are interchangeable.
Use the approach that makes it easiest for developers to identify the relationship between tests and the code they are testing.

Note that some test frameworks allow you to keep the tests in the same file as the code that is being tested.
This is a good way of keeping tests and code associated,
but you should follow good modular code practices to separate unrelated code into different files.
Additional arguments are made to separate tests and functions when you are packaging your code.
If you store unit tests and code in the same file,
the unit tests would also be packaged and installed by additional users.
Therefore when packaging code,
you should move the unit tests to an adjacent test folder as users will not need to have unit tests installed when installing the package.

When separating unit tests into main package and testing scripts, it is important to import your package to ensure the correct functions are being unit tested.
For the module structure outlined previously, use `from src.math import my_math_function`.
For R, you need to specify the name of your package within the `testthat.R` file within your tests folder.

## Structuring tests

To maintain a consistency across modules you develop, you should follow [PEP8](https://peps.python.org/pep-0008) (Python)
or [Google](https://google.github.io/styleguide/Rguide.html) / [tidyverse](https://style.tidyverse.org/) (R) standards when structuring unit tests.

For python this involves importing all needed functions at the beginning of the test file.
To ensure you import the correct functions from your module,
we recommended you install a local editable version into your virtual environment.
Run `pip install -e .` and any changes made to your
module functions will also be updated in your python environment.
Following this it is recommended to define fixtures, classes and then test functions.
An example of this is below.
More information can be found in Real Python [Getting Started With Testing in Python](https://realpython.com/python-testing/).

You should follow a similar structure in R, with all modules loaded in the beginning of a test script.
Test contexts and then functions should be defined in turn as shown above.
For more information see [testing design in R](https://r-pkgs.org/testing-design.html).

Generally, tests within the same file should follow some structure or order.
We recommend that the order that functions are defined in the main script is also mirrored
within the test scripts.
This will be easier for future developers to debug and follow and
ensures that no functions have been missed and do not have unit tests written.


## Test that new logic is correct using unit tests

When you implement new logic in code, tests are required to assure that the code works as expected.

To make sure that your code works as expected, you should write tests for each individual unit in your code.
A unit is the smallest modular piece of logic in the code - a function or method.

Unit tests should cover realistic use cases for your function, such as:
* boundary cases, like the highest and lowest expected input values
* positive, negative, zero, and missing value inputs
* examples that trigger errors that have been defined in your code

When your function documentation describes the expected inputs to your function, there is less need to test unexpected cases.
If misuse is still likely or risky, then providing the user with an error is the best approach to mitigate this risk.

Reusing logic from an existing package that is already tested does not require tests when we use that logic alone.
You should be aware of whether your dependencies are sufficiently tested.
Newly developed packages or those with very few users are more likely to not be thoroughly tested.

## Test that different parts of the code interact correctly using integration tests

Integration tests are those that test on a higher level than a unit. This includes testing that:
* multiple units work together correctly
* multiple high level functions work together (e.g., many units grouped into stages of a pipeline)
* the analysis works with typical inputs from other systems

Integration tests give you assurance that your analysis is fit for purpose.
Additionally, they give you safety when refactoring or rearranging large parts of code.
Refactoring is an important part of managing the complexity of your analysis as it grows.

You can similarly consider a high level stage of an analysis pipeline.
If you have a stage responsible for imputing missing values, you can create integration tests to check that all values are
imputed and that you used particular imputation methods for specific cases in your test data.
When changes are made to individual imputation methods you might not expect these general characteristics to change.
This test helps to identify cases where this inadvertently has changed.

```{note}
Integration tests are more robust when they focus on general high level outcomes that you don't expect to change often.
Integration tests that check very specific outcomes will need to be updated with any small change to the logic within the part that is being tested.
```

## Test that the analysis runs as expected using end-to-end tests

End-to-end testing (sometimes called system testing) checks the entire workflow from start to finish, ensuring all components work correctly in real-world scenarios. While integration testing focuses on the interaction of specific modules, end-to-end testing involves all elements of a pipeline. This is useful when refactoring code for example, by providing assurance that overall functionality remains unchanged. 

For example, a piece of analysis has an end-to-end test to check that outputs are generated and the data are the right shape or format. There might also be a "regression" test that checks that the exact values in the output remain the same. After you make any changes to tidy up or refactor the code, these end-to-end tests can be run to assure no functionality has accidentally changed.

Use end-to-end tests to also quality assure a project from an end user's perspective; these should be run in an environment that replicates the production environment as closely as possible. This type of testing can catch errors that individual unit tests might miss and confirms that the output is fit for purpose and the user requirements are met. End-to-end testing is a form of 'black box' testing, meaning the tester verifies functionality without focusing on the underlying code. It is therefore important to use end to end testing alongside other forms of testing such as unit tests.


## Good practices for integration and end-to-end testing

When devising an integration or end-to-end testing it’s important to follow these good practices:

- Planning ahead: Have a clear plan of what you want to test and how before you start.
- Testing Early:  Start testing integration as soon as parts are combined rather than waiting until everything is finished. This helps catch issues sooner.
- Use Real Data: Whenever possible, use real data in your tests to make sure everything behaves like it would in the real world. When not possible, make sure the test data reflect the complexities of real data.
- Automate tests: Automate your integration tests. This makes it easier to run them frequently and catch problems quickly.
- Checking dependencies: Make sure to test how different components rely on each other, as issues can arise there.
- Test for failures: don’t just test for success; also check how the system behaves when things go wrong. This helps ensure it handles errors gracefully.
- Keep tests isolated: Try to isolate tests so that one failure doesn’t affect another, making it easier to pinpoint issues.
- Document: Keep a record of tests, results, and issues found. This helps with future testing and understanding what changes might affect integration.




## Isolate code tests from external systems

Testing code that interacts with an external system can be particularly challenging when you can't guarantee
that the system will provide you with the same response each time; this could include code querying a database or
making API requests, for example.

Best practice is to separate external system dependencies from your code tests as much as possible. This can mitigate against various risks, depending on your application:

- Testing database interaction with a production database could result in damage to, or loss of, data.
- Making real API calls when testing a function that handles requests could incur unintended monetary costs.

Isolating code from external systems allows for tests to run without reliance on the real systems; for example, tests for a database interaction that can still run even if the database connection goes down.
Writing tests in this way means that tests evaluate how your code handles an output or response, and not the system dependency itself.
This is another benefit of enforcing isolation in unit tests - helping you understand when errors are coming from an external system, and when they're coming from your code.
The unit of code being tested is referred to as the 'System Under Test' (SUT).

One way of achieving this is with mocking. This is where a response from an outside system is replaced with a mock object that you can test your code against.
In this example, there's a function making an API request in `src/handle_api_request.py`, and two test functions in `tests/test_handle_api_request.py`.
The response from `requests.get()` is mocked with a `Mock()` object, to which `text` and `status_code` attributes are assigned.
You can now evaluate the `get_response()` function for how it handles successful and unsuccessful requests; but thanks to the mocking, get requests are not made to `http://example.com`.

```{code-block} python
# AI has been used to produce content within this artefact.

# src/handle_api_request.py
import requests

def get_response(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        raise(requests.HTTPError("Unsuccessful request"))

    return response.text

...

# tests/test_handle_api_request.py
from src.api_requests import get_response
import requests
import pytest
from unittest import mock

@mock.patch("requests.get")
def test_get_response_success(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.text = "Successful"
    mock_response.status_code = 200

    mock_requests_get.return_value = mock_response
    
    actual = get_response("http://example.com/good-request")
    assert(actual == "Successful")

@mock.patch("requests.get")
def test_get_response_fail(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_requests_get.return_value = mock_response
    
    with pytest.raises(requests.HTTPError):
        actual = get_response("http://example.com/bad-request")

```

These tests pass successfully. However, if the mocking was implemented incorrectly and the real request executed, our tests may continue to pass depending on how the response was handled by our function. Better practice is to assert that the mock function was called - for example, with `mock_function.assert_called()` or `mock_function.assert_called_one_with(parameter)` - in order be assured of the tests working as expected. Additional stringency comes from matching warnings and error message strings with `pytest.raises()`.

```{code-block} python
# tests/test_handle_api_request.py
from src.api_requests import get_response
import requests
import pytest
from unittest import mock

@mock.patch("requests.get")
def test_get_response_success(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.text = "Successful"
    mock_response.status_code = 200

    mock_requests_get.return_value = mock_response
    
    actual = get_response("http://example.com/good-request")
    assert(actual == "Successful")

    mock_requests_get.assert_called()
    mock_requests_get.assert_called_once_with("http://example.com/good-request")


@mock.patch("requests.get")
def test_get_response_fail(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_requests_get.return_value = mock_response
    
    with pytest.raises(requests.HTTPError, match="Unsuccessful request"):
        get_response("http://example.com/bad-request")

    mock_requests_get.assert_called()
    mock_requests_get.assert_called_once_with("http://example.com/bad-request")

```

Consider using fixtures to make test code more concise by generating the necessary `Mock` object attributes dynamically. Use [`Mock.reset_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.reset_mock) to remove the attributes associated with a mock object between different test cases.

```
# tests/test_handle_api_request.py
from src.api_requests import get_response
import requests
import pytest
from unittest import mock

@pytest.fixture(scope="function")
def mock_response():
    def _create_mock_response(url):
        """factory function allows flexible return values when evaluated"""
        mock_response = mock.Mock()
        if url == "http://example.com/good-request":
            mock_response.text = "Successful"
            mock_response.status_code = 200
        elif url == "http://example.com/bad-request":
            mock_response.status_code = 400
        return mock_response
    return _create_mock_response


@mock.patch("requests.get")
def test_get_response_all_conditions(mock_requests_get, mock_response):

    good_url = "http://example.com/good-request"
    mock_requests_get.return_value = mock_response(good_url)
    actual = get_response(good_url)
    assert actual == "Successful"
    mock_requests_get.assert_called_once_with(good_url)

    mock_requests_get.reset_mock()

    bad_url = "http://example.com/bad-request"
    mock_requests_get.return_value = mock_response(bad_url)
    with pytest.raises(requests.HTTPError, match="Unsuccessful request"):
        get_response(bad_url)
    mock_requests_get.assert_called_once_with(bad_url)

```

[Monkeypatching](https://docs.pytest.org/en/stable/how-to/monkeypatch.html#how-to-monkeypatch-mock-modules-and-environments) in `pytest` provides an alternative way of handling mock objects and attributes, and allows for the mocking of environment variables.

## Write tests to assure that bugs are fixed

Each time you find a bug in your code, you should write a new test to assert that the code works correctly.
Once you resolve the issue, this new test should pass and give you confidence that the bug has been fixed.

When you change or refactor your code in future, the new tests
will continue to assure that bugs you have already fixed will not reappear.
Doing this increases the coverage of your tests in a proportionate way.

## Write tests before writing logic

The best practice for testing code is to use test-driven development (TDD).
This is an iterative approach that involves writing tests before writing the logic to meet the tests.

For a piece of analysis logic, you should know in advance what the desired outcome is.
This might be from a user need (for example, someone needs output data in a certain shape) or an internal requirement (for example, you need to impute all missing values).
Given that you know the expected outcome, you can write the test before you think about how you are going to write the solution.

```{note}
This section is framed more like training. Once dedicated training has been produced this section will likely be adapted to provide more concise guidance on
the practice.
```

TDD typically repeats three steps:
1. Red - Write a test that we expect to fail.
2. Green - Write or update our code to pass the new test.
3. Refactor - Make improvements to the quality of the code without changing the functionality.

As with any code that is adequately covered by tests, code written using TDD can be safely refactored.
You can be more confident that your tests will capture any changes that would unintentionally alter the way our code works.

Repeat the above three steps to gradually increase the complexity of your code.
The first test you write should focus on the minimum functionality.
Then this minimal functionality is implemented, to do nothing more than the test requires.
On the next iteration the test becomes more complex, as does the code logic.
In each iteration the refactoring steps means that you manage the increasing complexity of the code.

This approach provides many benefits beyond good test coverage.
The iterative nature of TDD encourages you to follow a number of other good practices.
These include keeping test data minimal and keeping functions or classes simple and focussed on doing one thing well.
TDD requires practice but is proven to produce clean, robust and adaptable code.

[Behaviour driven development](https://en.wikipedia.org/wiki/Behavior-driven_development) and
[acceptance test driven development](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)
are extensions of TDD with a useful focus on user needs.

## Modelling-relevant testing

To ensure you conduct model-relevant tests within the analysis, it is important to use data that is representative of real-world scenarios and free from biases. Select diverse datasets that reflect the variety of conditions the model will encounter in practice. Additionally, it is important to regularly update test data to capture any changes in the environment or user behaviour.

### Acceptance testing
Acceptance testing ensures that the model meets specified requirements and performs well in real-world scenarios. It verifies that the model's outputs align with business needs and user expectations. There are three types of acceptance testing:

•	User Acceptance Testing (UAT): End-users test the system to ensure it meets their needs and provides accurate outputs. This involves real-world scenarios where users interact with the model and provide feedback on its performance.

•	Business Acceptance Testing (BAT): Validates that the system meets business requirements and integrates well with existing workflows. This type of testing ensures that the model supports business processes and delivers value to the organization.

•	Operational Acceptance Testing (OAT): Ensures the system is operationally ready, including backup, recovery, and maintenance. This involves testing the model's performance under different operational conditions to ensure it can handle various scenarios.


### Defining and Using Appropriate Metrics

Evaluating model performance using metrics is essential. Choose metrics that align with the specific goals of the project and provide meaningful insights into the performance of the model in this context.

Use appropriate metrics to evaluate model performance. For example, precision and recall are well established measures for evaluating the performance of data linkage. The right metrics help assess the model's effectiveness in different scenarios.

### Cross-Validation Techniques

To ensure that the model generalises well to unseen data, you can use techniques like k-fold cross-validation. This method involves dividing the data into k subsets and training the model k times, each time using a different subset as the validation set and the remaining data as the training set. Cross-validation helps identify potential overfitting and ensures that the model performs consistently across different data subsets.

### Stress Testing

Stress testing evaluates how the model performs under extreme conditions or with noisy data. This helps identify the model's robustness and ability to handle unexpected inputs. Stress testing involves introducing variations or noise into the input data and observing how this affects the model's outputs. This type of testing is useful for understanding the model's limits and ensuring it can handle real-world challenges.

### Sensitivity Analysis

Sensitivity analysis tests how sensitive the model's outputs are to changes in input data or parameters. This analysis helps understand the model's behaviour and identify potential weaknesses. Sensitivity analysis involves systematically varying the input data or model parameters and measuring the impact on the model's outputs. This helps in identifying critical factors that influence the model's performance and making necessary adjustments.

### Model Interpretability

Implementing methods to make the model's outputs interpretable is essential for building trust with stakeholders. Techniques like SHAP (SHapley Additive exPlanations) values or LIME (Local Interpretable Model-agnostic Explanations) can help explain the model's decisions. These methods provide insights into how different features contribute to the model's outputs, making it easier for analysts and stakeholders to understand and trust the model's outputs.

### Model Optimisation

Use optimisation to adjust the model's parameters to achieve the best overall performance. Continuous optimisation ensures that the model remains effective and efficient over time as inputs change. There are lots of techniques available to optimise performance; most are designed to help find the best parameters for the model to enhance its accuracy and efficiency.

Examples of optimisation techniques for machine learning include grid search and parameter tuning. Grid search involves systematically searching through a predefined set of hyperparameters, while hyperparameter tuning adjusts the model's parameters to achieve the best possible performance.

## Reduce repetition in test code (fixtures and parameterised tests)

Where possible, you should reduce repetition in your tests. Tests are code too, so you should still [make this code reusable](functions).
As with functional code, test code is much easier to maintain when it is modular and reusable.

### Use fixtures to reduce repetition in test set up

As your test suite grows, many of your tests may use similar code to prepare your tests or to clean up after each test has run.
You can be more tolerant of repetition in test code.
However, copying code snippets for each test is laborious and increases the risk of applying those steps inconsistently.

You can use fixtures to help avoid this form of repetition in tests.
A fixture allows you to define your test preparation and clean up as functions.
You then use the fixture to carry out these steps consistently for each test that they are required for.

In Class-based testing frameworks, these functions tend to be separated into `SetUp` and `TearDown` functions.
These are set to run before and after each test, respectively.

Fixtures can be most useful when setting up a test object takes a large amount of time or resource.
They can be designed to run for each test, once for a group of tests or once for the whole test suite.

```{code-block} python
import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark_session():
    """Session-wide SparkSession to optimise testing PySpark functions."""
    spark_session = SparkSession.builder.master("local[*]").getOrCreate()
    yield spark_session
    spark_session.stop()

def test_my_function(spark_session):
    ...

def test_another_function(spark_session):
    ...
```

This example shows a fixture named `spark_session` with a testing session scope.
Starting a new spark session can take a few seconds, so creating a new session
for each test function would significantly increase the time it takes to run all of the tests.
With a session level scope, you call the function once for the whole testing session
and share the resulting `SparkSession` object between your tests.
Reusing the same `SparkSession` object is safe to do if none of our tests modify the object.

```{code-block} python
import pytest

@pytest.fixture(scope="function")
def database_connection():
    database_connection = connect_to_test_database()
    yield database_connection
    database_connection.reset_to_default()

def test_my_function(database_connection):
    ...

def test_another_function(database_connection):
    ...
```

Fixtures can also be useful for undoing any effects that each test run might have on the global environment.
For example, they can remove test data which has been written to a temporary file or database.
The example above shows how you might use a fixture to reset a test database between each test.
It uses a test function scope, so the fixture is run separately for each test function that uses it.
The fixture performs a reset on the database after the database connection has been used by the test.

For usage details see the documentation for packages that offer fixtures:
* [Python `pytest` Fixture](https://docs.pytest.org/en/stable/fixture.html) documentation
* [R `testthat` Fixture](https://testthat.r-lib.org/articles/test-fixtures.html) documentation

### Use parameterisation to reduce repetition in test logic

Similar steps are often repeated when testing multiple combinations of inputs and outputs.
Parameterisation allows reduction of repetition in test code, in a similar way to writing your logic in functions.
Specify pairs of inputs and expected outputs, so your testing tool can repeat the same test for each scenario.

Using parameterisation in a test framework is equivalent to using a for-loop to apply a test function over multiple inputs and expected outputs.
Using functionality from test packages may provide improved running efficiency and more detailed reporting of test failures.

In `pytest`, this can be achieved using the [Parametrize mark](https://docs.pytest.org/en/stable/parametrize.html).

In R, the `patrick` package extends `testthat` to provide a
[`with_parameters_test_that`](https://rdrr.io/cran/patrick/man/with_parameters_test_that.html) function to achieve this.

### Define Source Code

Take the below function for example, which can take 2 arguments.

```{code-block} python
def sum_two_nums(num1:int, num2:int) -> int:
    """Sum two numbers. Numbers can be integer or float."""
    return num1 + num2
```

### Simple Parameterisation

It is simple to check multiple assertions for this simple function. In the most
basic example, simply define a parameterised list of parameter values and
expected outcomes.

```{code-block} python
import pytest

@pytest.mark.parametrize("num_1s, expected_out", [(1, 2), (-1, 0), (0, 1)])
def test_sum_two_nums_parameterise_arg_1(num_1s, expected_out):
    assert sum_two_nums(num1=num_1s, num2=1) == expected_out

```

We reference the parameter values and expected answers in the same way that we
access pytest fixtures, covered earlier in this article. Running `pytest -v`
reveals 3 tests are run, with the parameterised values printed to the console:

```{code-block}

collected 3 items                                                             

foo.py::test_sum_two_nums_parameterise_arg_1[1-2] PASSED                  [ 33%]
foo.py::test_sum_two_nums_parameterise_arg_1[-1-0] PASSED                 [ 66%]
foo.py::test_sum_two_nums_parameterise_arg_1[0-1] PASSED                  [100%]

============================= 3 passed in 0.00s ==============================

```

It would be trivial to repeat a similar parameterised test for `num_2` values.
But how is it possible to make assertions when parameterising **both**
arguments?

### Stacked Parameterisation

In order to test multiple values for `num1` and `num2`, a fixture should be
defined that returns a dictionary of the expected values. For example:

```{code-block} python

@pytest.fixture
def expected_answers() -> dict:
    """A nested dictionary of expected answers for all combinations in 0:5.

    First level key corresponds to `num1` and the second level key to `num2`.
    The dictionary values are the expected answers. So that when we subset the
    dictionary with parameterised values, we provide the expected values to
    assert statements.

    Returns
    -------
    dict
        Dictionary of cases and their expected tuples.
    """
    expected= {
        0: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4,},
        1: {0: 1, 1: 2, 2: 3, 3: 4, 4: 5,},
        2: {0: 2, 1: 3, 2: 4, 3: 5, 4: 6,},
        3: {0: 3, 1: 4, 2: 5, 3: 6, 4: 7,},
        4: {0: 4, 1: 5, 2: 6, 3: 7, 4: 8,},
    }
    return expected

```

This fixture of expected answers can be served to a parameterised test and the
returned dictionary can be accessed to provide the expected answer for
parameter combinations. To parameterise both of the required arguments,
the parameterise statements are simply stacked on top of each other:

```{code-block} python

@pytest.mark.parametrize("num1s", range(0,5))
@pytest.mark.parametrize("num2s", range(0,5))
def test_sum_two_nums_stacked_parameterise(num1s, num2s, expected_answers):
    assert sum_two_nums(
        num1=num1s, num2=num2s
        ) == expected_answers[num1s][num2s]
```

Executing this test with `pytest -v` shows all combinations are tested:

```{code-block}
collected 25 items                                                            

foo.py::test_sum_two_nums_stacked_parameterise[0-0] PASSED                [ 14%]
foo.py::test_sum_two_nums_stacked_parameterise[0-1] PASSED                [ 17%]
foo.py::test_sum_two_nums_stacked_parameterise[0-2] PASSED                [ 21%]
foo.py::test_sum_two_nums_stacked_parameterise[0-3] PASSED                [ 25%]
foo.py::test_sum_two_nums_stacked_parameterise[0-4] PASSED                [ 28%]
foo.py::test_sum_two_nums_stacked_parameterise[1-0] PASSED                [ 32%]
foo.py::test_sum_two_nums_stacked_parameterise[1-1] PASSED                [ 35%]
foo.py::test_sum_two_nums_stacked_parameterise[1-2] PASSED                [ 39%]
foo.py::test_sum_two_nums_stacked_parameterise[1-3] PASSED                [ 42%]
foo.py::test_sum_two_nums_stacked_parameterise[1-4] PASSED                [ 46%]
foo.py::test_sum_two_nums_stacked_parameterise[2-0] PASSED                [ 50%]
foo.py::test_sum_two_nums_stacked_parameterise[2-1] PASSED                [ 53%]
foo.py::test_sum_two_nums_stacked_parameterise[2-2] PASSED                [ 57%]
foo.py::test_sum_two_nums_stacked_parameterise[2-3] PASSED                [ 60%]
foo.py::test_sum_two_nums_stacked_parameterise[2-4] PASSED                [ 64%]
foo.py::test_sum_two_nums_stacked_parameterise[3-0] PASSED                [ 67%]
foo.py::test_sum_two_nums_stacked_parameterise[3-1] PASSED                [ 71%]
foo.py::test_sum_two_nums_stacked_parameterise[3-2] PASSED                [ 75%]
foo.py::test_sum_two_nums_stacked_parameterise[3-3] PASSED                [ 78%]
foo.py::test_sum_two_nums_stacked_parameterise[3-4] PASSED                [ 82%]
foo.py::test_sum_two_nums_stacked_parameterise[4-0] PASSED                [ 85%]
foo.py::test_sum_two_nums_stacked_parameterise[4-1] PASSED                [ 89%]
foo.py::test_sum_two_nums_stacked_parameterise[4-2] PASSED                [ 92%]
foo.py::test_sum_two_nums_stacked_parameterise[4-3] PASSED                [ 96%]
foo.py::test_sum_two_nums_stacked_parameterise[4-4] PASSED                [100%]

============================= 25 passed in 0.01s =============================

```

## Testing SQL
Although testing SQL is outside the scope of this guidance, many of the concepts discussed
in this guidance are also applicable to SQL. In SQL,
single queries often contain several parts. These can be more readily
tested by breaking up these queries and taking a more step-by-step approach,
similar to breaking up functions. Use [Integration testing](#test-that-different-parts-of-the-code-interact-correctly-using-integration-tests) to verify
that queries and functions behave as expected when combined.

Test functions that interact with a database (DB) within a development
environment, rather than with a production database. This prevents
unintended data modification or deletion. Functions can also be unit tested
from simplified dummy data.

There are a range of established SQL testing frameworks. Examples include [tSQLt](https://github.com/tSQLt-org/tSQLt)
and [pgTAP](https://github.com/theory/pgtap/) for Postgres.


## In a time crunch? The risks to skipping tests
In an ideal world, you would never skip testing code, ensuring the software is reliable
and easily reproducible. However, in practice there are times when skipping tests may be necessary —
perhaps due to tight deadlines, limited resources, or the need to quickly get a feature up
and running. While this can save time in the moment, it’s important to be cautious, as
skipping tests can lead to hidden problems that may become harder to fix later, particularly
as the project grows. Whenever tests are set aside, it’s best to have a plan for going back to add
them, to avoid risks to the stability and quality of the software.

<!-- file: book/continuous_integration.md -->

# Automating code quality assurance

## Motivation

You can automate various tasks to increase the quality of code and make development easier and less tedious.
Automating the running of unit tests is especially important to establish trust in your pipeline or package, by ensuring that all unit tests pass before every merge.


(automate-tests)=
### Automate tests to reduce risk of errors

You should run tests whenever you make changes to your project.
This ensures that changes do not break the existing, intended functionality of your code.
However, it is easy to forget to run your tests at regular intervals.

"Surely I can automate this too?"

Absolutely! Automatic testing, amongst other quality assurance measures, can be triggered when you make changes to your remote version control repository.
You can use these tools to ensure that all changes to a project are tested.
Additionally, it allows others, who are reviewing your code, to see the results of your tests.


(continuous-integration)=
## Commit small changes often

Committing small changes regularly is often referred to as Continuous Integration (CI).
You can achieve this easily through the use of [version control](version_control.md), such as Git.

You should commit every time you make a working change.
Fixed a typo? Commit. Fixed a bug? Commit. Added a function? Commit. Added a test? Commit.
As a very rough guide, you should expect to commit a few times each hour and push your changes to your shared software repository at least once a day.
If the task is unfinished at the end of the day, you should consider if the task has been sufficiently broken down.

CI should be underpinned by automating routine code quality assurance tasks.
This quality assurance includes verifying that your code successfully builds or installs. It also ensures your [code tests](testing_code.md) run successfully.
You can achieve this in a number of ways such as use of Git hooks and workflows.


## Use Git hooks to encourage good practice

[Git hooks](https://git-scm.com/docs/githooks) are scripts that can be set to run locally at specific points in your Git workflow,
such as pre-commit, pre-push, etc.
You can use them to automate code quality assurance tasks, e.g., run tests, follow style guides, or enforce commit standards.

For example, you could set up a `pre-commit` or `pre-push` hook that runs your tests before you make each commit or push to the remote repository.
This might stop your commit/push if the tests fail, so that you won't push breaking changes to your remote repository.

```{note}
If your code is likely to be run on a range of software versions or operating systems, you can test on a variety of these.
Tools exist to support local testing of combination software versions and package dependency versions:

* [tox](https://tox.readthedocs.io/en/latest/) or [nox](https://nox.thea.codes/en/stable/) for Python
* [rhub](https://r-hub.github.io/rhub/) for R
```


(linters-formatters)=
### Linters and formatters

Style guides are important for making sure your code is clear and readable and should form part of your quality assurance process.
However, as discussed in [](automate-style-checks), the process of checking and fixing code for style and formatting is tedious.
Automation can speed up this work, either by providing suggestions as you write the code or by reformatting your code to follow your chosen style.

Two main types of tool exist for these tasks:

* Linters - these analyse your code to flag stylistic errors (and sometimes bugs or security issues too).
* Formatters - these not only detect when you have diverged from a style, but will automatically correct the formatting of your code to conform to a particular style.

```{list-table} Packages that can be used for linting or formatting in Python and R
:header-rows: 1
:name: linters

* - Language
  - Linters
  - Formatters
* - Python
  - `flake8`, `pylint`, `Bandit`
  - `Black`, `Isort`
* - R
  - `lintr`
  - `formatR`, `styler`
* - Markdown
  - `pymarkdownlnt`
  -
```

You can use these tools locally (in the command line) or as git pre-commit hooks.
As described above, using pre-commit hooks allows you to run these automatically every time there are changes;
this can reduce the burden on developers and reviewers checking that code conforms to style guides.

Make sure you read the documentation for these tools before you use them to understand what they are checking or changing in your code.
You can configure some of them to ignore or detect specific types of formatting error.
You can also run multiples of the tools to catch a broader range of stylistic or programmatic errors.

## Workflows

GitHub Actions and GitLab Pipelines are both able to define custom workflows using YAML.
Workflow refers to a defined sequence of steps and actions that you need to perform
to complete a specific task or process.
Workflows are commonly used in software development to automate repetitive or complex tasks,
such as building and deploying software, testing code, and managing code reviews.
GitHub Actions and GitLab Pipelines both allow automated workflows that trigger
builds and tests whenever code changes are pushed to the repository.

### Example use cases for GitHub Actions

Here are some examples to support understanding of these ideas.

#### Configure GitHub actions to automate tests

Here is an example configuration file, for use with GitHub actions.
The `YAML` file format, used below, is common to a number of other CI tools.

```yaml
name: Test python package

on:
  push:
    branches:
      - master
  pull_request:

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10, 3.11]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest 
        pip install -r requirements.txt
        
    - name: Test with pytest
      run: |
        pytest
```

The first section of this example describes when we should run our workflow.
In this case, we're running the CI workflow whenever code is `push`ed to the `master` branch or where any Pull Request is created.
In the case of Pull Requests, the results of the CI workflow will be report on the request's page.
If any of the workflow stages fail, this can block the merge of these changes onto a more stable branch.
Subsequent commits to the source branch will trigger the CI workflow to run again.

Below `jobs`, we're defining what tasks we would like to run when we trigger our workflow.
We define what operating system we would like to run our workflow on - the Linux operating system `ubuntu` here.
The `matrix` section under `strategy` defines parameters for the workflow.
We will repeat the workflow for each combination of parameters supplied here - in this case 4 recent Python versions.

The individual stages of the workflow are defined under `steps`.
`steps` typically have an informative name and run code to perform an action.
Here `uses: actions/checkout@v3` references [existing code](https://github.com/actions/checkout) that will retrieve the code from our repo.
The subsequent `steps` will use this code.
The next step provides us with a specific Python version, as specified in the `matrix`.
Then we install dependencies/requirements for our code and the `pytest` module.
Finally, we run `pytest` to check that our code is working as expected.

This workflow will report whether our test code ran successfully for each of the specified Python versions.

#### Configure GitHub actions to build and deploy documentation

It is important to maintain the documentation relating to your project to ensure contributors and users can understand, maintain, and use your product correctly.
One basic way of doing this is maintaining markdown files within a GitHub repository.
However, multiple tools exist that can transform these markdown files into HTML content.
A popular tool for building and deploying HTML documentation is [Sphinx](https://www.sphinx-doc.org/en/master/).
Here are two examples of repositories that use sphinx to build its documentation:

* [Quality assurance of code for analysis and research (this book)](https://github.com/best-practice-and-impact/qa-of-code-guidance/blob/main/.github/workflows/book.yaml)
* [govcookiecutter](https://github.com/best-practice-and-impact/govcookiecutter/blob/main/.github/workflows/govcookiecutter-deploy-documentation.yml)

### Example GitLab Pipeline

GitLab has an equivalent to GitHub Actions called GitLab Pipelines.
The use cases for these are practically the same, with a change in syntax and file structure.
[PATRICK'S SOFTWARE BLOG](https://web.archive.org/web/20230321180431/https://www.patricksoftwareblog.com/setting-up-gitlab-ci-for-a-python-application/) provides a simple GitLab
pipeline example and detailed description on how to use it.
For further details [GitLab provides documentation on how to create and use GitLab Pipelines](https://docs.gitlab.com/ee/ci/).

### Comprehensive example of automating code quality assurance

You can see a detailed example of CI in practice in the `jupyter-book` project.
A recent version of the
[`jupyter-book` CI workflow](https://github.com/executablebooks/jupyter-book/blob/6fb0cbe4abb5bc29e9081afbe24f71d864b40475/.github/workflows/tests.yml) includes:

* Checking code against style guidelines, using [pre-commit](https://pre-commit.com/).
* Running code tests over:
  * a range of Python versions.
  * multiple versions of specific dependencies (`sphinx` here).
  * multiple operating systems.
* Reporting test coverage.
* Checking that documentation builds successfully.
* Deploying a new version of the `jupyter-book` package to [the python package index (PyPI)](https://pypi.org/).

<!-- file: book/learning.md -->

# Learning resources

This section links to training and self-led learning resources, which relate to sections of the guidance.

Many of these learning resources point to the UK Statistics Authority Learning Hub.
All government analysts can request an account for the hub via a [form](https://forms.office.com/pages/responsepage.aspx?id=vweIB4LOiEa84A2BFoTcRlPdx8djn4tCqrCyavGcBe9UNTY3RUpEQkkwVDhITDAxUk8wTUhBQ01MNS4u&route=shorturl&wdLOR=c0BA596B0-B641-4BF9-BCDB-8C188FCB872C).

Please note that learning resources from non-government training providers (i.e. not accessed through the Hub) may not always follow best practice.
However, exposure to a range of applied examples will still benefit your learning.
You should compare and contrast your learning to the good practices outlined in the guidance.


## Core programming

The [RAP learning pathway](https://learninghub.ons.gov.uk/course/view.php?id=1273) covers training for most of the good practices outlined in this book,
with a focus on Python and R.
Other courses below can be used to supplement this learning.


### Python

* [Introduction to object-oriented programming (OOP) in Python](https://learninghub.ons.gov.uk/enrol/index.php?id=1199)
* [The Official Python Getting Started Guide](https://www.python.org/about/gettingstarted/)
* [Learn Python](https://www.learnpython.org/), supported by DataCamp


### R

* [R Basics on Udemy](https://www.udemy.com/course/r-basics/)


### General

* [Software carpentry](https://software-carpentry.org/lessons/)
* [Data carpentry](https://datacarpentry.org/lessons/)


## Data manipulation

### Python

* [Dataframes, manipulation and cleaning in Python](https://learninghub.ons.gov.uk/enrol/index.php?id=1156)
* [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/index.html)
* [Python for Data Analysis](https://github.com/wesm/pydata-book)


### R

* [Dataframes, manipulation and cleaning in R](https://learninghub.ons.gov.uk/enrol/index.php?id=1158)
* [R for Data Science](https://r4ds.had.co.nz/)
* [Advanced R](https://adv-r.hadley.nz/index.html)


### SQL

* [Foundations of SQL](https://learninghub.ons.gov.uk/enrol/index.php?id=1162)
* [w3schools.com SQL Tutorial](https://www.w3schools.com/sql/default.asp)
* [Python SQL libraries](https://realpython.com/python-sql-libraries/)
* [SQL databases and R](http://datacarpentry.org/R-ecology-lesson/05-r-and-databases.html)


## Command line tools

### General

* [Windows and UNIX Command Line Basics](https://learninghub.ons.gov.uk/enrol/index.php?id=1166)
* [Learn enough (UNIX) command line to be dangerous](https://www.learnenough.com/command-line-tutorial/basics)
* [The UNIX workbench](https://seankross.com/the-unix-workbench/)


(git-learning)=
### Git

* [Intro to Git](https://learninghub.ons.gov.uk/enrol/index.php?id=1165)
* [Introduction to continous integration](https://learninghub.ons.gov.uk/course/view.php?id=1200)
* [The Pro Git book](https://git-scm.com/book/en/v2)
* [Software Carpentry: Version Control with Git](https://swcarpentry.github.io/git-novice/) - an applied project
* Interactive online training with [Katacoda](https://www.katacoda.com/courses/git) or [Learn Git Branching](https://learngitbranching.js.org/)
* [GitHub's Git Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [GitHub Git Handbook](https://guides.github.com/introduction/git-handbook/)
* [Atlassian's Learn Git](https://www.atlassian.com/git)


## Testing

* [Introduction to Unit Testing in Python and R](https://learninghub.ons.gov.uk/course/view.php?id=1171)


## Making software accessible

* [A11Y Project software, books and tools](https://www.a11yproject.com/resources/)


## Reproducible Analytical Pipelines

* [Analysis Function RAP overview](https://analysisfunction.civilservice.gov.uk/support/reproducible-analytical-pipelines/)
* [The cross government RAP Champion Network](https://analysisfunction.civilservice.gov.uk/support/reproducible-analytical-pipelines/reproducible-analytical-pipeline-rap-champions/)
* [ONS Data Science Campus RAP learning materials](https://github.com/datasciencecampus/gov-uk-rap-materials)


## Learning from mistakes

Finally, it is often good to see what not to do and learn from the mistakes of others.
The following is a compilation of bad code in Python, but worth a read whatever your language as most apply to R and Python, as well as other languages.

* [The Little Book of Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/index.html)

<!-- file: book/tools.md -->

# Tools

This section highlights tools that support reproducible analysis and research.
This includes tools for general software development and bespoke packages that have been developed for government analysis.
Those developed or contributed to within government are marked with the abbreviation (gov).

If you have developed a package for use in analysis or recommend any that are not included here, please add them to the list.
You can request a new tool to be added to the list by [creating an issue on GitHub](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/new/choose)
or [contacting us by email](mailto:ASAP@ons.gov.uk?subject=Duck%20Book%20Tools).
Alternatively, you can add it directly to the project by creating a Pull Request.
You can do this using the "Suggest edit" link under the GitHub logo at the top of this page.
Please include a link and brief description when requesting a new tool to be added.

The tools included on this page will in general follow the good quality assurance practices described in this guidance.
However, as with any software there is a chance that they may still contain bugs or limitations.
Please apply your own judgement when using them.
If you feel a tool should no longer be included in this list, please suggest an edit or get in touch.

## Data manipulation and analysis

Manipulating and analysing data.

### Python

* [pandas](https://pandas.pydata.org/) - common data analysis and manipulation
* [Polars](https://www.pola.rs/) - high performance data manipulation
* [PySpark](https://spark.apache.org/docs/latest/api/python/)  - data manipulation for distributed (large) data
* [Splink](https://moj-analytical-services.github.io/splink/) (gov) - probabilistic data linkage

### R

* [dplyr](https://dplyr.tidyverse.org/)  - common data analysis and manipulation
* [sparklyr](https://spark.rstudio.com/) - for distributed (large) data

## Publishing

* afcolours ([Python](https://pypi.org/project/py-af-colours/) and [R](https://cran.r-project.org/web/packages/afcolours/index.html)) (gov) - ease the use of the Analysis Function colour palettes for visually accessible graphs.
* [Quarto](https://quarto.org/) - reproducible documents for Python and R
* [a11ytables (R only)](https://co-analysis.github.io/a11ytables/index.html) (gov) - creating reproducible, accessible spreadsheets
* [gptables (Python and R)](https://gptables.readthedocs.io/en/latest/index.html) (gov) - creating reproducible, accessible spreadsheets

## Testing

Tools for implementing automated code testing.

### Python

* [pytest](https://docs.pytest.org/en/stable/) - common testing framework
* [unittest](https://docs.python.org/3/library/unittest.html) - common testing framework
* [hypothesis](https://hypothesis.readthedocs.io/en/latest/) - property-based testing
* [chispa (PySpark)](https://pypi.org/project/chispa/) - helper for testing PySpark code
* [coverage](https://coverage.readthedocs.io/en/coverage-5.3/) - measuring test coverage


### R

* [testthat](https://testthat.r-lib.org/) - common testing framework
* [assertr](https://docs.ropensci.org/assertr/) - common testing framework
* [patrick](https://github.com/google/patrick) - parameterised testing extension for `testthat`
* [covr](https://covr.r-lib.org/) - measuring test coverage

## Dependency management

* [venv (Python)](https://docs.python.org/3/library/venv.html) - manage packages using virtual environments
* [pyenv (Python)](https://github.com/pyenv/pyenv) - manage independent Python versions for different projects
* [renv (R)](https://rstudio.github.io/renv/articles/renv.html) - virtual environments for managing packages
* [conda](https://docs.conda.io/en/latest/) - manage language versions and packages for most languages

## Version control

* [Git](https://git-scm.com/) - common open source version control system
* [pre-commit](https://pre-commit.com/) - trigger checks (e.g. linters and formatters) before Git commits are created

## Project templates

* [govcookiecutter (Python)](https://github.com/best-practice-and-impact/govcookiecutter) (gov) - template project for reproducible analysis
* [Rgovcookiecutter (R)](https://github.com/best-practice-and-impact/Rgovcookiecutter) (gov) - template project for reproducible analysis

## Code Linters

Analysing code for stylistic errors, and sometimes bugs.

### Python

* [pylint](https://www.pylint.org/) - check coding style and identify some logical errors
* [flake8](https://flake8.pycqa.org/en/latest/) - check code style
* [Bandit](https://bandit.readthedocs.io/en/latest/) - check for common security issues
* [mypy](https://mypy.readthedocs.io/en/stable/) - check static types
* [Radon](https://radon.readthedocs.io/en/latest/) - check code complexity

### R

* [lintr](https://github.com/jimhester/lintr) - check code style


## Code Formatters

Automated code formatters.
These check code style, like linters, but also actively make changes to your code to meet a particular style.


### Python

* [Black](https://black.readthedocs.io/en/stable/)
* [Isort](https://pycqa.github.io/isort/)


### R

* [formatR](https://yihui.org/formatr/)
* [styler](https://styler.r-lib.org/)


## Packaging Code

Creating and releasing code as a package.

### Python

* [twine](https://pypi.org/project/twine/) - utility for publishing Python packages to [the Python Package Index PyPI](https://pypi.org/)

### R

* [goodpractice](http://mangothecat.github.io/goodpractice/) - gives advice on the quality of your R packages
* [fusen](https://thinkr-open.github.io/fusen/) - builds R packages from Rmarkdown file specifications


## Pipeline Orchestration

* [Apache Airflow](https://airflow.apache.org/) - workflow management platform
* [targets (R)](https://wlandau.github.io/targets-manual/) - defining and executing pipelines in R


(CI-tools)=
## Continuous Integration Platforms

* [GitHub Actions](https://github.com/features/actions)
* [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
* [Travis](https://travis-ci.org/)
* [Jenkins](https://www.jenkins.io/)
* [Coveralls](https://coveralls.io/)

<!-- file: book/generative_ai.md -->

# Generative AI

```{figure} ./_static/copilot_output.png
---
width: 90%
name: copilot_output
alt: A conversation with an Artifical Intelligence?
---
A conversation with an Artifical Intelligence?
```

```{note}
This guide is a work in progress. For corrections and suggested changes, please raise an [issue](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues) or contact the [Analysis Standards and Pipelines hub](mailto:ASAP@ons.gov.uk).
```

Generative AI (Artificial Intelligence) has become the most talked-about technological development in recent years. Chatbots and image generators are now widespread in workplaces. Most of us have heard the confident assertion that the use of generative AI as a coding assistant will revolutionise how coders work. Whether you are curious about using AI tools at work, or you have been encouraged to do so, this guide will explain some of the fundamental technology behind them so you can understand how they work, and offer suggestions for how to get the most out of them. This guide is intended to supplement the existing [Government Playbook on AI](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government) - all the principles laid out in the playbook still apply here.

## Introduction - Machine learning and Large Language Models

Generative AI (Artificial Intelligence) is a term that refers to a class of machine learning models. A machine learning model is a piece of software that is trained on a set of data to make predictions when given new data. Machine learning has been around for a long time and it is used in almost every industry to solve a wide variety of problems. As a government analyst, you may be quite familiar with machine learning already.

```{admonition} If you have never heard of machine learning before, click here
:class: dropdown
:name: ml-primer
### Machine learning rapid primer - linear regression

Say you worked for a company that wanted to know how to value land based on land area. You could train a machine learning model on existing real estate data, using price and land area.

A linear regression model of price and land area can be given as:

$$y' = b + m_1x_1$$

Where:
    
- $y'$ is the price, the variable we want to predict, called the **label**
- $x_1$ is the land area, our predictor variable, called a **feature**
- $b$ is the model **bias**
- $m_1$ is the **weight** for our feature $x_1$

To predict $y'$ (price) from $x_1$ (land area), we need the values of $b$ and $m_1$. We can calculate these values using machine learning, by **training** a linear regression model on a dataset of price and land area. The data we will train the model on is our **training data**. Because this data contains both the label and feature, it is also called **labelled data**. Linear regression is a form of **supervised** machine learning, because it uses labelled data as training data.

We can attain the values of $b$ and $m_1$ through **gradient descent**. This is an iterative process used to minimise **loss** - the difference between the label predicted by the model and the real label in the training data for each observation in the training data.

For a given $b$, $m_1$ and $x_1$, we calculate from the data:

$$b + m_1x_1 = predicted = y'$$

We can then compare this to the real value, $y$, in our training dataset, to calculate loss (using $L_2$ loss):

$$loss = (actual - predicted)^2 = (y - y')^2$$

We can then calculate the average loss across $N$ examples in the training dataset (using Mean Squared Error):

$$\frac{1}{N}\sum_{i=1}^{N}(y_i - y'_i)^2$$

The goal of training a machine learning model is to minimise average loss. For a linear regression model we do this through the process of gradient descent:

- The model begins with a randomised weight ($w_1$) and bias ($b$) close to zero, and then loss is calculated via the chosen loss function. This will in most cases result in high average loss, which is to say the model does not accurately predict the label with the given weight and bias.
- The model then determines the gradient of the tangent to the loss function at the weight and the bias, by taking the derivative of the loss function with respect to the weight and the bias.
- The model then modifies the weight and bias by incrementing them a small amount in the direction of the gradient of the tangent to the loss function. The process then repeats using this new weight and bias.

    ```{figure} ./_static/gradient_descent.png
    ---
    width: 100%
    name: gradient_descent
    alt: Gradient descent in supervised learning. Credit: Google
    ---
    Gradient descent in supervised learning. Credit: Google
    ```

This iterative process ends when further changes to the weight and bias produce very small reductions in loss. At this point, the model has **converged**, and we have a trained model with a weight and bias that produce the lowest possible loss for this model. The trained model can now be used to make predictions from new data.

This is how a linear regression machine learning model works! There are many different kinds of machine learning models, some are relatively simple (like linear regression), others are highly complex (such as deep learning models), but the idea of training a model by iteratively modifying weights and bias to minimise loss is a fundamental concept that applies to a wide range of different models.
```

In a generative AI model, these predictions are novel instances of text, images, video or audio (or any combination of these) that are produced when given some input data. This guide will focus on a particular subcategory of generative AI models called Large Language Models, or LLMs. LLMs typically take text as input and generate text as output (although most major LLMs today can take inputs and generate outputs in multiple formats, the typical use case is still text-to-text). The most well known LLMs include OpenAI's [GPT series](https://openai.com/index/introducing-gpt-5-4/), Google's [Gemini](https://deepmind.google/models/gemini/), Anthropic's [Claude](https://www.anthropic.com/claude/sonnet), and DeepSeek's [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek_(chatbot)).

How do LLMs generate novel instances of text that so closely resemble something that was written by a human? The simplest way of putting it is that LLMs are next-word-predictor machines. They continuously predict the next word in a sequence over and over again, until they have a 'finished' output, whether that is a business email, an academic essay, or an entire Python package. But how does a model know what word to add to the end of a sequence of words so that it 'looks right'? This is only possible because the model has learned a mathematical pattern for human text. The technology behind this is a neural network, a form of machine learning model architecture used to find non-linear patterns in data.

Neural networks get their name because they consist of a network of model 'neurons' - computational units that take many inputs to deliver one output. Neural networks are layered constructions. They first consist of an input layer, which takes the inputs to the model. The next set of layers in a neural network are the hidden layers, of which there can be one or more. 

Each hidden layer consists of one or more neurons. Each neuron of a hidden layer takes every input of the layer before it and computes a singular output. This is done by computing the linear product of the previous layer's outputs with a unique set of weights, plus a bias, and then feeding this into an activation function that transforms the linear output into a non-linear output. 

An example of a commonly used activation function used is a rectified linear unit, which is defined as $f(x) = max(0, x)$. The activation function is a crucial component in neural networks, as without them they cannot learn to predict non-linearity. The activation function also models how real neurons function - they only fire after the electrical stimulus from their inputs reaches a certain threshold.

```{figure} ./_static/neural_net_layers.png
---
width: 60%
name: neural_net_layers
alt: A diagram of neural network, showing two hidden layers consisting of four neurons each. The input layer takes two inputs, and the output layer produces four outputs. The outputs for the first hidden layer are calculated using the outputs of the input layer, weight vector $W_1$, bias vector $b_1$ and the activation function, the outputs of the second hidden layer are calculated using the outputs of the first hidden layer, weight vector $W_2$, bias vector $b_2$ and the activation function, and so on. Credit: Wolfram Research
---
A diagram of neural network, showing two hidden layers consisting of four neurons each. The input layer takes two inputs, and the output layer produces four outputs. The outputs for the first hidden layer are calculated using the outputs of the input layer, weight vector $W_1$, bias vector $b_1$ and the activation function, the outputs of the second hidden layer are calculated using the outputs of the first hidden layer, weight vector $W_2$, bias vector $b_2$ and the activation function, and so on. Credit: Wolfram Research
```

While the individual components of a neural network are performing essentially quite trivial mathematical operations, when networks are scaled up to include many hidden layers of many neurons (this is where the term deep learning comes from - deep neural networks, meaning neural networks of many layers), they can predict exceptionally complex non-linear patterns. An even more surprising feature is they can decide by themselves what these patterns are, they do not need instructions. For example, a neural network trained as an image classifier is able to learn on its own what constitutes an image of a car and what constitutes an image of a bicycle, just by being given examples of each - it does not need a definition of what is 'car-like' or 'bicycle-like' in advance.

Training a neural network to recognise a pattern or reproduce a non-linear function requires supplying it with enough examples that consist of an input and the desired output. From this point onwards, the neural network is trained to find the weights and biases that are needed to reproduce the desired outputs. This is done via gradient descent. Loss is calculated, the weights and biases are modified in the direction that reduces loss, and the process repeats until the model converges. 

[The drop down section above](#ml-primer) contains a primer on loss and gradient descent. In neural networks, gradient descent is implemented using an algorithm called [backpropagation](https://developers.google.com/machine-learning/glossary#backpropagation).

```{figure} ./_static/neural_net_training.png
---
width: 100%
name: neural_net_training
alt: A neural network learning to predict a non-linear function. Credit: Stephen Wolfram
---
A neural network learning to predict a non-linear function. Credit: Stephen Wolfram
```

LLMs are essentially just very large neural networks. The underlying neural network of an LLM is trained on a vast set of text, and the neural network is able to learn patterns of words and then assign probabilities to individual words occurring within sequences of other words, allowing the model to produce long sequences of text that quite accurately mimic human language. However, it's important to remember that a trained LLM is a black box. The trained model contains billions if not trillions of terms, so nobody can say for sure why it is capable of such accurate mimicry, we can only assess that it is.

The explanation for why LLMs are so ubiquitous now (given previous language models got far less attention) is a specific type of neural network architecture called a 'transformer', that was [invented in 2017 at Google](https://research.google/pubs/attention-is-all-you-need/) for the purpose of machine translation. This architecture represented a breakthrough in language models, as it opened up the models to 'hyperscaling' - increasing the size of the neural network and increasing the size of the training data led to predictable increases in performance, so both have increased exponentially ever since. Further discussion of the transformer architecture is beyond the scope of this guide, but the [Financial Times' Visual Storytelling Team have written an excellent introduction](https://ig.ft.com/generative-ai/).

An important point of note about LLMs is that from a user perspective the neural network training is only half the story. The neural network training produces the 'foundation' model (e.g., a GPT-5 series model), but a finished chatbot product (such as ChatGPT) has also gone through an enormous post-training (also known as 'fine-tuning') phase. It can be summarised as a kind of reinforcement learning that uses human feedback, but it is much harder to discuss, as different companies have developed different methods for what seems to work, and in many cases it is less about technology and more about [substantial human labour](https://time.com/6247678/openai-chatgpt-kenya-workers/). Even though we cannot offer a discussion about it in this guide, post-training is increasingly important in the field of LLMs.

Now that we have a rough handle on what LLMs are and how they work, we can discuss their use in the workplace.

## Vibe coding: Using LLMs to write code in the workplace

LLM-powered chatbots have become particularly popular as automated coding assistants. Many programmers around the world have opted (or been instructed) to use LLMs to generate code as a way to increase productivity, the logic behind this being that it is faster to write prompts to generate code than it is to hand write code. The slang term for this working practice is 'vibe coding'.

Before we go any further we need to cover **hallucinations**. LLMs can and regularly do generate **plausible but inaccurate** statements. The production of hallucinations is [**mathematically inevitable**](https://arxiv.org/pdf/2401.11817). This is not an example of the models 'failing', it is a feature - as we discussed earlier, all LLMs do is model patterns in text and replicate them. Outputs that 'look right' are all that the models are trained to produce. You must always keep in mind that LLMs do not have an internal world-model of what is true and false, only a very long list of parameters that are used to output next-word probabilities. It is from this that we get the first golden rule of vibe coding: 

```{admonition} The first golden rule of vibe coding
:class: important
**You must never use or submit to peer review any code generated by an LLM without first reviewing it yourself.**
```

We can then derive the second golden rule of vibe coding directly from the first rule:

```{admonition} The second golden rule of vibe coding
:class: important
**The only person responsible for the code you generated with an LLM is you.**
```

We need one more golden rule to round everything out. Our first two golden rules concern **outputs**, but we must also set a rule for **inputs**. An LLM-powered chatbot is also a website, so you should be taking the same general precautions you would with using any other website on the internet.

```{admonition} The third golden rule of vibe coding
:class: important
**Treat the input of an LLM chatbot as you would any other public online domain. Under no circumstances should you enter sensitive information or data in the input of an LLM chatbot.**
```

We can now discuss the benefits and risks of vibe coding, while bearing in mind that we must refer to our golden rules at all times.

### Don't kill my vibe - The benefits of vibe coding

The most touted advantage of vibe coding is a significant increase in productivity.  From prompts of only a few words, an LLM can generate expressions, functions, classes, even entire modules for you to add to your project. Integrating an LLM-powered chatbot into an IDE (such as pairing VS Code with GitHub CoPilot) allows the LLM to directly modify code files, removing the need to even copy and paste outputs. Vibe coding can free you and your team from time consuming menial tasks to focus on delivering functionality, and it can empower individuals to tackle more ambitious tasks than they would otherwise be comfortable with.

One study across two companies (Microsoft and Accenture) found [experimental evidence](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566) supporting the assertion that AI-assisted programmers write code faster than non-AI-assisted programmers. In this study there was a statistically significant increase in the number of pull requests and builds submitted by AI-assisted programmers when compared to non-AI-assisted programmers. However, there was no overall statistically significant difference in the number of *successful* builds between the two groups.

### Vibe check failed - The risks of vibe coding

Although vibe coding lets you write code faster, in practice you will inevitably be forced to spend a substantial amount of re-prompting, reviewing, and editing the outputs of LLMs to achieve the desired final result. An AI-powered programmer may find themselves quickly turning into a full time code reviewer for their LLM assistant, with the total time spent on a task staying the same or even increasing, despite code being written faster. 

Researchers at [METR](https://metr.org/) tested the productivity of experienced programmers and found the surprising result that AI-assisted programmers actually took [longer](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) to complete tasks than non-AI-assisted programmers, but the AI-assisted programmers believed that they had been more efficient! The authors of the study proposed 5 potential explanations for the result:

- There is a degree of complacency caused by overoptimism about the usefulness of AI tools
- AI tools lack domain-specific knowledge.
- AI tools perform worse in large and complex codebases.
- There is a high level of rejection of AI-generated outputs, and a significant amount of time is spent reviewing and editing AI-generated outputs.
- AI tools lack a lot of the implicit context that exists in projects.

There is also the pertinent question of how individuals and organisations build and retain skill in workplaces inundated with vibe coding. A [study by Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills) suggests that LLM adoption, especially if it is done quickly and aggressively, can have a negative impact on individuals' ability to learn on the job. This has potentially quite serious implications at the organisational level regarding internal career progression and technical debt within teams. [Negative impacts on psychological wellbeing](https://www.nature.com/articles/s41598-025-98385-2) have also been measured after the adoption of LLMs in the workplace, with increased boredom and decreased motivation associated with using LLMs.

There is also a risk that LLM-generated code can contain [critical security vulnerabilities](https://www.databricks.com/blog/passing-security-vibe-check-dangers-vibe-coding). This is of particular importance to anybody working on web-based platforms and applications.

Finally, we should also quickly mention the environmental and ethical concerns related to LLM-powered chatbots. These chatbots are not efficient machines. They consume vast quantities of electricity and fresh water (especially in the model training process), and the demand for both is only increasing. There are also ethical concerns around using LLMs, such as how LLMs use copyrighted works in their training data, the bias exhibited by LLMs as a result of them reproducing biases present in their training data, and the use of LLMs to produce offensive and harmful content.

### Conclusion - Centaurs and reverse-centaurs

Author and journalist Cory Doctorow uses the idea of [centaurs and reverse-centaurs](https://www.theguardian.com/us-news/ng-interactive/2026/jan/18/tech-ai-bubble-burst-reverse-centaur) when discussing AI-assisted work. A centaur is a human that is assisted in their work by a machine. It's nice to be a centaur, as the machine takes some of the drudgery out of work by doing the menial time-consuming tasks at a fraction of the effort, allowing you to be more productive and creative. 

A reverse-centaur is a human that assists a machine in their work. It's much less nice to be a reverse-centaur, as you are stripped of agency in your work - the machine dictates what you do and when you do it. When we use AI tools at work, we want to be centaurs and we don't want to be reverse-centaurs.

Let's look at the following example. Say you're working on a data pipeline, and you need a function that flags outliers in your data. You could use CoPilot as an LLM-powered chatbot assistant, and give it the following prompt:

```{figure} ./_static/reverse-centaur-prompting.png
---
width: 70%
name: reverse-centaur-prompting
alt: A prompt offloading most of the thinking to CoPilot.
---
A prompt offloading most of the thinking to CoPilot.
```

I then get the following Python code from CoPilot:

```{admonition} Click here to view the CoPilot output
:class: dropdown

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional, Tuple, Union

import numpy as np
import pandas as pd


Method = Literal["iqr", "zscore", "mad"]


@dataclass(frozen=True)
class OutlierConfig:
    """
    Configuration for outlier detection.

    Attributes
    ----------
    method : Literal["iqr", "zscore", "mad"]
        The statistical method used for outlier detection.
    iqr_mult : float
        Multiplier for IQR fences (used when method="iqr"). Default is 1.5 (Tukey).
        Use 3.0 for extreme outliers.
    z_thresh : float
        Absolute Z-score threshold (used when method="zscore"). Common values: 3.0, 3.5.
    mad_thresh : float
        Threshold for modified Z-score using MAD (used when method="mad"). Common default: 3.5.
    """
    method: Method = "iqr"
    iqr_mult: float = 1.5
    z_thresh: float = 3.0
    mad_thresh: float = 3.5


def _validate_array_like(x: Union[pd.Series, np.ndarray, list]) -> np.ndarray:
    """
    Validate and convert input to a 1D float NumPy array. NaNs are preserved.
    """
    if isinstance(x, pd.Series):
        arr = x.to_numpy(dtype=float)
    else:
        arr = np.asarray(x, dtype=float)

    if arr.ndim != 1:
        raise ValueError("Input must be a 1D array-like (pandas Series, 1D numpy array, or list).")
    return arr


def _iqr_outliers(arr: np.ndarray, iqr_mult: float) -> Tuple[np.ndarray, dict]:
    """
    IQR-based outlier mask and diagnostics.
    """
    q1 = np.nanpercentile(arr, 25)
    q3 = np.nanpercentile(arr, 75)
    iqr = q3 - q1
    # Handle zero-IQR edge case gracefully
    if not np.isfinite(iqr) or iqr == 0:
        mask = np.zeros_like(arr, dtype=bool)
        return mask, {
            "q1": q1, "q3": q3, "iqr": iqr,
            "lower_fence": np.nan, "upper_fence": np.nan,
            "note": "IQR is zero or non-finite; no outliers flagged."
        }

    lower = q1 - iqr_mult * iqr
    upper = q3 + iqr_mult * iqr
    mask = (arr < lower) | (arr > upper)
    # NaNs are not flagged by default (only finite comparisons above are True/False); keep them False
    mask = np.where(np.isnan(arr), False, mask)

    return mask, {"q1": q1, "q3": q3, "iqr": iqr, "lower_fence": lower, "upper_fence": upper}


def _zscore_outliers(arr: np.ndarray, z_thresh: float) -> Tuple[np.ndarray, dict]:
    """
    Z-score outlier mask and diagnostics (uses mean and std, ignoring NaNs).
    """
    mean = np.nanmean(arr)
    std = np.nanstd(arr, ddof=0)  # population std; change to ddof=1 for sample std if desired

    if not np.isfinite(std) or std == 0:
        mask = np.zeros_like(arr, dtype=bool)
        return mask, {
            "mean": mean, "std": std,
            "note": "Standard deviation is zero or non-finite; no outliers flagged."
        }

    z = (arr - mean) / std
    mask = np.abs(z) > z_thresh
    mask = np.where(np.isnan(arr), False, mask)

    return mask, {"mean": mean, "std": std, "z_scores": z}


def _mad_outliers(arr: np.ndarray, mad_thresh: float) -> Tuple[np.ndarray, dict]:
    """
    MAD-based outlier mask and diagnostics using the 'modified Z-score' approach.
    Formula: modified_z = 0.6745 * (x - median) / MAD
    Where MAD = median(|x - median|)
    """
    med = np.nanmedian(arr)
    abs_dev = np.abs(arr - med)
    mad = np.nanmedian(abs_dev)

    if not np.isfinite(mad) or mad == 0:
        mask = np.zeros_like(arr, dtype=bool)
        return mask, {
            "median": med, "mad": mad,
            "note": "MAD is zero or non-finite; no outliers flagged."
        }

    # 0.6745 approximates the scaling to make MAD consistent with std for normal data
    modified_z = 0.6745 * (arr - med) / mad
    mask = np.abs(modified_z) > mad_thresh
    mask = np.where(np.isnan(arr), False, mask)

    return mask, {"median": med, "mad": mad, "modified_z": modified_z}


def flag_outliers(
    x: Union[pd.Series, np.ndarray, list],
    *,
    method: Method = "iqr",
    iqr_mult: float = 1.5,
    z_thresh: float = 3.0,
    mad_thresh: float = 3.5,
    return_details: bool = False,
    return_frame: bool = False,
    column_name: Optional[str] = None,
) -> Union[np.ndarray, Tuple[np.ndarray, dict], pd.DataFrame]:
    """
    Flag outliers in a 1D numeric array/Series using IQR, Z-score, or MAD.

    Parameters
    ----------
    x : Union[pd.Series, np.ndarray, list]
        Input data (1D). NaNs are allowed and ignored for statistics.
    method : {"iqr", "zscore", "mad"}, default "iqr"
        Outlier detection method.
    iqr_mult : float, default 1.5
        IQR multiplier for Tukey fences (method="iqr").
    z_thresh : float, default 3.0
        Absolute Z-score threshold (method="zscore").
    mad_thresh : float, default 3.5
        Modified Z-score threshold (method="mad").
    return_details : bool, default False
        If True, returns (mask, details_dict) with diagnostics.
    return_frame : bool, default False
        If True, returns a DataFrame with columns: ["value", "is_outlier", "score", ...]
        Note: `return_frame` takes precedence over `return_details`.
    column_name : Optional[str], default None
        Column name to use for the "value" column in the returned DataFrame.

    Returns
    -------
    Union[np.ndarray, Tuple[np.ndarray, dict], pd.DataFrame]
        - If return_frame is False and return_details is False:
            returns boolean mask (np.ndarray).
        - If return_frame is False and return_details is True:
            returns (mask, details_dict).
        - If return_frame is True:
            returns a pandas DataFrame with the original values, outlier flags,
            and a method-specific score (z-score, modified_z, or distance from fence).

    Notes
    -----
    - IQR fences: [Q1 - iqr_mult * IQR, Q3 + iqr_mult * IQR].
    - Z-score uses mean and std that ignore NaNs.
    - MAD uses the modified Z-score scaled by 0.6745.
    - NaN values are never flagged as outliers; they have `is_outlier=False` and score NaN.
    """
    arr = _validate_array_like(x)
    method = method.lower()
    if method not in ("iqr", "zscore", "mad"):
        raise ValueError("method must be one of: 'iqr', 'zscore', 'mad'.")

    if method == "iqr":
        mask, details = _iqr_outliers(arr, iqr_mult=iqr_mult)
        # Score: distance beyond nearest fence; NaNs for in-range
        q1, q3, iqr = details.get("q1"), details.get("q3"), details.get("iqr")
        lower, upper = details.get("lower_fence"), details.get("upper_fence")
        # Compute a signed distance to the nearest fence; positive outside, negative inside
        score = np.full_like(arr, np.nan, dtype=float)
        with np.errstate(invalid="ignore"):
            below = arr < lower
            above = arr > upper
            score[below] = lower - arr[below]
            score[above] = arr[above] - upper

    elif method == "zscore":
        mask, details = _zscore_outliers(arr, z_thresh=z_thresh)
        z = details.get("z_scores")
        score = np.where(np.isnan(arr), np.nan, z)

    else:  # method == "mad"
        mask, details = _mad_outliers(arr, mad_thresh=mad_thresh)
        mz = details.get("modified_z")
        score = np.where(np.isnan(arr), np.nan, mz)

    if return_frame:
        name = column_name or (x.name if isinstance(x, pd.Series) and x.name is not None else "value")
        df = pd.DataFrame({name: arr, "is_outlier": mask, "score": score})
        # Attach diagnostics as attributes for downstream inspection
        df.attrs["outlier_details"] = {
            "method": method,
            "iqr_mult": iqr_mult,
            "z_thresh": z_thresh,
            "mad_thresh": mad_thresh,
            **details,
        }
        return df

    if return_details:
        # Attach method and thresholds for clarity
        details = {
            "method": method,
            "iqr_mult": iqr_mult,
            "z_thresh": z_thresh,
            "mad_thresh": mad_thresh,
            **details,
        }
        return mask, details

    return mask
```

You asked for one function, but because the prompt was vague, and also asked for 'quality standards' to be adhered to (rather than verifying that by yourself!), CoPilot has given a verbose, defensively-coded response. The output has in total:

- 1 class (that contains only attributes)
- 5 functions
- 225 new lines
- An import of `__future__` that suggests there could be compatibility issues in the code

You have to review all of this before you can add some simple outlier flagging into the data pipeline - practically the size of an entire pull request. By being too vague in prompting and offloading too much of the cognitive work to CoPilot, you may find yourself turning into a reverse-centaur - CoPilot gets to design and write all the code, while you must test and review it. Can we change this prompt so that we are being centaurs, not reverse-centaurs?

Try the following updated prompt:

```{figure} ./_static/centaur-prompting.png
---
width: 70%
name: centaur-prompting
alt: An updated prompt where I am more precise with my requirements.
---
An updated prompt where I am more precise with my requirements.
```

And CoPilot produces the following output:

```{admonition} Click here to view the CoPilot output
:class: dropdown

```python
import pandas as pd
import numpy as np

def flag_upper_outliers(df: pd.DataFrame, cols=None, threshold: float = 3.0, ddof: int = 0):
    """
    Flag values that are more than `threshold` standard deviations ABOVE the mean
    for each specified numeric column.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    cols : list or None, optional
        List of columns to check. If None, all numeric columns are used.
    threshold : float, optional
        Number of standard deviations above the mean to define an outlier (default: 3.0).
    ddof : int, optional
        Delta degrees of freedom for std calculation (default: 0, i.e., population std).
        Use ddof=1 for sample std.

    Returns
    -------
    pd.DataFrame
        Boolean DataFrame with True marking values > mean + threshold * std in each column.
        Only includes the columns evaluated.
    """
    # Choose numeric columns by default
    if cols is None:
        cols = df.select_dtypes(include=[np.number]).columns.tolist()
    else:
        # Keep only those that exist and are numeric
        cols = [c for c in cols if c in df.columns and pd.api.types.is_numeric_dtype(df[c])]

    if not cols:
        return pd.DataFrame(index=df.index)  # nothing to do

    # Compute mean and std per column
    means = df[cols].mean(axis=0, skipna=True)
    stds  = df[cols].std(axis=0, ddof=ddof, skipna=True)

    # Thresholds per column
    cutoffs = means + threshold * stds

    # Broadcast comparison; NaNs remain False by default after fillna(False)
    outlier_mask = df[cols].gt(cutoffs)  # elementwise >
    return outlier_mask.fillna(False)
```

You now have only 1 function and 46 new lines to review (we are also only importing numpy and pandas). By thinking about what you actually needed in the data pipeline (i.e., specifying that you're working with numerical data and pandas DataFrames, and deciding on the thresholding) rather than offloading the cognitive work to CoPilot, CoPilot has output a much more compact piece of code that will be easier to review and add into the data pipeline. In this example, you're much more like a centaur - You get to design the code, while CoPilot is doing the menial work of typing it up.

This outlines a general principle - LLM-powered chatbots are most useful when you direct them to work for you, rather than when you are picking up after them and trying to shape their outputs into something functional. Remember that they have no world-model of what is right and wrong, they don't have any innate understanding of the requirements for your work, and they can't be held responsible for shoddy work.

## Acknowledgements

Stephen Wolfram's article [What Is ChatGPT Doing ... and Why Does It Work](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) is an excellent primer on the underlying mechanics of LLMs and informed much of the first section in this guide. In addition, the [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/) was enormously helpful and is another starting point for anyone interested in machine learning and AI. The sections on [neural networks](https://developers.google.com/machine-learning/crash-course/neural-networks), [embeddings](https://developers.google.com/machine-learning/crash-course/embeddings), and [LLMs](https://developers.google.com/machine-learning/crash-course/llm) are particularly relevant.
