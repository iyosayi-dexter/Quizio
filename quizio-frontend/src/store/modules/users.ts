interface user {
    user: {
        username:String,
        id: number
    },
    about: String| null,
    xp: number,
    profile_image: String | null
}

interface state {
    all:user[],
    show_users_modal:boolean
}

const initialState:user[] = []

const users = {
    namespaced:true,
    state(): state{
        return {
            all:initialState,
            show_users_modal:false
        }
    },
    mutations:{
        setUsers(state:state, users:user[]){
            state.all = users
        },
        toggleModal(state:state){
            state.show_users_modal = !state.show_users_modal
        }
    }
}

export default users