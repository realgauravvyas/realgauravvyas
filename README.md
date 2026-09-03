<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1200&color=6C63FF&center=true&vCenter=true&width=680&lines=a%2818%29-a%2823%29%20from%20Gaurav%20Vyas%20%20--%20%20OEIS%20A181671%3BRamanujan%20primes%20past%2010%5E23%2C%20computed%20on%20a%20laptop%3BTurning%20equations%20into%20things%20you%20can%20actually%20watch%20move.%3BBSc%28Hons.%29%20Data%20Science%20%26%20AI%2C%20IIT%20Guwahati" alt="typing banner" />

<a href="https://oeis.org/A181671"><img src="https://img.shields.io/badge/OEIS%20A181671-a(18)--a(23)%20published-6C63FF?style=for-the-badge&labelColor=0D1117" alt="OEIS A181671" /></a>
<a href="https://realgauravvyas.github.io/mathematical-surprises/"><img src="https://img.shields.io/badge/live-250%2B%20visualizations-00E6C8?style=for-the-badge&labelColor=0D1117" alt="Mathematical Surprises" /></a>

</div>

# Gaurav Vyas

I build things where the math is the point, not the plumbing — and then I make sure
you can *see* it happen, not just read about it.

**BSc(Hons.) Data Science & AI**, IIT Guwahati · **PG Diploma in Applied Statistics**,
ISI Kolkata. Most of what's below started as *"is this actually true?"* and turned into
a repo. One of them turned into an entry in the OEIS.

---

### 📐 In the OEIS

In August 2026, six terms I computed were accepted into
**[OEIS A181671](https://oeis.org/A181671)** — the count of Ramanujan primes below each
power of ten. The sequence's EXTENSIONS section now reads:

> a(18)-a(23) from *Gaurav Vyas*, Aug 15 2026

That pushes the table from 10¹⁷ out to **10²³**, computed on a laptop and a desktop —
no institute, no cluster — with a 128-bit segmented sieve, bracketed analytic tail
bounds, and a machine-checkable certificate behind every term. The
[b-file](https://oeis.org/A181671/b181671.txt) now runs `n = 1..23`.

<div align="center">

<img src="https://raw.githubusercontent.com/realgauravvyas/realgauravvyas/output/ramanujan.gif" alt="The counting function pi(x) - pi(x/2) climbing, with each Ramanujan prime marked" width="480" />

<sub>The definition, animated: π(x) − π(x/2) climbing, and each Ramanujan prime <i>Rₙ</i>
lighting up at the <i>last</i> place the curve crosses level n — which is exactly what
makes it Rₙ. Rendered fresh by CI.</sub>

</div>

```
while (curious) {
    pick_an_equation();
    make_it_move();
    ask("why is this surprising?");
}
```

---

### 🔭 Live right now

**[Mathematical Surprises →](https://realgauravvyas.github.io/mathematical-surprises/)**
250+ interactive visualizations — fractals, chaos, number theory, calculus — each one a
real simulation you can drag sliders on, not a screenshot. Opens the same on your phone
as on your laptop.

<div align="center">

<img src="https://raw.githubusercontent.com/realgauravvyas/realgauravvyas/output/epicycles.gif" alt="Fourier epicycles tracing a square wave" width="480" />

<sub>Nine rotating circles on the odd harmonics, tracing a square wave — one of the 250+
live pieces in <a href="https://realgauravvyas.github.io/mathematical-surprises/">Mathematical Surprises</a>.</sub>

</div>

---

### 🧭 What I'm building

**Mathematics & number theory**

| | |
|---|---|
| 🔢 **[ramanujan-primes-beyond-1e19](https://github.com/realgauravvyas/ramanujan-primes-beyond-1e19)** | The A181671 extension above — paper, C++/Python sieve, and certificates for a(1)–a(23) |
| ⚡ **[ramanujan-primes-beyond-2-56](https://github.com/realgauravvyas/ramanujan-primes-beyond-2-56)** | The base-2 sibling: a(57)–a(72) of A190502 certified by the same method, Q = 2ⁿ instead of 10ᵏ |
| 🌀 **[mathematical-surprises](https://github.com/realgauravvyas/mathematical-surprises)** | A live gallery of interactive math & physics — the equation, the picture, and *why it's weird*, side by side |

**Machine learning**

| | |
|---|---|
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

Neither animation above is a checked-in file. Both are drawn from scratch by CI on every
push to `main` and again once a day, then published to the `output` branch:

- [`scripts/generate_ramanujan.py`](scripts/generate_ramanujan.py) — sieves primes, computes
  π(x) − π(x/2), solves for each Rₙ as the last crossing of level n, and animates the sweep.
  It asserts its own output against the known head of A104272, so a broken render fails the
  build instead of shipping a wrong picture.
- [`scripts/generate_epicycles.py`](scripts/generate_epicycles.py) — sums nine odd harmonics
  into a square wave and traces the tip.

Both are pure Pillow, no matplotlib, so the whole job stays cheap. The contribution snake
comes from [`Platane/snk`](https://github.com/Platane/snk).

</details>

---

<div align="center">

![Followers](https://img.shields.io/github/followers/realgauravvyas?style=flat-square&label=followers&color=6C63FF&labelColor=0D1117)
![Stars](https://img.shields.io/github/stars/realgauravvyas?style=flat-square&label=stars&color=6C63FF&labelColor=0D1117)
![Profile views](https://komarev.com/ghpvc/?username=realgauravvyas&style=flat-square&color=6C63FF)

<img src="https://raw.githubusercontent.com/realgauravvyas/realgauravvyas/output/github-contribution-grid-snake-dark.svg#gh-dark-mode-only" />
<img src="https://raw.githubusercontent.com/realgauravvyas/realgauravvyas/output/github-contribution-grid-snake.svg#gh-light-mode-only" />

</div>

---

<div align="center">

*"The purpose of computing is insight, not numbers."* — Richard Hamming

</div>
