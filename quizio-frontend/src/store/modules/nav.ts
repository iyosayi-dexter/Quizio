export interface nav_state {
    active:boolean,
    current_url:string|null
}

const nav = {
    namespaced:true,
    state(): nav_state{
        return {
            active:false,
            current_url:''
        }
    },
    mutations:{
        toggle_nav(state:nav_state){
            state.active = !state.active
        }
    }
}

export default nav