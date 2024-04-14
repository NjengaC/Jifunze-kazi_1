PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "user" (
        id SERIAL PRIMARY KEY,
        username VARCHAR(20) NOT NULL,
        email VARCHAR(120) NOT NULL,
        image_file VARCHAR(20) NOT NULL,
        password VARCHAR(60) NOT NULL
);
INSERT INTO "user" (id, username, email, image_file, password) VALUES
(1,'admin','admin@blog.com','default.jpg','$2b$12$xDWiLZWavM0wT5Q7mbnSjeT6rJP6UgTCQ/oop9ncuR.DueO76mgXa'),
(2,'Victor','victorcyrus01@gmail.com','default.jpg','$2b$12$9MXGmfwLxaOTSLjaUygOBurz7myBPivVbVSpdY9a2YzGRc5GMEGJ.'),
(3,'Njenga','njengavictor08@gmail.com','default.jpg','$2b$12$0vT4GSVyhI1yNVPEkJJDLOFD.ZbeszNw069eCTirAPfBclRfwvG3u'),
(4,'Brian','Brianmwangi@gmail.com','default.jpg','$2b$12$h4rXhE8BLroYiC4bzw.H4u.1rOwRARwaMfK7cUetcejTzKoXmAkwe'),
(5,'Kay','kay@gmail.com','default.jpg','$2b$12$mUUCBgsYNrdKLk9NRhe5y.Lcp4416HqQc3HLd7on9CtbSoNZdiJJK'),
(6,'Yvonne','yvonne@gmail.com','default.jpg','$2b$12$1m9jMLHl/2KO482a1TJKsepGm4bR0owDjUjtNy.AtQ/pWBlAyVGlS'),
(7,'Yvonne_Gichovi','yvonne1@gmail.com','default.jpg','$2b$12$YrK5Mr1MviEdAyCzT2xa8uHBjWvLmd1g8S.5gxzhy4d6ZLxhh8DtW');
COMMIT;

