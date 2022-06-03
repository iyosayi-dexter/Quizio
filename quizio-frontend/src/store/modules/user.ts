interface profile {
    username:String|null,
    email:String|null,
    is_email_verified:boolean|null,
    id:number|null
}
const initialState = {
    username:'dexter',
    email:'dexter@test.com',
    is_email_verified:true,
    id:5
}

const user = {
    namespaced:true,
    state(): profile{
        return {
            ...initialState
        }
    },
    mutations:{
    }
}

export default user