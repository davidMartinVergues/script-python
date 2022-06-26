import jsonschema


# Describe what kind of json you expect.
santander_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "field_1": {
            "anyOf":[
                {
                    "type":"string"
                },
                {
                    "type":"null"
                }
            ]
            },
        "field_2":  {
            "anyOf":[
                {
                    "type":"string"
                },
                {
                    "type":"null"
                }
            ]
            },
        "field_13":  {
            "anyOf":[
                {
                    "type":"string"
                },
                {
                    "type":"null"
                }
            ]
            }
    },
}

def isValid(jsonData):
    try:
        jsonschema.validate(instance=jsonData, schema=santander_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True
