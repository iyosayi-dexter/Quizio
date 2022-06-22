interface state {
    lessons: [],
    courses: {title:string, id:number , thumbnail:string}[]
}
const lesson = {
    namespaced:true,
    state(): state{
        return {
            lessons:[],
            courses:[]
        }
    },
    mutations:{
        setCourses(state:state , courses:{title:string, id:number , thumbnail:string}[]){
            state.courses = courses
        }
    }
}

export default lesson