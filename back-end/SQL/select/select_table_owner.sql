SELECT tablename, tableowner
FROM pg_tables
WHERE schemaname = 'public' AND tablename = 'users';