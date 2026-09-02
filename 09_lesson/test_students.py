from conftest import Student


def test_add_student(db_session):
    new_student = Student(
        user_id=99999, level="Advanced", education_form="group", subject_id=1
    )

    db_session.add(new_student)
    db_session.commit()

    found_student = db_session.query(Student).filter_by(user_id=99999).first()
    assert found_student is not None
    assert found_student.level == "Advanced"
    assert found_student.education_form == "group"


def test_update_student(db_session):
    student = Student(
        user_id=88888,
        level="Elementary",
        education_form="personal",
        subject_id=1
    )

    db_session.add(student)
    db_session.commit()

    student.level = "Upper Intermediate"
    student.education_form = "group"
    db_session.commit()

    updated_student = (
        db_session.query(Student).filter_by(user_id=88888).first()
    )

    assert updated_student.level == "Upper Intermediate"
    assert updated_student.education_form == "group"


def test_delete_student(db_session):
    student = Student(
        user_id=77777,
        level="Pre-Intermediate",
        education_form="group",
        subject_id=1
    )

    db_session.add(student)
    db_session.commit()

    db_session.delete(student)
    db_session.commit()

    deleted_student = (
        db_session.query(Student).filter_by(user_id=77777).first()
    )

    assert deleted_student is None
