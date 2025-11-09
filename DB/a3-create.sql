-- Delete the table if it exists
DROP TABLE IF EXISTS students;

-- Create table `students` with values from specification
CREATE TABLE IF NOT EXISTS students(
    student_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name      TEXT NOT NULL,
    last_name       TEXT NOT NULL,
    email           TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

-- Create three students as defined in specification
INSERT INTO students(first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
