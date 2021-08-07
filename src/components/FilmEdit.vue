<template>
<div class="container mt-5">
    <form @submit.prevent="updateFilm">
      <label>TITLE</label><input type="text" class="form-control" placeholder="Please enter title" v-model="title"/>
      <br/>
      <label>DESCRIPTION</label><textarea rows="1" class="form-control"
                placeholder="Please enter description"
                                        v-model="description"></textarea>
      <br/>
      <label>REALEASE YEAR</label>
      <br/>
      <input type="number" min="1900" max="2099" step="1" placeholder="2021" v-model="release_year"/>
      <br/>
      <button class="btn btn-success mt-4">
        Update information
      </button>
    </form>
    <div v-if="error" class="alert alert-warning alert-dismissible fade show mt-5"
         role="alert">
      <strong>{{error}}</strong>
    </div>
  </div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory"
const FilmRepository = Repository.get("films")
export default {
  name: "FilmEdit",
  props:{
    film_id:{
      type:[Number,String],
      required:true
    }
  },
  methods:{
    updateFilm(){
      console.log("call update film")
      if (!this.title || !this.description ) {
        this.error = "Please add all text fields"
      } else if(!this.release_year || this.release_year < 1900 || this.release_year > 2021) {
        this.error = "Please correct release year"
      }
      else {
        let body_request = {
          title:this.title,
          description:this.description,
          release_year:this.release_year
        }
        FilmRepository.update(body_request, this.film_id).then(() => {
          this.$router.push({
            name:'filmshome'
          })
        })
      }
    }
  },
  data(){
    return {
      title:null,
      description:null,
      release_year:null,
      error:null
    }
  },
  async beforeRouteEnter(to, from, next){
    if(to.params.film_id !== undefined){
      await FilmRepository.getFilm(to.params.film_id).then(data =>{
        console.log(data)
        return next(vm => (vm.title=data.title, vm.description=data.description, vm.release_year=data.release_year))
      })
    }
    else{
      return next()
    }
  }
}

</script>

<style scoped>

</style>