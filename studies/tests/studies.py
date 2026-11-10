#functions - small research management system

#find one study
def get_study_by_id(studies, study_id):
    for study in studies:
        if study["id"] == study_id:
            return study
    return None
#filtering,lists
def get_studies_by_status(studies, status):
    # Your implementation
    result = []
    for study in studies:
        if study["status"] == status:
            result.append(study)
    return result
#dictionary aggregation
def count_studies_by_status(studies, status):
    for study in studies:
        if study["status"] == status:
            return len([s for s in studies if s["status"] == status])
#add new studies rejecting duplicate IDs
def add_study(studies, new_study):
    if not get_study_by_id(studies, new_study["id"]):
        studies.append(new_study)
    return studies
#cdictionary updates, edge cases
def update_study_status(studies, study_id, new_status):
    study = get_study_by_id(studies, study_id)
    if study:
        study["status"] = new_status
    return studies

