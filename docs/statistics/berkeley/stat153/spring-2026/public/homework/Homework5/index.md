---
title: Stat 153/248 - Homework 5 - YOUR NAME HERE
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf
source_file: sources/berkeley-stat153/spring-2026/public/homework/Homework5.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat 153/248 - Homework 5 - YOUR NAME HERE

**Source:** [`public/homework/Homework5.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Split into 30 sections.

1. [Stat 153/248 - Homework 5 - YOUR NAME HERE](01-stat-153-248---homework-5---your-name-here.md)
2. [Apply it to a batch of 2 univariate signals of length 10](02-apply-it-to-a-batch-of-2-univariate-signals-of-length-10.md)
3. [Before running the lines below, predict](03-before-running-the-lines-below-predict.md)
4. [1. What output shape do you expect if kernelsize is 5 instead of 3?](04-1-what-output-shape-do-you-expect-if-kernelsize-is-5-instead.md)
5. [2. What if you add padding=2 (with kernelsize=5)?](05-2-what-if-you-add-padding-2-with-kernelsize-5.md)
6. [3. What if the input has 3 channels instead of 1 (so x.shape = (2, 3, 10](06-3-what-if-the-input-has-3-channels-instead-of-1-so-x-shape-2.md)
7. [with kernelsize=3 and outchannels=4? How many weights does the laye](07-with-kernelsize-3-and-outchannels-4-how-many-weights-does-th.md)
8. [Uncomment one block at a time after making your prediction.](08-uncomment-one-block-at-a-time-after-making-your-prediction.md)
9. [(1) kernelsize=5](09-1-kernelsize-5.md)
10. [print('\nkernelsize=5, padding=0, stride=1, length=10')](10-print-nkernelsize-5-padding-0-stride-1-length-10.md)
11. [layer2 = nn.Conv1d(1, 4, kernelsize=5)](11-layer2-nn-conv1d-1-4-kernelsize-5.md)
12. [print(layer2(torch.randn(2, 1, 10)).shape)](12-print-layer2-torch-randn-2-1-10-shape.md)
13. [(2) kernelsize=5, padding=2](13-2-kernelsize-5-padding-2.md)
14. [print('\nkernelsize=5, padding=2, stride=1, length=10')](14-print-nkernelsize-5-padding-2-stride-1-length-10.md)
15. [layer3 = nn.Conv1d(1, 4, kernelsize=5, padding=2)](15-layer3-nn-conv1d-1-4-kernelsize-5-padding-2.md)
16. [print(layer3(torch.randn(2, 1, 10)).shape)](16-print-layer3-torch-randn-2-1-10-shape.md)
17. [(3) inchannels=3](17-3-inchannels-3.md)
18. [print('\ninputchannels=3, kernelsize=3, padding=0, stride=1, length=10')](18-print-ninputchannels-3-kernelsize-3-padding-0-stride-1-lengt.md)
19. [layer4 = nn.Conv1d(3, 4, kernelsize=3)](19-layer4-nn-conv1d-3-4-kernelsize-3.md)
20. [print(layer4(torch.randn(2, 3, 10)).shape)](20-print-layer4-torch-randn-2-3-10-shape.md)
21. [print("\nn weight params:", layer4.weight.numel())](21-print-nn-weight-params-layer4-weight-numel.md)
22. [Print output shape](22-print-output-shape.md)
23. [Print weight tensor shape](23-print-weight-tensor-shape.md)
24. [Print total number of weights](24-print-total-number-of-weights.md)
25. [Expected (by hand)](25-expected-by-hand.md)
26. [conv1 weight: 11632 = 512, bias: 16 -> 528](26-conv1-weight-11632-512-bias-16---528.md)
27. [conv2 weight: 16323 = 1536, bias: 32 -> 1568](27-conv2-weight-16323-1536-bias-32---1568.md)
28. [conv3 weight: 32643 = 6144, bias: 64 -> 6208](28-conv3-weight-32643-6144-bias-64---6208.md)
29. [fc weight: 6410 = 640, bias: 10 -> 650](29-fc-weight-6410-640-bias-10---650.md)
30. [Homework5 Part 30 —](30-homework5-part-30.md)

---

[Up: contents](../../../index.md)
