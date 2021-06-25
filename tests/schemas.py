pet = {
    "$schema": "http://json-schema.org/draft/2019-09/schema#",

    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "type": "number"
            },
            "category": {
                "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "name": {
                                "type": "string"
                            }
                        },
                "required": ["id", "name"]
            },
            "name": {
                "type": "string"
            },
            "photoUrls": {
                "type": "array",
                        "items": {
                            "type": "string"
                        }
            },
            "tags": {
                "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "number"
                                },
                                "name": {
                                    "type": "string"
                                }
                            }
                        }
            },
            "status": {
                "type": "string"
            }
        }

    }
}
