---
title: P3. Protein structure with PyRosetta (6 points).
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/03-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# P3. Protein structure with PyRosetta (6 points).

**Source:** `psets/03-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, you will explore protein structure with PyRosetta, an interactive Python-based interface to the powerful Rosetta molecular modeling suite.

In the following, we will provide instructions on how to complete this problem on Athena’s Dialup Service, where PyRosetta has previously been installed as a module for another class – you may install PyRosetta (http://www.pyrosetta.org/dow) locally on your own computer and complete the problem there, but we will not provide help for installation or operating systemspecific Python issues, so we highly recommend you complete it on Athena.

Log onto Athena’s Dialup Service

(http://kb.mit.edu/confluence/pages/viewpage.action?pageId=3907166), either at a workstation on campus or from a Terminal on your personal machine:

ssh <your Kerberos username>@athena.dialup.mit.edu

Once logged on, load the PyRosetta module with the following 2 commands:

<mark>cd /afs/athena/course/20/20.320/PyRosetta</mark>

<mark>source SetPyRosettaEnvironment.sh</mark>

If you log onto Athena to complete the problem at a future time, you will have to execute these two commands again, otherwise you will get the following error:

ImportError: No module named rosetta

Now, head to the course’s Athena directory, copy the <mark>pyRosetta</mark> _ <mark>materials.zip</mark> folder of files for this problem to your home directory (~), and then unzip it in your home directory with the following commands:

cd /afs/athena/course/7/7.91/sp_2014

<mark>cp pyRosetta_materials.zip ~</mark>

<mark>cd ~</mark>

<mark>unzip pyRosetta_materials.zip</mark>

<mark>cd pyRosetta_materials</mark>

<mark>You should now be able to edit any of these files. Most of the code you’ll need is contained in the script pyRosetta</mark> _ <mark>1YY8.py that you’ll work with below, but for any additional functions you want to use you can reference the PyRosetta documentation:</mark>

<mark>http://graylab.jhu.edu/~sid/pyrosetta/downloads/documentation/PyRosetta_Manual.pdf, particularly Units 2 (Protein Structure in PyRosetta), 3 (Calculating Energies in PyRosetta), and 6 (Side-chain Packing and Design).</mark>

**<mark>(A – 1 point)</mark>** <mark>Go to the Protein Data Bank (http://www.rcsb.org/pdb/home/home.do) and search for the protein we’ll be working with – 1YY8. What is this molecule? By looking at the “3D View” tab of this protein, what is the predominant secondary structure (α-helix or β-sheet)?</mark>

10

1YY8 is Cetuximab (pharmaceutical name), a chimeric mouse/human monoclonal antibody that is an epidermal growth factor receptor (EGFR) inhibitor used for the treatment of metastatic colorectal cancer and head and neck cancer. It is predominantly composed of <mark>β-sheets.</mark>

**<mark>(B – 1 point)</mark>** <mark>In order to open and edit the pyRosetta</mark> _ <mark>1YY8.py file, you will need to use a text editor on Athena’s Dialup Service, which doesn’t register commands from the mouse. If you’re familiar with emacs or vim, these are great options, otherwise we recommend nano, a friendly text editor that can be navigated with the arrow keys. Open the file for editing by typing:</mark>

<mark>nano pyRosetta_1YY8.py</mark>

<mark>You can scroll with the arrow keys, and additional commands are shown at the bottom of the Terminal, where ^ is the Control key. Once you’ve made any changes, to exit and save, type “Control + x” followed by “y” and then Enter to signify yes, you want to save your changes.</mark>

<mark>Look over how the code for part</mark> _ <mark>b() loads the PDB file 1YY8.clean.pdb (which has been cleaned to remove non-atomic annotation information) and prints out the protein’s angles and energy score. Then run the script from the command line with python pyRosetta</mark> _ <mark>1YY8.py (note that it may take up a couple of minutes to load the module the first time you run it; it will also print out many lines of initialization warnings before printing out what is in the code). What is the energy of the structure, and what categories are the primary contributors (weighted score) for and against the total energy? (describe the categories in words as on the lecture slides, not just the shortened names that appear)</mark>


The largest contributor to the structure’s energy is the Van der Waals net attractive energy, and the largest contributor against is Solvation.

11

**(C – 1 point)** <mark>In the code for part</mark> _ <mark>c(), Monte-Carlo side-chain packing is implemented. At the indicated region, add code to print out the post-packed energy score. At the bottom of the script, uncomment part</mark> _ <mark>c() and run the script. What is the energy of the structure after packing, and which two categories have decreased the most compared to part (b)? (describe the categories in words as on the lecture slides, not just the shortened names that appear)</mark>


The Van der Waals net repulsive energy and the Dunbrack rotamer energy have decreased the most compared to part (b).

(Side-chain packing is a stochastic Monte Carlo process in PyRosetta, so you may get a slightly different answer each time)

**(D – 1 point)** The 1YY8.rotated.pdb structure is the same as 1YY8.clean.pdb, except that one residue’s phi or psi angle has been changed. Fill in the code for <mark>part</mark> _ <mark>d() to load the rotated structure and perform side-chain packing on it, printing out the energy of the structure before and after side-chain packing. What is the energy before and after? Why is the post-side-chain packing energy not the same as that of part (c)?</mark>

12


The energy after side-chain packing for the rotated protein is not the same as that of the original protein because side-chain packing only optimizes the side-chain conformations, not the protein backbone (e.g. phi and psi) angles, one of which we know is changed in the rotated protein.

**(E – 1 point)** Add code to <mark>part</mark> _ <mark>e() to determine which angle (phi or psi, as well as which residue number this angle belongs to) is changed in the rotated structure. Which residue/angle is it?</mark>

13


The phi angle of residue 50.

**(F – 1 point)** Using the residue and angle you determined in part (e), add code to <mark>part</mark> _ <mark>f() to determine the energy of the structure with that angle changed to each of the possible angles [-180,-179,….,180]. Which of these angles has the lowest energy, and does this agree with the corresponding angle in the original structure from part (b)?</mark>

<mark>Add each of these energies to the energies</mark> _ <mark>of</mark> _ <mark>angle list, and then modify set</mark> _ <mark>title to include the residue and angle that you changed. If you’ve done this correctly, an energy</mark> _ <mark>vs</mark> _ <mark>angle.pdf plot will be written to the directory where the script is. If you’re at an Athena workstation, you can view this PDF directly (Home Folder > pyRosetta_materials); if you’ve ssh’ed into Athena from a Terminal on your local computer, you can copy this PDF to your local computer and then open it in your computer’s PDF viewer with the following commands using scp (secure copy):</mark>

<mark><in a new Terminal on your computer, cd into your local computer’s directory where you want to download the PDF></mark>

<mark>scp <your Kerberos username>@athena.dialup.mit.edu:~/pyRosetta_materials/e</mark> nergy_vs_angle.pdf .

Using the phi angle of reside 50 that we determined in part (e),

14


The energy minimum occurs at φ = 53° (energy = 505.297). For the original residue 50 angles from the structure in part (b), φ = 52.84, so our φ minimum matches the original structure as expected.


<!-- Start of picture text -->
Energy of 1YY8 by Residue 50 φ  degree<br>250000<br>200000<br>150000<br>100000<br>50000<br>0<br>-50000<br>-200 -150 -100 -50 0 50 100 150 200<br>Angle Degree<br>Energy<br><!-- End of picture text -->

15

---

[← Traceback #3](09-traceback-3.md) · [Up: contents](index.md) · [P4. Queuing theory/connections (4 points). →](11-p4-queuing-theory-connections-4-points.md)
