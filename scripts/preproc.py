from mini_mne import SimpleRaw


def preprocess(raw: SimpleRaw, reref_params: list | None, filter_low_cutoff: float, filter_high_cutoff: float):

    # re-reference
    raw_reref = raw.re_reference(reref_params)

    # filter
    raw_filtered = raw_reref.filter(
        l_freq = filter_low_cutoff,
        h_freq = filter_high_cutoff
    )

    return raw_filtered
