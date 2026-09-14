---
title: 1 Clinical Trial Design
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_13_Design_of_Experiments.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_13_Design_of_Experiments.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Clinical Trial Design

**Source:** [`notes/Lecture_13_Design_of_Experiments.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_13_Design_of_Experiments.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

As discussed in Pocock (1979), patient assignment in a clinical trial for the evaluation of one or more new treatments raises several fundamental statistical issues:

- _Size and representation of sample_ A new treatment should be given to a sufficiently large and representative sample of patients in order to make inferences about its effectiveness for the population with a particular disease.

- _Comparative Experimentation_ The results for new treatment(s) need to be compared with a control group of patients receiving a standard treatment (or placebo/no treatment if no effective standard exists).

- _Randomization_ The avoidance of bias in the comparison of treatment groups may best be achieved by adopting some random mechanism for patient assignments.

- _Stratification_ Randomization may need to be restricted in some way to ensure that treatment groups are comparable as regards their pre-treatment state, as summarized by one or more prognostic factors.

In practice, in most clinical trials, patients become available for entry one at a time. Therefore, patient assignment is a developing process requiring careful monitoring rather than an entirely preplanned exercise. There used to be many debates in the light of medical practice:

1. Small trials lead to unreliable conclusions.

2. Phase I trial is aimed at finding an acceptable does schedule with emphasis on toxic effects rather than disease response, thus comparison with other treatments is normally unnecessary. Phase II trial is a screening study to determine whether a treatment has activity worthy of further investigation. Phase III trial is the full scale evaluation of any new treatment, but there used to be many instances where uncontrolled studies took place. Because investigators find less ethical difficulty and quicker results and more frequent, optimistic publications by carrying out uncontrolled studies.

3. Many clinicians find randomization an unnatural interference with individual clinical judgement (Gehan and Freireich, 1974).

Randomization servers as the basis of valid statistical inference, and today it is commonly accepted randomization (with controlled and uncontrolled units) is needed to guarantee the trial result validity.

1

### **1.1 Randomization strategies**

When two treatments are compared in a clinical trial, simple randomization, also called complete randomization, allocates patients randomly into two treatment groups. In medical studies, however, patients arrive subsequently and often need be treated immediately. Hence, the simple randomization (or pure randomization) procedure<sup>1</sup> may suffer from the at least two issues: (1) this simple randomization does not balance patients’ prognostic factors such as age, gender and disease stage that may influence the outcome (although statistical inference remains valid), and (2) sampling variations may lead to unequal sized treatment groups.

Many different randomization methods have been proposed. We now discuss some of the famous ones in the long history.

#### **1.1.1 Covariate-adaptive randomization**

Covariate-adaptive randomization method, which refers to a randomized treatment allocation scheme that depends on covariates or prognostic factors but is conditionally independent of the outcomes, given the covariates used in randomization. We start with introducing some notations.

We consider two-treatment clinical trials. Suppose the patients come to the clinic sequentially and respond to treatments without delay. Let _n_ be the total number of patients under treatments, let _Di ∈{_ 0 _,_ 1 _}_ be the treatment assignment status, _Yi_ ( _t_ ) be the potential outcome, and


be the observed outcome. For patient _i_ , let _Xi_ be a vector of covariates used in the construction of the test procedure, and _Zi_ denotes the covariates or prognostic factors used in covariate-adaptive randomization. Suppose we are interested in a two-sided test


A common characteristic of all covariate-adaptive randomization method is that, given _Zi_ ’s and _Xi_ ’s, _Di_ is independent withs the potential outcomes.

1. **Biased coin method.** Efron (1971) proposed a “biased coin” method that assigns the _i_ th patient to treatment with probability _p >_ 1 _/_ 2 according to:


where _G_ 0 = 0, and _Gi−_ 1 is the difference between the number of patients in treatment 1 and the number of patient in the control after _i −_ 1 assignments have been made. This assignment rule tends to achieve balance between the numbers of patients in two treatment groups, since _p >_ 1 _/_ 2 and _Gi−_ 1

> 1In Pocock (1979), the author mentioned a commonly used method to ensure clinicians do not know treatment assignments in advance is to: Transfer the list of randomly assigned treatment to an ordered set of sealed envelopes; after each patient is entered on trial the investigator opens the next envelope to discover which treatment is to be given to that patient. This system is not infallible and if practicable it may be better to have the randomization list kept in secret by a person not involved with the patients, who is consulted each time an assignment is needed. In multi-centre trials one should have a central assignment office which can be contacted by telephone.

2

is an imbalance metric. Efron (1971) shows that the difference between treatment and control armed patients after _n_ assignments vanishes asymptotically. Note that the biased coin method does not make sure of any covariate, and thus is not a covariate-adaptive randomization method.

2. **Stratified block randomization** of Pocock and Simon (1975) applies block randomization to patients grouped by prognostic factors, are the most popular randomization methods in clinical trials. Advantages of these methods, such as minimizing imbalance between treatment groups, reducing selection bias, minimizing accidental bias and improving efficiency in inference.

Concretely, Pocock and Simon (1975) apply biased coin method in a covariate-adaptive fashion. In a special case, suppose _Zi_ is discrete and takes value _zk k_ = 1 _, . . . , K_ , a special case is to apply the biased coin method within the category of patients with _Zi_ = _zk_ . The motivation is to achieve balance between treatment groups for each prognostic factor. When _Zi_ is a continuous covariate, we can form a discrete function _D_ ( _Zi_ ) and then apply the biased coin method. This method is also called _“covariate-adaptive” biased coin method_ . More generally, Pocock and Simon (1975) generalized the the minimization procedure (Taves, 1974) so as to replace _Gi−_ 1 by


where _j_ is the stratum formed by a prognostic factor.

3. Taves (1974)’s minimization procedure is its special case of Pocock and Simon (1975) with _p_ = 1. Note that one of the oldest covariate-adaptive randomization methods is the _minimization_ procedure proposed by Taves (1974).

Although covariate-adaptive randomization is commonly adopted in medical research, valid statistical testing procedures associated with it are not rigorously studied until the past decade. It is stated in for Proprietary Medicinal Products et al. (2004) that “it remains controversial whether the analysis adequately reflects the randomization scheme.” Two question are of critical importance:

1. Can we develop a test procedure valid under covariate-adaptive randomization?

2. If we use covariate-adaptive randomization and a test procedure under simple randomization, will the Type-I error of the test be inflated?

3. Is a test under covariate-adaptive randomization more powerful than it is under simple randomization?

Rosenberger and Sverdlov (2008) writes “‘Very little theoretical work has been done in this area, despite the proliferation of papers. The original source papers are fairly uninformative about theoretical properties of the procedures.”

Shao et al. (2010) show that if the covariate _Z_ used in covariate-adaptive randomization is a function of the covariates used to construct a test _T_ valid under **any** fixed treatment allocation, then _T_ is valid under covariate-adaptive randomization. But this also says _T_ is a very conservative test given it remains valid under any fixed treatment allocation. Furthermore, Shao et al. (2010) show that two sample t-test is conservative under covariate-adaptive biased coin randomization, which is quite intuitive. Because the averaged potential outcomes are correlated between treatment groups, and the simple t-test ignores this correlation when constructing the test statistics. A less conservative test is carried out via bootstrap. Ma

3

et al. (2015) further provide theoretical foundation of hypothesis testing under covariate-adaptive designs based on linear models.

#### **1.1.2 Response-adaptive randomization**

Response-adaptive randomization procedures are desirable for ethical and efficiency reasons (Hu and Rosenberger, 2003). The key component of the response-adaptive randomization are the allocation proportion. Consider a binary response clinical trial where treatment _A_ is assumed to have probability of success (failure) _pA_ ( _qA_ = 1 _− pA_ ), and treatment _B_ is assumed to have probability of success (failure) _pB_ ( _qB_ = 1 _− pB_ ). It is well known that for fixed sample size _n_ , we can maximize the power of the test


of the simple difference:


Such an allocation ratio _R_ ( _pA, pB_ ), called Neyman allocation, cannot be implemented directly in a clinical trial, because we d not know the values of _pA_ and _pB_ . Even if we could implement Neyman allocation, when _pA_ + _pB >_ 1, we would be assigning more patients to the inferior treatment, which would compromise certain ethical objectives.

Rosenberger et al. (2001) have argued for the criteria that fix the variance of the estimator under an alternative hypothesis, to minimize the expected number of treatment failures. That is, for a binary response trial suing _pA − pB_ as the measure of the treatment effect, the variance of the estimator _p_ � _A − p_ � _B_ is fixed, say equals _K_ :


and the expected number of treatment failtures, _nA_ (1 _− pA_ ) + _nB_ (1 _− pB_ ) is minimized. This optimization problem (!again) leads to the optimal allocation ratio:


Such an allocation deals with both the power objective and the objective favoring the individual patients’ experience.

Although particular allocation ratio may be optimal in terms of power and other criteria, responseadaptive randomization induces correlation among treatment assignments that leads to extra binomial variability when performing inference. This additional variability can have severe adverse effects on power, as has been demonstrated by simulation studies in a number of papers.

#### **1.1.3 Modern adaptive design?**

While classical RCTs are often designed to maximize statistical power to detect clinically relevant differences in treatment outcomes, the objectives of RCTs are modernized in the hope of improving the overall welfare

4

of program participants ( **?** Kasy and Sautmann, 2021) and better incorporating real world evidence ( **??** ). As documented in the literature (Thall and Wathen, 2007), in a clinical trial when a physician favours one treatment over another based on personal experience or published data, it may be more appropriate ethically for that physician to use the favoured treatment, rather than enrolling patients on a randomised trial. Thall and Wathen (2007) provided an example: “Mm. Fornier, I have two possible treatments for your cancer, A and B, but I do not know which is better. So I would like to enroll you in a clinical trial aimed at comparing these treatments to each other. If you agree to enter the trial, your treatment will be chosen by flipping a coin.” This statement reflects the physician’s equipoise, but it also reflects the fact that, outside the scientific community, randomisation is a rather strange idea. Patients entrust physicians with their wellbeing, and sometimes their lives, based on the assumption that physicians are highly knowledgeable and have their patients’ best interests foremost in mind when choosing treatment regimens. Many physicians feel that admitting complete uncertainty, as illustrated above, may damage the bond of trust underlying the physician-patient relationship.

Now, suppose you are a trial designer and facing such dilemmas, what options do you have? To partially answer this question, we will introduce multi-armed bandit problems widely studied in computer science.

---

[Up: contents](index.md) · [2 Multi-arm Bandit →](02-2-multi-arm-bandit.md)
