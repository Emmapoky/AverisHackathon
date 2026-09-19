-- Run once in Supabase → SQL editor (free project, no card needed).
create table if not exists reviews (
  email_id   text primary key,
  data       jsonb not null,
  updated_at timestamptz default now()
);
create table if not exists processed (
  email_id   text primary key,
  data       jsonb not null,
  updated_at timestamptz default now()
);
-- The app uses the service_role key server-side only (never in the browser),
-- so row-level security can stay on with no public policies.
alter table reviews enable row level security;
alter table processed enable row level security;
