"""
Research questions:
1. Is the percentage of n-gram types in partition 1 relative to whole corpus smaller compared to partition 2?
"""
import matplotlib.pyplot as plt

from childesngrams import configs
from childesngrams.io import load_tokens
from childesngrams.utils import get_sliding_windows

CORPUS_NAME = 'childes-20201026'
MAX_NGRAM_SIZE = 7

tokens = load_tokens(CORPUS_NAME)
tokens1 = tokens[:len(tokens) // 2]
tokens2 = tokens[-len(tokens) // 2:]

ngram_sizes = list(range(1, MAX_NGRAM_SIZE + 1))
part_id2y = {1: [], 2: []}
for ngram_size in ngram_sizes:
    # make n-grams
    ngrams1 = get_sliding_windows(ngram_size, tokens1)
    ngrams2 = get_sliding_windows(ngram_size, tokens2)
    num_ngrams1 = len(ngrams1)
    num_ngrams2 = len(ngrams2)

    # get unique n-grams
    unique_ngrams1 = set(ngrams1)
    unique_ngrams2 = set(ngrams2)

    ngram_set_len1 = len(unique_ngrams1)
    ngram_set_len2 = len(unique_ngrams2)
    unique_ngrams2.update(unique_ngrams1)
    num_updated_ngrams = len(unique_ngrams2)
    yi1 = ngram_set_len1 / num_updated_ngrams
    yi2 = ngram_set_len2 / num_updated_ngrams

    # collect
    part_id2y[1].append(yi1)
    part_id2y[2].append(yi2)

    print(ngram_size)
    print(yi1)
    print(yi2)
    print()

# plot_comparison
fig, ax = plt.subplots(1, figsize=configs.Fig.fig_size, dpi=configs.Fig.dpi)
plt.title('')
ax.set_ylabel('Percent of total n-gram types', fontsize=configs.Fig.ax_fontsize)
ax.set_xlabel('n-gram size', fontsize=configs.Fig.ax_fontsize)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(axis='both', which='both', top=False, right=False)
# plot
for part_id, y in part_id2y.items():
    x = range(1, len(y) + 1)
    ax.plot(x, y, label='partition {}'.format(part_id), linewidth=2)
ax.legend(loc='best', frameon=False, fontsize=configs.Fig.leg_fontsize)
plt.tight_layout()
plt.show()
