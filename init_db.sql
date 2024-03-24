CREATE TABLE uidsToUsers(
    uid int,
    uname varchar(20),
    age int,
    email varchar(50)
);

CREATE TABLE chatLog(
    sendID int,
    recvID int,
    timestamp int,
    msg varchar(256),
    foreign key(sendID) references uidsToUsers,
    foreign key(recvID) references uidsToUsers,
    primary key(sendID, recvID, timestamp)
);
