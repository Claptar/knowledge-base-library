---
title: Bayesian Networks
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bayesian Networks

**Source:** `recitations/2014-04-09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- The directed graph consists of:

   - Nodes   = random variables (events)

   - Edges indicate dependencies between variables

- Then the distribuPon of a random variable _depends   only   on its parent   nodes_ : **Parent and child nodes** : if there is directed edge starPng from _i_ and ending at _j_ , then _i_ is a parent of _j_ and

- <u>A Bayesian network with 4 nodes</u> _j_ is a child of _i_


-­‐ **C** has parent **B** , **B** has child **C**

- **-­‐ A** has parents **B** and **D**

**Root nodes** = nodes with no parents (no incoming edges) – here **B** and **D Leaf nodes** = nodes with no children

– here **A** and **C**

<u>Need the following probabiliPes to fully specify the model:</u>

- -­‐ Prior probabiliPes of all root nodes = P(B) and P(D) -­‐ CondiPonal prob. of all child nodes given parents = P(C|B) and P(A|B,D)

9

## Independencies   in   Bayesian   Networks

There   are   3   types   of   connec'ons   that   can   occur   between   a   random variable _B_ and   its   immediate   neighbors _A_ and _C_ :

### **<u>Linear</u>**


Factor   P(A,B,C)   according   to   the independencies   indicated   in   this   graph: P(A,B,C)   =   P(A)P(B|A)P(C|B)

Are   A   and   C   independent   if   B   is   unknown? **No** –   if   B   is   unknown,   then   knowing   A   tells us   something   about   C   (through   unknown   B) Are   A   and   C   independent   if   B   is   known? **Yes** –   if   B   is   known,   there   is   no   further informa'on   in   A   about   C

10

## ������������������������������������

���������������������������������������������������������������� ��������� _�_ ����������������������������� _�_ ����� _�_ ��

**<u>���������</u>**


<!-- Start of picture text -->
�<br><!-- End of picture text -->


<!-- Start of picture text -->
� �<br><!-- End of picture text -->

### �����������������

**��** ����������������������� ���� **�** ����� **�** ���������

������������ �������������������� ���������

��������������������������������� ���������������������������������������� ����������������������������

���������������������������������������� **��** ����������������������������������������� �����������������������������������������

�������������������������������������� **���** �������������������������������������� ��������������������������������������

11

## Independencies   in   Bayesian   Networks

There   are   3   types   of   connec'ons   that   can   occur   between   a   random variable _B_ and   its   immediate   neighbors _A_ and _C_ :

**����������**


<!-- Start of picture text -->
� �<br>�<br><!-- End of picture text -->

- Example   of   this: **A** and **C** are   two independent   coin flips, **B** checks

- whether   the   resul'ng values   are   the   same

Factor   P(A,B,C)   according   to   the independencies   indicated   in   this   graph: P(A,B,C)   =   P(A)P(C)P(B|A,C)

Are   A   and   C   independent   if   B   is   unknown? **Yes** –   if   B   is   unknown,   then   knowing   A   tells us   nothing   about   C

- Are   A   and   C   independent   if   B   is   known?

- **No** –   if   B   is   known,   it   tells   us   something

- about   both   A   and   C,   so   A   and   C   are   no longer   independent

12

## ������������������������������������

**<u>�����������</u>** ���������������������������������������� ����������������������������������������� � � ����������������������������� ����������������� _P_ ( _A, C_ ) = _P_ ( _A_ ) _P_ ( _C_ ) � _P_ ( _A, C_ ) = _P_ ( _A, B, C_ ) ������������������� � _B_

= _P_ ( _A_ ) _P_ ( _C_ ) _P_ ( _B|A, C_ ) � _B_ � = _P_ ( _A_ ) _P_ ( _C_ ) _P_ ( _B|A, C_ ) � _B_

= _P_ ( _A_ ) _P_ ( _C_ )

13

---

[← Bayesian Networks](07-bayesian-networks.md) · [Up: contents](index.md) · [Bayesian Networks →](09-bayesian-networks.md)
