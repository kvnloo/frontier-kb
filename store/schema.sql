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
