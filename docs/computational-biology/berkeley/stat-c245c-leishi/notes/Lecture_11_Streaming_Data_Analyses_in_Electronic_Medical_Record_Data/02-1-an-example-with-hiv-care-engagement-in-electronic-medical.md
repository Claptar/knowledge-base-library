---
title: 1 An example with HIV care engagement in electronic medical record data
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 An example with HIV care engagement in electronic medical record data

**Source:** [`notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The World Health Organization (WHO) reports that in the treatment of human immunodeficiency virus (HIV) and acquired immunodeficiency syndrome (AIDS), adherence to antiretroviral therapies (ART) varies between 37% and 83% depending on the drug under study, and lifelong ART success, including retention in care, is often undermined by stigma, food insecurity, negative clinic experiences, anticipated or actual side effects, and myriad factors potentially related to poverty (WorldHealthOrganization, 2003).

The increased availability of routinely collected electronic medical record data (EMR) enables the construction of accurate prediction algorithms of non-adherence, which allows us to proactively support patients struggling to comply with HIV care. As more healthcare systems are going through digital transformation and patient EMR information is updated periodically through linked pharmacies, once the prediction algorithm based on EMR data is scalable, it can be integrated into the clinical workflow in an online fashion and be used to identify patients in need of additional support, whether that be counseling or other supportive interventions.

To fully develop a dynamically updated generalizable predictive model using online EMR data, there are

1


Figure 1: Ideal case for EHR prediction problems described in Section 1.

many challenges we face in practice. First, EMR data analysis often encounters privacy constraints in that individual patient data typically cannot be shared across different clinical sites, as breach of privacy arising from data sharing is a growing concern in general for scientific studies (Duan et al., 2018; Cai et al., 2021). Second, non-adherent patients living with chronic conditions may default and reengage in care numerous times over a lifetime, consequently, healthcare adherence is a dynamic process and our prediction algorithms must take this into account. Third, actionable prediction algorithms based on massive EMR need to be scalable and computationally efficient to be incorporated into the clinical workflow. To date, limited work on dynamic risk/health outcome prediction that overcomes above mentioned challenges simultaneously. See a ideal depiction of the clinical workflow in Figure 1.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Online streaming data analysis with continuous outcomes →](03-2-online-streaming-data-analysis-with-continuous-outcomes.md)
