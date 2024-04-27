CREATE TABLE IF NOT EXISTS patients(
    uid uuid UNIQUE NOT NULL DEFAULT gen_random_uuid (),
    name varchar(60) NOT NULL,
    phone_number varchar(30) NOT NULL,
    create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (uid),
    CONSTRAINT name_phone_number UNIQUE (name, phone_number)
);

CREATE TABLE IF NOT EXISTS users(
    uid uuid UNIQUE NOT NULL DEFAULT gen_random_uuid (),
    account varchar(60) UNIQUE NOT NULL,
    password varchar(60) NOT NULL,
    name varchar(60) NOT NULL,
    user_group varchar(60) NOT NULL,
    level smallint NOT NULL CHECK (level >=0 AND level <=2),
    email varchar(120),
    phone_number varchar(30) NOT NULL,
    create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_active boolean NOT NULL DEFAULT TRUE,
    PRIMARY KEY (uid)
);

CREATE TABLE IF NOT EXISTS admin_basic(
    uid serial UNIQUE NOT NULL,
    fk_user uuid NOT NULL,
    patient_medical_fees smallint ,
    time_appointment_limit smallint,
    people_appointment_limit smallint,
    create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_active boolean NOT NULL DEFAULT TRUE,
    PRIMARY KEY (uid),
    FOREIGN KEY (fk_user) REFERENCES users (uid) ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS reports(
    uid serial UNIQUE NOT NULL,
    year varchar(30) NOT NULL,
    month varchar(30) NOT NULL,
    total_appointment_people int NOT NULL,
    total_site_people int NOT NULL,
    total_cancel_people int NOT NULL,
    total_not_arrived_people int NOT NULL,
    total_pay_people int NOT NULL,
    total_money int NOT NULL,
    PRIMARY KEY (uid),
    CONSTRAINT year_month UNIQUE (year, month)
);

CREATE TABLE IF NOT EXISTS appointments(
    uid uuid UNIQUE NOT NULL DEFAULT gen_random_uuid (),
    fk_patient uuid NOT NULL,
    fk_report int,
    fk_user uuid,
    ip varchar(60),
    appointment_status smallint NOT NULL CHECK (appointment_status >=0 AND appointment_status <=3),
    people_number smallint NOT NULL,
    date date NOT NULL,
    time_period varchar(30) NOT NULL CHECK(time_period IN ('15:00', '16:00', '17:00', '18:00')),
    medical_fees smallint,
    create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_completed boolean NOT NULL DEFAULT FALSE,
    is_reported boolean NOT NULL DEFAULT FALSE,
    PRIMARY KEY (uid),
    FOREIGN KEY (fk_patient) REFERENCES patients (uid) ON UPDATE CASCADE,
    FOREIGN KEY (fk_report) REFERENCES reports (uid) ON UPDATE CASCADE,
    FOREIGN KEY (fk_user) REFERENCES users (uid) ON UPDATE CASCADE,
    CONSTRAINT ip_appointment_status_date_time_period UNIQUE (ip, appointment_status, date, time_period)
);

CREATE TABLE IF NOT EXISTS clinic_status(
    uid serial UNIQUE NOT NULL,
    fk_user uuid NOT NULL,
    date date NOT NULL,
    time_period varchar(30) CHECK(time_period IN ('15:00', '16:00', '17:00', '18:00')),
    create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_closed boolean NOT NULL DEFAULT TRUE,
    PRIMARY KEY (uid),
    FOREIGN KEY (fk_user) REFERENCES users (uid) ON UPDATE CASCADE,
    CONSTRAINT date_time_period UNIQUE (date, time_period)
);
