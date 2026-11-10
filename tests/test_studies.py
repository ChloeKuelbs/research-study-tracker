import pytest

from studies import (
    add_study,
    count_studies_by_status,
    get_studies_by_status,
    get_study_by_id,
    update_study_status,
)


@pytest.fixture
def studies():
    return [
        {"id": 1, "title": "Cancer Biomarkers", "status": "active"},
        {"id": 2, "title": "Protein Folding", "status": "completed"},
        {"id": 3, "title": "Drug Discovery", "status": "active"},
    ]


def test_get_study_by_id_returns_match(studies):
    assert get_study_by_id(studies, 2) == studies[1]


def test_get_study_by_id_returns_none_for_missing_id(studies):
    assert get_study_by_id(studies, 99) is None


def test_get_studies_by_status_returns_matches(studies):
    assert get_studies_by_status(studies, "active") == [studies[0], studies[2]]


def test_get_studies_by_status_returns_empty_list_without_matches(studies):
    assert get_studies_by_status(studies, "paused") == []


def test_count_studies_by_status_counts_matches(studies):
    assert count_studies_by_status(studies, "active") == 2


def test_count_studies_by_status_returns_zero_without_matches(studies):
    assert count_studies_by_status(studies, "paused") == 0


def test_add_study_appends_new_id(studies):
    new_study = {"id": 4, "title": "Cell Therapy", "status": "planned"}

    assert add_study(studies, new_study) is studies
    assert studies[-1] == new_study


def test_add_study_ignores_duplicate_id(studies):
    duplicate = {"id": 1, "title": "Duplicate", "status": "planned"}

    assert add_study(studies, duplicate) is studies
    assert len(studies) == 3
    assert studies[0]["title"] == "Cancer Biomarkers"


def test_update_study_status_updates_match(studies):
    assert update_study_status(studies, 2, "active") is studies
    assert studies[1]["status"] == "active"


def test_update_study_status_leaves_list_unchanged_for_missing_id(studies):
    original = [study.copy() for study in studies]

    assert update_study_status(studies, 99, "active") is studies
    assert studies == original
