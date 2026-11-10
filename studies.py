# Small research management system


def get_study_by_id(studies, study_id):
    """Return the study with the matching ID, or None if it is not found."""
    for study in studies:
        if study["id"] == study_id:
            return study
    return None


def get_studies_by_status(studies, status):
    """Return all studies with the requested status."""
    return [study for study in studies if study["status"] == status]


def count_studies_by_status(studies, status):
    """Count studies with the requested status."""
    return sum(study["status"] == status for study in studies)


def add_study(studies, new_study):
    """Add a study unless its ID already exists."""
    if get_study_by_id(studies, new_study["id"]) is None:
        studies.append(new_study)
    return studies


def update_study_status(studies, study_id, new_status):
    """Update a study's status when its ID exists."""
    study = get_study_by_id(studies, study_id)
    if study is not None:
        study["status"] = new_status
    return studies
