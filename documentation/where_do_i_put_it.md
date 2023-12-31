# Make it easy

[Return to Readme](../readme.md)


## Some other notes

While I'm halfhazardly just throwing some things together, let's make a list of what I've done so far.

1. **[.garbarge.py](../.garbarge.py)** is loose script for gathering some titbits of information and saving them. Like updating the requirments.txt, this isn't a final measure, just a quick fix that needs fine tuning. It will likely build some of the path information for cfg

- [Make it easy](#make-it-easy)
  - [Some other notes](#some-other-notes)
  - [All documentation](#all-documentation)
    - [Precursory](#precursory)
    - [Participatory](#participatory)
  - [Content](#content)
    - [ARID](#arid)
    - [Skimmable](#skimmable)
    - [Exemplary](#exemplary)
    - [Consistent](#consistent)
    - [Current](#current)
  - [Sources](#sources)
    - [Nearby](#nearby)
    - [Unique](#unique)
  - [Publications](#publications)
    - [Discoverable](#discoverable)
    - [Addressable](#addressable)
    - [Cumulative](#cumulative)
    - [Complete](#complete)
    - [Beautiful](#beautiful)
  - [Body](#body)
    - [Comprehensive](#comprehensive)








Getting started should be as easy and straight-forward as possible. Most people don’t like change, and introducing new tooling and things will already rouse a negative response in some. This is why you need to make it as simple as possible to get started.

Build templates
It should take about 5 seconds to get a basic outline of the documentation for a project started.

Also have a standard hierarchy for the docs, so that people know where to look for things in any project.

---------------------------------------------------------------

## All documentation

[Top of Page](#make-it-easy) | [Return to Readme](../readme.md)

In general, documentation should be…

- [Precursory](#precursory)
- [Participatory](#participatory)

### Precursory

Begin documenting before you begin developing.

Before coding, write requirements and specifications that also serve as the first draft of documentation. These texts no doubt will need a bit of clean up before publishing, but by front-loading the documentation, you lay a clear path forwards. Early documentation also helps facilitate peer feedback and group decisions to guide your work. This model is the sentiment behind documentation driven design.

### Participatory
In the documentation process, include everyone from developers to end users.

Integrate documentation into the standard workflow of developers, and seek to reduce silos that solicit documentation from only a subset of the software’s contributors. Developers and engineers are the people with the best access to in-demand information, and getting them to document it will help foster a culture of documentation.

As well, documentation readers (i.e., users) should have clear avenues towards involvement in documentation. A good first step is to give readers the ability to offer feedback in the form of comments or suggestions. Allowing readers to edit documentation directly (e.g., in a wiki) can also be effective but must be weighed against the need and capacity for editorial oversight.

Encourage everyone to become a documentarian!

## Content

[Top of Page](#make-it-easy) | [Return to Readme](../readme.md)

“Content” is the conceptual information within documentation.

Content should be…

- [ARID](#arid)
- [Skimmable](#skimmable)
- [Exemplary](#exemplary)
- [Consistent](#consistent)
- [Current](#current)

### ARID

Accept (some) Repetition In Documentation.

If you want to write good code, Don’t Repeat Yourself. But if you adhere strictly to this DRY principle when writing documentation, you won’t get very far. Some amount of business logic described by your code will need to be described again in your documentation.

In an ideal world, an automated system would generate documentation from the software’s source code, and the system would be smart enough to generate good documentation without any additional input. Unfortunately we do not (yet) live in that world, and today the best documentation is hand-written, which means that just by writing any documentation, you are repeating yourself. Sure, documentation generators exist and are useful, but it’s important to acknowledge that they still require input from humans to function.

The pursuit of minimizing repetition remains valiant! ARID does not mean WET, hence the word choice. It means: try to keep things as DRY as possible but also recognize that you’ll inevitably need some amount of “moisture” to produce documentation.

Cultivating an awareness of this inconvenient truth will hopefully be a helpful step toward reminding developers that a need often exists to update documentation along with code.

### Skimmable

Structure content to help readers identify and skip over concepts which they already understand or see are not relevant to their immediate questions.

Burying concepts in prose and verbiage demands more time from readers seeking answers to specific questions. Save your readers’ time by writing like a newspaper instead of a novel.

Specifically:

Headings — should be descriptive and concise.
Hyperlinks — should surround words which describe the link itself (and never phrases like “click here” or “this page”).
Paragraphs and list items — should begin with identifiable concepts as early as possible.

### Exemplary

Include (some) examples and tutorials in content.

Many readers look first towards examples for quick answers, so including them will help save these people time. Try to write examples for the most common use cases, but not for everything. Too many examples can make the documentation less skimmable. Also, consider separating examples and tutorials from more dense reference information to further help readers skim.

### Consistent

Use consistent language and formatting in content.

The more content editors you have, the more important a style guide becomes in facilitating consistency. Consistency also helps make documentation skimmable and beautiful.

### Current

Consider incorrect documentation to be worse than missing documentation.

When software changes faster than its documentation, the users suffer. Keep it up to date.

Make every effort to write content that is version-agnostic and thus in less need of maintenance. For example, generalize version numbers of software when they occur in tutorials (such as extracting a source code tarball with the version number in the file name).

Be aware as well that some users will remain on older versions of your software, and thus require older versions of your documentation. Proper documentation platforms will accommodate such needs gracefully.

## Sources

[Top of Page](#make-it-easy) | [Return to Readme](../readme.md)

A “source” refers to a system used to store and edit content. Examples of sources include: text files written using reStructuredText or Markdown, HTML content in a CMS database, help text stored within strings in application code, code comments to be assembled later into formalized documentation, and others too.

All sources should be…

- [Nearby](#nearby)
- [Unique](#unique)

### Nearby

Store sources as close as possible to the code which they document.

Give developers systems which allow them to easily make documentation changes along with their code changes. One way is to store documentation content in comment blocks within application source code. Another is to store it in separate text files but within the same repository as the application’s source code. Either way, the goal is merge (as much as possible) the workflows for development and documentation.

### Unique

Eliminate content overlap between separate sources.

Storing content in different sources is okay, as long as the scope of each source is clearly defined and disjoint with other sources. The goal here is to prevent any parallel maintenance (or worse — lack of maintenance) of the same information across multiple sources.


## Publications

[Top of Page](#make-it-easy) | [Return to Readme](../readme.md)

- [Discoverable](#discoverable)
- [Addressable](#addressable)
- [Cumulative](#cumulative)
- [Complete](#complete)
- [Beautiful](#beautiful)

A “publication” refers to a single, cohesive tool that readers use to consume documentation. It may be static or interactive — digital or paper. Multiple publications may be created from a single source (such as web and PDF versions of the same manual). Although rarer, multiple sources may be used to create a single publication. More examples of publications include: API reference, man page, command line ``–help`` output, in-application help tips, online tutorials, internal engineering manuals, and others too.

Each publication should be…

### Discoverable

Funnel users intuitively towards publications through all likely pathways.

Try to identify everywhere the user might go looking for documentation, and in all of those places, insert helpful pointers for them to find it. Documentation need not exist in all of these places, just pointers to it.

If a user manual is published in the woods, and no one is around to read it, does it exist? Discoverability says “no”.

### Addressable

Provide addresses to readers which link directly to content at a granular level.

The ability to reference specific sections deep within a body of documentation facilitates productive communication about the documentation, even with one’s self. These addresses can take the form of URLs, page numbers, or other forms depending on the publication medium. Readers may wish to bookmark certain sections, share them with other users, or provide feedback to the authors. The more granular this ability, and the easier it is to access, the better.

### Cumulative

Content should be ordered to cover prerequisite concepts first.

Can a reader follow your entire body of documentation, linearly, from start to finish without getting confused? If so, the documentation is perfectly “cumulative”, which is great, but not always possible. It’s something to strive for, especially in tutorials and examples. If you have separated your tutorials and examples from the reference documentation, then put the tutorials and examples first. Then, content within the reference information section may be ordered alphabetically or topically without regard to prerequisite needs.

The goal of cumulative ordering is not to encourage readers to consume your documentation linearly — rather it is to help them narrow their search for information when filling in gaps in their knowledge. If a reader arrives with some knowledge of the software and begins reading the documentation at the 25% mark, they are likely to “rewind” when confused.

### Complete

Within each publication, cover concepts in-full, or not at all.

Picture some documentation of software like a map of a neighborhood. If the map displays roads, readers will expect it to display all roads (which exist and are of the same type being displayed). Perhaps the map does not display railroads, for example. Thus, a reader approaching the map to look for railroads will find zero and then seek a different map — but the map is still “complete”, even with this shortcoming. “Complete” does not mean that the map must describe all characteristics of the land. It means simply that, for the characteristics it chooses to describe, it should describe all of them. A map that displays fifty out of one hundred fire hydrants in a neighborhood is worse than a map which displays none.

As a good example, iconv is a command line tool for working with character encodings. Its man page covers all of its available options but none of the possible character encodings accepted as values to these options. Instead, the man page instructs the user to run iconv -l to produce a list of character encodings. In this example, the man page and the list are separate publications, both of which are complete, which is good!

Publishing partially completed documentation must be done cautiously. To avoid misleading readers, make every effort to clearly state, up front, that a particular concept is only covered partially.

### Beautiful

Visual style should be intentional and aesthetically pleasing.

Aesthetics don’t matter to everyone — but (consciously or not) some readers will struggle to find comfort in documentation that lacks attention to visual style. Even in text-only documentation such as --help output, visual style is still present in the form of spacing and capitalization. If visual style is not important to you personally, then consider soliciting stylistic improvements from others for whom it is.

## Body

[Top of Page](#make-it-easy) | [Return to Readme](../readme.md)

A “body” refers to the collection of all the publications within a software project and any of its sub-projects

A documentation body should be…

- [Comprehensive](#comprehensive)

### Comprehensive

Ensure that together, all the publications in the body of documentation can answer all questions the user is likely to have.

We can never create enough documentation to satisfy all questions, however obscure, that might arise from users — but satisfying the likely questions is certainly attainable and thus should be the goal of a body of documentation. “Likely” is admittedly a blurry term, but it’s also relative, which means that a body of documentation which answers very unlikely questions while failing to answer likely ones is somewhat out of balance.

Answering some questions may require the user to read multiple publications, which is okay.

[Top of Page](#make-it-easy) | [Return to Readme](../readme.md)
