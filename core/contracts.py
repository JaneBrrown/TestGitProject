USER_DATA_SCHEME = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "number"},
        "email" : {"type" : "string"},
        "first_name" : {"type" : "string"},
        "last_name" : {"type" : "string"},
        "avatat" : {"type" : "string"}
    },
    "required" : ["id", "email", "first_name", "last_name", "avatar"]

}