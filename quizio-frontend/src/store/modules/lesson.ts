interface state {
    lessons: {topic:string, exert:string, slug:string ,  thumbnail:string, date_created:string}[],
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
        },
        setLessons(state:state, lessons:{topic:string, exert:string, slug:string, thumbnail:string, date_created:string}[]){
            state.lessons == lessons
        }
    }
}

export default lesson