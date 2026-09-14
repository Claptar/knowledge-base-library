---
title: Experimental Design
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference.Rmd
source_file: sources/gtpb-psls20/theory/05-statisticalInference.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Experimental Design

**Source:** [`theory/05-statisticalInference.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- 15 patients were drawn at random from the population of patients with hypertension
- pre-test/post-test design: the systolic and diasystolic blood pressure are measured before and after administering captopril
- Advantage: we can assess the effect of administering captopril on the blood pressure for each individual patient.
- Disadvantage?

```r
if ("pi"%in%ls()) rm("pi")
kopvoeter<-function(x,y,angle=0,l=.2,cex.dot=.5,pch=19,col="black")
{
angle=angle/180*pi
points(x,y,cex=cex.dot,pch=pch,col=col)
lines(c(x,x+l*cos(-pi/2+angle)),c(y,y+l*sin(-pi/2+angle)),col=col)
lines(c(x+l/2*cos(-pi/2+angle),x+l/2*cos(-pi/2+angle)+l/4*cos(angle)),c(y+l/2*sin(-pi/2+angle),y+l/2*sin(-pi/2+angle)+l/4*sin(angle)),col=col)
lines(c(x+l/2*cos(-pi/2+angle),x+l/2*cos(-pi/2+angle)+l/4*cos(pi+angle)),c(y+l/2*sin(-pi/2+angle),y+l/2*sin(-pi/2+angle)+l/4*sin(pi+angle)),col=col)
lines(c(x+l*cos(-pi/2+angle),x+l*cos(-pi/2+angle)+l/2*cos(-pi/2+pi/4+angle)),c(y+l*sin(-pi/2+angle),y+l*sin(-pi/2+angle)+l/2*sin(-pi/2+pi/4+angle)),col=col)
lines(c(x+l*cos(-pi/2+angle),x+l*cos(-pi/2+angle)+l/2*cos(-pi/2-pi/4+angle)),c(y+l*sin(-pi/2+angle),y+l*sin(-pi/2+angle)+l/2*sin(-pi/2-pi/4+angle)),col=col)
}

par(mar=c(0,0,0,0),mai=c(0,0,0,0))
plot(0,0,xlab="",ylab="",xlim=c(0,10),ylim=c(0,10),col=0,xaxt="none",yaxt="none",axes=FALSE)
rect(0,6,10,10,border="red",lwd=2)
text(.5,8,"population",srt=90,col="red",cex=2)
symbols (3, 8, circles=1.5, col="red",add=TRUE,fg="red",inches=FALSE,lwd=2)
grid=seq(0,1.3,.01)

for (i in 1:50)
{
	angle1=runif(n=1,min=0,max=360)
	angle2=runif(n=1,min=0,max=360)
	radius=sample(grid,prob=grid^2*pi/sum(grid^2*pi),size=1)
	kopvoeter(3+radius*cos(angle1/180*pi),8+radius*sin(angle1/180*pi),angle=angle2)
}
text(7.5,8,"Effect of captopril in population",col="red",cex=1.2)

rect(0,0,10,4,border="blue",lwd=2)
text(.5,2,"sample",srt=90,col="blue",cex=2)
symbols (3, 2, circles=1.5, col="red",add=TRUE,fg="blue",inches=FALSE,lwd=2)
for (i in 0:2)
	for (j in 0:4)
{

	kopvoeter(2.1+j*(3.9-2.1)/4,1.1+i)
}
text(7.5,2,"Effect of captopril in sample",col="blue",cex=1.2)

arrows(3,5.9,3,4.1,col="black",lwd=3)
arrows(7,4.1,7,5.9,col="black",lwd=3)
text(1.5,5,"EXP. DESIGN (1)",col="black",cex=1.2)
text(8.5,5,"ESTIMATION &\nINFERENCE (3)",col="black",cex=1.2)
text(7.5,.5,"DATA EXPLORATION &\nDESCRIPTIVE STATISTICS (2)",col="black",cex=1.2)
```

---

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Data exploration and Descriptive Statistics →](03-data-exploration-and-descriptive-statistics.md)
