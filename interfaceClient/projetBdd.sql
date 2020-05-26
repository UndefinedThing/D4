create table Users (
   Id                   INTEGER             PRIMARY KEY AUTOINCREMENT not null,
   Email                varchar(255)        not null,
   Username             varchar(255)        not null,
   Password             varchar             not null,
   Wins                 INTEGER             null default 0,
   Looses               INTEGER             null default 0,
   Draws                INTEGER             null default 0,
   Created_at           datetime            not null,
   Updated_at           datetime            not null
)