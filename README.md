<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1200&color=6C63FF&center=true&vCenter=true&width=750&lines=OEIS%20A181671%20%26%20A190502%20Published%20Extensions%3BRamanujan%20primes%20to%2010%5E23%20%26%202%5E72%20on%20a%20laptop%3BDROSOMIND%3A%20Live%20Fruit%20Fly%20Connectome%20Simulator%20%28Cell%202026%29%3BTurning%20equations%20into%20things%20you%20can%20watch%20move%3BBSc%28Hons.%29%20Data%20Science%20%26%20AI%2C%20IIT%20Guwahati" alt="typing banner" />

<a href="https://realgauravvyas.github.io/"><img src="https://img.shields.io/badge/portfolio-what%20survives%20the%20sieve-FFC14D?style=for-the-badge&labelColor=0D1117" alt="Portfolio" /></a>
<a href="https://realgauravvyas.github.io/assets/Gaurav_Vyas_Resume.pdf"><img src="https://img.shields.io/badge/resume-PDF-E55039?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white&labelColor=0D1117" alt="Resume PDF" /></a>
<a href="https://www.socialpsychology.org/member/gaurav-vyas"><img src="https://img.shields.io/badge/personal%20website-social%20psychology%20network-4B6584?style=for-the-badge&labelColor=0D1117" alt="Personal Website - Social Psychology Network" /></a>
<a href="https://oeis.org/A181671"><img src="https://img.shields.io/badge/OEIS%20A181671-a(18)--a(23)%20published-6C63FF?style=for-the-badge&labelColor=0D1117" alt="OEIS A181671" /></a>
<a href="https://oeis.org/A190502"><img src="https://img.shields.io/badge/OEIS%20A190502-a(57)--a(72)%20published-00b894?style=for-the-badge&labelColor=0D1117" alt="OEIS A190502" /></a>
<a href="https://realgauravvyas.github.io/drosomind/"><img src="https://img.shields.io/badge/DROSOMIND-3D%20Connectome%20Live-FF007F?style=for-the-badge&labelColor=0D1117" alt="DROSOMIND" /></a>
<a href="https://realgauravvyas.github.io/mathematical-surprises/"><img src="https://img.shields.io/badge/live-250%2B%20visualizations-00E6C8?style=for-the-badge&labelColor=0D1117" alt="Mathematical Surprises" /></a>

</div>

# Gaurav Vyas

I build things where the math is the point, not the plumbing — and then I make sure
you can *see* it happen, not just read about it.

**BSc(Hons.) Data Science & AI**, IIT Guwahati · **PG Diploma in Applied Statistics**,
ISI Kolkata. Most of what's below started as *"is this actually true?"* and turned into
a repo. Two of them turned into official extensions in the OEIS.

