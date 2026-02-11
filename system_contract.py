# system_contract.py
# Definerer den logiske kontrakt mellem input og output i systemet.
# Ingen forretningslogik – kun struktur.

INPUT_SCHEMA = {
    "name": "string",
    "department": "string",
    "priority": "low|medium|high",
    "description": "string"
}

OUTPUT_SCHEMA = {
    "status": "auto|manual",
    "reason": "string",
    "next_action": "string"
}
