"""Vendored stub -- lives under vendor/ so the ingestion pipeline's
should_skip() path-fragment rule excludes it. Not part of PedalWorks' own
source; the distinctive symbol below proves whether a vendored file leaked
into the knowledge base."""


def VENDORED_DO_NOT_INGEST_MARKER():
    """If this symbol shows up in extracted KB text, the vendor/ skip rule
    failed to exclude this file."""
    return "vendor-marker"