🌐 **Personal Website & Academic Profile:** [socialpsychology.org/member/gaurav-vyas](https://www.socialpsychology.org/member/gaurav-vyas) &bull; 📄 **Resume:** [Gaurav_Vyas_Resume.pdf](https://realgauravvyas.github.io/assets/Gaurav_Vyas_Resume.pdf)

<div align="center">

### 🔶 [**realgauravvyas.github.io**](https://realgauravvyas.github.io/)

Twenty-two projects and experiments, indexed by the Ramanujan primes that survive a real sieve running in
your browser. Click a gold number, land on the work — including the OEIS entries below,
the AES key I pulled out of power traces, and the chess result I didn't want.

</div>

---

### 📐 In the OEIS

Two sequence extensions I computed have been accepted and published in the
**On-Line Encyclopedia of Integer Sequences (OEIS)**:

- **[OEIS A181671](https://oeis.org/A181671)** (Base 10) — The count of Ramanujan primes below powers of ten.
  Extended the table from 10¹⁷ out to **10²³** (accepted 15 Aug 2026, `a(18)-a(23) from Gaurav Vyas`).
  The [b-file](https://oeis.org/A181671/b181671.txt) now runs `n = 1..23`.

- **[OEIS A190502](https://oeis.org/A190502)** (Base 2) — The count of Ramanujan primes below powers of two ($2^n$).
  Extended the table from $n=56$ out to **2⁷²** (approved by editor Joerg Arndt on 13 Sep 2026).
  The official [b-file](https://oeis.org/A190502/b190502.txt) now runs through $n=72$, and the OEIS entry directly links to
  [ramanujan-primes-beyond-2-56](https://github.com/realgauravvyas/ramanujan-primes-beyond-2-56).

Both were computed entirely on a consumer laptop and desktop — no institute, no cluster — with a 128-bit segmented sieve, bracketed analytic tail bounds, and machine-checkable certificates behind every term.

| Published Sequence | Base / Domain | Previous Record | Extended &amp; Published Record (Gaurav Vyas) | Status | Verification &amp; Source |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **[OEIS A181671](https://oeis.org/A181671)** | Base 10 ($10^n$) | $10^{17}$ | **$10^{23}$** (`a(18)–a(23)`) | **Published** (Aug 2026) | [Official b-file](https://oeis.org/A181671/b181671.txt) &bull; [GitHub Repo](https://github.com/realgauravvyas/ramanujan-primes-beyond-1e19) |
| **[OEIS A190502](https://oeis.org/A190502)** | Base 2 ($2^n$) | $2^{56}$ | **$2^{72}$** (`a(57)–a(72)`) | **Published** (Sep 2026) | [Official b-file](https://oeis.org/A190502/b190502.txt) &bull; [GitHub Repo](https://github.com/realgauravvyas/ramanujan-primes-beyond-2-56) |

```text
Definition : Rₙ is the smallest integer such that π(x) - π(x/2) ≥ n for all x ≥ Rₙ
Technique  : 128-bit Segmented Sieve of Eratosthenes + Bracketed Analytic Tail Bounds
Execution  : High-performance C++20 / Python with independent mathematical certificates
```

```
while (curious) {
    pick_an_equation();
    make_it_move();
    ask("why is this surprising?");
}
```

---

### 🔭 Live Interactive Simulations & Experiments

<p align="center">
  <a href="https://realgauravvyas.github.io/drosomind/">
    <img src="https://raw.githubusercontent.com/realgauravvyas/drosomind/main/assets/screenshots/dashboard_split_view.png" alt="DROSOMIND Live Connectome Simulator" width="100%" />
  </a>
</p>

<p align="center">
  <b>🪰 <a href="https://realgauravvyas.github.io/drosomind/">DROSOMIND — Live In-Silico Connectome Organism</a></b><br>
  <i>Dual Split View: 3D Connectome (166k neurons, 125M synapses) paired with an articulated Drosophila melanogaster model &amp; real-time LIF neural dynamics (inspired by Google Research &amp; HHMI Janelia, Cell 2026).</i>
</p>

| 🪰 **[DROSOMIND Simulator](https://realgauravvyas.github.io/drosomind/)** | 🌀 **[Mathematical Surprises](https://realgauravvyas.github.io/mathematical-surprises/)** | 🔶 **[What Survives The Sieve](https://realgauravvyas.github.io/)** | 🌱 **[CarbonCampus PWA](https://realgauravvyas.github.io/carboncampus/)** |
| :---: | :---: | :---: | :---: |
| 166k neurons &middot; 125M synapses &middot; 3D fly organism | 250+ live interactive simulations with real-time sliders | Live in-browser Sieve of Eratosthenes indexing 12 projects | Offline-first campus carbon calculator (Avinya 2026) |
| [Launch Simulator ↗](https://realgauravvyas.github.io/drosomind/) | [Explore 250+ Visuals ↗](https://realgauravvyas.github.io/mathematical-surprises/) | [Visit Live Portfolio ↗](https://realgauravvyas.github.io/) | [Open Web App ↗](https://realgauravvyas.github.io/carboncampus/) |

---

### 🧭 What I'm building

**Mathematics & number theory**

| | |
|---|---|
| 🔢 **[ramanujan-primes-beyond-1e19](https://github.com/realgauravvyas/ramanujan-primes-beyond-1e19)** | The A181671 extension: a(18)–a(23) published in OEIS — paper, C++/Python sieve, and certificates |
| ⚡ **[ramanujan-primes-beyond-2-56](https://github.com/realgauravvyas/ramanujan-primes-beyond-2-56)** | The base-2 sibling: a(57)–a(72) of A190502 accepted and published in the OEIS through 2⁷² |
| 🌀 **[mathematical-surprises](https://github.com/realgauravvyas/mathematical-surprises)** | A live gallery of interactive math & physics — the equation, the picture, and *why it's weird*, side by side |

**Machine learning & computational biology**

| | |
|---|---|
| 🪰 **[drosomind](https://github.com/realgauravvyas/drosomind)** ([Live Demo](https://realgauravvyas.github.io/drosomind/)) | Live in-silico male fruit fly connectome & bio-acoustic organism simulator (Google Research *Cell* 2026 milestone) |
| ♟️ **[chess-ai](https://github.com/realgauravvyas/chess-ai)** | A 760k-parameter residual policy–value net: supervised pretraining, then gated self-play RL, with a live training dashboard — see below for what it actually measured |
| ✍️ **[ocr2tex](https://github.com/realgauravvyas/ocr2tex)** | LoRA fine-tunes of GLM-OCR turning handwritten math into compilable LaTeX |
| 🤖 **[Gemini-AI-Studio](https://github.com/realgauravvyas/Gemini-AI-Studio)** | Gemini-powered assignment evaluator |

**Applied**

| | |
|---|---|
| 🌱 **[carboncampus](https://realgauravvyas.github.io/carboncampus/)** | Campus-calibrated urban carbon calculator — offline-first PWA, no backend needed. Avinya 2026, IIT Guwahati |
| 🛰️ **[drishti](https://github.com/realgauravvyas/drishti)** | Post-disaster "information fog" resolver: calibrated belief over conflicting settlement reports plus asset routing on a damaged road network |
| 📷 **[hemispheR-py](https://github.com/realgauravvyas/hemispheR-py)** | Hemispherical canopy photo analysis — LAI, clumping, gap fraction, without OpenCV or R |

---

### 🧪 A result I didn't want

The chess engine's self-play half **did not work**, and that's the interesting part.
A 40-game match against its own frozen pretrained baseline scored **46.2%**
(95% CI 37.4–55.1) — no detectable improvement. The run before it was actively *worse*,
and the reason took a while to find: the eval metric had been scoring one colour while
the net alternated, so 159 logged evaluation points sat pinned at exactly 50% and
carried no information at all. Mirror augmentation was also flipping board files without
swapping the castling planes, quietly corrupting half of every minibatch.

The binding constraint turned out to be sample efficiency — 128 simulations is about
4.3 visits per legal move, against AlphaZero's ~27. All of it is written up in the
repo's `RESULTS.md`, because a negative result you can reproduce is worth more than a
positive one you can't.

---

### 🎮 Blackout Studio

I also build complete games solo — engine, art and audio. Both are zero-dependency and
fully offline, with every sprite and sound generated at runtime.

| | |
|---|---|
| 📱 **[Voltfall](https://github.com/realgauravvyas/blackout-studio/tree/main/voltfall)** — Android | Neon survival-action roguelite, ~95 KB |
| 🖥️ **[Neon Depths](https://github.com/realgauravvyas/blackout-studio/tree/main/neon-depths)** — Windows | Neon twin-stick roguelite, twelve floors, one life, ~99 MB |

---

### 🛠 Toolbox

<div align="center">

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/-C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Kotlin](https://img.shields.io/badge/-Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black)
![LaTeX](https://img.shields.io/badge/-LaTeX-008080?style=flat-square&logo=latex&logoColor=white)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/-GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

</div>

---

<details>
<summary><b>🔧 How this page builds itself</b></summary>

<br>

The GitHub contribution snake animation is automatically drawn fresh by CI on every push to `main` and once daily, then published to the `output` branch via [`Platane/snk`](https://github.com/Platane/snk).

</details>

---

<div align="center">

![Followers](https://img.shields.io/github/followers/realgauravvyas?style=flat-square&label=followers&color=6C63FF&labelColor=0D1117)
![Stars](https://img.shields.io/github/stars/realgauravvyas?style=flat-square&label=stars&color=6C63FF&labelColor=0D1117)
![Profile views](https://komarev.com/ghpvc/?username=realgauravvyas&style=flat-square&color=6C63FF)

<img src="https://raw.githubusercontent.com/realgauravvyas/realgauravvyas/output/github-contribution-grid-snake-dark.svg#gh-dark-mode-only" />
<img src="https://raw.githubusercontent.com/realgauravvyas/realgauravvyas/output/github-contribution-grid-snake.svg#gh-light-mode-only" />

</div>

<div align="center">

📄 [**Resume (PDF)**](https://realgauravvyas.github.io/assets/Gaurav_Vyas_Resume.pdf) &bull; 🌐 [**Personal Website &amp; Profile**](https://www.socialpsychology.org/member/gaurav-vyas) &bull; 🔶 [**Interactive Portfolio**](https://realgauravvyas.github.io/) &bull; ✉️ [**g.vyas@op.iitg.ac.in**](mailto:g.vyas@op.iitg.ac.in)

</div>

---

<div align="center">

*"The purpose of computing is insight, not numbers."* — Richard Hamming

</div>
