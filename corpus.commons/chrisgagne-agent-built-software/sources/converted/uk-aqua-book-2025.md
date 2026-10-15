<div class="govspeak">

## Acknowledgements

The AQuA Book is the work of many authors from across the Government Analysis Function. The original version of the book was compiled by the Quality Assurance Working Group set up after [Sir Nicholas Macpherson’s review of modelling in government](https://www.gov.uk/government/publications/review-of-quality-assurance-of-government-models).

This revised edition of the book was produced by a task and finish group drawn from across the Government Analysis Function. We would like to thank everybody who has given of their time and expertise to produce the revised edition and give a special mention to the task and finish group who gave their time and expertise to the book:

- Faye Clancy
- Will England
- Andrew Friedman
- Nick Harris
- Jordan Low
- James McGlade
- Ian Mitchell
- Iris Oren
- Adam Powell
- Martin Ralphs
- Philippa Robinson
- Sarjeet Soni
- Lorna Wilson
- Rebecca Wodcke

Alec Waterhouse 10th June 2025

[Back to contents](https://www.gov.uk/guidance/the-aqua-book#contents)

Skip to chapter [1](#intro), [2](#definitions), [3](#proportionality), [4](#qac), [5](#roles), [6](#engagement), [7](#designseven), [8](#analysiseight), [9](#delivery), [10](#resources)

------------------------------------------------------------------------

## 1  Introduction

The Analytical Quality Assurance (AQuA) Book provides guidance on producing good quality analysis for government to support well informed decision-making that creates better outcomes and improve the lives of citizens.

The AQuA Book has made a significant contribution to the cultural change in assurance practices in government by clearly setting out the core framework for assuring all forms of analytical evidence.

### 1.1 The updated version (2025)

The last version of the AQuA Book was published in 2015, following Sir Nicholas Macpherson’s [Review of quality assurance of government models](https://www.gov.uk/government/publications/review-of-quality-assurance-of-government-models). Since then assurance has become part of the fabric of good practice for developing evidence to support policy development, implementation and operational excellence.

The world of analysis has developed since we published the first edition of the AQuA Book. Increasingly, in our data driven world, the insights provided by analysis underpin almost all policies and help to support operational excellence. At the same time, our working practices have developed. For example, the dominant analytical tools when we wrote the last edition were spreadsheets and proprietary software. We have now broadened the range of methods we use to include open-source software, machine learning and Artificial Intelligence (AI).

Based on feedback from our users, for this new edition we have added guidance on:

- multi-use models - large models used for many purposes with many stakeholders
- assuring <a href="https://en.wikipedia.org/wiki/Black_box" rel="external">black box</a> systems (defined by their inputs and outputs, without insight into internal workings), analysis, including AI
- development, maintenance and continuous review
- working with third parties such as contractors and academic groups
- publishing models

We provide improved guidance on what [a proportionate approach to assurance means](#proportionality) and have made the whole guide relevant to all types of analysis.

The AQuA Book is a vital supporting guide for the [Analysis Function Standard](https://www.gov.uk/government/publications/government-analysis-functional-standard--2). This Standard refers extensively to the AQuA Book and notes that the “detailed guidance on the analytical cycle and management of analysis included in the Aqua Book should be followed.”

It is also referred to by the [Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2020), the [Magenta Book](https://www.gov.uk/government/publications/the-magenta-book) and other Functional Standards, such as the [Finance Function](https://www.gov.uk/government/publications/government-finance-standards-page) Standards, <a href="https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html" rel="external">Duck Book for Code Quality Assurance</a>, The National Audit Office - <a href="https://www.nao.org.uk/insights/quality-assurance-of-models/" rel="external">Quality assurance of models: a guide for audit committees</a>.

### 1.2 Who the AQuA Book is for

This edition has been developed for Government Analysis and is intended for anyone who commissions, uses, conducts, or assures analysis. While it is designed with government needs in mind, the guidance is broadly applicable. It covers the full process of producing analysis that is robust, reliable, and fit for purpose. We would like to see producers and users of analysis from all backgrounds using this book, especially those producing analysis, evidence and research to support decision-making in government. The book can help users of analysis make the most of work that has been commissioned and senior leaders with an interest in analytical assurance. The AQuA Book is for anyone carrying out analysis, including:

- actuaries
- data scientists
- economists
- finance professionals
- geographers
- operational researchers
- science and engineering professionals
- social researchers
- statisticians

### 1.3 How to use this book

The AQuA Book has been developed to help the analysis community:

- publish analytical insights that will be used for major decisions and operations
- minimise the risk of errors arising that cause operational, business or reputational damage
- create greater trust in analysts’ work
- ensure appropriate quality assurance is in place to help to manage mistakes, handle changes to requirements and ensure appropriate re-use of analysis
- develop the confidence in analysis that is needed for transparency and public openness
- support the [analytical assurance](#rigour) that is required for audit purposes (see [Managing public money](https://www.gov.uk/government/publications/managing-public-money) Annex 4.2 Use of models)

The first four chapters of this book cover definitions and themes, while the second half of the book goes into more detail on the [analytical life cycle](#roles). This can be pictured as follows:

<figure class="image embedded">
<div class="img">
<img src="https://assets.publishing.service.gov.uk/media/6853d80ba3a28280485814d2/analytical_lifecycle_diagram.svg" />
</div>
</figure>

<div class="call-to-action">

The image shows a flowchart of the analytical life cycle, which includes four main stages:

1.  Engagement and Scoping ([Chapter 6](#engagement))
2.  Design ([Chapter 7](#designseven))
3.  Analysis ([Chapter 8](#analysiseight))
4.  Delivery and Communication ([Chapter 9](#delivery))

The image emphasises that:

- The process is often iterative, meaning stages may repeat or happen out of order
- Proportionality ([Chapter 3](#proportionality)) should be considered at every stage

</div>

Each chapter in the second half of the book is structured as follows:

- an overview of the stage and chapter
- roles and responsibilities
- assurance activities
- documentation
- uncertainty
- black box models
- multi-use models
- any other guidance specific to the stage of the life cycle

The AQuA Book uses the following terms to indicate whether recommendations are mandatory or advisory:

- ‘shall’ denotes a requirement, a mandatory element, which applies in all circumstances and at all times
- ‘should’ denotes a recommendation, an advisory element, to be met on a ‘comply or explain’ basis
- ‘may’ denotes approval i.e. it’s a good idea but not mandatory or advisory
- ‘might’ denotes a possibility
- ‘can’ denotes both capability and possibility
- is/are is used for a description

This is consistent with the [UK Government Functional Standards](https://www.gov.uk/government/publications/guide-to-functional-standards/guide-to-functional-standards#interpreting-a-functional-standard).

### Principles of analytical quality assurance

No single piece of guidance provides a definitive assessment of whether a piece of analysis is of sufficient quality for an intended purpose. There are some important principles that support that commissioning and production of fit-for-purpose analysis.

#### 1.3.1 Proportionate assurance

Quality assurance effort should be appropriate to the risk associated with the intended use of the analysis and the complexity of the analytical approach. These risks include financial, legal, operational and reputational effects.

You can read more about proportionality in chapter [3.](#proportionality)

#### 1.3.2 Assurance throughout development

Quality assurance should be considered throughout the whole life cycle of the analysis. Effective communication is crucial when understanding the problem, designing the analytical approach, conducting the analysis and relaying the outputs.

You can read more on the analysis life cycle in chapter [5.](#roles)

#### 1.3.3 Verification and validation

Analytical quality assurance is more than checking that the analysis is error-free and satisfies its specification (verification). It should also include checks that the analysis is appropriate and fit for the purpose for which it is being used (validation).

You can read more on verification and validation in chapters [5-9.](#roles)

#### 1.3.4 Uncertainty

It is important to accept that uncertainty is inherent in the inputs and outputs of any piece of analysis. [Chapters 5 to 9](#roles) cover the treatment of uncertainty in each analytical phase. You can read more about uncertainty in the <a href="https://analystsuncertaintytoolkit.github.io/UncertaintyWeb/index.html" rel="external">Uncertainty Toolkit for Analysts in Government</a>.

#### 1.3.5 Analysis with RIGOUR

An acronym some users find helpful to consider when completing analysis is RIGOUR. Throughout all the stages of an analytical project, the analyst should ask questions of their own analysis. The mnemonic “RIGOUR” may assist:

- Repeatable
- Independent
- Grounded in reality
- Objective
- Uncertainty-managed
- Robust

Repeatable: For an analytical process to be considered valid we might reasonably expect that the analysis produces the same outputs for the same inputs and constraints. Different analysts might approach the analytical problem in different ways, while methods might include randomised processes. In such cases, exact matches are not guaranteed or expected. Taking this into account, repeatability means that if an approach is repeated the results should be as expected.

Independent: Analysis should be (as far as possible) free of prejudice or bias. Care should be taken to balance views appropriately across all stakeholders and experts.

Grounded in reality: Quality analysis takes the Commissioner and Analyst on a journey as views and perceptions are challenged and connections are made between the analysis and its real consequences. Connecting with reality like this guards against failing to properly grasp the context of the problem that is being analysed.

Objective: Effective engagement and suitable challenge reduce the risk of bias and enables the Commissioner and the Analyst to be clear about the interpretation of results.

Uncertainty-managed: Uncertainty is identified, managed and communicated throughout the analytical process.

Robust: Analytical results are error free in the context of residual uncertainty and accepted limitations that make sure the analysis is used appropriately.

[Back to contents](https://www.gov.uk/guidance/the-aqua-book#contents)

Skip to chapter [1](#intro), [2](#definitions), [3](#proportionality), [4](#qac), [5](#roles), [6](#engagement), [7](#designseven), [8](#analysiseight), [9](#delivery), [10](#resources)

------------------------------------------------------------------------

## 2  Definitions and concepts

This chapter sets out definitions and concepts that are used throughout the rest of the book.

### Analysis

Analysis is the collection, manipulation and interpretation of information and data for use in decision-making. Analysis can vary widely between situations and many different types of analysis may be used to form the evidence base that supports the decision-making process.\
Examples of types of analysis that are frequently encountered in government are:

- actuarial
- data science
- economic
- financial
- geographical
- operational research
- scientific, technical and engineering research
- statistical
- social research

### Assurance

Analytical assurance is the process and set of practices that ensure analysis is fit for purpose.

### Assurance activities

Assurance activities are any actions carried out in order to validate and verify analysis.

This may include:

- analyst testing
- peer review
- reconciliation of results to independent sources

### Artificial Intelligence

Artificial Intelligence (AI) attempts to simulate human intelligence using techniques and methods such as [machine learning](#machine-learning), natural language processing, robotics, and generative AI. AI aims to perform tasks that typically require human intelligence, such as problem-solving, -making, and language understanding. AI models are usually considered [black box models](#bbm). They can be pre-trained models or custom built.

### Black box models

Black box models’ internal workings are not visible, easily understood, or succinctly explained. These models take input and produce output without providing clarity about the process used to arrive at the output. This also includes proprietary models with protected intellectual property. [Artificial Intelligence](#artificial) models (including [Machine Learning](#machine-learning)) can often be considered a type of black box model. Other types of black box model may arise in future.

### Business critical analysis

Business critical analysis refers to analysis that:

- has a significant influence over finance and funding or departmental operation(s)

- is necessary to the achievement of a departmental business plan or

- is analysis where an error could have a significant reputational, economic or legal implications.

### Business critical models

Business critical models are models to support or provide [Business critical analysis](#bca).

### Documentation

#### Specification documentation

Specification documentation records the initial engagements with the commissioner. It describes the question, the context and any boundaries of the analysis. The specifications provide a definition of the scope of the project and a mechanism for agreeing project constraints (for example, deadlines and available resources) and define what level of assurance is required by the commissioner.

#### Design documentation

Design documents describe the analytical plan, including the methodology, inputs and software that will be used. They also contain details of the planned [verification](#verification) and [validation](#validation) of the analysis. They provide a basis for the analytical assurer to verify whether the analysis meets the specified requirements.

You can read more about design documentation in the [Design](#designseven) chapter.

#### Assumptions log

The assumptions log is a register of assumptions, whether provided by the commissioner or gathered from the analysis, that have been risk assessed and signed off by an appropriate governance group or stakeholder. Assumption logs should:

- describe each assumption
- quantify its effect and reliability
- set out when it was made
- explain why it was made
- explain who made the assumption and who signed it off

#### Decisions log

The decisions log is a register of decisions, whether provided by the commissioner or derived from the analysis. Decisions logs should:

- describe each decision
- set out when it was made
- explain why it was made
- explain who made the decision and who signed it off

#### Data log

A register of data provided by the commissioner or derived from the analysis that has been risk assessed and signed-off by an appropriate governance group or stakeholder.

#### User and technical documentation

All analysis shall have user documentation, even if the only user is the analyst leading the analysis. This documentation should include:

- a summary of the analysis including the context to the question being asked
- what analytical methods were considered
- what analysis was planned and why
- what challenges were encountered and how they were overcome
- what verification and validation steps were performed
- whether the analysis, including its data and assumptions, has a defined lifespan or depends on specific conditions to remain valid.

Where relevant, the analyst may include a model map that describes data flows and transformations.

For analysis that is likely to be revisited or updated in the future, more comprehensive documentation should be provided to assist a future analyst. It may also be helpful to include guidance on what should be considered or updated.

#### Assurance statement

A brief description of the analytical assurance that have been performed to assure the analysis. The statement should refer to known limitations and conditions associated with the analysis.

Example of publishing quality assurance tools

The Department for Energy Security and Net Zero (DESNZ) and Department for Business and Trade (DBT) have published a range of quality assurance tools and guidance to help people with the quality assurance of analytical models. [Modelling Quality Assurance tools and guidance](https://www.gov.uk/government/publications/energy-security-and-net-zero-modelling-quality-assurance-qa-tools-and-guidance) are used across the departments to ensure analysis meets the standards set out in the AQuA Book and provide assurance to users of the analysis that proportionate quality assurance has been completed.

### Machine Learning

Machine Learning uses algorithms to learn from patterns in data without needing to programme explicit business rules. Some models are white box models and others are considered [black box models](#bbm). Machine Learning is a subset of [Artificial Intelligence](#artificial).

### Model

A model is a tool used to study, or understand, a part of the real world. Often, they use quantative methods and theories drawn from statistics, economics, or mathematics together with assumptions, to turn input data into numerical estimates. Models can be:

- descriptive - what is?
- predictive - what might be?
- prescriptive - what should be done if?

### Maturity Model

The Quality Assurance [Maturity Model](https://www.gov.uk/government/publications/analytical-quality-assurance-at-the-department-for-education) is a structured framework used to assess an organisation’s capability in applying quality assurance to analysis. It helps identify the level of maturity in quality assurance practices, from basic awareness to fully embedded, systematic approaches.

### Multi-use models

Multi-use models are used by more than one user or group of users for related but different purposes. These are often complex and large.

A Steering Group may be created to oversee the analysis of these kind of models. This Steering Group should be chaired by the senior officer in charge of the group developing the model and include senior representatives from each major user group. The members of the Steering Group may have decision-making responsibilities in their area of work.

### Quality analysis

Quality analysis is fit for the purpose it was commissioned to meet. It should be:

- accurate
- appropriately assured
- evidenced
- proportionate to its effect
- adequately communicated
- documented
- accepted by its commissioners

### Roles and responsibilities

The AQuA Book defines the following roles:

- commissioner
- analyst
- assurer
- approver

You can read more in the [Roles and Responsibilities](#roles) section.

### Symbolic proxies

A symbolic proxy is a representation of data or variables using symbols instead of concrete values. It allows you to reason about the program’s behaviour without needing to know the exact data values. These proxies are used to represent inputs, outputs, or states symbolically, which makes it possible to analyse how different parts of the program interact or how inputs lead to outputs, even when you don’t have specific data.

### Third party

Any individual or group of individuals that are not commissioners or the analysts. For example, they may be working for a different government department, a different function or an outside company, person or group besides the two primarily involved in a situation, especially a dispute.

### Uncertainty

Uncertainties are things that are not known, are in a state of doubt or are things whose effect is difficult to know. They have the potential to have major consequences for a project, programme or piece of analysis meeting its objectives. The National Audit Office have published a <a href="https://www.nao.org.uk/wp-content/uploads/2023/08/Good-practice-guide-Managing-uncertainty.pdf" rel="external">good practice guide on managing uncertainty</a>.

There are different types of uncertainty. A common classification divides uncertainty into known knowns, known unknowns and unknown unknowns. The type of uncertainty will influence the analytical approach and assurance activities required.

The <a href="https://analystsuncertaintytoolkit.github.io/UncertaintyWeb/index.html" rel="external">Uncertainty Toolkit for Analysts in Government</a> is a tool produced by a cross-government group to help assessing and communicating uncertainty.

### Validation 

Validation ensures the analysis meets the needs of its intended users and the intended use environment.

You can read more in [Verification and validation for the AQuA Book](https://www.gov.uk/government/publications/verification-and-validation-for-the-aqua-book) by Paul Glover.

### Verification

Verification ensures the analysis meets it specified design requirements.

You can read more in [Verification and Validation for the AQuA Book](https://www.gov.uk/government/publications/verification-and-validation-for-the-aqua-book) by Paul Glover.

### Version control

It is important to ensure that the latest version of the analysis is being used and any changes made can be easily seen and quality assured by the analytical assurer. There are tools and templates that can be used to record any updates and checks made during a project. They can help to provide a log of the changes that have been made including why and when they were made, and who made them.

[Back to contents](https://www.gov.uk/guidance/the-aqua-book#contents)

Skip to chapter [1](#intro), [2](#definitions), [3](#proportionality), [4](#qac), [5](#roles), [6](#engagement), [7](#designseven), [8](#analysiseight), [9](#delivery), [10](#resources)

------------------------------------------------------------------------

## 3  Proportionality

All analysis shall be assured.

The assurer and the analyst shall be independent. The degree of separation depends on many factors including the importance of the output, and the size and complexity of the analysis. This does not mean that the analyst should not undertake assurance, rather that there shall also be some formal independent assurance.

The assurance should be proportionate to the potential effect it will have and the size and complexity of the analysis. The level of assurance should be guided by a structured assessment of the business risks.

### 3.1 Factors for determining appropriate assurance

While there is a need to be confident in the analysis, it is not necessary to spend months assuring simple analysis that will have a minor influence on a decision. The level of assurance should be appropriate (proportionate) to the analysis.

Table 3-1 provides a list of factors that should be considered when determining what level of assurance is appropriate.

<div class="call-to-action">

Table 3-1 Factors for determining appropriate assurance

| Factor | Comments |
|----|----|
| Business criticality | Different issues will affect how business critical the analysis is. For example, its financial, legal, operational, political and reputational effects. |
| Relevance of the analysis to the decision-making process | When analysis forms only one component of a broad evidence base, less assurance is required for that specific analysis than if the decision is heavily dependent on the analysis alone. Significant assurance is still likely to be required for the whole evidence base. |
| Type and complexity of analysis | Highly complex analysis requires more effort to assure. The nature of that analysis may also require the engagement of appropriate subject matter experts. |
| Novelty of approach | A previously untried method requires more assurance. Confidence will grow as the technique is repeatedly tested. |
| Reusing or repurposing existing work | Reusing work may require validation and verification to confirm that original approach. For example, confirming the original method and assumptions data are still appropriate for the new requirement. |
| Level of precision required in outputs | Lower precision analysis often uses simplified assumptions, models and data. The assurance approach is the same but will take less time than more precise analysis. |
| Amount of resource available for the analysis and assurance | The value for money of any additional assurance must be balanced alongside the benefits and risk appetite that exists. Analysis that is used for many purposes (for example, population projections) may require greater levels of quality assurance than might be suggested by any of the individual decisions they support. |
| Longevity of the analysis | Ongoing analysis will require robust change control and regular review. |
| Effects on the public | Analysis which will have a significant effect on the public may require more assurance. |
| Repeat runs for the same analysis | Assurance should concentrate on version control and the assurance of data and parameters for each run. |

</div>

You can read more on the Data Quality Hub’s <a href="https://dataqualityhub.github.io/resources-for-quality-analysis-external/" rel="external">Quality Questions and Red Flags</a>.

Figure 3-1 - Assurance techniques considered for different levels of analysis complexity and business risk

<figure class="image embedded">
<div class="img">
<img src="https://assets.publishing.service.gov.uk/media/68823d71f47abf78ca1d3634/Figure_3-1_Business_Risk_and_or_Analytical_Complexity_.svg" />
</div>
</figure>

<div class="call-to-action">

Figure 3-1 shows some assurance techniques that might be considered for different levels of analysis complexity and business risk. These include:

- consultation on methods (internal to expert)
- use of RAP tools (minimal viable to full project)
- analyst-assurer separation (analyst-lead testing to external audit)
- and documentation detail (in-line to full project).

The need for more assurance interventions increases with the complexity of the analysis and the business risk associated with it.

</div>

The interventions in figure 3-1 must not be viewed in isolation. The interventions should build on each other. For example, some complex and risky analysis that would benefit from an external review should also be using the methods relevant to “Low” business risk and/or analytical complexity, such as analyst led testing and internal consultation.

The total elimination of risk will never be achieved, so a balance needs to be found that reduces the overall business risk to an acceptable level. The diagram indicates a few practical assurance techniques. The analyst should consider and implement other techniques where necessary.

### 3.2 Structured assessment of business risk and complexity

A structured approach should be taken to determine what assurance is needed when reviewing business risks. Business risk should be viewed as the combination of the potential effect of analytical errors and the likelihood of errors occurring. In situations where the risk is high, it is more important to reduce likelihood of errors than the level of the effect.

This can be visualised by considering the situation as a risk matrix (figure 3-2). The matrix is used to estimate the risk for each combination of effect and likelihood of an error, where increasing levels of effect and likelihood increase the level of risk. The effect the analysis will have is usually beyond the control of the analyst to change, so there will be few options to lessen the effect of a risk. However, there will usually be treatments (or mitigations) involving additional assurance measures that will allow the assessed business risk to become less likely to occur.

Figure 3-2 - Example of a risk matrix

<figure class="image embedded">
<div class="img">
<img src="https://assets.publishing.service.gov.uk/media/688394bac02b468fa1ae098e/Table_3.2_risk_matrix_v2.svg" />
</div>
</figure>

<div class="call-to-action">

This diagram shows an example of a risk matrix. Each cell in the table represents a level of risk based on the likelihood of an error happening and the effect of that error.  As we move from left to right the likelihood of an error increases. As we move from the bottom to the top of the table  the severity of the effect increases.  Risk increases as you move away from the bottom left corner, with the highest levels of risk in the top-right cells.

</div>

The example in table 3-3 shows some appropriate responses to a risk assessment. Where business risk is high, appropriate mitigations must be considered to reduce the probability of errors occurring. This will depend on the mitigations already in place and on the complexity of the analysis (figure 3-1).

For a situation where simple analysis is being employed, a review by an appropriate expert may be sufficient as the additional mitigation. However, for complex analysis that is already employing a wide range of internal assurance measures, options such as external peer review may be necessary.

In cases with significant time and resource constraints, it may not be possible to do as much assurance as desirable. In these situations, addressing the areas of greatest risk should take priority. You should inform the commissioner about how you have addressed the risks and any remaining risks together with appropriate caveats.

<div class="call-to-action">

Table 3-3 Responses to risk assessment levels

| Assessed risk | Mitigations to consider |
|----|----|
| High | High risk should not be tolerated. New assurance measures must be considered to treat the likelihood of errors occurring. If treatment isn’t an option, consideration must be given to terminating or transferring the risk. If it remains necessary to tolerate the risk the commissioner should to fully understand this risk. |
| Medium | Medium risk should not be tolerated without the agreement of the commissioner. New assurance measures should be put in place to treat the likelihood of errors occurring. Continue with planned or existing mitigations. |
| Low | Low risk can be tolerated. Continue with existing or planned mitigations. New treatments may also be considered. |
| Very Low | Very low risk can be tolerated. Continue with existing or planned mitigations. |

</div>

You can read more on risk management in the [Orange Book](https://www.gov.uk/government/publications/orange-book) which covers risk management principles and risk control frameworks.

### 3.3 Externally commissioned work

Proportionate assurance of externally commissioned work is just as important as for internally produced analysis. The commissioner should be fully informed of the business risk associated with the work. This should be provided by an appropriate mix of documented risk assessments provided as part of the work and by joint risk assessments planned throughout the life of the project. For commissioned work the options for mitigation will be similar to those for internal analysis.

The difference will be in ensuring the assessment of risks and the applied mitigations are fully understood by the commissioner.

### 3.4 Black-box models and business risk

Increasingly, analysis may be underpinned by AI or other forms of black-box models. With these models the need to understand business risk remains and the same structured approach to assessing business risk should be taken. The challenges in providing this assessment will be in ensuring the transparency of the analysis, availability of a suitable mix of experts and developing understanding of what mitigations are possible.

To note the [Generative AI Framework for HMG](https://www.gov.uk/government/publications/generative-ai-framework-for-hmg/generative-ai-framework-for-hmg-html) has assurance highlighted in “Principle 10”.

[Back to contents](https://www.gov.uk/guidance/the-aqua-book#contents)

Skip to chapter [1](#intro), [2](#definitions), [3](#proportionality), [4](#qac), [5](#roles), [6](#engagement), [7](#designseven), [8](#analysiseight), [9](#delivery), [10](#resources)

------------------------------------------------------------------------

## 4  Quality assurance culture

Creating and maintaining a strong culture of quality assurance is vital for ensuring analysis is robust and of a high quality.

This chapter particularly addresses senior leaders and describes their role in developing a strong culture of quality assurance. It outlines processes and approaches to support and embed quality assurance in their teams. However, everyone has a role to play in creating a strong quality assurance culture and the approaches outlined here are useful for everyone.

For the purposes of this chapter, culture is defined as the shared ways of working, beliefs and habits of an organisation. 

A strong culture of quality assurance means that quality assurance is understood, expected and valued by all those involved in the analytical process, including commissioners, analysts, users of analysis, managers, senior leaders and stakeholders.  

A strong quality assurance culture also enables effective [risk management](#risk).

<div class="call-to-action">

#### Assessing and Guiding Organisational Performance

The Department for Education has developed a Quality Assurance [Maturity Model](https://www.gov.uk/government/publications/analytical-quality-assurance-at-the-department-for-education) to help government departments and arm’s length bodies. It is an objective self-assessment method for assessing an organisation’s relative strengths and weaknesses. Organisations can judge their level of QA maturity in nine assessment areas to give an overall picture of their QA Maturity. It can be used as an aid to setting direction and activities.

</div>

### 4.1 Leadership

A strong quality assurance culture starts with senior leaders. They are accountable for the quality of analysis carried out in their departments. Senior leaders should clearly set out the priority of quality within their teams and create processes for embedding quality assurance. 

Annex 4.2 of [Managing Public Money](https://www.gov.uk/government/publications/managing-public-money) assigns accountability for ensuring appropriate assurance processes are in place to the accounting officer. In practice the accounting officer may assign the responsibility to a senior leader reporting to the senior management board. They may collect information on the state of assurance processes and include this in their annual report. The Department of Energy Strategy and Net Zero (DESNZ) reports this in each <a href="https://assets.publishing.service.gov.uk/media/6532741b26b9b1000faf1ca7/CCS0123681176-001_PN6763756_BEIS_2022-23_Annual_Report_Web_Accessible.pdf" rel="external">DESNZ Annual report</a>.

Senior leaders should ensure there is clear messaging and standards on quality assurance through guidance, training and regular updates. Senior leaders can demonstrate the importance of quality assurance through long term initiatives. For example, by setting up and embedding quality assurance processes within the team and creating roles and teams to support quality assurance. Senior leaders should ensure teams have a common understanding of the quality standards required for their work and regularly talk about quality with their teams, highlighting quality successes.

As part of a strong quality assurance culture, senior leaders should empower all those in the analytical process to identify any risks to the quality of the work, ensure people at any level can raise any quality concerns. Teams should be able to discuss and constructively challenge each other if they feel those standards are not being met. To underpin this, senior leaders should ensure teams have a common understanding of the quality standards required for their work. The Quality Assurance Maturity Model refers to this as the Departmental Governance assessment area. This area helps senior leaders review their Quality Assurance systems and give direction to the overall departmental Quality Assurance strategy.

Creating transparency at all levels can help embed a culture of quality assurance. This includes peer review, open source of code (where possible), [external publication of models or methods](#publish) and publication of the register of [Business Critical Analysis](#delivery). 

Senior leaders should also develop processes that enable teams to report when things have gone wrong, be open and honest when issues occur, carry out reviews to understand the failures in the assurance process and share the lessons learnt across the analytical community.

<div class="call-to-action">

#### An open culture when things go wrong

When the Department for Education made an error producing the schools national funding formula allocations for 2024-25 they ran a detailed internal review to understand what went wrong and why it was not detected by the quality assurance process. The department also commissioned and <a href="https://assets.publishing.service.gov.uk/media/65819c6f23b70a000d234c08/Independent_review_to_assess_the_error_made_in_the_production_of_the_schools_block_NFF.pdf" rel="external">published an external, independent review</a> to assess the error and put forward recommendations. The independent review praised the team for its culture of open learning taking responsibility for mistakes.

</div>

### 4.2 Capacity and capability

Senior leaders should create the conditions in which quality assurance processes can operate effectively by ensuring staff have sufficient time for all stages of the analytical lifecycle, including design, quality assurance and documentation. The culture should also ensure staff can draw on expertise and experience from others and have access to the tools and data they need.

#### 4.2.1 Capacity

There is a risk that work and time pressures could affect the quality of work. Senior leaders can mitigate this through strong prioritisation and supporting teams to push back on lower value work. Through this prioritisation senior leaders can emphasise the importance of quality. Senior leaders can also support quality assurance by ensuring all parties (both analytical and non-analytical) consider it at all stages during the life cycle of a project.

If time constraints mean insufficient assurance has taken place this should be explicitly acknowledged and reported in an assurance statement that sets out the known limitations and conditions associated with the analysis.

Peer review should be carried out by independent, skilled and competent individuals or groups. It can be difficult to identify available experts who are able to provide a review but there are several ways to support and embed independent review. These may include:

- setting up specific teams to review and audit a sample of analytical projects
- developing assurance networks of analysts who can provide reviews when needed
- partnering with another department
- procuring an independent review from an independent source such as the [Government Actuary’s Department (GAD)](https://www.gov.uk/government/publications/gad-services/government-actuarys-department-services), an academic institution or contractor

Team leaders can support this by making time for analysts to carry out peer reviews and ensuring analysts are clear that supporting such reviews is part of their role.

<div class="call-to-action">

#### HM Revenue and Customs (HMRC) independent review team

HMRC has a small analytical team which independently reviews analysis from across the department, including a sample of HMRC’s business-critical models. The reviews provide assurance for high profile analysis and support the sharing of best practice.

</div>

#### 4.2.2 Capability

There is a risk of errors occurring because of a lack of skills or experience. Senior leaders can identify common skill or knowledge gaps and provide training or mentoring to help fill these gaps. Processes to support knowledge sharing, innovation and dissemination of best practice will all help develop capability. Rolling out training on departmental assurance processes can also mitigate this risk.

There are various cross-government resources to support and guide commissioners and users of analysis. For example, the Analysis Function’s <a href="https://analysisfunction.civilservice.gov.uk/policy-store/advice-for-policy-professionals-using-statistics/" rel="external">Advice for policy professionals using statistics and analysis</a> supports policy professionals working with analysts and analysis. It introduces some important statistical ideas and concepts to help policy professionals ask the right questions when working with statistical evidence.

#### 4.2.3 Quality assurance champions

In organisations with large analytical community, it is good practice for the senior leaders to appoint a quality assurance champion or group of quality assurance champions. They may share best practice in implementation of quality assurance and provide advice on issues such as proportionality and communication of assurance.

<div class="call-to-action">

#### Building assurance capability

DESNZ is building assurance capacity with a programme of quality assurance colleges. The colleges run regular virtual sessions, open to colleagues across government and partner organisations.

These sessions include an interactive activity looking at a purposefully sabotaged model, which is used to introduce and familiarise colleagues with the quality assurance logbook and the departmental system of actively monitoring models using the logbooks.

College participants also join the Modelling Integrity Network and help to provide assuring analyst capacity in policy areas where lead analysts do not have existing assurance support.

</div>

<div class="call-to-action">

#### Sharing best practice on quality assurance

HMRC have developed a Quality Champions network of analysts across the department. The network discuss quality assurance initiatives, quality issues, how issues are resolved and shares wider best practice.

</div>

### 4.3 Tools

There is a risk of technology or analytical tools being out of date. This means that analysts cannot follow best practice or must spend time fixing processing issues instead of concentrating on quality. Senior leaders can support teams by:

- making funding available for new tools or improving existing tools
- gathering common issues
- escalating issues to appropriate points in their organisation

### 4.4 Data

There is a risk that issues of data quality and data understanding affect the quality of analysis. Senior leaders can escalate data quality issues with wider data teams, championing and overseeing changes to improve data quality.

### 4.5 Uncertainty in analysis

Uncertainty is an inevitable part of government work. Analysis should support government decision-making by treating uncertainty appropriately.

Senior leaders are responsible for creating a culture in which the proportionate handling of uncertainty is part of all analytical work. To do so, senior leaders should gain an understanding of how to identify uncertainty, how uncertainty can be analysed and how to plan for uncertainty.

The National Audit Office has published <a href="https://www.nao.org.uk/wp-content/uploads/2023/08/Good-practice-guide-Managing-uncertainty.pdf" rel="external">guidance for decision makers and senior leaders</a> on managing uncertainty. It is the responsibility of decision makers to challenge analysts, as well as other members of a project team, on whether uncertainties have been considered, treated appropriately and communicated.

### 4.6 Governance and control

Governance supports a strong quality assurance culture by overseeing the effective management and assurance of analysis. The [Government Functional Standard for Analysis](https://www.gov.uk/government/publications/government-analysis-functional-standard--2) sets out the requirements for a governance framework for analysis. Each organisation should have a defined and established approach to assurance. This should be applied proportionately to the risk and value of the activity and integrated with the organisation’s overall assurance framework. 

Project level governance can provide oversight over a particular model or work area. This will allow the approver to ensure the analysis is fit for purpose. For example, formally agreeing assumptions (which may be recorded in an [assumptions log](#a-log)) will reduce the need for reworking the analysis providing more time for assurance. Project governance can also fit within the wider programme level governance. 

Analytical governance boards for new, high-profile or complex pieces of analysis can allow senior analytical leaders and experts to provide oversight, challenge and ensure best practice is followed. These boards are multi-disciplinary and can cover a range of analytical approaches based on their expertise and experience. This can help ensure that innovations and new approaches are disseminated across teams, and standards are applied equally across similar work. 

### 4.7 Transparency

Transparency at all levels can help embed a culture of quality assurance. For example, peer review, sharing lessons learnt and [making analysis open](#publish) (where appropriate) can all contribute to an open culture of high quality work.

### 4.8 Externally commissioned analysis

Analysis may be commissioned externally such as qualitative or quantitative research, or the production of models.

The commissioning department remains accountable for ensuring the requirements set out in the AQuA Book are met when working with third parties such as <a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/519571/Classification-of-Public_Bodies-Guidance-for-Departments.pdf" rel="external">Arm’s Length Bodies (ALBs)</a>. ALBs include executive agencies, non-departmental public bodies and non-ministerial departments.

For example, the third party may only undertake the analyst role in the analysis phase or they may undertake the analyst, assurer and approver roles in all stages of the lifecycle.

Third parties may set out in a framework document how they will demonstrate compliance with Annex 4.2 of Managing Public Money and the Analysis Function Standard.

[Back to contents](https://www.gov.uk/guidance/the-aqua-book#contents)

Skip to chapter [1](#intro), [2](#definitions), [3](#proportionality), [4](#qac), [5](#roles), [6](#engagement), [7](#designseven), [8](#analysiseight), [9](#delivery), [10](#resources)

------------------------------------------------------------------------

## 5  Roles and the analytical lifecycle

An analytical project can be viewed as a variation on an archetypal project defined by roles and stages.

This chapter gives an overview of the roles and the project stages in the analytical lifecycle. Chapters 6 to 9 give more explanation of each stage and the responsibilities of each role during a given stage.

### 5.1 Roles and responsibilities 

Organisations may have their own titles for the main functional roles involved in analysis that are set out here.

Each role may be fulfilled by a team or committee of people. However, a single individual (for example, the chair of a committee) will have overall accountability for each role.

The AQuA Book defines four roles.

The commissioner (may be known as customer):

- requests the analysis and sets out their requirements

- agrees that what the analyst is going to do will satisfy the need

- accepts the analysis and assurance as fit for purpose

The analyst:

- designs the approach, including the assurance, to meet the commissioner’s requirements

- agrees the approach with the commissioner

- carries out the analysis

- carries out their own assurance

- acts on findings from the assurer

- can be a group of analysts, in which case the lead analyst is responsible

The assurer (may be known as the analytical assurer or assuring analyst):

- reviews the assurance completed by the analyst

- carries out any further validation and verification they may see as appropriate

- reports errors and areas for improvement to the analyst

- undertakes repeated reviews as required

- confirms the work has been appropriately scoped, executed, validated and verified and documented to the approver

- can be a group of assurers, in which case the leader of the group is responsible

- must be independent from the analysts

The approver (may be known as senior analyst or senior responsible officer):

- scrutinises the work of the analyst and assurer

- confirms (if necessary) to the analyst, assurer and commissioner that the work has been appropriately assured

The roles of analyst and assurer shall be distinct from each other. The analyst should carry out their own assurance but responsibility for formal assurance to the approver and commissioner lies with the assurer. In some instances, particularly for quick or simple analysis, an individual may fulfil more than one of the roles, apart from the assurer and analyst roles which shall be separate from one another in all cases.

### 5.2 The analytical lifecycle

Quality assurance activities should take place throughout an analytical project. An effective quality assurance process involves ongoing engagement between the commissioner and the analyst to ensure an appropriate balance is maintained between time, resource and quality, and to ensure a shared understanding of the assurance activities required and risks involved.

Figure 2 - The analytical cycle

<figure class="image embedded">
<div class="img">
<img src="https://assets.publishing.service.gov.uk/media/6853d80ba3a28280485814d2/analytical_lifecycle_diagram.svg" />
</div>
</figure>

<div class="call-to-action">

The image shows a flowchart of the analytical life cycle, which includes four main stages:

1.  Engagement and Scoping ([Chapter 6](#engagement))
2.  Design ([Chapter 7](#designseven))
3.  Analysis ([Chapter 8](#analysiseight))
4.  Delivery and Communication ([Chapter 9](#delivery))

The image emphasises that:

- The process is often iterative, meaning stages may repeat or happen out of order
- Proportionality ([Chapter 3](#proportionality)) should be considered at every stage

</div>

Figure 2 is adapted from the [Government Functional Standard for Analysis](https://www.gov.uk/government/publications/government-analysis-functional-standard--2). Analytical quality assurance activities should take place during every phase of the cycle and should consider proportionality, although analytical quality considerations may vary depending on project governance and the specific phase of the cycle. All projects will involve some element of every phase of the cycle, even if this is not clearly defined.

It is important that [proportionality](#proportionality) is considered and that there is transparency about the analytical decisions, process, limitations and changes made at each stage to enable effective assurance and communication. This should be clearly shown in:

- documentation of the analysis, assumptions and data
- records of the analytical decisions made
- records of the quality assurance processes and checks completed

#### 5.2.1 Engagement and scoping

Analytical projects typically start with customer engagement although other events may trigger them. Scoping ensures that an appropriate, common understanding of the problem is defined and that expectations are aligned with what can be produced. During this phase the commissioner plays an important role in communicating the questions to be addressed and working with the analyst to ensure the requirements and scope are defined and understood.

Where analysis requires multiple cycles (for example to develop, use and update analytical models), the engagement and scoping phase may follow on from the delivery and communication phase. In these cases, engagement and scoping will concentrate on the questions to be addressed in the next stage of the analytical project.

In this phase more effort may be needed to define the requirements and scope for research, evaluation or other projects that may need to seek a wider range of perspectives or for which subsequent phases and work may be provided through a product or service.

#### 5.2.2 Design

During the design phase, the analyst will convert the commission into an analytical plan. This will set out the assurance required and ensure the analysis is sufficient to answer the questions posed. This phase includes the communication and approval of plans. Some iteration between the commissioner and the analyst is to be expected as the analytical solution is developed and limitations understood.

For larger projects or those that require multiple cycles, the design phase may include consideration of the staging of work over the whole scope of the project as well as the work required in each stage. Analysis plans for work that is dependent on insights from earlier stages may be high-level and necessitate a return to the design phase at a later date.

#### 5.2.3 Analysis

The analysis phase is where planned analysis is undertaken and progress and relevance are monitored. The design and plan may be amended to account for changing circumstances, emerging information or unexpected difficulties or limitations encountered. This phase also includes maintaining appropriate records of the analysis conducted, changes, decisions and assumptions made. In some cases changes, or limitations encountered, may mean the scoping or design phase will need to be revisited.

Throughout this phase traceable documentation of the assurance activities that have been undertaken shall also be produced.

In larger analytical projects, some outputs of the analysis may be completed at different times as work develops and aspects of other phases may therefore take place concurrently.

#### 5.2.4 Delivery, communication and sign-off

During the delivery stage, insights and analytical assurances are communicated to the approver and the commissioner. These should be sufficiently understood for the approver and commissioner to determine whether the work has been appropriately assured and meets their requirements. Additional analysis and further assurance may be required as analytical projects frequently need further iteration or extension to satisfy the commissioner’s needs.

Work in this stage can vary considerably depending on the commission, impact, approval processes and the nature of the project. Delivery and communication activities may include producing summary packs and reports, launching dashboards or websites and presentations.

After analysis results have been determined to meet the requirements, they are formally approved for dissemination during sign-off. Sign-off includes confirming that the commission was met, documentation and evidence are captured and appropriate assurance was conducted. This approval may be phased as work develops and insights are produced.

### 5.3 Maintenance and continuous review

The analytical lifecycle is not a linear process. Where analysis is used on an ongoing basis all aspects of the lifecycle should be regularly updated. For example, consideration should be made as to whether:

- the inputs used remain appropriate
- the initial communication methods remain the best way to deliver the information
- any software relied on continues to be supported and up to date
- the model continues to be calibrated appropriately (this is particularly important for [black box models](#bbm))

Additionally, a robust version control process should be in place to ensure any changes to the analysis are appropriately assured.

### 5.4 Urgent analysis

Sometimes there is a need for urgent analysis that cannot follow all the steps in this guide. For example, the need for the analysis may outweigh the risk of poor quality. In this case analysts should follow the Government Data Quality Hub’s [Urgent data quality assurance guidance](https://www.gov.uk/government/publications/urgent-data-quality-assurance-guidance/urgent-data-quality-assurance-guidance).

[Back to contents](https://www.gov.uk/guidance/the-aqua-book#contents)

Skip to chapter [1](#intro), [2](#definitions), [3](#proportionality), [4](#qac), [5](#roles), [6](#engagement), [7](#designseven), [8](#analysiseight), [9](#delivery), [10](#resources)

------------------------------------------------------------------------

## 6  Engagement and scoping

During the first stage of the analytical lifecycle initial engagement takes place and the commissioner’s requirements are scoped out. This stage identifies what is relevant for the analysis.

During this engagement and scoping stage the commissioner and the analyst shape the analysis by developing a shared understanding of the problem and the context. This shared understanding will be used as the basis for designing analysis that meets the commissioner’s requirements.

### 6.1 Roles and responsibilities

#### 6.1.1 The commissioner’s responsibilities

In the engagement and scoping stage the commissioner should:

- inform the analyst about the important aspects of the problem, its scope, and any constraints or issues

- be available to engage with the analyst to appropriately shape the work

- ensure that they understand risks where time and resource pressures constrain the approach

- inform the analyst about any sources of uncertainty they have identified

- sign-off on the specification document produced by the analyst

- indicate the consequences for decision-making of different degrees of uncertainty, if possible, as this may enable the analyst to conduct their analysis at a proportionate level

#### 6.1.2 The analyst’s responsibilities

In the engagement and scoping stage the analyst should:

- engage with the commissioner to identify the question, the context, and the boundaries of the analysis, as well as constraints (for example, deadlines and available resource) assumptions, risks, identified uncertainties and business-criticality
- create a specification document which captures the Commissioner’s requirements

The specification document should provide a definition of the scope and project constraints. It should state the acceptable level of risk and the required level of assurance. It may also state the degree of uncertainty allowed for decision-making and record identified sources of uncertainty. The analyst should share this specification with the commissioner for sign-off.

#### 6.1.3 The assurer’s responsibilities

In the engagement and scoping stage the assurer may confirm that the engagement process has been sufficient to fully understand the problem. For more business critical projects, the assurer may wish to confirm that the specification document adequately captures the outcomes of the engagement process.

#### 6.1.4 The approver’s responsibilities

In the engagement and scoping stage the approver should note the new project and confirm that resources and plans are in place for the appropriate assurance to take place. For example, they should ensure that the analyst and assurer are aware of local assurance protocols. The approver might provide support in securing a sufficiently qualified and experienced assurer.

The approver should ensure that there is sufficient governance in place to support the analyst and their role in the wider project or programme. This is particularly important if the analysis supports business critical decisions. This may need to be revisited at the design stage if a novel or riskier approach is required (for example, if AI models are used).

### 6.2 Assurance activities

If the commissioner is unable to present a well-defined problem, the engagement stage may require the use of problem structuring methods to develop a shared understanding of the requirements. Techniques such as the Strategic Choice Approach, Rich Pictures and Systems Thinking can help the analyst and commissioner to reach a joint understanding of the problem and define the scope of the work.

You can read more about these techniques in the [Systems Thinking Toolkit](https://www.gov.uk/government/publications/systems-thinking-for-civil-servants/toolkit).

If the engagement and scoping techniques are complex or the project is deemed business critical, the assurer might also provide assurance of the <a href="https://publications.tno.nl/publication/100301/Zs2SUz/wijnmalen-2012-natoclient.pdf" rel="external">engagement methodology</a>.

The engagement and scoping stage should lead to agreement between the analyst and commissioner about the outputs of the work, including acceptable levels of accuracy, precision and margins of error. This will inform the handling and the assurance of uncertainty in later stages.

The commissioner should communicate to the analyst any relevant information about data sources and data quality. This will be used to guide the design of data processing.

The analyst and commissioner should also clarify risks and potential effects on the outcomes to inform the decisions around [proportionate assurance](#proportionality). Constraints around resources and timelines should also be clarified and agreed.

### 6.3 Documentation

The output of the engagement and scoping stage should be a [specification document](#d-doc) that captures the commissioner and analyst’s joint understanding of the task. This document provides a reference for later [validation](#validation) assurance activities (for example, by confirming that the analysis meets the specification). This document also provides the approver with evidence that the analysis meets the specification during the [delivery stage](#delivery). The document should be signed off by the commissioner and might also be reviewed by the assurer.

### 6.4 Treatment of uncertainty

The engagement and scoping stage will inform the treatment of uncertainty by:

- providing a clear definition of the analytical question

- identifying sources of high or intractable uncertainty

- establishing an understanding of how the analysis will inform decisions

You can read more about uncertainty in engagement and scoping in the <a href="https://analystsuncertaintytoolkit.github.io/UncertaintyWeb/chapter_2.html#Jointly_agreeing_how_uncertainty_should_be_used" rel="external">Uncertainty Toolkit</a>.

### 6.5 Black box models

Where the commissioner has engaged with the analyst to deliver [black box models](#bbm) such as AI or machine learning, the engagement and scoping stage should include discussions around ethics and risks to assess whether such models would be appropriate for addressing the given problem. For example, discussions might include considerations of regulations such as UK GDPR, organisational skills, internal governance, use of regular tests to ensure the model continues to work as expected and risk management.

You can read more in the [Introduction to AI assurance](https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance).

### 6.6 Multi-use models

When working with multi-use models, the analyst may be required to engage with a group of end-users to develop an understanding of their respective requirements. Where requirements differ or contradict, techniques such as Strategic Options Development and Analysis (<a href="https://www.ifm.eng.cam.ac.uk/research/dstools/soda/" rel="external">SODA</a>) and <a href="https://en.wikipedia.org/wiki/Soft_systems_methodology" rel="external">Soft Systems Methodology</a> may be used to develop a shared understanding across multiple groups.

[Back to contents](https://www.gov.uk/guidance/the-aqua-book#contents)

Skip to chapter [1](#intro), [2](#definitions), [3](#proportionality), [4](#qac), [5](#roles), [6](#engagement), [7](#designseven), [8](#analysiseight), [9](#delivery), [10](#resources)

------------------------------------------------------------------------

## 7  Design

During the design stage the analyst creates an actionable [analytical plan](#spec-doc) from the scope for the analysis agreed with the commissioner.

This chapter sets out recommended practices around designing the analysis, deciding on the associated assurance activities, documenting the design and assuring the design. It also discusses considerations around the treatment of uncertainty in design and the design of multi-use and AI models.

The development of the analytical plan should consider:

- methodology for producing results, including the treatment of uncertainty
- project management approach (for example <a href="https://en.wikipedia.org/wiki/Agile_software_development" rel="external">Agile Software Development</a>, <a href="https://en.wikipedia.org/wiki/Waterfall_model" rel="external">Waterfall planning</a>, or a combination of approaches)
- sourcing of inputs and assumptions
- data and file management
- change management and version control
- programming language and software
- code management, documentation and testing
- communication between stakeholders
- verification and validation procedures during the project lifetime
- documentation to be delivered
- process for updating the analytical plan
- process for ongoing review and maintenance of models, including reviewing inputs and calibrations and ensuring that software relied on continues to be supported and up to date
- ethics
- reporting
- the use and application of the analysis

Iteration of the plan between the commissioner and the analyst is normal and expected while the analytical design develops.

<div class="call-to-action">

#### Reproducible analytical pipelines

The recommended approach for developing analysis in code is to use a <a href="https://analysisfunction.civilservice.gov.uk/support/reproducible-analytical-pipelines/" rel="external">Reproducible Analytical Pipeline (RAP)</a>. RAPs shall:

- follow the practices set out in the <a href="https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html" rel="external">Analysis Function Quality Assurance of Code for Analysis and Research manual</a>
- meet the requirements of the <a href="https://github.com/best-practice-and-impact/rap_mvp_maturity_guidance/blob/master/Reproducible-Analytical-Pipelines-MVP.md" rel="external">RAPs minimum viable product</a>

</div>

### 7.1 Roles and responsibilities in the design stage

#### 7.1.1 The commissioner’s responsibilities

The commissioner should confirm that the analytical approach will satisfy their needs. To assist in this, the commissioner may review the analytical plan.

The commissioner’s expertise can be a useful resource for the analyst in the design stage. The commissioner might provide information regarding the input assumptions, data requirements and the most effective ways to present the outputs. All of these can inform the design.

#### 7.1.2 The analyst’s responsibilities

The analyst should:

- develop the method and plan to address the commissioner’s needs
- establish assurance requirements
- develop a plan for proportionate verification and validation as described in the <a href="https://www.nao.org.uk/wp-content/uploads/2016/03/11018-002-Framework-to-review-models_External_4DP.pdf" rel="external">National Audit Office Framework to review models</a>;
- plan in sufficient time for the assurance activity
- document the analytical plan in a proportionate manner
- follow any organisation governance procedures for project design

#### 7.1.3 The assurer’s responsibilities

The assurer should review the analytical plan to ensure that it is able to conduct the required assurance activities. They may provide feedback on the analytical plan. The assurer should plan sufficient time for the assurance activity.

#### 7.1.4 The approver’s responsibilities

In smaller projects, the approver may not be heavily involved in the design stage. However, for business critical analysis, the approver may want to confirm that organisational governance procedures for design have been followed.

### 7.2 Assurance activities

When the design stage has been completed the assurer should be aware of the quality assurance tasks that will be required of them during the project lifetime and have assured the necessary elements of the analytical plan.

The assurance of the design stage should consider whether the analytical plan is likely to:

- address commissioner’s requirements (validation)
- deliver as intended (verification)
- meet the principles of [RIGOUR](#rigour) by, for example, providing a well-structured, data driven plan with a sound overall design

The assurance of the design stage may be carried out by the assurer. For more complex analysis, it is good practice to engage subject matter experts to provide independent assurance and to ensure the accuracy and limitations of the chosen methods are understood, ideally with tests baselining their response against independent reference cases.

### 7.3 Documentation

The design process should be documented in a proportionate manner. A design document that records the analytical plan should be produced by the analyst and signed-off by the commissioner. The design document may be reviewed by the assurer.

For modelling, an initial model map may be produced that describes data flows and transformations. This can be updated as the project progresses through the Analysis stage.

It is best practice to use formal version control to track changes in the design document.

### 7.4 Treatment of uncertainty in the design stage

During the design stage, analysts should mine the planned analysis systematically for possible sources and types of uncertainty. This is to maximise the chance of identifying all that are sufficiently large to breach the acceptable margin of error.

You can read more in Chapter 3 of the <a href="https://analystsuncertaintytoolkit.github.io/UncertaintyWeb/chapter_3.html" rel="external">Uncertainty Toolkit for Analysts</a>.

### 7.5 Black box models

Using [black box models](#bbm) places greater weight on the design of the analysis and the assurance and validation of outputs by domain experts.

This [guidance on AI assurance](https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance) outlines considerations for the design of AI models, including risk assessment, impact assessment, bias audits and compliance audits.

In the design of AI and machine learning models, the analyst should:

- define the situation they wish to model
- the prediction they wish to make
- assess the quality of data that could be used to make the prediction, this includes the data used in any pretrained models
- carry out a literature review to identify appropriate modelling, valuation verification methods and document the rationale for selecting their approach
- consider the appropriate data training, validation and testing strategy for the models - it is usual to design a model with a fraction of the data, validate with a separate portion and then test the final model with the data that was not used in the design
- consider the strategy when testing a pre-trained model, including appropriate validation methods for the models such as calculating similarity to labelled images or ground truths for generative AI
- consider developing automatic checks to identify if the model is behaving unexpectedly, this is important if the model is likely to be used frequently to make regular decisions or is deployed into a production environment
- consider the plan for maintenance and continuous review, including the thresholds or timeline to retrain the model and the resources required to support this - see the [maintenance and continuous review](#maincontrev) section
- consider referring the model to their ethics committee, or a similar group dependent on your internal governance structures - see the [Data Ethics Framework](https://www.gov.uk/government/publications/data-ethics-framework/data-ethics-framework-2020)
- consider setting up a peer or academic review process to test the methodologies and design decisions

### 7.6 Multi-use models

Designing multi-use models should take into account the needs of all users of the analysis. An Analysis Steering Group may be an effective means for communication about the design with a range of user groups.

The design of multi-use models may entail a modular structure with different analysts and assurers responsible for different elements. The design of assurance activities should capture both the assurance of individual modules and their integration.

[Back to contents](https://www.gov.uk/guidance/the-aqua-book#contents)

Skip to chapter [1](#intro), [2](#definitions), [3](#proportionality), [4](#qac), [5](#roles), [6](#engagement), [7](#designseven), [8](#analysiseight), [9](#delivery), [10](#resources)

------------------------------------------------------------------------

## 8  Analysis

During the analysis stage, the planned analysis is undertaken and assured, and progress and relevance are monitored. The design may be amended to account for any changing circumstances, emerging information, unexpected difficulties or limitations that may be encountered. This stage also includes maintaining appropriate and traceable records of the analysis and assurance activities conducted, changes, decisions and assumptions made. In some cases changes or limitations encountered may mean that the design or scoping stage need to be revisited to address these issues.

### 8.1 Roles and responsibilities in the analysis stage

#### 8.1.1 The commissioner’s responsibilities

The commissioner should:

- be available to provide input and clarifications to the analyst
- review any changes in design or methodology that the analyst brings to their attention

#### 8.1.2 The analyst’s responsibilities

The analyst should:

- follow the conduct the verification and validation activities that were designed as part of the analytical plan in [the design stage](#design)
- provide traceable documentation of the assurance they have undertaken
- respond to recommendations from the assurer and act on them as appropriate
- proportionately follow [best practice for code development](#code), where relevant
- produce documentation of the data (as described in [The Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework)) and methods used
- ensure all documentation is sufficient for the assurer to understand the approach
- document any changes to the analytical plan in a proportionate manner
- maintain appropriate contact with commissioner and assurer to provide an opportunity for them to advise on whether the analysis is still meeting the commissioner’s needs or whether there are any new requirements

#### 8.1.3 The assurer’s responsibilities

The assurer shall:

- review the assurance completed by the analyst
- carry out any further validation and verification they may see as appropriate
- report errors and areas for improvement to the analyst
- review that the work proportionately adheres to [best practice for code development](#code), where relevant

The assurer may need to:

- re-review the analytical work completed, as required
- provide feedback on changes to the analytical plan,
- consider whether they are qualified to provide rigorous assurance on the revised methodology

#### 8.1.4 The approver’s responsibilities

The approver should be aware of the progress of the analysis and ensure that they are available for approving the work at the delivery stage.

### 8.2 Assurance activities

#### 8.2.1 Verification and validation

Verification that the implemented methodology meets the design requirements should be part of the analysis. <a href="https://typeset.io/pdf/guidelines-for-selecting-and-using-simulation-model-143kzp6h5s.pdf" rel="external">Whitener and Balci (1989)</a> reviewed verification techniques in relation to simulation modelling but these techniques also extend to analysis more broadly. They include:

- informal analysis - techniques that rely on human reasoning and subjectivity
- static analysis - tests that the implementation of the analysis before it is run (for example, checking that code adheres to code conventions)
- dynamic analysis - tests the behaviour of the system, model or code to find errors that arise during execution, includes <a href="https://en.wikipedia.org/wiki/Unit_testing" rel="external">unit testing</a>, <a href="https://en.wikipedia.org/wiki/Integration_testing" rel="external">integration testing</a> and <a href="https://en.wikipedia.org/wiki/Stress_testing_(computing)" rel="external">stress testing</a>
- symbolic analysis - focuses on how model inputs are transformed into outputs using [symbolic proxies](#s-proxy), involving techniques like <a href="https://typeset.io/pdf/guidelines-for-selecting-and-using-simulation-model-143kzp6h5s.pdf" rel="external">path tracing and cause-effect testing</a>.
- constraint analysis - particularly relevant to modelling and tests the implementation of constraints during model execution, includes checking the assertions of the model and boundary analysis
- formal analysis - tests logical correctness through <a href="https://en.wikipedia.org/wiki/Formal_verification#Formal_verification_for_software" rel="external">formal verification</a> such as logic or mathematical proofs

Validation is testing whether the product meets the requirements of users. It is important to involve the users in the process. <a href="https://en.wikipedia.org/wiki/Verification_and_validation#Aspects_of_analytical_methods_validation_" rel="external">Methods for validation</a> include quantification and judgment of acceptable sensitivity, specificity, accuracy, precision and reproducibility.

Validation of models includes testing the validity of the conceptual model and the operational validity of any computerised model.

You can read more about <a href="https://www.informs-sim.org/wsc11papers/016.pdf" rel="external">techniques that may be useful in validation of models</a>.

The analyst has primary responsibility for conducting verification and validation. The assurer is responsible for reviewing the verification and validation that is carried out by the analyst, and for conducting or recommending additional verification and validation as required. The assurer may refer to the [specification document](#spec-doc) to assure that the analysis meets the specification.

#### 8.2.2 Data validity and data considerations

Testing data validity (for example, ensuring that data meet the specification for which they are used) is a vital part of analysis. Procedures for assuring data validity include testing for internal consistency, screening for data characteristics such as outliers, trends and expected distributions, and assuring robust data management practices such as automating data creation and data sourcing.

Consideration may be given to the conditions for the data to continue to be valid. For example, data might be updated or become out of date. In some cases it may be appropriate to specify a “sunset date” for the data i.e. the date beyond which the data should be refreshed or reviewed.

It is rare to have the perfect dataset for an analytical commission. This could be because:

- the data is not available in the time frame required for the ideal analysis

- the data definition does not perfectly align with the commission

- there are data or coverage gaps

- the data may be experimental or there are other reasons why it is not mature

When no data is available that is directly and precisely relevant to the parameter and conditions of interest it is often possible to use surrogate data. This is the measurements of another parameter (or of the parameter of interest under different conditions) that is related to the parameter and conditions of interest. This implies extrapolating between parameters, or between conditions for the same parameter. Although the use of surrogate data introduces further uncertainty additional to that already associated with the data itself, it may be possible to quantify this additional uncertainty using expert knowledge of the relationship between the surrogate and the parameter of interest.

The effect of using a proxy dataset should be explored and if the uncertainty associated with the dataset has a large bearing on the analysis, its appropriateness should be revisited. This exploration and the decision to use a particular dataset or input should be recorded for the assurer to verify.

#### 8.2.3 Assurance of code

<a href="https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html" rel="external">Quality Assurance of Code for Analysis and Research (known informally as the Duck Book)</a> provides detailed good practice guidance on developing analytical software and assurance for delivering quality code. It includes guidance on:

- structuring code
- producing documentation
- using version control
- data management
- testing
- peer review
- automation

The analyst shall follow the guidance for good quality code development in a proportionate manner and the assurer shall review this accordingly.

### 8.3 Documentation

The analyst should:

- maintain appropriate records of the work
- fully document any code following agreed standards
- log the data, assumptions and inputs used in the analysis, and decisions made in appropriate [documentation](#spec-doc)
- record the verification and validation that has been undertaken, documenting any activities that are outstanding and noting what remedial action has been taken and its effect on the analysis
- produce [user and technical documentation](#utd)

For modelling, the analyst may include a model map that describes data flows and transformations.

### 8.4 Treatment of uncertainty

While the scoping and design stages identified and described risks and uncertainties, the analysis stage assesses and quantifies how uncertainty may influence the analytical outcome and its contribution to the range and likelihoods of possible outcomes. <a href="https://analystsuncertaintytoolkit.github.io/UncertaintyWeb/chapter_5.html" rel="external">The Uncertainty Toolkit for Analysts</a> reviews methods of quantifying uncertainty. The verification and validation by the analyst and assurer should assure the appropriate treatment of uncertainty.

### 8.5 Black box models

[Black box models](#bbm) such as AI and machine learning models are not as transparent as traditionally coded models. This adds challenge to the assurance of these models as compared to other forms of analysis.

- should include the verification steps set out in the design stage
- should include validation and verification of automatic tests to ensure the model behave as expected
- may include performance testing in a live environment

More guidance is available in :

- [Portfolio of AI assurance techniques](https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques)
- [Introduction to AI Assurance](https://www.gov.uk/government/publications/introduction-to-ai-assurance)

### 8.6 Multi-use models

In multi-use models, analysis and edits may be carried out on individual elements of the model at differing times. This requires mechanisms for assuring that the changes integrate into the larger model as expected. An example of how this can be achieved is by using test suites.

[Back to contents](https://www.gov.uk/guidance/the-aqua-book#contents)

Skip to chapter [1](#intro), [2](#definitions), [3](#proportionality), [4](#qac), [5](#roles), [6](#engagement), [7](#designseven), [8](#analysiseight), [9](#delivery), [10](#resources)

------------------------------------------------------------------------

## 9  Delivery, communication and sign-off

The successful delivery of analysis to the commissioner marks its transition from being a product under development to one that is fit and ready to be used to inform decision-making in your organisation and, possibly, inform the public.

This chapter provides information on the assurance of communication of analysis and delivery of analytical output.

### 9.1 Roles and responsibilities in delivery, communication and sign-off

#### 9.1.1 The commissioner’s responsibilities

The commissioner should:

- confirm that the analysis is likely to meet their needs
- use the analysis as specified
- understand and apply any limitations to its use

#### 9.1.2 The analyst’s responsibilities

The analyst shall:

- follow organisational governance procedures for delivery and sign-off, including, where appropriate, updating the [business-critical analysis register](#bca) and making the analysis [publicly available](#publish)
- describe any limitations to using the analysis

The analyst should:

- ensure that communication meets audience requirements such as accessibility
- be prepared to respond to challenge from the approver or scrutiny from project or programme boards

The analyst should communicate the assurance state to the approver if this is not done directly by the assurer.

#### 9.1.3 The assurer’s responsibilities

The assurer should communicate the assurance state to the approver. This includes confirmation that the work has been appropriately scoped, executed, validated, verified, documented and that it provides adequate handling of uncertainty. This communication may be undertaken by the analyst.

#### 9.1.4 The approver’s responsibilities

The approver shall:

- review the assurance evidence that has been provided to them
- be confident that the analysis meets the design requirements, is of sufficient quality and is adequately and proportionately documented
- follow organisation governance procedures for sign-off, including updating of the [business-critical analysis register](#delivery), where appropriate

The approver should:

- provide sufficient challenge to the analysts to gain assurance that the analysis is fit for purpose
- provide the analyst with evidence that the analysis outputs have been properly reviewed and formally approved when they are satisfied with the validity and robustness of the analysis

### 9.2 Assurance activities

#### 9.2.1 Delivery

When delivering a piece of analysis, the assurer (or analyst) should communicate its assurance state to the approver and provide evidence that the analysis and associated outputs have undergone proportionate quality assurance. They should also demonstrate that the analysis is ready for delivery. This may include confirming that the analysis:

- uses suitable data and assumptions

- has provisions for regular review to consider whether methodology, data and assumptions remain valid or a “sunset date” - a date beyond which the analysis and / or the model should not be used

- meets the purpose of its commission

- has been carried out correctly and to its agreed specification

- has a risk assessment and statement against the programme risk register

- meets analytical standards, such as those around coding standards and documentation

- adheres to relevant professional codes of practice (for example, <a href="https://code.statisticsauthority.gov.uk/" rel="external">The Code of Practice for Statistics</a>

- is accompanied by a completed <a href="https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fassets.publishing.service.gov.uk%2Fmedia%2F65c5021f9c5b7f0012951b83%2F20231101-analysis-evidence-quality-assurance-report-gov-uk-E02.docx&amp;wdOrigin=BROWSELINK" rel="external">assurance statement</a>, where appropriate

Though not strictly assurance, the analyst should also consider areas such as:

- security ratings
- retention policies
- intellectual property
- ethics and related concerns

The approver should scrutinise the evidence delivered and approve the work if the analysis meets the required standard. The approver should then feedback the outcome of any approval activities to the analyst so that the analysis can be updated if required.

The exact nature of any scrutiny made by the approver should be proportionate to the effect the analysis is likely to have and the governance process of their programme or organisation. It should follow the [principles of proportionality](#proportionality).

To ensure that the analysis is used as intended, the commissioner should use the analysis as specified at the start of the analytical cycle, applying any limitations to its use as described by the analyst.

#### 9.2.2 Communication

Effective and transparent communication is essential to ensure analysis is adopted and trusted by the commissioner and onward users. Depending on its final use and likelihood of publication, any analysis may be communicated to a wide audience including:

- commissioners and users of the analysis

- external scrutineers such as the <a href="https://committees.parliament.uk/committee/127/public-accounts-committee/" rel="external">Public Accounts Committee</a>, the <a href="https://www.nao.org.uk/" rel="external">National Audit Office</a>, internal and external auditors

- the public, through publications and <a href="https://www.legislation.gov.uk/ukpga/2000/36/contents" rel="external">Freedom of Information Act</a> requests

- academic experts, possibly through a departmental [Areas of Research Interest](https://www.gov.uk/government/publications/dwp-areas-of-research-interest-2023/dwp-areas-of-research-interest-2023) document

- national and international governmental partners

The form of communication should be tailored to the audience. The communication should be quality assured in a proportionate manner to ensure an accurate reflection of the analytical results.

The Analysis Function’s <a href="https://analysisfunction.civilservice.gov.uk/policy-store/making-analytical-publications-accessible/" rel="external">Making Analytical Publications Accessible Toolkit</a> gives guidance to help ensure that any that websites, tools, and technologies produced from analysis are designed and developed so that they meet accessibility guidelines.

If the outcome of any analysis needs to be published the analyst should follow departmental and statutory guidance. There are different guidelines depending on the work that is being published. These are:

- <a href="https://osr.statisticsauthority.gov.uk/publication/regulatory-guidance-publishing-official-statistics-and-national-statistics/" rel="external">The regulatory guidance for publishing official statistics and national statistics</a>

- [The Government Social Research Publication protocol](https://www.gov.uk/government/publications/government-social-research-publication-protocols)

- any recommendations from the [Evaluation Task Force](https://www.gov.uk/government/organisations/evaluation-task-force) for evaluations

#### 9.2.3 Sign-off

The exact nature of the approval process may vary depending on the:

- effect the analysis is likely to have

- approval process of the organisation

- nature of the programme, project or board approving the analysis

The formality of the sign-off process should be governed by organisational procedures and be proportionate to the analysis.

The approver should provide the analyst with evidence that the analysis outputs have been properly reviewed and formally approved. For example, through the notes of a project or programme board where the decision to approve the analysis was made.

### 9.3 Documentation

When the analyst and assurer are satisfied that the analysis is ready to hand over to the commissioner, they should ensure that any associated documentation supporting the analysis is ready and has also undergone quality assurance. Supporting documentation may include:

- [specification](#d-doc) and [design documentation](#d-doc)

- logs of [data](#utd), [assumptions](#a-log) and [decisions](#d-log) including their source, ownership, reliability and any details of any sensitivity analysis carried out

- [user and technical documentation](#utd)

- advice on uncertainty and its affect on the outputs of the analysis

- a description of the limits of the analysis and what it can and cannot be used for

- any materials for presenting the analysis to the commissioner (for example, slide decks or reports)

- a record of the analysis including methods used, dependencies, process maps, change and version control logs and error reporting

- the code-base, when it has been agreed to [publish the analysis openly](#publish)

- the test plan and results of the tests made against that plan

- a statement of assurance

- a statement confirming that ethical concerns have been addressed, especially in cases that include the application of [black-box models](#bbm)

### 9.4 Treatment of uncertainty

Government has produced a range of guidance to support analysts in presenting and communicating uncertainty in analysis, providing valuable advice on how to estimate and present uncertainty when describing the limitations of use of a piece of analysis. This includes:

- The Office for Statistical Regulation’s <a href="https://osr.statisticsauthority.gov.uk/publication/approaches-to-presenting-uncertainty-in-the-statistical-system/" rel="external">Approaches to presenting uncertainty in the statistical system</a>

- The <a href="https://analystsuncertaintytoolkit.github.io/UncertaintyWeb/chapter_6.html" rel="external">Uncertainty Toolkit for Analysts</a>

- The Government Analysis Function guidance note on <a href="https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/" rel="external">Communicating quality, uncertainty and change</a>

### 9.5 Black-box models and the delivery, communication and sign-off stage

The approver is responsible for signing-off that all risks and ethical considerations ([see principles](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principles) in the <a href="https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principles" rel="external">Artificial Intelligence Playbook for the UK Government</a>) around the use of black-box models have been addressed.

This may include:

- formal consultation and approval by an ethics committee or similar depending on internal governance structures
- provisions for regular review, including whether on-going peer review is required to ensure the latest guidance and assurance methodology is taken into account
- communicating the “health” of the model at regular intervals to the commissioner.

<div class="call-to-action">

#### Regularly reviewing model health

Model effectiveness can change over time. For example, does the model continue to behave as expected or has there been data drift where the model’s performance decreases? This can happen when a model is trained on historical data, but then uses current data when it is being used in production. Such a model may become less effective because it is no longer conditioned on the current state of the data.

You can read more about this in the [Introduction to AI assurance](https://www.gov.uk/government/publications/introduction-to-ai-assurance).

</div>

### 9.6 Multi-use models

There is a greater risk that multi-use models may be used for purposes outside the intended scope. This means it is important that the analyst very clearly communicates to all users the limitations and intended use. The analyst may consider testing communication with different user groups to ensure that the analytical outputs are used as intended.

### 9.7 Analytical transparency

Supporting and encouraging the public to understand and scrutinise analysis promotes public confidence in decisions. This includes providing the public with information on models used for [business-critical decisions](#delivery), [making analysis open](#publish) and ensuring <a href="https://osr.statisticsauthority.gov.uk/publication/regulatory-guidance-on-intelligent-transparency/" rel="external">transparency</a>.

The UK Statistics Authority has <a href="https://osr.statisticsauthority.gov.uk/publication/guidance-for-models-trustworthiness-quality-and-value/pages/1/" rel="external">published guidance</a> on how the principles of Trustworthiness, Quality and Value from the Code of Practice for Statistics can be applied in the design, development and use of models.

#### 9.7.1 Business critical models register

Departments and <a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/519571/Classification-of-Public_Bodies-Guidance-for-Departments.pdf" rel="external">Arm’s Length Bodies (ALBs)</a> should publish a list of [business critical models](#bca) (BCM) in use within their organisations at least annually. The list should meet accessibility guidelines.

Each Department and ALB should decide what is defined as business critical based on the extent to which they influence significant financial and funding decisions, are necessary to the achievement of a departmental business plan, or where an error could lead to serious financial, legal or reputational damage.

The definitions and thresholds of business criticality should be aligned with their organisation’s own risk framework. The thresholds should be agreed by the director of analysis or equivalent.

ALB’s are responsible for publishing their own BCM list, unless agreed otherwise with the department. The ALB’s accounting officer is accountable for ensuring publication and the sponsor department’s accounting officer oversees this.

The BCM list should include all Business critical models unless there is an internally documented reason for the analysis to be excluded. This should be agreed with the director of analysis (or equivalent) and that agreement should be documented.

Justification for not publishing a model in the list may include, but is not limited to:

- exemptions under the Freedom of Information (FOI) Act 2000
- national security
- policy under development
- commercial interests

In addition to these exemptions there may be further reasons where the risk of a negative consequence is deemed to outweigh the potential benefits resulting from publication of the model. For example, where population behaviour may change in response to awareness of a model or modelling.

For clarity, the name of the analysis or model and what it is used for should be included alongside links to any published material.

#### 9.7.2 Open publishing of analysis

To facilitate public scrutiny departments may choose to make the analysis or model (for example, source code or spreadsheets) and any relevant data, assumptions, methodology and outputs open to the public. [Open publishing of source code](https://www.gov.uk/service-manual/service-standard/point-12-make-new-source-code-open) and other parts of the analysis allows others to reuse and build on the work.

You can read more about making [source code open and reusable](https://www.gov.uk/service-manual/technology/making-source-code-open-and-reusable).

The [guidance for publishing Business Critical Analysis lists](#delivery) should be applied to the publication of analysis as in some cases it might not be appropriate to publish the work. For example, if the analysis is extremely complex it may be more appropriate to publish summary information to make the analysis more accessible.

[Back to contents](https://www.gov.uk/guidance/the-aqua-book#contents)

Skip to chapter [1](#intro), [2](#definitions), [3](#proportionality), [4](#qac), [5](#roles), [6](#engagement), [7](#designseven), [8](#analysiseight), [9](#delivery), [10](#resources)

------------------------------------------------------------------------

## 10  Resources

### 10.1 Written resources

The key additional resources referred to in the AQuA Book:

- The [Government Functional Standard for Analysis](https://www.gov.uk/government/publications/government-analysis-functional-standard--2)
- The [Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2020)
- The [Magenta Book](https://www.gov.uk/government/publications/the-magenta-book)
- The [Orange Book](https://www.gov.uk/government/publications/orange-book)

#### 10.1.1 Guidance and advice for performing analysis

- The <a href="https://analystsuncertaintytoolkit.github.io/UncertaintyWeb/index.html" rel="external">Uncertainty Toolkit for Analysts in Government</a> provides support for handling uncertainty in analysis.

- <a href="https://analysisfunction.civilservice.gov.uk/policy-store/advice-for-policy-professionals-using-statistics/" rel="external">Advice for policy professionals using statistics and analysis</a> helps policy professionals work effectively with statisticians and other analysts. It introduces some important statistical ideas and concepts to help policy professionals ask the right questions when working with statistical evidence.

- The [Data Ethics Framework](https://www.gov.uk/government/publications/data-ethics-framework/data-ethics-framework-2020) guides appropriate and responsible data use in government and the wider public sector. It helps public servants understand ethical considerations, address these within their projects, and encourages responsible innovation.

- The [Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework) supports the production of sustainable high quality data.

- The <a href="https://analysisfunction.civilservice.gov.uk/support/reproducible-analytical-pipelines/" rel="external">Reproducible Analytical Pipelines</a> guidance sets out what a Reproducible Analytical Pipeline is and points to resources for analysts who need to build them.

#### 10.1.2 Guidance and advice for performing assurance

- The Department for Education’s Quality Assurance [Maturity Model](https://www.gov.uk/government/publications/analytical-quality-assurance-at-the-department-for-education) helps to evaluate organisational strengths and weaknesses in Quality Assurance related to analysis.

- The <a href="https://www.nao.org.uk/wp-content/uploads/2016/03/11018-002-Framework-to-review-models_External_4DP.pdf" rel="external">National Audit Office Framework to review models</a> provides a structured approach to review models which organisations can use to determine whether the modelling outputs they produce are reasonable, robust and have a minimal likelihood of errors being made.

- <a href="https://www.gov.uk/government/publications/energy-security-and-net-zero-modelling-quality-assurance-qa-tools-and-guidance" rel="external">Department for Energy Security and Net Zero modelling tools and QA guidance</a> provides resources to help quality assure new and existing models, including those developed by third parties.

- [Introduction to AI assurance](https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance) outlines considerations for the design and assurance of AI models, including risk assessment, bias audits and considering the ongoing ‘health’ of the model.

- The <a href="https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html" rel="external">Duck Book</a> provides guidance on assuring code.

#### 10.1.3 Guidance and advice for communicating analysis

- The Office for Statistical Regulation’s <a href="https://osr.statisticsauthority.gov.uk/publication/approaches-to-presenting-uncertainty-in-the-statistical-system/" rel="external">Approaches to presenting uncertainty in the statistical system</a> explores ways of communicating uncertainty in statistics.

- The Government Analysis Function guidance note <a href="https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/" rel="external">Communicating quality, uncertainty and change</a> explains how to communicate information about quality, uncertainty and change to users.

- The Analysis Function’s <a href="https://analysisfunction.civilservice.gov.uk/policy-store/making-analytical-publications-accessible/" rel="external">Making Analytical Publications Accessible Toolkit</a> gives guidance to help ensure that any that websites, tools, and technologies produced from analysis are designed and developed so that they are accessible.

- If you are publishing statistics you shall follow your organisation’s guidance and the <a href="https://osr.statisticsauthority.gov.uk/wp-content/uploads/2018/10/Publishing_official_statistics_National_Statistics_1218.pdf" rel="external">regulatory guidance for publishing official statistics and national statistics</a>.

- If you are publishing research, you shall follow your organisations guidance and the [Government Social Research Publication protocol](https://www.gov.uk/government/publications/government-social-research-publication-protocols).

- If you are publishing an evaluation, refer to any recommendations from the [Evaluation Task Force](https://www.gov.uk/government/organisations/evaluation-task-force).

### 10.2 External sources of quality assurance

The [Government Actuary’s Department (GAD)](https://www.gov.uk/government/publications/gad-services/government-actuarys-department-services) can provide expert quality assurance reviews of models across the public sector. GAD are a team of financial risk professionals and are experts in reviewing models on all modern platforms, including Excel, R, and Python. As a non-ministerial department, GAD can offer unique support from within government.

[Back to contents](https://www.gov.uk/guidance/the-aqua-book#contents)

Skip to chapter [1](#intro), [2](#definitions), [3](#proportionality), [4](#qac), [5](#roles), [6](#engagement), [7](#designseven), [8](#analysiseight), [9](#delivery), [10](#resources)

------------------------------------------------------------------------

## Improving the book

### Accessibility

The AQuA Book, when final, will comply with the [www.gov.uk accessibility statement](https://www.gov.uk/help/accessibility-statement). Compliance does not extend to third-party content outside the www.gov.uk domain that is referenced from the guidance.

### Help us improve this book

We are always looking to improve our guidance. If you have comments or suggestions about the content of the AQuA Book or suggestions for how it might be improved, you can contact us by emailing [Analysis.Function@ons.gov.uk](mailto:analysis.function@ons.gov.uk?subject=Aqua%20Book). Please use the words “AQuA Book” in the subject line of your email.

</div>
