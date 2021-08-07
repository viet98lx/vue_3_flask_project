<template>
<div class="container mt-5">
  <p><strong>ID:</strong> {{film.film_id}}</p>
  <p><strong>TITLE:</strong> {{film.title}}</p>
  <p><strong>DESCRIPTION:</strong> {{film.description}}</p>
  <p><strong>RELEASE YEAR:</strong> {{film.release_year}}</p>
  <p><strong>LANGUAGE:</strong> {{film.language}}</p>
  <p><strong>LENGTH:</strong> {{film.length}} minutes</p>
  <p><strong>RATING:</strong> {{film.rating}}</p>
  <p><strong>PRICE:</strong> {{film.price}}</p>
  <button class="btn btn-danger mx-3 mt-3" @click="deleteFilm">Delete</button>
  <router-link :to="{name:'film_edit', params:{film_id:film.film_id}}"
  class="btn btn-success mt-3">Update</router-link>
</div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory"
const FilmRepository = Repository.get("films")
export default {
  name: "FilmDetail",
  data(){
    return {
      film:{}
    }
  },
  props: {
    film_id: {
      type:[Number,String],
      required:true
    }
  },
  methods: {
    async getFilmData() {
      console.log("call get film detail")
      const resp = await FilmRepository.getFilm(this.film_id)
      this.film = resp['data']
      console.log(this.film.film_id)
      console.log(this.film)
    },
    async deleteFilm(){
      console.log("call get films")
      await FilmRepository.delete(this.film_id)
      this.$router.push({
            name:'filmshome'
      })
    }
  },
  created() {
    this.getFilmData()
  }
}
</script>

<style scoped>

</style>