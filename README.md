# A Diachronic Graph Embedding Framework (D-GEF)

## Dataset Description

The dataset `data.db` in `data.zip` was collected from `0day.today` for our experiments and case study. Data was parsed and stored in a `SQLite` database with the following schema:

```SQL
CREATE TABLE zero_day19 (
    sourceData TEXT,    -- Source exploit
    title TEXT,         -- Exploit title
    published date,     -- Exploit post publish date
    description TEXT,   -- Exploit description
    attackType TEXT,    -- Exploit attack types (e.g., local, remote, webapp, dos)
    platform TEXT       -- Targeted platform (e.g., windows, linux, php)
);
```

## Code Structure

TBA
