GRANT ALL PRIVILEGES ON flaskdb.* TO 'flask_user'@'%' IDENTIFIED BY 'flask_password';

USE flaskdb;
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    image_file VARCHAR(20) NOT NULL DEFAULT 'default.jpg',
    password VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS post (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    date_posted DATETIME NOT NULL,
    content TEXT NOT NULL,
    user_id INT NOT NULL,
    gpx_file VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

