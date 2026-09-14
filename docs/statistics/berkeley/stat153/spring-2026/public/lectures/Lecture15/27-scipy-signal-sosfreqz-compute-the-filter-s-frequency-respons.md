---
title: scipy.signal.sosfreqz — compute the filter's frequency response
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# scipy.signal.sosfreqz — compute the filter's frequency response

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

def apply_filter(y, sr, cutoff, btype, order=5):
    """Design and apply a Butterworth filter.

    btype: 'low' or 'high'
    Returns: filtered signal, filter coefficients (sos)
    """
    sos = butter(order, cutoff, btype=btype, fs=sr, output='sos')
    y_filt = sosfiltfilt(sos, y)
    return y_filt, sos


def plot_filter_result(y_orig, y_lp, y_hp, sos_lp, sos_hp, sr,
                       cutoff_lp, cutoff_hp, title=''):
    """Comprehensive filter demo figure."""
    fig = plt.figure(figsize=(16, 12))
    gs = gridspec.GridSpec(3, 3, hspace=0.45, wspace=0.3)

    # --- Row 1: Filter frequency response (using sosfreqz) ---
    ax_resp = fig.add_subplot(gs[0, :])
    for sos, label, color in [
        (sos_lp, f'Low-pass (cutoff={cutoff_lp} Hz)', '#0f3460'),
        (sos_hp, f'High-pass (cutoff={cutoff_hp} Hz)', '#e94560'),
    ]:
        w, h = sosfreqz(sos, worN=2048, fs=sr)
        ax_resp.plot(w, 20*np.log10(np.abs(h) + 1e-10), color=color,
                     linewidth=2, label=label)
    ax_resp.axhline(-3, color='#aaa', linestyle='--', linewidth=0.8, label='-3 dB')
    ax_resp.set_title('Filter frequency responses (sosfreqz)', fontsize=12, fontweight='bold')
    ax_resp.set_xlabel('Frequency (Hz)')
    ax_resp.set_ylabel('Gain (dB)')
    ax_resp.set_xlim(0, 5000)
    ax_resp.set_ylim(-60, 5)
    ax_resp.legend(fontsize=10)

    # --- Row 2: Spectrograms (original, LP, HP) ---
    for i, (y, lab) in enumerate([
        (y_orig, 'Original'),
        (y_lp, f'Low-pass (< {cutoff_lp} Hz)'),
        (y_hp, f'High-pass (> {cutoff_hp} Hz)'),
    ]):
        ax = fig.add_subplot(gs[1, i])
        nps = 2048
        f_s, t_s, Sxx = spectrogram(y, fs=sr, nperseg=nps, noverlap=nps*3//4)
        ax.pcolormesh(t_s, f_s, 10*np.log10(Sxx + 1e-10),
                      cmap='magma', shading='gouraud')
        ax.set_ylim(0, 5000)
        ax.set_title(lab, fontsize=10, fontweight='bold')
        ax.set_xlabel('Time (s)')
        if i == 0:
            ax.set_ylabel('Frequency (Hz)')

    # --- Row 3: Periodograms overlay ---
    ax_psd = fig.add_subplot(gs[2, :])
    for y, lab, color, lw in [
        (y_orig, 'Original', '#aaa', 0.5),
        (y_lp, f'Low-pass (< {cutoff_lp} Hz)', '#0f3460', 1.2),
        (y_hp, f'High-pass (> {cutoff_hp} Hz)', '#e94560', 1.2),
    ]:
        f_w, Pxx_w = welch(y, fs=sr, nperseg=4096)
        ax_psd.semilogy(f_w, Pxx_w, color=color, linewidth=lw, label=lab)
    ax_psd.set_title('PSD before and after filtering (welch)', fontsize=12, fontweight='bold')
    ax_psd.set_xlabel('Frequency (Hz)')
    ax_psd.set_ylabel('PSD')
    ax_psd.set_xlim(0, 5000)
    ax_psd.legend(fontsize=9)

    if title:
        plt.suptitle(title, fontsize=14, fontweight='bold', y=1.01)
    plt.tight_layout()
    plt.show()
```

```python

---

[← scipy.signal.sosfiltfilt — apply it (zero-phase, so no time shift)](26-scipy-signal-sosfiltfilt-apply-it-zero-phase-so-no-time-shif.md) · [Up: contents](index.md) · [Apply to the dance track →](28-apply-to-the-dance-track.md)
