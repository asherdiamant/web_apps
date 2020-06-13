import os
import db
import data.db_session as db_session
from data.package import Package
from data.releases import Release


def main():
    init_db()
    while True:
        insert_a_package()


def insert_a_package():

    p = Package()
    p.id = input('Package id / name: ').strip().lower()
    p.summary = input('Package summary: ').strip()
    p.license = input('License: ').strip()

    print("Release 1:")
    r = Release()
    r.major_ver = int(input("Major Version:"))
    r.minor_ver = int(input("Minor Version:"))
    r.build_ver = int(input("Build Version:"))
    r.size = int(input("Size in bytes:"))
    p.releases.append(r)

    print("Release 2:")
    r = Release()
    r.major_ver = int(input("Major Version:"))
    r.minor_ver = int(input("Minor Version:"))
    r.build_ver = int(input("Build Version:"))
    r.size = int(input("Size in bytes:"))
    p.releases.append()

    import sqlalchemy.orm
    session = db_session.create_session()
    session.add(p)

    session.commit()


def init_db():
    db_folder = os.path.dirname(db.__file__)
    db_file = os.path.abspath(os.path.join(db_folder, 'pypi.sqlite'))
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()
