<template>
<!--<h1>Create</h1>-->
  <div class="container mt-5">
    <form @submit.prevent="insertActor">
      <input type="text" class="form-control" placeholder="Please enter your first name" v-model="first_name"/>
      <br/>
      <textarea rows="1" class="form-control"
                placeholder="Please enter your last name"
                v-model="last_name"></textarea>
      <button class="btn btn-success mt-4">
        Publish information
      </button>
    </form>
    <div v-if="error" class="alert alert-warning alert-dismissible fade show mt-5"
         role="alert">
      <strong>{{this.error}}</strong>
    </div>
  </div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory"
const ActorRepository = Repository.get("actors")

export default {
  name: "Create",
  data(){
    return {
      first_name:null,
      last_name:null,
      error:null
    }
  },
  methods: {
    async insertActor() {
      console.log("call insert actor")
      if (!this.first_name || !this.last_name) {
        this.error = "Please add all fields"
      } else {
        let body_request = {
          first_name:this.first_name,
          last_name:this.last_name
        }
        await ActorRepository.create(body_request)
        this.$router.push({
            name:'actorshome'
        })
      }
    }
  }
}
</script>

<style scoped>

</style>