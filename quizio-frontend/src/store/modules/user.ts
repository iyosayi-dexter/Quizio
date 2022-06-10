interface profile {
    username:String|null,
    email:String|null,
    email_verified:boolean|null,
    id:number|null,
    is_authenticated:null| boolean,
    tokens:{
        access:String|null,
        refresh:String|null
    }
}


interface userDataInterface {
    user:{
        username:String|null,
        email:String|null,
        email_verified:boolean|null,
        user_id:number|null,
    },
    tokens:{
        access:String|null,
        refresh:String|null
    }
}
const initialState = {
    username:null,
    email:null,
    email_verified:null,
    id:null,
    is_authenticated: null,
    tokens:{
        access:null,
        refresh:null
    }
}
const user = {
    namespaced:true,
    state(): profile{
        return {
            ...initialState
        }
    },
    mutations:{
        set_user(state:profile, user_data:userDataInterface){
            const {tokens, user} = user_data
            state.tokens = tokens
            state.username = user.username,
            state.email = user.email
            state.email_verified = user.email_verified
            state.id = user.user_id
            state.is_authenticated = true
        }
    }
}

export default user