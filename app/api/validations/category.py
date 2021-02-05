def validate_category_sections_data(data):
    if "sections" not in data:
        return {"message": "List of sections must be provided."}
