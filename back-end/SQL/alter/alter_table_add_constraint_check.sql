ALTER TABLE users
ADD CONSTRAINT users_level_check CHECK (level >=0 AND level <=3);