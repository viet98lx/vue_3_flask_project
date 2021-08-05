<template>
  <div class="container mt-5">
    <form @submit.prevent="updateActor">
      <input type="text" class="form-control" placeholder="Please enter your first name" v-model="first_name"/>
      <br/>
      <textarea rows="1" class="form-control"
                placeholder="Please enter your last name"
                v-model="last_name"></textarea>
      <button class="btn btn-success mt-4">
        Update information
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
  name: "ActorEdit",
  props:{
    actor_id:{
      type:[Number,String],
      required:true
    }
  },
  methods:{
    async updateActor(){
      console.log("call update actor")
      if (!this.first_name || !this.last_name) {
        this.error = "Please add all fields"
      } else {
        let body_request = {
          first_name:this.first_name,
          last_name:this.last_name
        }
        await ActorRepository.update(body_request, this.actor_id)
        this.$router.push({
            name:'actorshome'
        })
      }
    }
  },
  data(){
    return {
      first_name:null,
      last_name:null,
      error:null
    }
  },
  async beforeRouteEnter(to, from, next){
    if(to.params.actor_id != undefined){
      const data = await ActorRepository.getActor(to.params.actor_id)
      return next(vm => (vm.first_name=data.first_name, vm.last_name=data.last_name))
    }
    else{
      return next()
    }
  }
}
</script>

<style scoped>

</style>