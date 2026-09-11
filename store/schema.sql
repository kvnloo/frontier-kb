-- frontier-kb machine store. Markdown remains the git/Obsidian projection.
-- 100 writers: INSERT unique ids freely; UPDATE uses CAS on notes.version.
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE TABLE IF NOT EXISTS notes (
    id TEXT PRIMARY KEY,
    path TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    type TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'draft',
    body TEXT NOT NULL,
    frontmatter JSONB NOT NULL DEFAULT '{}'::jsonb,
    writer TEXT,
    version INT NOT NULL DEFAULT 1 CHECK (version > 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    embedding vector(8)
);

CREATE TABLE IF NOT EXISTS links (
    src TEXT NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
    dst TEXT NOT NULL,
    rel TEXT NOT NULL DEFAULT 'wikilink',
    PRIMARY KEY (src, dst, rel)
);

CREATE TABLE IF NOT EXISTS events (
    seq BIGSERIAL PRIMARY KEY,
    note_id TEXT,
    op TEXT NOT NULL,
    writer TEXT,
    expected_version INT,
    new_version INT,
    ok BOOLEAN NOT NULL DEFAULT true,
    detail TEXT,
    at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS notes_type_idx ON notes (type);
CREATE INDEX IF NOT EXISTS notes_updated_idx ON notes (updated_at DESC);
CREATE INDEX IF NOT EXISTS notes_title_trgm ON notes USING gin (title gin_trgm_ops);
CREATE INDEX IF NOT EXISTS notes_fts_idx ON notes USING gin (
    to_tsvector('english', coalesce(title, '') || ' ' || coalesce(body, ''))
);
CREATE INDEX IF NOT EXISTS events_note_idx ON events (note_id, at DESC);

-- Brain: notes are neurons. Wikilinks seed synapses. Human/agent use
-- potentiates (Hebbian) or prunes (synaptic homeostasis). Never delete a
-- neuron on prune — set notes.status = 'pruned' and log the reason.
CREATE TABLE IF NOT EXISTS synapses (
    src TEXT NOT NULL,
    dst TEXT NOT NULL,
    rel TEXT NOT NULL DEFAULT 'wikilink',
    weight REAL NOT NULL DEFAULT 1.0 CHECK (weight >= 0),
    fires INT NOT NULL DEFAULT 0 CHECK (fires >= 0),
    last_fired TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (src, dst, rel)
);

CREATE TABLE IF NOT EXISTS usage_events (
    seq BIGSERIAL PRIMARY KEY,
    note_id TEXT,
    actor TEXT NOT NULL,
    kind TEXT NOT NULL DEFAULT 'human',
    op TEXT NOT NULL,
    detail TEXT,
    at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS prune_log (
    seq BIGSERIAL PRIMARY KEY,
    note_id TEXT NOT NULL,
    reason TEXT NOT NULL,
    weight REAL,
    idle_days REAL,
    actor TEXT,
    at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS cycles (
    id BIGSERIAL PRIMARY KEY,
    phase TEXT NOT NULL,
    actor TEXT,
    started_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    ended_at TIMESTAMPTZ
);

CREATE INDEX IF NOT EXISTS synapses_weight_idx ON synapses (weight DESC);
CREATE INDEX IF NOT EXISTS synapses_src_idx ON synapses (src);
CREATE INDEX IF NOT EXISTS synapses_dst_idx ON synapses (dst);
CREATE INDEX IF NOT EXISTS synapses_fired_idx ON synapses (last_fired DESC);
CREATE INDEX IF NOT EXISTS usage_note_idx ON usage_events (note_id, at DESC);
CREATE INDEX IF NOT EXISTS notes_status_idx ON notes (status);
