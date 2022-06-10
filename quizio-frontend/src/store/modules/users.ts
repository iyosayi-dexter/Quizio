interface user {
    user: {
        username:String,
        id: number
    },
    about: String| null,
    xp: number,
    profile_image: String | null
}

const initialState:user[] = [
    {
        "user": {
            "username": "dexter",
            "id": 1
        },
        "about": null,
        "xp": 0,
        "profile_image": null
    },    {
        "user": {
            "username": "Gwen",
            "id": 5
        },
        "about": null,
        "xp": 0,
        "profile_image": null
    }
]

const users = {
    namespaced:true,
    state(): user[]{
        return initialState
    },
    mutations:{

    }
}

export default users