---
title: 4 Collaboration
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/millman-perez.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/section/millman-perez.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Collaboration

**Source:** [`section/millman-perez.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/millman-perez.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Open source developers build on one another’s work just as scientists build on each other’s work. Since development communities are geographically spread and often dependent on contributions from volunteers, there has been careful attention paid to efficient and productive tools and processes for managing collaborations. As scientific practice becomes increasingly computational, it is imperative that we learn from the collaborative practices used in the open source world.

### **4.1 Distributed version control**

Earlier we discussed how version control system (VCS) should be the foundation of a reproducible research workflow, even for a single investigator working in isolation. But the true power of these systems comes when collaborating with others. Modern systems such as Git and Mercurial were designed from the ground up for large-scale distributed collaboration: Git was written by Linus Torvalds, the creator of the Linux kernel, to coordinate its development. The Linux kernel is arguably the largest and most complex open source development project today: version 3.7 of the kernel included roughly 12,000 distinct sets of changes affecting over 1,100,000 lines of code by nearly 1,300 individual contributors.<sup>25</sup> Git’s entire design aims to make collaboration on this scale smooth and efficient, and it succeeds admirably. Scientists can benefit from this power as well for any project that requires collaboration, whether it is the development of an open source research code or the writing of a manuscript or grant proposal with multiple authors.

Git and other tools like it are called _distributed_ version control systems (DVCS) because they don’t depend on a central server for their functioning, instead maintaining the entire history of a project inside every repository. This is in contrast to legacy systems such as CVS and SVN, that made a distinction between the “working copy” that users would work on and which contained only the most recent version of files, and a special repository hosted on a central server that had the entire project history. The centralized model does enable collaboration, but it also creates a number of problems that the distributed model addresses. In a DVCS there is no single point of failure, as every repository carries all the project history and therefore serves as an automatic backup.

More importantly, a DVCS enables anyone who can _clone_ a repository (the term used to indicate getting a full copy of an existing repository to start new work off of it) to develop their own history with new commits, even if they don’t have write permission to the original source from where the repository was cloned. This means that once you have a clone of a repository (which could be someone else’s or yours from a different computer), you can start working on that copy and building new history even if you are disconnected from the original system, such as when working on a plane or train without network access. If at a later stage you decide to merge your new history with the original repository, the merge capabilities in all DVCS make this straightforward.

This model of cloning an existing repository, building new history in isolation and then merging it back into a common history, is the basis for how these systems enable fluid collaboration. When the time comes for a merge operation, DVCS can communicate the necessary changes even via email attachments, but the simplest way to do so is to have a special repository<sup>26</sup> in a common location that all parties have access to and where the changes are

> 25 `http://lwn.net/Articles/526748`

> 26We note that this central repository does not change the distributed nature of the process: while it plays

16

_pushed_ . Pushing, as the term suggests, means sending the set of changes from one repository into another; once the changes have been put into this central repository, all parties can _pull_ them into their personal copies to synchronize their states and continue working again. So in practice, the simplest and most common collaboration workflow with a DVCS is one where each person has a copy they develop on, and they all connect in a star topology to a central node where a shared copy exists that is used for synchronization.

### **4.2 Code review**

In recent years, a number of web services have appeared that play the role of this central node; the most popular of them by far is GitHub,<sup>27</sup> but others such as BitBucket<sup>28</sup> and Gitorious<sup>29</sup> play similar roles. GitHub has had a tremendous impact in the open source community, reaching in a few years millions of active users and gaining rapidly popularity in scientific circles. We can attest to the power of this platform with our own experience: IPython moved its development to GitHub in early 2010 and immediately saw a rapid uptick in the pace of contributions. The workflow for collaboration enabled by GitHub was so much smoother than all previously available tools that many people were more willing to send contributions, while the core team was able to review and integrate these contributions at a much more rapid pace.

The core element of the collaborative process on GitHub is known as a _pull request_ , and it is something akin to a public peer review of a set of changes to a manuscript. Let us illustrate how it works with a simple example: Alice wants to contribute to IPython, a project available on GitHub<sup>30</sup> but to which she does not have write access. She can do so by getting her own personal copy of the IPython Git repository where she makes all the changes she wants, and once she is ready to share them with the IPython team she can publish them on her GitHub user account.<sup>31</sup> At that point, she can click on a button to create a pull request for these changes: this contacts the IPython developers and creates a special page on the website that summarizes her changes as well as allowing everyone to begin a discussion about the changes. This discussion page allows the developers to ask Alice questions (even making comments on specific lines of her new code), and she can respond to these questions, update her code with new commits in order to address any required improvements, etc. Once the IPython developers are satisfied with this review and discussion (which may happen immediately or may require a lengthy back-and-forth process, depending on the changes), they can apply the changes to the official IPython repository with a click of a button. Once the changes are merged, they become part of the official project source and every individual commit that was merged is credited to Alice from the time she made it while she was working on her personal copy. Furthermore, even closed pull requests remain available on the website to inform future discussions, making the entire collaboration process an open one.<sup>32</sup>

> a special role for purposes of _synchronization_ , the central repository is otherwise completely symmetrical to everyone’s personal copy in the information it holds, and can be replaced at any time in case it is lost or damaged from anyone’s copy.

> 27 `http://github.com`

> 28 `http://bitbucket.org`

> 29 `http://gitorious.org`

> 30 `http://github.com/ipython`

> 31 `http://gitub.com/alice/ipython` if her GitHub user name is `alice` for example

> 32 `http://github.com/ipython/ipython/pull/1732` is an example pull request and the entire, recorded review process.

17

The pull request process allows for a dynamic and open peer review process of all proposed changes to a project. The only special role that the official project authors have is the ability to approve the final merging of new changes, but otherwise everyone participates on an equal footing in terms of access to tools. This highly symmetrical structure proves to be extremely beneficial in encouraging a meritocratic process of contribution and review, where there are few points of special authority and where the discussions can remain focused around the contribution that initiated the pull request. Paraphrasing how some of the GitHub employees describe the process in public presentations: “a pull request is a conversation that starts with code.”

From a scientific research perspective, we should consider these ideas in a broader context that goes beyond code: while peer review is one of the pillars of how the scientific community moves forward, in practice modern scientific peer review is often an opaque, arbitrary, and limited process. The open, dynamic, and ongoing process of peer review enabled by the GitHub pull request system (or the equivalent ones that exist on similar services) stands in sharp contrast to some of our institutional traditions, and the scientific community could benefit significantly from adopting these ideas in our own review practices [11].

It is worth noting that by using a DVCS, authors can maintain private branches in the context of a publicly available project; this can be useful if new work needs to be developed in private prior to publication and subsequent public release. By tracking the public repository but keeping a private branch, they can maintain exclusive access to their new work until it is published, while continuing to develop the openly accessible code with the rest of the scientific community. Once the code is ready to be made public, the new contributions can be seamlessly merged with the public version and their entire provenance (including information such as time of invention and individual credit within the lab) becomes available for inspection. This simple observation shows how these tools can be used to balance the sometimes valid requests for privacy that may exist in a research environment with the desire for subsequent disclosure and publication, without losing any of the benefits of version control with regard to attribution and provenance tracking.

### **4.3 Infrastructure redux**

Once we have adopted tools that allow for distributed collaboration (e.g., Git and GitHub) and our computational machinery has tests and scripts that allow for automated installation and execution of the test suite, we achieve a number of important benefits that we can think of as _machine collaboration_ . That is, once we have described in a standard way how our software must be installed or tested, then not only can our colleagues do that as they start collaborating with us, but so can machines. The Travis CI system, for example, can be configured to automatically run a project’s test suite on every pull request created on GitHub. This means that when the humans come to review the proposed code, a report is already attached to the pull request that indicates whether the test suite passed or not (and provides details of any failures). This can save enormous amounts of time and make the collaboration much smoother, as reviewers don’t need to wait before starting a new review for the tests to complete on their system, and may even review when they are away from a development machine capable of actually running the tests. In the IPython project we have seen the value of having this information always ready, as it reduces the small but persistent amount of ‘friction’ we had before when each reviewer was responsible for running all tests first locally for each new pull request. While we still have tools for that and occasionally run tests

18

beyond what Travis does (as Travis doesn’t install every optional library we require), saving even five minutes for each review can make a huge difference for a project that sometimes has to process multiple pull requests in a day.

In a similar vein, the ReadTheDocs<sup>33</sup> project does for documentation what Travis does for CI. ReadTheDocs hosts documentation built with Sphinx, but more importantly, can be configured to automatically build it when new commits are made to the project at GitHub. In this way, users can always find a fully updated build of the project documentation without developers having to spend time on this.

Automated CI testing and documentation building are only two aspects of the benefits that can be gained from building on a foundation of distributed version control, well automated processes, integrated test suites, and documentation generation. Once all these elements come together, a virtuous cycle can be sustained where the focus of the scientists or developers can be on producing new results (be they text, code, or computational outputs) and this machinery ensures that everything is validated and documented along the way.

While some of these points are more easily applied in the context of pure software development, the critical thing is how these ideas and tools work in concert to produce an environment of robust, reproducible results. Adopting this viewpoint, it is always possible to adapt to the specifics of any given project and apply only what is relevant. We conclude noting that the practices, tools, and ideas described in the previous two sections ( _§_ 3 and _§_ 4) may be put to use relatively quickly, but writing high-quality, trustworthy, scientific code is not easy. Mastery and expertise in developing reliable code that can be trusted to provide valid results takes sustained focus and deliberate practice.<sup>34</sup>

---

[← 3 Routine practice](04-3-routine-practice.md) · [Up: contents](index.md) · [5 Communication →](06-5-communication.md)
