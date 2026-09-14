---
title: 'AUDIENCE: [INAUDIBLE]'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/ct855rpx8bc-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [INAUDIBLE]

**Source:** `recordings/ct855rpx8bc-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**JEFF GORE: The common motor? AUDIENCE: Yeah, [INAUDIBLE] JEFF GORE: Oh. Well, I'd say that the other class of motors that are seen a lot in the context of these molecular motors are motors that travel along linear tracks. So there's kinesin that walks along microtubules. There are various myosins that walk on actin. And then, of course, DNA and RNA polymerase, we don't normally think of them as motors but indeed, they take an energy fuel and then they have to walk along the template as they make either the DNA or the RNA. So I'd say there are many, many examples of molecular motors that convert chemical energy into mechanical force and motion, particularly along one-dimensional tracks. So those, I think, are the most well-studied examples.**

11

**Now, one way to study this run and tumble motion is, of course, to actually apply a gradient and then watch the cells as they swim it. And that has been done. A lot's been learned from that kind of assay, but it turns out that there are two other assays that maybe allowed for more controlled analysis of this chemotaxis kind of response. So let's just say-- so studying chemotaxis.**

**The most obvious thing is to apply a gradient and then watch. And indeed, the classic assays where you add a little pipette with an attractant or a repellent and watch the bacteria swim toward or away, that demonstrates there is indeed chemotaxis. But it's a little bit difficult to quantify that process in many cases. What are the assays that maybe you've read about recently? In [? Yuri's ?] book, how is it that they actually analyzed this perfect adaptation? Yes?**

**AUDIENCE: So you can bind the flagella on the slide and then [INAUDIBLE]**

**JEFF GORE: So one thing that you can do is you can-- I may put it here. All right. So you can kind of attach the cell to a slide. And typically attach it to the slide by what? This isn't it. And does it matter where you attach the cell to the slide?**

**AUDIENCE: By the flagella.**

**JEFF GORE: Yeah, so you typically have attach it via this hook that's at the end, so by some part of the flagella-- to the slide by the flagella, we'll say. Flagellum? Flagella-- whatever. And the nice thing there is that as the cell is doing its thing and it's spinning either clockwise or counterclockwise, you can directly visualize that because the whole cell is moving.**

**And the cell is both the thing that is doing the work and processing the signals and everything, but it's also your marker for what the state of this little hook is, right? This is a wonderfully quantitative assay where you can get high time resolution. It's easy to do the image analysis. And then, how do you typically get this cell to change its, for example, tumbling frequency?**

**AUDIENCE: Put an attractant.**

12

**JEFF GORE:**

**Right, so you can add an attractant. And indeed, I just wanted to separate this a little bit, because you can-- even without doing this-- this is kind of the next order step-- you can just add an attractant and mix, because you don't want the spatial patterns.**

**But a nice thing here, this is a gradient in space and then you can watch the bacteria swim. But you can also have the gradient in time. And the cells can't tell the difference. The nice thing here is that you can then just add the attractant, mix, and then you just watch all the cells as they're going. You don't need to try to follow them or whatnot, but you can just look to see how the tumbling frequency changes over time. And of course, you would typically use this trick together with this in order to study perfect adaptation and so forth.**

**If you collect this sort of data and you plot the tumbling frequency as a function of time, what you might see is that it starts out at one per second. Now, if at this time, I add an attractant, does the tumbling frequency go up or down? And we're going to do a verbal answer. Ready? Three, two, one.**

**AUDIENCE: Down.**

**JEFF GORE: Down. And that makes sense because the cells think that they're moving up an attractant gradient. So over a very short time scale, tumbling frequency goes down. But then, over a time scale of minutes-- it might be 5, 10 minutes-- that tumbling frequency goes back to where it started. I just want to-- this varies, but this could be order of 10 minutes.**

**AUDIENCE: Why is it so long?**

**JEFF GORE: Yeah.**

**AUDIENCE: 10 minutes is a very long time.**

**JEFF GORE: Yeah, it's a long time scale. And here's a question. Is it because this is the time that it takes to make new protein? New protein synthesis, we'll say.**

**AUDIENCE: You're asking if that's the time or if that's the reason why is it long?**

13

|**JEFF GORE:**|**I'm saying is this the explanation for why this is 10 minutes, because the cell has to**<br>**go make new protein in order to do this? So the cell is presumably going to be**<br>**making some new proteins, but is this what you would really describe as being the**<br>**causative agent of this thing taking 10, 20 minutes? Ready? Three, two, one. All**<br>**right. So I'd say most people are agreeing that actually, yes, it is. The answer is no.**<br>**This is not. It may be the case that the cell is making new protein, but this is not**<br>**what's setting the time scale there. Is--**|
|---|---|
|**AUDIENCE:**|**More [INAUDIBLE]**|
|**JEFF GORE:**|**Right. You agreed that that was the answer, but you didn't-- well, so I would say**<br>**there are several ways you can think about this, but we're going to go through the**<br>**model that is supported by, I think, a fair amount of experimental evidence. But the**<br>**key feature there is that in this model, it works even if all the protein concentrations**<br>**are constant over time. So everything that's happening in this network is happening**<br>**as a result of changes of the states of the protein. So proteins are either getting**<br>**methylated or phosphorylated and these-- right. But then, of course, it's the**<br>**question of, why is it 10 minutes instead of 10 seconds or a minute?**|
|**AUDIENCE:**|**You need a [INAUDIBLE] in there that's on the order of minutes, like 100 minutes,**<br>**which is very slow. Is there--**|
|**JEFF GORE:**|**Yeah, well, their one question is, this is what is called the adaptation time. Now, is**<br>**this a robust feature in this model or in the cells, for that matter? We'll just add**<br>**verbal, yes or no. Ready? Three, two, one,**|
|**AUDIENCE:**|**No.**|
|**JEFF GORE:**|**No. Now, and what that means is that indeed, different kind of versions of this**<br>**network will have different times. And there is data looking at variation in this**<br>**between different cells. And I guess I don't have a clear feeling for what would be**<br>**optimal, in the sense of allowing optimal climbing up of an attractant gradient. This**<br>**thing has to be much longer than the typical times for a tumble. Otherwise, it's not**|


14

**even-- well, we wouldn't have been able to measure it, I guess. But I agree that it could have been one minute and I wouldn't have batted an eye, in the sense that I don't have any feeling for why it had to have been this or something else. But somebody who actually studies this might be able to give a better answer. All right.**

---

[← AUDIENCE](03-audience.md) · [Up: contents](index.md) · [AUDIENCE →](05-audience.md)
