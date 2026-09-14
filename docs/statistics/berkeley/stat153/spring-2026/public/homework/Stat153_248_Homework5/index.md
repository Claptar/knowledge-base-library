---
title: Stat 153/248 - Homework 5 - YOUR NAME HERE {-}
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_248_Homework5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Stat 153/248 - Homework 5 - YOUR NAME HERE {-}

**Source:** [`public/homework/Stat153_248_Homework5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Split into 34 sections.

1. [Stat 153/248 - Homework 5 - YOUR NAME HERE {-}](01-stat-153-248---homework-5---your-name-here.md)
2. [Build the layer from the worked example](02-build-the-layer-from-the-worked-example.md)
3. [Apply it to a batch of 2 univariate signals of length 10](03-apply-it-to-a-batch-of-2-univariate-signals-of-length-10.md)
4. [---- Predict-then-verify ----](04------predict-then-verify.md)
5. [Before running the lines below, predict](05-before-running-the-lines-below-predict.md)
6. [1. What output shape do you expect if kernelsize is 5 instead of 3?](06-1-what-output-shape-do-you-expect-if-kernelsize-is-5-instead.md)
7. [2. What if you add padding=2 (with kernelsize=5)?](07-2-what-if-you-add-padding-2-with-kernelsize-5.md)
8. [3. What if the input has 3 channels instead of 1 (so x.shape = (2, 3, 10)),](08-3-what-if-the-input-has-3-channels-instead-of-1-so-x-shape-2.md)
9. [with kernelsize=3 and outchannels=4? How many weights does the layer have now?](09-with-kernelsize-3-and-outchannels-4-how-many-weights-does-th.md)
10. [Uncomment one block at a time after making your prediction.](10-uncomment-one-block-at-a-time-after-making-your-prediction.md)
11. [(1) kernelsize=5](11-1-kernelsize-5.md)
12. [print('\nkernelsize=5, padding=0, stride=1, length=10')](12-print-nkernelsize-5-padding-0-stride-1-length-10.md)
13. [layer2 = nn.Conv1d(1, 4, kernelsize=5)](13-layer2-nn-conv1d-1-4-kernelsize-5.md)
14. [print(layer2(torch.randn(2, 1, 10)).shape)](14-print-layer2-torch-randn-2-1-10-shape.md)
15. [(2) kernelsize=5, padding=2](15-2-kernelsize-5-padding-2.md)
16. [print('\nkernelsize=5, padding=2, stride=1, length=10')](16-print-nkernelsize-5-padding-2-stride-1-length-10.md)
17. [layer3 = nn.Conv1d(1, 4, kernelsize=5, padding=2)](17-layer3-nn-conv1d-1-4-kernelsize-5-padding-2.md)
18. [print(layer3(torch.randn(2, 1, 10)).shape)](18-print-layer3-torch-randn-2-1-10-shape.md)
19. [(3) inchannels=3](19-3-inchannels-3.md)
20. [print('\ninputchannels=3, kernelsize=3, padding=0, stride=1, length=10')](20-print-ninputchannels-3-kernelsize-3-padding-0-stride-1-lengt.md)
21. [layer4 = nn.Conv1d(3, 4, kernelsize=3)](21-layer4-nn-conv1d-3-4-kernelsize-3.md)
22. [print(layer4(torch.randn(2, 3, 10)).shape)](22-print-layer4-torch-randn-2-3-10-shape.md)
23. [print("\nn weight params:", layer4.weight.numel())](23-print-nn-weight-params-layer4-weight-numel.md)
24. [Solution for Q6](24-solution-for-q6.md)
25. [Print output shape](25-print-output-shape.md)
26. [Print weight tensor shape](26-print-weight-tensor-shape.md)
27. [Print total number of weights](27-print-total-number-of-weights.md)
28. [Solution for Q7](28-solution-for-q7.md)
29. [Expected (by hand)](29-expected-by-hand.md)
30. [conv1 weight: 11632 = 512, bias: 16 -> 528](30-conv1-weight-11632-512-bias-16---528.md)
31. [conv2 weight: 16323 = 1536, bias: 32 -> 1568](31-conv2-weight-16323-1536-bias-32---1568.md)
32. [conv3 weight: 32643 = 6144, bias: 64 -> 6208](32-conv3-weight-32643-6144-bias-64---6208.md)
33. [fc weight: 6410 = 640, bias: 10 -> 650](33-fc-weight-6410-640-bias-10---650.md)
34. [Stat153 248 Homework5 Part 34 —](34-stat153-248-homework5-part-34.md)

---

[Up: contents](../../../index.md)
